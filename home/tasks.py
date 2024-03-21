# your_app/tasks.py
from celery import shared_task
from django.contrib.auth import get_user_model
import requests
import pyotp
import dateutil.parser
import datetime
import json
User = get_user_model()
@shared_task
def add(x, y):
    return x + y

# tasks.py
from celery import shared_task
from home.models import AdditionTask_main_time, StrategyScheduleTaskResult
from django.utils import timezone

@shared_task
def perform_addition(task_id):
    print(f"Task ID: {task_id} - Task execution started.")
    print(task_id)
    try:
        task = AdditionTask_main_time.objects.get(pk=task_id)
        print(f"Task ID: {task_id}, Task Status: {task.status}, Scheduled Time: {task.schedule_time}")

        # Check if the task's status is active and if the schedule time has passed
        if task.status == 'active' and task.schedule_time <= timezone.now():
            result = task.number1 + task.number2
            task.result = result
            task.save()
            print(f"Task ID: {task_id} - Addition completed. Result: {result}")
        else:
            print(f"Task ID: {task_id} is inactive or not yet scheduled. Skipping.")

    except AdditionTask_main_time.DoesNotExist:
        print(f"Task with id {task_id} not found.")
    except Exception as e:
        print(f"Error processing task ID {task_id}: {str(e)}")



import requests

import json

class ZerodhaAPI:
    def __init__(self, enctoken):
        self.headers = {"Authorization": f"enctoken {enctoken}"}
        self.session = requests.Session()
        self.root_url = "https://kite.zerodha.com/oms"
        self.session.get(self.root_url, headers=self.headers)

    def get_user_profile(self):
        profile_url = f"{self.root_url}/user/profile/full"
        response = self.session.get(profile_url, headers=self.headers)
        return response.json() if response.status_code == 200 else None
    

    def quote(self, instruments):
        data = self.session.get(f"{self.root_url}/quote", params={"i": instruments}, headers=self.headers).json()["data"]
        return data
    
    def positions(self):
        positions = self.session.get(f"{self.root_url}/portfolio/positions", headers=self.headers).json()["data"]
        return positions
    
    def holdings(self):
        holdings = self.session.get(f"{self.root_url}/portfolio/holdings", headers=self.headers).json()["data"]
        return holdings
    def nudges(self, params):
        # print(params)
        headers = {"Content-Type": "application/json", **self.headers}
        nudges = self.session.post(f"{self.root_url}/nudge/orders", json=params, headers=headers)

        return nudges.json() if nudges.status_code == 200 else None
    

    
        
    def margins(self):
        margins = self.session.get(f"{self.root_url}/user/margins", headers=self.headers).json()
        return margins

       
    PRODUCT_MIS = "MIS"
    PRODUCT_CNC = "CNC"
    PRODUCT_NRML = "NRML"
    PRODUCT_CO = "CO"

    # Order types
    ORDER_TYPE_MARKET = "MARKET"
    ORDER_TYPE_LIMIT = "LIMIT"
    ORDER_TYPE_SLM = "SL-M"
    ORDER_TYPE_SL = "SL"

    # Varities
    VARIETY_REGULAR = "regular"
    VARIETY_CO = "co"
    VARIETY_AMO = "amo"

    # Transaction type
    TRANSACTION_TYPE_BUY = "BUY"
    TRANSACTION_TYPE_SELL = "SELL"

    # Validity
    VALIDITY_DAY = "DAY"
    VALIDITY_IOC = "IOC"

    # Exchanges
    EXCHANGE_NSE = "NSE"
    EXCHANGE_BSE = "BSE"
    EXCHANGE_NFO = "NFO"
    EXCHANGE_CDS = "CDS"
    EXCHANGE_BFO = "BFO"
    EXCHANGE_MCX = "MCX"

    def place_order(self, variety, exchange, tradingsymbol, transaction_type, quantity, product, order_type, price=None,
                    validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None,
                    trailing_stoploss=None, tag=None):
        # Check if the provided product, order type, variety, transaction type, validity, and exchange are valid
        if product not in [self.PRODUCT_MIS, self.PRODUCT_CNC, self.PRODUCT_NRML, self.PRODUCT_CO]:
            raise ValueError("Invalid product type")

        if order_type not in [self.ORDER_TYPE_MARKET, self.ORDER_TYPE_LIMIT, self.ORDER_TYPE_SLM, self.ORDER_TYPE_SL]:
            raise ValueError("Invalid order type")

        if variety not in [self.VARIETY_REGULAR, self.VARIETY_CO, self.VARIETY_AMO]:
            raise ValueError("Invalid variety")

        if transaction_type not in [self.TRANSACTION_TYPE_BUY, self.TRANSACTION_TYPE_SELL]:
            raise ValueError("Invalid transaction type")

        if validity not in [self.VALIDITY_DAY, self.VALIDITY_IOC]:
            raise ValueError("Invalid validity")

        if exchange not in [self.EXCHANGE_NSE, self.EXCHANGE_BSE, self.EXCHANGE_NFO, self.EXCHANGE_CDS, 
                            self.EXCHANGE_BFO, self.EXCHANGE_MCX]:
            raise ValueError("Invalid exchange")

        params = locals()
        print(params)
        del params["self"]
        for k in list(params.keys()):
            if params[k] is None:
                del params[k]
        # print(f"{self.root_url}/orders/{variety}")
        params_json = json.dumps(params, indent=2)
        # print(params_json)
        # print(self.headers)
        order_response = self.session.post(f"{self.root_url}/orders/{variety}", data=params, headers=self.headers)
        if order_response.status_code == 200:
            order_id = order_response.json()
            # print(order_id)
            return order_id
        else:
            print(order_response.text)
            # print(f"Failed to place order. Status Code: {response.status_code}")
            return order_response.text
        




    
 













