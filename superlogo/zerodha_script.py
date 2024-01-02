# Importing necessary modules
import os
import django
import requests
import pyotp
import dateutil.parser

# Setting up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superlogo.settings')
django.setup()

# Importing the Broker model
from home.models import Broker

# ZerodhaAPI class definition
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

    def orders(self):
        orders = self.session.get(f"{self.root_url}/orders", headers=self.headers).json()["data"]
        return orders

    def positions(self):
        positions = self.session.get(f"{self.root_url}/portfolio/positions", headers=self.headers).json()["data"]
        return positions

    def holdings(self):
        holdings = self.session.get(f"{self.root_url}/portfolio/holdings", headers=self.headers).json()["data"]
        return holdings

    def historical_data(self, instrument_token, from_date, to_date, interval, continuous=False, oi=False):
        from_date_str = from_date.strftime('%Y-%m-%d %H:%M:%S')
        to_date_str = to_date.strftime('%Y-%m-%d %H:%M:%S')

        params = {
            "from": from_date_str,
            "to": to_date_str,
            "interval": interval,
            "continuous": 1 if continuous else 0,
            "oi": 1 if oi else 0
        }

        response = self.session.get(
            f"{self.root_url}/instruments/historical/{instrument_token}/{interval}",
            params=params,
            headers=self.headers
        )

        if response.status_code == 200:
            lst = response.json()["data"]["candles"]
            records = []

            for i in lst:
                record = {"date": dateutil.parser.parse(i[0]), "open": i[1], "high": i[2], "low": i[3],
                          "close": i[4], "volume": i[5]}
                if len(i) == 7:
                    record["oi"] = i[6]
                records.append(record)

            return records
        else:
            print(f"Historical data request failed. Status code: {response.status_code}, Message: {response.text}")
            return []

# Function to get enctoken
def get_enctoken(userid, password, twofa):
    session = requests.Session()
    response = session.post('https://kite.zerodha.com/api/login', data={
        "user_id": userid,
        "password": password
    })

    # Checking for successful login before proceeding to two-factor authentication
    if response.status_code != 200:
        raise Exception("Login failed. Check your credentials.")

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
        raise Exception("Failed to obtain enctoken. Please try again.")

# Function to read enctoken from file
def read_enctoken():
    try:
        with open('enctoken.txt', 'r') as file:
            enctoken = file.read().strip()
        return enctoken
    except FileNotFoundError:
        return None
