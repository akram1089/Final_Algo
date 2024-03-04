from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.http import HttpRequest
from user_agents import parse

from .models import UserLoginHistory

import socket

from geolite2 import geolite2

import json

def get_country_from_ip(ip_address):

    reader = geolite2.reader()

    try:
        # Lookup the IP address in the GeoLite2 database
        match = reader.get(ip_address)
        if match:
            # Extract the country name from the match
            country = match['country']['names']['en']
            print(country)
            return country
        else:
            return "Unknown"
    finally:
        # Close the reader to release resources
        geolite2.close()
        return "Unkown"

@receiver(user_logged_in)
def user_login_handler(sender, request, user, **kwargs):
    # Get the user's IP address
    ip_address = request.META.get('REMOTE_ADDR')

    country = get_country_from_ip(ip_address)
    # Save login history

    user_agent = request.META.get('HTTP_USER_AGENT', '')
    user_agent_info = parse(user_agent)
    
    # Extract browser name and version
    browser = user_agent_info.browser.family
    browser_version = user_agent_info.browser.version_string

    

    print(f"User {user.username} logged in from IP address {ip_address}")
    UserLoginHistory.objects.create(user=user, ip_address=ip_address, action='Login',  browser=browser, browser_version=browser_version, origin=country)

@receiver(user_logged_out)
def user_logout_handler(sender, request, user, **kwargs):
    # Get the user's IP address
    ip_address = request.META.get('REMOTE_ADDR')
    # Save logout history
    print(f"User {user.username} logged out from IP address {ip_address}")
    UserLoginHistory.objects.create(user=user, ip_address=ip_address, action='Logout')