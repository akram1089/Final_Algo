
# Create your views here.
import datetime
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'index.html')






# views.py
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from .models import ExchangeData
from .serializers import ExchangeDataSerializer

@csrf_exempt
def get_all_exchange_data(request):
    if request.method == 'GET':
        exchange_data = ExchangeData.objects.all()
        serializer = ExchangeDataSerializer(exchange_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import pyotp
import datetime
from home.models import CustomUser

@api_view(['POST'])
@permission_classes([AllowAny])


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'Phone number already in use'}, status=400)

        user = CustomUser.objects.create_user(username=username, password=password, phone_number=phone_number)
        user.secret_key = pyotp.random_base32()
        user.save()

        totp = pyotp.TOTP(user.secret_key)
        otp_value = totp.now()
        print(otp_value)
        print(user.id)
        print(user.phone_number)
        # Replace the placeholder values with your actual credentials and recipient number
        api_url = "https://login5.spearuc.com/MOBILE_APPS_API/sms_api.php"
        user_name = "kozytran"
        password = "987654"
        sender = "KOZYKR"
        to_mobileno = user.phone_number  # Replace XXX with the actual recipient number
        name= user.username
        otp_num = otp_value
        sms_text = f"Dear {name} , OTP {otp_num} for registration please use it one time. Valid for only 10 minutes KOZY KREATIVE CONCEPTS PRIVATE LIMITED"
        t_id="1707170635727341007"

        # Call the function to send the SMS
        send_sms(api_url, user_name, password, sender, to_mobileno, sms_text,t_id)

        # Send OTP via SMS using your local SMS provider here

        return redirect('verify_otp', user_id=user.id)

    return render(request, 'register.html')



import requests

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























@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def verify_otp(request, user_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=user_id)
        print(user_id)
        otp_value = request.POST.get('otp')
        print(otp_value)

        totp = pyotp.TOTP(user.secret_key)
        print(totp)

        if totp.verify(otp_value):
            login(request, user)
            return redirect('authenticated_home')
        else:
            return redirect('user_login_page')
    elif request.method=="GET":
         if request.user.is_authenticated:
             return redirect('authenticated_home' ,status=400)
         else:
           return render(request, 'verify_otp.html', {'user_id': user_id})

def login_page(request):
     if request.user.is_authenticated:
             return redirect('authenticated_home')
     else:
        return render(request, 'login.html')
     
def user_login_page(request):
     if request.user.is_authenticated:
             return redirect('authenticated_home')
     else:
        return render(request, 'user_login_page.html')
     


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def authenticated_home(request):
    if not request.user.is_authenticated:
        # If the user is not logged in, redirect to the registration page
        return redirect('login')
    
    return render(request, 'authenticated_home.html', {'user': request.user})

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('user_login_page')  # Redirect to the home page or any other desired page




@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')

        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if not user:
            return Response({'error': 'User not found'}, status=400)

        user.secret_key = pyotp.random_base32()
        user.save()

        totp = pyotp.TOTP(user.secret_key)
        otp_value = totp.now()

        # Replace the placeholder values with your actual credentials and recipient number
        api_url = "https://login5.spearuc.com/MOBILE_APPS_API/sms_api.php"
        user_name = "kozytran"
        password = "987654"
        sender = "KOZYKR"
        to_mobileno = user.phone_number  # Replace XXX with the actual recipient number
        name= user.username
        otp_num = otp_value
        sms_text = f"Dear {name} , OTP {otp_num} for registration please use it one time. Valid for only 10 minutes KOZY KREATIVE CONCEPTS PRIVATE LIMITED"
        t_id="1707170635727341007"

        # Call the function to send the SMS
        send_sms(api_url, user_name, password, sender, to_mobileno, sms_text,t_id)
        
        # Send OTP via SMS using your local SMS provider here

        return redirect('verify_otp', user_id=user.id)

    return render(request, 'login.html')




