import pprint
import time
from django.shortcuts import get_object_or_404, render
import requests
import time
import pyotp
from urllib.parse import parse_qs, urlparse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint
from django.contrib.auth import authenticate, login, logout

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
from selenium import webdriver
from pyotp import TOTP

from django.contrib.auth import get_user_model
User = get_user_model()


from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home if user is already logged in
    else:
        return render(request, 'login.html')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('/')  # Redirect to home if user is already logged in
    else:
        return render(request, 'sign_up.html')
def landing_page(request):
    return render(request,"landing_page.html")
def broker_details(request):
    return render(request,"broker_details.html")



def logout_user(request):
    logout(request)

    return redirect("/")



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print("ipmain",ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print("ipmain",ip)
    return ip



# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import pyotp
import datetime


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import pyotp
import json

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt  # Only use this decorator for testing purposes. In production, implement proper CSRF protection.
def user_signUp(request):
    if request.method == 'POST':
        try:
            # Deserialize the JSON data received from the AJAX request
            data = json.loads(request.body)
            print(data)

            # Extract form fields from the data
            name = data.get('name')
  
            phone_code = data.get('phone_code')
            mobile = data.get('mobile')
            password = data.get('password')
            confirm_password = data.get('Cofirm_password')
            terms_of_service = data.get('terms_of_service')

            # Perform your signup logic here

            # Example: Dummy response


            # if User.objects.filter(Mobile_number=mobile, is_active=True).exists():
            #     return JsonResponse({'error': 'Phone number already registered'}, status=400)

            # user = User.objects.create_user(full_name=name, password=password,Phone_code=phone_code, Mobile_number=mobile,confirm_password=confirm_password,terms_of_service=terms_of_service,is_active=False)
            # user.save()
            secret_key = pyotp.random_base32()

            print(secret_key)
     

            totp = pyotp.TOTP(secret_key, interval=600)
            otp_value = totp.now()
            print(otp_value)
           
            user_ip = get_client_ip(request)
            print("user_ip",user_ip)
            # Replace the placeholder values with your actual credentials and recipient number
            api_url = "https://login5.spearuc.com/MOBILE_APPS_API/sms_api.php"
            user_name = "kozytran"
            password = "987654"
            sender = "KOZYKR"
            to_mobileno = mobile  # Replace XXX with the actual recipient number
            name= name
            otp_num = otp_value
            sms_text = f"{otp_value } is the OTP to verify your mobile number with Kozy. OTP is valid for 10 mins. Do not share with anyone - By Kozy Kreative"
            t_id="1707170678076165075"

            # Call the function to send the SMS
            send_sms(api_url, user_name, password, sender, to_mobileno, sms_text,t_id)

        # Send OTP via SMS using your local SMS provider here
            response_data = {'status': 'success', 'message': 'OTP has been sent you mobile number !','secret_key':secret_key}
            return JsonResponse(response_data)


        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

        
@csrf_exempt
def resend_user_signup(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            print(data)

            secret_key = data.get('UserID')
            print(secret_key)
            name = data.get('name')
            mobile = data.get('mobile')
            

            # Check if the user with the given ID exists
            
        except User.DoesNotExist:
            return JsonResponse({'status': False, 'message': 'User not found'})


        # Generate OTP using the user's secret key
        totp = pyotp.TOTP(secret_key, interval=600)
        otp_value = totp.now()

        # Print for testing purposes (consider removing in production)
        print(f"Generated OTP for User : {otp_value}")

        # Replace the placeholder values with your actual credentials and recipient number
        api_url = "https://login5.spearuc.com/MOBILE_APPS_API/sms_api.php"
        user_name = "kozytran"
        password = "987654"
        sender = "KOZYKR"
        to_mobileno = mobile  # Replace XXX with the actual recipient number
        name = name
        sms_text = f"{otp_value } is the OTP to verify your mobile number with Kozy. OTP is valid for 10 mins. Do not share with anyone - By Kozy Kreative"
        t_id = "1707170678076165075"
      #var#} is the OTP to verify your mobile number with Kozy. OTP is valid for 10 mins. Do not share with anyone - By Kozy Kreative
        # Call the function to send the SMS
        send_sms(api_url, user_name, password, sender, to_mobileno, sms_text, t_id)

        return JsonResponse({"status": True, "message": "OTP has been resent to your number!"})
    else:
        return JsonResponse({'status': False, 'message': 'Invalid request method'})


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        # Parse JSON data from the request body
        data = request.data
        print(data)

        # Access the 'UserID' from the parsed data
        secret_key = data.get('UserID')
                # Extract form fields from the data
        name = data.get('name')

        phone_code = data.get('phone_code')
        mobile = data.get('mobile')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        terms_of_service = data.get('terms_of_service')

        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return JsonResponse({'success': False, 'message': 'User not found'})

        otp_value = data.get('modalOTPSignUp')
        
        if User.objects.filter(Mobile_number=mobile, is_active=True).exists():
            return JsonResponse({'error': 'Phone number already registered'}, status=400)




        # Assuming otp_value is the entered OTP
        # pyotp.TOTP(user.secret,interval=30).verify(otp_value)

        veri_otp =pyotp.TOTP(secret_key,interval=600)
        print(secret_key)
        print(verify_otp)
        print(veri_otp.now())
        user_ip = get_client_ip(request)


        if veri_otp.verify(otp_value):
            user = User.objects.create_user(full_name=name, password=password,Phone_code=phone_code, Mobile_number=mobile,confirm_password=confirm_password,terms_of_service=terms_of_service,secret_key=secret_key,ip_address_user=user_ip)
            user.save()
            print(user.is_active)
    

            return JsonResponse({'success': True, 'message': 'You are successfully signup !'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid OTP'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})



def all_users(request):
    users = User.objects.all()
    print(users)
    user_list = [{'id': user.id, 'username': user.username,'ip_address':user.ip_address ,'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'date_joined': user.date_joined, 'last_login': user.last_login} for user in users]
    
    return JsonResponse({'users': user_list})

def send_sms(api_url, user_name, password, sender, to_mobileno, sms_text,t_id):
    print(sms_text)
    # Construct the URL with the provided parameters
    url = f"{api_url}?type=smsquicksend&user={user_name}&pass={password}&sender={sender}&to_mobileno={to_mobileno}&sms_text={sms_text}&t_id={t_id}"
    print(url)
    try:
        # Make the GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("SMS sent successfully.")
        else:
            print(f"Failed to send SMS. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")



@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        Mobile_number = request.POST['phone_number']
        password = request.POST['password']
        print(Mobile_number, password)
        user_ip = get_client_ip(request)
        print("user_ip",user_ip)
     
        user = authenticate(Mobile_number=Mobile_number, password=password)
        if user is not None:
            if user.ip_address_user != user_ip:
                print("Your account logged in different device !!")
            login(request, user)
            if request.user.is_superuser:
               
                return redirect("/")
            else:
            
                return redirect("/")
        else:
   
            return redirect("/")



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json
from .models import Broker  # Make sure to import your Broker model or adjust as needed

@csrf_exempt

def add_broker_api_main(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        user = request.user

        # Ensure the user is logged in
        if not user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Please login first !'})

        trading_platform = data.get('trading_platform')

        if trading_platform == 'zerodha_kite':
            return add_zerodha_broker(request, data)
        elif trading_platform == 'smart_api':
            return add_angel_one_broker(request, data)
        elif trading_platform == 'upstox_api':
            return add_upstox_broker(request, data)
        else:
            return JsonResponse({"message": "Unsupported trading platform"}, status=400)

    elif request.method == 'GET':
        user = request.user

        # Ensure the user is logged in
        if not user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Please login first !'})

        brokers = Broker.objects.filter(user=user).values()
        brokers_json = list(brokers)
        return JsonResponse({'brokers': brokers_json})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

from .models import Broker
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
# from django.contrib.auth.models import User  # Import the User model

import pyotp

def get_enctoken_internal(zerodha_username, zerodha_password, totp_secret):
    try:
        totp = pyotp.TOTP(totp_secret)
        otp = totp.now()
        print(otp)

        session = requests.Session()
        login_response = session.post('https://kite.zerodha.com/api/login', data={
            "user_id": zerodha_username,
            "password": zerodha_password
        })
        
        if login_response.status_code != 200 or 'data' not in login_response.json():
            return "Error in login: {}".format(login_response.text)

        twofa_response = session.post('https://kite.zerodha.com/api/twofa', data={
            "request_id": login_response.json()['data']['request_id'],
            "twofa_value": otp,
            "user_id": login_response.json()['data']['user_id']
        })

        if twofa_response.status_code != 200 or 'enctoken' not in twofa_response.cookies:
            return "Error in two-factor authentication: {}".format(twofa_response.text)

        enctoken = twofa_response.cookies.get('enctoken')

        if enctoken:
            return enctoken
        else:
            return "Invalid TOTP"

    except Exception as e:
        return str(e)



def add_zerodha_broker(request, data):
    user = request.user
    logging_id = data.get('logging_id')

    # Check if logging_id already exists
    if Broker.objects.filter(user=user, logging_id=logging_id).exists():
        return JsonResponse({"message": "You have already logged in with this login ID !!"}, status=400)

    broker_name = data.get('broker_name')
    password = data.get('password')
    totp_key = data.get('totp_key')
    fa_pin = data.get('fa_pin', '')
    phone_number = data.get('phone_number', '')
    api_key = data.get('api_key', '')
    api_secret = data.get('api_secret', '')
    app_name = data.get('app_name')
    advanceTotpSecurity = data.get('advanceTotpSecurity')

    enctoken = get_enctoken_internal(logging_id, password, totp_key)
    
    if enctoken:
        zerodha_api = GetEncToken(enctoken)
        user_profile = zerodha_api.get_user_profile()
        
        if user_profile:
            print(f"User Profile: {user_profile}")

            # Save enctoken to the Broker model
            broker = Broker.objects.create(
                user=user,
                broker_name=broker_name,
                trading_platform='zerodha_kite',
                logging_id=logging_id,
                password=password,
                totp_key=totp_key,
                fa_pin=fa_pin,
                phone_number=phone_number,
                api_key=api_key,
                api_secret=api_secret,
                app_name=app_name,
                enctoken=enctoken,
                advance_totp_security=advanceTotpSecurity.lower() == 'yes',
                added_at=timezone.now(),
                updated_at=timezone.now()
            )

            return JsonResponse({"message": "Broker added successfully"})
        else:
            return JsonResponse({"message": "Invalid API credentials"}, status=400)
    else:
        return JsonResponse({"message": "Failed to generate enctoken"}, status=400)


class GetEncToken:
    def __init__(self, enctoken):
        self.headers = {"Authorization": f"enctoken {enctoken}"}
        self.session = requests.Session()
        self.root_url = "https://kite.zerodha.com/oms"
        self.session.get(self.root_url, headers=self.headers)

    def get_user_profile(self):
        profile_url = f"{self.root_url}/user/profile/full"
        response = self.session.get(profile_url, headers=self.headers)
        return response.json() if response.status_code == 200 else None
 







# def handle_broker(user, broker_name, trading_platform, logging_id, password, totp_key,
#                   fa_pin, phone_number, api_key, api_secret, app_name):
#     try:
#         broker = Broker.objects.get(user=user, broker_name=broker_name, app_name=app_name)
#     except Broker.DoesNotExist:
#         # If the broker doesn't exist, create a new one for the current user
#         broker = Broker.objects.create(
#             user=user,
#             broker_name=broker_name,
#             trading_platform=trading_platform,
#             logging_id=logging_id,
#             password=password,
#             totp_key=totp_key,
#             fa_pin=fa_pin,
#             phone_number=phone_number,
#             api_key=api_key,
#             api_secret=api_secret,
#             app_name=app_name,
#             active_api=False,
#             added_at=timezone.now(),
#             updated_at=timezone.now(),
#         )
#         return {'status': 'success', 'message': 'Broker added successfully'}
#     else:
#         # If the broker already exists, update its fields
#         broker.trading_platform = trading_platform
#         broker.logging_id = logging_id
#         broker.password = password
#         broker.totp_key = totp_key
#         broker.fa_pin = fa_pin
#         broker.phone_number = phone_number
#         broker.api_key = api_key
#         broker.api_secret = api_secret
#         broker.updated_at = timezone.now()
#         broker.save()
#         return {'status': 'success', 'message': 'Broker updated successfully'}
    















import requests
import json
from django.http import HttpResponse
from home.models import Broker  # Replace 'your_app' with the actual name of your Django app

class ZerodhaPlaceOrder:
    def __init__(self, enctoken):
        # print("enctoken  :" + enctoken)
        self.headers = {"Authorization": f"enctoken {enctoken}"}
        self.session = requests.Session()
        self.root_url = "https://kite.zerodha.com/oms"
        self.session.get(self.root_url, headers=self.headers)

    def get_user_profile(self):
        profile_url = f"{self.root_url}/user/profile/full"
        response = self.session.get(profile_url, headers=self.headers)
        return response.json() if response.status_code == 200 else None

    def calc_margin(self, order_params):

        print("order_params",order_params)
        order_url = f"{self.root_url}/margins/basket?consider_positions=&mode=compact"
        response = self.session.post(order_url, json=order_params, headers=self.headers)
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
    def cancel_order(self, variety, order_id, parent_order_id=None):
        order_id = self.session.delete(f"{self.root_url}/orders/{variety}/{order_id}",
                                       data={"parent_order_id": parent_order_id} if parent_order_id else {},
                                       headers=self.headers).json()["data"]["order_id"]
        return order_id
    
    
    def orders(self):
        orders = self.session.get(f"{self.root_url}/orders", headers=self.headers).json()["data"]
        return orders




    





def add_angel_one_broker(request, data):
    # Handle the logic for 'smart_api' trading platform
    print("Handling 'smart_api' broker addition:")
    
    # Print each data individually
    print("Broker Name:", data.get('broker_name'))
    print("Trading Platform:", data.get('trading_platform'))
    print("Logging ID:", data.get('logging_id'))
    print("Password:", data.get('password'))
    print("TOTP Key:", data.get('totp_key'))
    print("API Key:", data.get('api_key'))
    print("App Name:", data.get('app_name'))

    try:
        trading_plateform =data.get('trading_platform')
        broker_name = data.get('broker_name')
  
    
        fa_pin = data.get('fa_pin', '')
        phone_number = data.get('phone_number', '')

        api_secret = data.get('api_secret', '')
        app_name = data.get('app_name')
        api_key = data.get('api_key')
        clientId = data.get('logging_id')
        pwd = data.get('password')
        smartApi = SmartConnect(api_key)
        token = data.get('totp_key')
        advanceTotpSecurity = data.get('advanceTotpSecurity')
        totp = pyotp.TOTP(token).now()
        
        data = smartApi.generateSession(clientId, pwd, totp)
        authToken = data['data']['jwtToken']
        refreshToken = data['data']['refreshToken']

        # fetch the feedtoken
        feedToken = smartApi.getfeedToken()

        print("Feed Token:", feedToken)

        # Check if getting the profile is successful
        profile_data = smartApi.getProfile(feedToken)

        if profile_data :
            # Extract relevant data from the profile_data
            print(profile_data)
            



            if Broker.objects.filter(user=request.user, logging_id=clientId).exists():
              return JsonResponse({"message": "You have already logged in with this login ID !!"}, status=400)

            # Save the data to the Broker model
            broker = Broker.objects.create(
                user=request.user,
                broker_name=broker_name,
                trading_platform=trading_plateform,
                logging_id=clientId,
                password=pwd,
                totp_key=token,
                fa_pin=fa_pin,
                phone_number=phone_number,
                api_key=api_key,
                api_secret=api_secret,
                app_name=app_name,
                advance_totp_security=advanceTotpSecurity.lower() == 'yes',
                enctoken=feedToken,  # You may need to generate enctoken or adjust this field based on your requirements
                added_at=timezone.now(),
                updated_at=timezone.now()
            )

            return JsonResponse({"message": "'smart_api' broker added successfully"})
    except Exception as e:
        print("Error adding 'smart_api' broker:", str(e))
        return JsonResponse({"message": "Your API details are incorrect or an error occurred"}, status=400)


def add_upstox_broker(request ,data):
    print("Broker Name:", data.get('broker_name'))
    print("Trading Platform:", data.get('trading_platform'))
    print("Logging ID:", data.get('logging_id'))
    print("Password:", data.get('password'))
    print("TOTP Key:", data.get('totp_key'))
    print("API Key:", data.get('api_key'))
    print("App Name:", data.get('app_name'))

    api_key= data.get("api_key")
    app_name= data.get("app_name")
    broker_name= data.get("broker_name")
    password= data.get("password")
    phone_number_val= data.get("phone_number_val")
    secret_key= data.get("secret_key")
    totp_key= data.get("totp_key")
    trading_plateform= data.get("trading_platform")
    logging_id= data.get("logging_id")
    fa_pin = data.get('fa_pin', '')
    advanceTotpSecurity = data.get('advanceTotpSecurity')


                         
    USER_ID=logging_id
    API_KEY = api_key
    SECRET_KEY = secret_key
    RURL = 'https://apix.stocksdeveloper.in/oauth/upstox'

    TOTP_KEY =totp_key
    MOBILE_NO = phone_number_val
    PIN =password


    def get_access_token(code):
        url = 'https://api-v2.upstox.com/login/authorization/token'
        headers = {
            'accept': 'application/json',
            'Api-Version': '2.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'code': code,
            'client_id': API_KEY,
            'client_secret': SECRET_KEY,
            'redirect_uri': RURL,
            'grant_type': 'authorization_code'
        }
        response = requests.post(url, headers=headers, data=data)
        json_response = response.json()
        # Access the response data
        # print(f"access_token:  {json_response['access_token']}")
        return json_response['access_token']


    def run_selenium():
        AUTH_URL = f'https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={API_KEY}&redirect_uri={RURL}'

        chrome_options = Options()  
        chrome_options.add_argument("--disable-web-security") 
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--log-level=1')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        chrome_options.add_argument("--enable-logging")

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        browser.get(AUTH_URL)
        browser.implicitly_wait(10)
        mobile_num_input_xpath = browser.find_element("xpath", "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div/div/div/div/div/div/input")
        mobile_num_input_xpath.send_keys(MOBILE_NO)
        time.sleep(1)

        browser.find_element("xpath", "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div/button").click()
        time.sleep(1)
        # browser.save_screenshot("screenshot1.png")
        otp_input_xpath = browser.find_element("xpath", "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]/div/div/div/input")
        totp = TOTP(TOTP_KEY)
        token = totp.now()
        time.sleep(1)
        # browser.save_screenshot("screenshot1-2.png")

        otp_input_xpath.send_keys(token)

        browser.find_element("xpath","/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(1)
        # browser.save_screenshot("screenshot2.png")

        twofa_input_xpath=browser.find_element("xpath","/html/body/main/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div/div/div/div/div/input")
        twofa_input_xpath.send_keys(PIN)
        browser.find_element("xpath","/html/body/main/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/form/button").click()
        time.sleep(1)
        # browser.save_screenshot("screenshot3.png")

        WebDriverWait(browser, 5).until(EC.url_contains(RURL))
        code = parse_qs(urlparse(browser.current_url).query)['code'][0]

        # Save screenshot
        # browser.save_screenshot("screenshot_final.png")

        return code

    # Run Selenium to get the code and then obtain the access token
    code = run_selenium()
    if code:
        access_token = get_access_token(code)
        print(access_token)
        
    # Configure OAuth2 access token for authorization: OAUTH2
        configuration = upstox_client.Configuration()
        configuration.access_token = access_token

        # create an instance of the API class
        api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))
        api_version = 'api_version_example' # str | API Version Header

        try:
            # Get profile
            api_response = api_instance.get_profile(api_version)
            pprint(api_response)

            
            if Broker.objects.filter(user=request.user, logging_id=USER_ID).exists():
              return JsonResponse({"message": "You have already logged in with this login ID !!"}, status=400)

            # Save the data to the Broker model
            broker = Broker.objects.create(
                user=request.user,
                broker_name=broker_name,
                trading_platform=trading_plateform,
                logging_id=USER_ID,
                password=password,
                totp_key=TOTP_KEY,
                fa_pin=fa_pin,
                phone_number=MOBILE_NO,
                api_key=API_KEY,
                api_secret=SECRET_KEY,
                app_name=app_name,
                enctoken=access_token,  # You may need to generate enctoken or adjust this field based on your requirements
                advance_totp_security=advanceTotpSecurity.lower() == 'yes',
                added_at=timezone.now(),
                updated_at=timezone.now()
            )




            return JsonResponse({"message": "'Upstox' broker added successfully"})
        except ApiException as e:
            print("Exception when calling UserApi->get_profile: %s\n" % e)
    else:
        print("Error retrieving code.")




def check_user_logged_in(request):
    if request.user.is_authenticated:
        return JsonResponse({'message': 'User is logged in.'})
    else:
        return JsonResponse({'user_logged_in': 'User not logged in.'})
    



@csrf_exempt
def delete_broker(request):
    # Ensure the request is a POST method
    if request.method == 'POST':
        # Get the broker ID from the AJAX request
        broker_id = request.POST.get('brokerId')
        print(broker_id)

        # Get the current user
        current_user = request.user

        # Get the broker or return a 404 response if not found
        broker = get_object_or_404(Broker, id=broker_id, user=current_user)

        # Delete the broker
        broker.delete()

        return JsonResponse({'message': 'Broker deleted successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)




@csrf_exempt

def verify_active_api(request):
    broker_id = request.POST.get('broker_id')

    print(broker_id)
 

    # Get the user associated with the broker
    user = request.user

    # Set is_active to False for all brokers of this user


    # Set is_active to True for the specified broker
    broker = get_object_or_404(Broker, pk=broker_id, user=user)
    print("broker.advance_totp_security",broker.advance_totp_security)
    if broker.advance_totp_security :

        
        return JsonResponse({"advance_activation":"active"})
    else:
        return JsonResponse({"advance_activation":"inactive"})


@csrf_exempt
def verify_otp_api_activation(request):
    broker_id = request.POST.get('broker_id')
    api_activation_otp = request.POST.get('api_activation_otp')

    print(broker_id)
 

    # Get the user associated with the broker
    user = request.user

    # Set is_active to False for all brokers of this user


    # Set is_active to True for the specified broker
    broker = get_object_or_404(Broker, pk=broker_id, user=user)
    print("broker.advance_totp_security",broker.advance_totp_security)
    secret_key = broker.totp_key
    otp = TOTP(secret_key)
# Generate an OTP using TOTP after every 60 seconds

    print(otp.now())
    now_totp = otp.now()




    if now_totp==api_activation_otp:
        return JsonResponse({'otp_verify':"success"})
       
        
    else:
        return JsonResponse({'otp_verify':"failed"})

@csrf_exempt

def update_active_api(request):
    broker_id = request.POST.get('broker_id')
    is_active = request.POST.get('is_active') == 'true'  # Convert the string to a boolean

    # Get the user associated with the broker
    user = request.user

    # Set is_active to False for all brokers of this user
    Broker.objects.filter(user=user).exclude(pk=broker_id).update(active_api=False)

    # Set is_active to True for the specified broker
    broker = get_object_or_404(Broker, pk=broker_id, user=user)
    broker.active_api = is_active
    broker.save()

    return JsonResponse({'message': 'API activation status updated successfully'})




def get_api_config_data(request):
    if request.method == 'GET':
        user = request.user

        # Ensure the user is logged in
        if not user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Please login first !'})

        brokers = Broker.objects.filter(user=user).values()
        brokers_json = list(brokers)
        return JsonResponse({'brokers': brokers_json})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    






def account_details(request):
    return render(request,"account_details.html")




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required
@csrf_exempt
def get_user_data(request):
    user = request.user

    print("user",user)
    print("user.first_name",user.first_name)
    full_name = user.full_name if user.full_name else f"{user.first_name} {user.last_name}"
    data = {
        'id': user.id,
        'username': user.username,
        'full_name': full_name,
        'email': user.email,
        'Mobile_number': user.Mobile_number,
        'Phone_code': user.Phone_code,
        'Country': user.Country,
        'State': user.State,
        # Add other fields as needed
    }

    return JsonResponse(data)


@csrf_exempt
def update_user_data(request):
    if request.method == 'POST':
        # Get data from POST request
        user_id = request.POST.get('id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        state = request.POST.get('state')
        mobile_num = request.POST.get('mobile_num')

        # Perform update operation, replace this with your logic
        user = User.objects.get(id=user_id)
        user.full_name = full_name
        user.email = email
        user.State = state
        user.Mobile_number = mobile_num
        user.save()

        # Return success or failure response
        return JsonResponse({'success': True})  # You can customize the response as needed



from .models import UserLoginHistory

def user_login_history(request):
    user_login_history = UserLoginHistory.objects.filter(user=request.user, action="Login").order_by('-login_time')[:10]
    
    # Convert login history queryset to JSON format
    login_history_data = []
    for entry in user_login_history:
        login_history_data.append({
            'ip_address': entry.ip_address,
            'login_time': entry.login_time,  # Format login time
            'browser': entry.browser,
            'browser_version': entry.browser_version,
            'origin': entry.origin
        })
    
    return JsonResponse(login_history_data, safe=False)








from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserSession
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@receiver(user_logged_in)
def capture_session_key(sender, request, user, **kwargs):
    # Store the session key associated with the login session
    UserSession.objects.create(user=user, session_key=request.session.session_key)

@csrf_exempt
def logout_all_devices(request):
    current_session_key = request.session.session_key
    
    # Get the user's active sessions excluding the current session
    user_sessions = UserSession.objects.filter(user=request.user).exclude(session_key=current_session_key)
    
    # Iterate through the sessions and delete them, except for the current session
    for user_session in user_sessions:
        try:
            # Find and delete the session associated with the session key
            session = Session.objects.get(pk=user_session.session_key)
            session.delete()
        except Session.DoesNotExist:
            pass  # Handle session not found
    
    # Return response without logging out the current device
    return JsonResponse({'message': 'Logged out from all devices except current device'})

def webhooks(request):
    return render(request,"webhooks.html")



from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.urls import reverse

def webhook_urls(request):
    user = request.user
    secret_key = user.secret_key.lower()
    user_id = user.id

    # Get the first site's URL
    site = Site.objects.first()
    site_url = site.domain

    # Construct webhook API URL
    webhook_api = f"{site_url}/webhook_auth_rest/{user_id}/{secret_key}/"

    return JsonResponse({"webhook_api":webhook_api})


    # path('webhook_auth/<str:user_id>/<str:secrect>/', views.webhook_auth, name='webhook_auth'),
@csrf_exempt
def webhook_auth(request, user_id, secret_key):
    print(request.user)
    if str(request.user.id) == user_id and str(request.user.secret_key.lower()) == secret_key:
        if request.method == 'POST':
            try:
                # Parse the JSON data from the request body
                data = json.loads(request.body.decode('utf-8'))
                
                # Process the data as needed
                # For testing purposes, let's just print the received data
                print(data)
                
                # Call the function to process the webhook data
                # order_zerodha_webwooks(data)
                
                # Respond with a success message
                return JsonResponse({"message": "Webhook received successfully"})
            except json.JSONDecodeError as e:
                # Return an error response if JSON decoding fails
                return JsonResponse({"error": "Invalid JSON format"}, status=400)
        else:
            return JsonResponse({"error": "Unsupported method"}, status=405)
    else:
        return HttpResponse("false")







from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_auth_token(request):
    if request.method == 'GET':
        user = request.user  # Retrieve the currently logged-in user
        
        if user.is_authenticated:
            # User authenticated, generate token if not exists
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def order_zerodha_webwooks(data,broker_instance_zerodha):
        print(broker_instance_zerodha)
        data_trade = data
        # print("data_trade", data_trade)
        logging_id = broker_instance_zerodha.logging_id
        password = broker_instance_zerodha.password
        totp_key = broker_instance_zerodha.totp_key


        
        enctoken = get_enctoken_internal(logging_id, password, totp_key)
        print(enctoken)

        # Check if login was successful
        if enctoken:
            zerodha_api = ZerodhaPlaceOrder(enctoken)
            order_details = []

            for trade_data in data_trade:
                tradingsymbol = trade_data.get('main_trading_symbol', '')
                print('tradingsymbol',tradingsymbol)
                sell_buy_indicator = trade_data.get('sell_buy_indicator', '').upper()  # Ensure it's uppercase
                quantity = int(trade_data.get('Quantity', 0))
                price = float(trade_data.get('price', 0))
                mis_select = trade_data.get('mis_select', '').lower()  # Ensure it's lowercase
                isRadioChecked = trade_data.get('isRadioChecked', '')  # assuming 'isRadioChecked' is present in each trade_data

                # Map sell_buy_indicator to TRANSACTION_TYPE
                if sell_buy_indicator == 'BUY':
                    transaction_type = zerodha_api.TRANSACTION_TYPE_BUY
                elif sell_buy_indicator == 'SELL':
                    transaction_type = zerodha_api.TRANSACTION_TYPE_SELL
                else:
                    print(f"Invalid sell_buy_indicator: {sell_buy_indicator}")
                    continue  # Skip processing this trade_data if the indicator is invalid

                # Map mis_select to product type
                if mis_select == 'overnight':
                    product_type = zerodha_api.PRODUCT_NRML
                elif mis_select == 'intraday':
                    product_type = zerodha_api.PRODUCT_MIS
                else:
                    print(f"Invalid mis_select: {mis_select}")
                    continue  # Skip processing this trade_data if the mis_select is invalid

                # Map isRadioChecked to order type
                if isRadioChecked == 'market':
                    order_type = zerodha_api.ORDER_TYPE_MARKET
                elif isRadioChecked == 'limit':
                    order_type = zerodha_api.ORDER_TYPE_LIMIT
                else:
                    print(f"Invalid isRadioChecked: {isRadioChecked}")
                    continue  # Skip processing this trade_data if the isRadioChecked is invalid

                order = zerodha_api.place_order(
                    variety=zerodha_api.VARIETY_REGULAR,
                    exchange=zerodha_api.EXCHANGE_NFO,
                    tradingsymbol=tradingsymbol,
                    transaction_type=transaction_type,
                    quantity=quantity,
                    product=product_type,
                    order_type=order_type,
                    price=price,
                    validity=zerodha_api.VALIDITY_DAY,
                    disclosed_quantity=0,
                    trigger_price=0,
                    squareoff=0,
                    stoploss=0,
                    trailing_stoploss=0,
                )
                order_details.append({
                    'tradingsymbol': tradingsymbol,
                    'transaction_type': transaction_type,
                    'mis_select': mis_select,
                    'order_type': order_type,
                    'order_id': order,
                })

                print(f"Order ID for {tradingsymbol} ({transaction_type}, {mis_select}, {order_type}): {order}")

                # Continue with your logic here, e.g., handling the order response

            return {'status': 'success','broker':'zerodha', 'message': 'Orders placed successfully', 'order_details': order_details}



from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import WebhookResponse

@csrf_exempt
def webhook_auth_rest(request, user_id, secret_key):

    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            
            # Retrieve the user based on the provided user_id
            try:
                user = User.objects.get(id=user_id)
                print(user)
            except User.DoesNotExist:
                return JsonResponse({"message": "User is not authenticated"}, status=401)
            
            # Check if the provided secret_key matches the user's secret_key
            if user.secret_key.lower() == secret_key.lower():
                # Process the data as needed
                # For testing purposes, let's just print the received data
                print(data)
                broker_instance_zerodha = Broker.objects.filter(user=user, broker_name="zerodha", active_api=True).first()
                broker_instance_angelone = Broker.objects.filter(user=user, broker_name="angelone", active_api=True).first()
                print(broker_instance_zerodha)

                if broker_instance_zerodha:
                    zerodha_response = order_zerodha_webwooks(data,broker_instance_zerodha)
                    print("zerodha_response",zerodha_response)

                    # Save the zerodha_response into WebhookResponse model
                    WebhookResponse.objects.create(user=user, zerodha_response_data=zerodha_response)

                    return JsonResponse(zerodha_response)
                else:
                    return JsonResponse({"message":"Unknown Broker or No broker is activated"})    
            else:
                return JsonResponse({"message": "Webhook error"}, status=401)
        except json.JSONDecodeError as e:
            # Return an error response if JSON decoding fails
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)