@shared_task(bind=True)
def perform_addition_task(self, user_id, all_strategy_values,custom_field_value,zerodha_username,zerodha_password,totp_secret):
    user = User.objects.get(id=user_id)
    print("all_strategy_values1",json.loads(all_strategy_values))

    # Parse the JSON string into a Python dictionary
    all_strategy_values_sysmbol = json.loads(all_strategy_values)

    # Now, you can access the "stockDropdown_main" value from the first dictionary
    first_stock_dropdown_value = all_strategy_values_sysmbol[0].get("stockDropdown_main", None)

    # Print the result
    print('stockDropdown_main value from the first index:', first_stock_dropdown_value)

    main_indices_symbol = ""  # Initialize with a default value
    if first_stock_dropdown_value == "NIFTY":
        main_indices_symbol = "NSE:NIFTY 50"
    elif first_stock_dropdown_value == "BANKNIFTY":
        main_indices_symbol = "NSE:NIFTY BANK"
    elif first_stock_dropdown_value == "FINNIFTY":
        main_indices_symbol = "NSE:NIFTY FIN SERVICE"

    print(main_indices_symbol)



    # Function to get enctoken
    def get_enctoken(userid, password, twofa):
        session = requests.Session()
        response = session.post('https://kite.zerodha.com/api/login', data={
            "user_id": userid,
            "password": password
        })
        response = session.post('https://kite.zerodha.com/api/twofa', data={
            "request_id": response.json()['data']['request_id'],
            "twofa_value": twofa,
            "user_id": response.json()['data']['user_id']
        })
        enctoken = response.cookies.get('enctoken')
        if enctoken:
            # Save the enctoken to a text file
            with open('enctoken.txt', 'w') as file:
                file.write(enctoken)
            return enctoken
        else:
            raise Exception("Enter valid details !!!!")

 # Function to read enctoken from file
    def read_enctoken():
        try:
            with open('enctoken.txt', 'r') as file:
                enctoken = file.read().strip()
            return enctoken
        except FileNotFoundError:
            return None

    # Replace these with your actual Zerodha credentials
    zerodha_username = zerodha_username
    zerodha_password = zerodha_password
    totp_secret = totp_secret

    # Try to read enctoken from the file
    enctoken = read_enctoken()

    # If enctoken is not available or invalid, generate a new one
    if not enctoken:
        # Generate TOTP
        totp = pyotp.TOTP(totp_secret)
        otp = totp.now()

        # Get enctoken using the provided function
        enctoken = get_enctoken(zerodha_username, zerodha_password, otp)

    print(f"Enctoken: {enctoken}")

    # Check if login was successful
    if enctoken:
        # Create ZerodhaAPI instance
        zerodha_api = ZerodhaAPI(enctoken)

        # Fetch user profile
        user_profile = zerodha_api.get_user_profile()
        if user_profile:
            print(f"User Profile: {user_profile}")
            ohlc_market_indepth = zerodha_api.quote(main_indices_symbol)
            print(ohlc_market_indepth)


            first_key = list(ohlc_market_indepth.keys())[0]

            # Extract last_price
            last_price = ohlc_market_indepth[first_key]['last_price']

            # Round to the nearest 50 or 100
            rounded_price_50 = round(last_price / 50) * 50
            rounded_price_100 = round(last_price / 100) * 100

            # Choose the closest rounding
            closest_price = rounded_price_50 if abs(last_price - rounded_price_50) < abs(last_price - rounded_price_100) else rounded_price_100
            print(closest_price)
                        
            orders_data = json.loads(all_strategy_values)
            # Update the values in all_strategy_values
            for strategy in orders_data:
                strategy['real_strike_price'] = int(strategy['main_strikePrice_values']) + int(closest_price)
                strategy['ultimate_trading_symbol'] = strategy['main_trading_symbol'].replace(strategy['strikePrice_order_window'], str(strategy['real_strike_price']))


            print("orders_data1",orders_data)

            all_orders=[]
            for order_data in orders_data:
                print("New Trade",order_data["ultimate_trading_symbol"])
                order = zerodha_api.place_order(

                variety=zerodha_api.VARIETY_REGULAR,
                exchange=zerodha_api.EXCHANGE_NFO,
                tradingsymbol=order_data["ultimate_trading_symbol"],
                transaction_type=order_data["sell_buy_indicator"],  # Assuming "SELL" as per your data
                quantity=order_data["Quantity"],
                product=zerodha_api.PRODUCT_NRML,  # Assuming "MIS" as per your data
                order_type=zerodha_api.ORDER_TYPE_MARKET,  # Assuming "LIMIT" as per your data
                price=order_data["price"],
                validity=zerodha_api.VALIDITY_DAY,
                disclosed_quantity=0,
                trigger_price=0,
                squareoff=0,
                stoploss=0,
                trailing_stoploss=0 )

                all_orders.append(order)


            current_user = User.objects.get(id=user_id)

            # Create a sample StrategyScheduleTaskResult instance with example values
            sample_result = StrategyScheduleTaskResult.objects.create(
                                strategy_name=custom_field_value,
                                broker_name="Zerodha",
                                broker_profile=user_profile,
                                user=current_user,
                                order_data=orders_data,
                                result_data=all_orders,
                                scheduled_time=timezone.now()  # Set scheduled_time to current date and time
                            )



            return all_orders
      

        else:
            # If fetching user profile fails, regenerate the enctoken and try again
            print("Failed to fetch user profile. Regenerating enctoken...")
            # Generate TOTP
            totp = pyotp.TOTP(totp_secret)
            otp = totp.now()

            # Get enctoken using the provided function
            enctoken = get_enctoken(zerodha_username, zerodha_password, otp)

            # Create ZerodhaAPI instance with the new enctoken
            zerodha_api = ZerodhaAPI(enctoken)

            # Fetch user profile again
            user_profile = zerodha_api.get_user_profile()
            if user_profile:
                print(f"User Profile: {user_profile}")
                ohlc_market_indepth = zerodha_api.quote(main_indices_symbol)
                    
                first_key = list(ohlc_market_indepth.keys())[0]

                # Extract last_price
                last_price = ohlc_market_indepth[first_key]['last_price']

                # Round to the nearest 50 or 100
                rounded_price_50 = round(last_price / 50) * 50
                rounded_price_100 = round(last_price / 100) * 100

                # Choose the closest rounding
                closest_price = rounded_price_50 if abs(last_price - rounded_price_50) < abs(last_price - rounded_price_100) else rounded_price_100
                            
                orders_data = json.loads(all_strategy_values)
                # Update the values in all_strategy_values
                for strategy in orders_data:
                    strategy['real_strike_price'] = int(strategy['main_strikePrice_values']) + int(closest_price)
                    strategy['ultimate_trading_symbol'] = strategy['main_trading_symbol'].replace(strategy['strikePrice_order_window'], str(strategy['real_strike_price']))


                print("orders_data1",orders_data)

                all_orders=[]
                for order_data in orders_data:
                    print("New Trade",order_data["ultimate_trading_symbol"])
                    order = zerodha_api.place_order(

                    variety=zerodha_api.VARIETY_REGULAR,
                    exchange=zerodha_api.EXCHANGE_NFO,
                    tradingsymbol=order_data["ultimate_trading_symbol"],
                    transaction_type=order_data["sell_buy_indicator"],  # Assuming "SELL" as per your data
                    quantity=order_data["Quantity"],
                    product=zerodha_api.PRODUCT_NRML,  # Assuming "MIS" as per your data
                    order_type=zerodha_api.ORDER_TYPE_MARKET,  # Assuming "LIMIT" as per your data
                    price=order_data["price"],
                    validity=zerodha_api.VALIDITY_DAY,
                    disclosed_quantity=0,
                    trigger_price=0,
                    squareoff=0,
                    stoploss=0,
                    trailing_stoploss=0 )

                    all_orders.append(order)

                current_user = User.objects.get(id=user_id)

                # Create a sample StrategyScheduleTaskResult instance with example values
                sample_result = StrategyScheduleTaskResult.objects.create(
                    strategy_name=custom_field_value,
                    broker_name="Zerodha",
                    broker_profile=user_profile,
                    user=current_user,
                    order_data=orders_data,
                    result_data=all_orders,
                    scheduled_time=timezone.now()  # Set scheduled_time to current date and time
                )

    

                return all_orders
            else:
                print("Failed to fetch user profile even after regenerating enctoken.")
    else:
        print("Login failed.")

            


    # return f"Addition Task for {user.username} completed: {number1} + {number2} = {result}"

