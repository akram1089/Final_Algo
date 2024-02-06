# your_app/tasks.py
from datetime import timezone
from celery import shared_task

@shared_task
def add(x, y):
    return x + y




# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from home.models import ExchangeData  # Import your model

@shared_task
@csrf_exempt
def get_indices_data():
    # Define the sets of symbols for NSE and BSE
    nse_symbols = ['NIFTY', 'BANKNIFTY', 'FINNIFTY', 'MIDCPNIFTY']
    bse_symbols = ['BANKEX', 'SENSEX']

    result_data = []

    for selected_exchange, selected_symbols in {'NSE': nse_symbols, 'BSE': bse_symbols}.items():
        for symbol in selected_symbols:
            try:
                # Make the API call for symbol expiry list
                api_url = f"https://webapi.niftytrader.in/webapi/symbol/symbol-expiry-list?symbol={symbol}&exchange={selected_exchange}"
                response = requests.get(api_url)
                api_data = response.json()

                # Move the option data URL and request inside the loop
                option_data_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={symbol}&exchange=nse"
                response_options = requests.get(option_data_url)
                data_option = response_options.json()

                # Make the API call for future expiry data
                future_data_url = "https://webapi.niftytrader.in/webapi/Symbol/future-expiry-data"
                payload_future = {"symbol": symbol}
                response_future = requests.post(future_data_url, json=payload_future)
                data_future = response_future.json()

                # Save the data into the database
                ExchangeData.objects.create(
                    exchange=selected_exchange,
                    symbol=symbol,
                    symbol_exp_data=api_data,
                    future_data=data_future,
                    data_option=data_option,
                    added_at=timezone.now()  # Set the added_at field to the current timestamp
                )

                # For demonstration, let's print the API response
                print(f"API Response for {symbol}: {api_data}")

                # Append the API response to the result_data list
                result_data.append({symbol: {'symbol_exp_data': api_data, 'future_data': data_future, "data_option": data_option}})
            except requests.RequestException as e:
                # Handle API request exceptions
                print(f"API Request Error for {symbol} on {selected_exchange}: {str(e)}")
            except Exception as e:
                # Handle other exceptions
                print(f"Error for {symbol} on {selected_exchange}: {str(e)}")

    # If you want to send this information as a JSON response
    return {'status': 'success', 'message': 'Data fetched and saved successfully'}
