from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.http import HttpRequest
from user_agents import parse

from .models import UserLoginHistory

import socket



import json
import requests
def get_country_from_ip(ip_address):
    print("ip_address1",ip_address)
    try:
        response = requests.get(f"https://geolocation-db.com/json/{ip_address}&position=true").json()
        # response = requests.get("https://geolocation-db.com/json/117.221.170.145&position=true").json()
        # print(response["country_name"])
        return response["country_name"]
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Unkown"


# @receiver(user_logged_in)
# def user_login_handler(sender, request, user, **kwargs):
#     # Get the user's IP address
#     ip_address = get_client_ip(request)
     

#     country = get_country_from_ip(ip_address)
#     # Save login history

#     user_agent = request.META.get('HTTP_USER_AGENT', '')
#     user_agent_info = parse(user_agent)
    
#     # Extract browser name and version
#     browser = user_agent_info.browser.family
#     browser_version = user_agent_info.browser.version_string

    

#     print(f"User {user.username} logged in from IP address {ip_address}")
#     UserLoginHistory.objects.create(user=user, ip_address=ip_address, action='Login',  browser=browser, browser_version=browser_version, origin=country)




@receiver(user_logged_in)
def user_login_handler(sender, request, user, **kwargs):
    # Get the user's IP address
    ip_address = get_client_ip(request)
     
    # Get country from IP address
    country = get_country_from_ip(ip_address)
    
    # Parse user agent
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    print("User Agent:", user_agent)
    try:
        user_agent_info = parse(user_agent)
        print("Parsed User Agent Info:", user_agent_info)
        
        # Extract browser information
        browser_family = user_agent_info.browser.family
        browser = browser_family.split()[0]  # Extract only the browser name

        print("Browser Family:", browser)
        browser_version = user_agent_info.browser.version_string
        print("Browser Version:", browser_version)

        print(f"User {user.username} logged in from IP address {ip_address}")
        
        # Create login history record
        UserLoginHistory.objects.create(
            user=user,
            ip_address=ip_address,
            action='Login',
            browser=browser,
            browser_version=browser_version,
            origin=country
        )
    except Exception as e:
        print("Error occurred while parsing user agent:", e)

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

@receiver(user_logged_out)
def user_logout_handler(sender, request, user, **kwargs):
    # Get the user's IP address
    ip_address = request.META.get('REMOTE_ADDR')
    # Save logout history
    print(f"User {user.username} logged out from IP address {ip_address}")
    UserLoginHistory.objects.create(user=user, ip_address=ip_address, action='Logout')