from django.template.loader import render_to_string
from .models import PromotionalEmail
import css_inline
from .models import Subscriber
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime 
from django.utils.html import strip_tags


@shared_task
def send_newsletter_emails():
    subscribers = Subscriber.objects.filter(active=True)
    
    # Define API endpoints
    api_endpoints = {
        'stock_index': 'https://webapi.niftytrader.in/webapi/symbol/stock-index-data',
        'global_market': 'https://webapi.niftytrader.in/webapi/usstock/global-market',
        'top_gainers': 'https://webapi.niftytrader.in/webapi/Symbol/top-gainers-historical-data?range_type=gainers&range_days=1day',
        'top_losers': 'https://webapi.niftytrader.in/webapi/Symbol/top-gainers-historical-data?range_type=loosers&range_days=1day',
        'world_news': 'https://webapi.niftytrader.in/webapi/Other/rss-feeds-data?NewsType=WorldNews&lanType=English',
        # Add more API endpoints as needed
    }
    
    collected_data = {}
    
    for key, endpoint in api_endpoints.items():
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            data = response.json().get('resultData', [])
            collected_data[key] = data
        else:
            return {'error': f'Failed to fetch data from {endpoint}.'}
        
    # Pass the collected data to the email template
    # Get today's date
    today_date = datetime.datetime.now().strftime('%d %B, %Y')
    
    # Construct subject with today's date
    subject = f'Fwd: Daily Pointer - {today_date}'
    html_content = render_to_string('news_letter_data_template.html', {'collected_data': collected_data})
    
    html_content_inline =css_inline.inline(html_content)

    for subscriber in subscribers:
        # Send email to each subscriber
        send_mail(subject, '', None, [subscriber.email], html_message=html_content_inline)
  

    return ({'message': 'Promotional emails sent successfully!'})