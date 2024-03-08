from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.http import HttpRequest
from user_agents import parse

from .models import UserLoginHistory

import socket

from geolite2 import geolite2

import json
import requests
def get_country_from_ip(ip_address):
    try:
        response = requests.get(f"https://geolocation-db.com/json/{ip_address}&position=true").json()
        return response.country_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@receiver(user_logged_in)
def user_login_handler(sender, request, user, **kwargs):
    # Get the user's IP address
    ip_address = get_client_ip(request)
     

    country = get_country_from_ip(ip_address)
    # Save login history

    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_info = parse(user_agent)
    
    # Extract browser name and version
    browser = user_agent_info.browser.family
    browser_version = user_agent_info.browser.version_string

    

    print(f"User {user.username} logged in from IP address {ip_address}")
    UserLoginHistory.objects.create(user=user, ip_address=ip_address, action='Login',  browser=browser, browser_version=browser_version, origin=country)



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