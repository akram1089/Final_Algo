import json
import random
from time import sleep
import requests

from channels.generic.websocket import WebsocketConsumer


class NumberGenerator(WebsocketConsumer):

    def connect(self):
        self.accept()

        while True:
            # Fetch data from the API
            api_url = "https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol=NIFTY+50"
            response = requests.get(api_url)
            data = response.json()

            # Extract relevant information
            result_data = data.get("resultData", {})
            symbol_name = result_data.get("symbol_name", "")
            last_trade_price = result_data.get("last_trade_price", 0.0)

            # Send the relevant information to the WebSocket
            payload = {
                'symbol_name': symbol_name,
                'last_trade_price': last_trade_price
            }
            self.send(json.dumps(payload))

            sleep(1)

    def disconnect(self, code):
        print("Socket disconnected with code", code)

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .zerodha_script import ZerodhaAPI, get_enctoken, read_enctoken
import pyotp
import asyncio
from home.models import Broker  # Import your Broker model

class ZerodhaAPIConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Get the authenticated user from the WebSocket connection
        user = self.scope["user"]
        print(user)

        # Fetch the relevant Broker instance for the authenticated user
        broker_instance_zerodha = Broker.objects.filter(user=user, broker_name="zerodha", active_api=True).first()

        if broker_instance_zerodha:
            # Generate TOTP
            totp = pyotp.TOTP(broker_instance_zerodha.totp_key)

            while True:
                # Try to read enctoken from the file
                enctoken = read_enctoken()

                # If enctoken is not available or invalid, generate a new one
                if not enctoken or not enctoken.strip() or not is_valid_enctoken(enctoken, broker_instance_zerodha):
                    # Generate TOTP
                    otp = totp.now()

                    # Get enctoken using the provided function
                    enctoken = get_enctoken(
                        broker_instance_zerodha.logging_id,
                        broker_instance_zerodha.password,
                        otp
                    )

                    # Save the new enctoken to a text file
                    with open('enctoken.txt', 'w') as file:
                        file.write(enctoken)

                # Create ZerodhaAPI instance
                zerodha_api = ZerodhaAPI(enctoken)

                # Fetch user profile
                user_profile = zerodha_api.get_user_profile()
                zerodha_positions = zerodha_api.positions()
                zerodha_holdings = zerodha_api.holdings()

                # Send the relevant information to the WebSocket
                payload = {
                    'all_profile': user_profile,
                    'all_position': zerodha_positions,
                    'all_holding': zerodha_holdings,
                }
                await self.send(text_data=json.dumps(payload))

                await asyncio.sleep(0.1)

    async def disconnect(self, close_code):
        print(f"Socket disconnected with code {close_code}")
from channels.db import database_sync_to_async

@database_sync_to_async
def is_valid_enctoken(enctoken, broker_instance):
    zerodha_api = ZerodhaAPI(enctoken)
    user_profile = zerodha_api.get_user_profile()
    if user_profile:
        # print(f"User Profile: {user_profile}")
        # print(zerodha_api.orders())
        # print(zerodha_api.positions())
        # print(zerodha_api.holdings())
        return True  # Replace with your actual logic

    else:
        # If fetching user profile fails, regenerate the enctoken and try again
        print("Failed to fetch user profile. Regenerating enctoken...")
        # Generate TOTP
        totp = pyotp.TOTP(broker_instance.totp_key)
        otp = totp.now()

        # Get enctoken using the provided function
        enctoken = get_enctoken(
            broker_instance.logging_id,
            broker_instance.password,
            otp
        )

        # Create ZerodhaAPI instance with the new enctoken
        zerodha_api = ZerodhaAPI(enctoken)

        # Fetch user profile again
        user_profile = zerodha_api.get_user_profile()
        if user_profile:
            # print(f"User Profile: {user_profile}")
            # print(zerodha_api.orders())
            # print(zerodha_api.positions())
            # print(zerodha_api.holdings())
            pass
        else:
            print("Failed to fetch user profile even after regenerating enctoken.")
    # Implement your logic to check if the enctoken is still valid
    # You might want to check the expiration time or make a test request to the API
    # Return True if the enctoken is valid, otherwise False


# trading/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from home.models import Broker
class BrokerDetailsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        user = self.scope['user']
        credential = Broker.objects.get(user=user)
        broker_details = credential.broker_details

        await self.send(text_data=json.dumps({
            'broker_details': broker_details
        }))
