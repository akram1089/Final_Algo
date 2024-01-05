import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
class NumberGenerator(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        # Run a background task to fetch data and send it to the WebSocket
        await self.send_number()

    async def disconnect(self, close_code):
        pass

    async def send_number(self):
        while True:
            # Replace this with your actual data fetching logic
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

            await self.send(text_data=json.dumps(payload))
            await asyncio.sleep(1)



# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .zerodha_script import ZerodhaAPI, get_enctoken, read_enctoken
# import pyotp
# import asyncio

# # Replace these with your actual Zerodha credentials
# zerodha_username = 'XF1020'
# zerodha_password = 'anaya2020'
# totp_secret = 'U4HYSBCQ2VKE446LTN765KX2U7SUXXWW'

# class ZerodhaAPIConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#         # Generate TOTP
#         totp = pyotp.TOTP(totp_secret)

#         while True:
#             # Try to read enctoken from the file
#             enctoken = read_enctoken()

#             # If enctoken is not available or invalid, generate a new one
#             if not enctoken or not enctoken.strip() or not is_valid_enctoken(enctoken):
#                 # Generate TOTP
#                 otp = totp.now()

#                 # Get enctoken using the provided function
#                 enctoken = get_enctoken(zerodha_username, zerodha_password, otp)

#                 # Save the new enctoken to a text file
#                 with open('enctoken.txt', 'w') as file:
#                     file.write(enctoken)

#             # Create ZerodhaAPI instance
#             zerodha_api = ZerodhaAPI(enctoken)

#             # Fetch user profile
#             user_profile = zerodha_api.get_user_profile()
#             zerodha_positions = zerodha_api.positions()

#             # Send the relevant information to the WebSocket
#             payload = {
#                 'all_profile': user_profile,
#                 'all_position': zerodha_positions,
#             }
#             await self.send(text_data=json.dumps(payload))

#             await asyncio.sleep(0.1)

#     async def disconnect(self, close_code):
#         print(f"Socket disconnected with code {close_code}")

# def is_valid_enctoken(enctoken):
#     zerodha_api = ZerodhaAPI(enctoken)
#     user_profile = zerodha_api.get_user_profile()
#     if user_profile:
#         # print(f"User Profile: {user_profile}")
#         # print(zerodha_api.orders())
#         # print(zerodha_api.positions())
#         # print(zerodha_api.holdings())
#         return True  # Replace with your actual logic

#     else:
#         # If fetching user profile fails, regenerate the enctoken and try again
#         print("Failed to fetch user profile. Regenerating enctoken...")
#         # Generate TOTP
#         totp = pyotp.TOTP(totp_secret)
#         otp = totp.now()

#         # Get enctoken using the provided function
#         enctoken = get_enctoken(zerodha_username, zerodha_password, otp)

#         # Create ZerodhaAPI instance with the new enctoken
#         zerodha_api = ZerodhaAPI(enctoken)

#         # Fetch user profile again
#         user_profile = zerodha_api.get_user_profile()
#         if user_profile:
#             print(f"User Profile: {user_profile}")
#             # print(zerodha_api.orders())
#             # print(zerodha_api.positions())
#             print(zerodha_api.holdings())
#         else:
#             print("Failed to fetch user profile even after regenerating enctoken.")
#     # Implement your logic to check if the enctoken is still valid
#     # You might want to check the expiration time or make a test request to the API
#     # Return True if the enctoken is valid, otherwise False
