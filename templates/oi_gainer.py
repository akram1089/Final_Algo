from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def future_dashboard_charts(request):
    url = "https://webapi.niftytrader.in/webapi/Symbol/future-expiry-current-month-all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    All_derivative_data = data["resultData"]

    for item in All_derivative_data:
        oi = item['oi']
        prev_oi = item['prev_oi']

        if prev_oi != 0:
            item['percentage_change_in_OI'] = (oi - prev_oi) / prev_oi * 100
        else:
            item['percentage_change_in_OI'] = 0

        if item['change_in_OI'] > 0 and item['change_in_LTP'] > 0:
            item['filter'] = 'Long Build Up'
        elif item['change_in_OI'] < 0 and item['change_in_LTP'] < 0:
            item['filter'] = 'Long Unwinding'
        elif item['change_in_OI'] > 0 and item['change_in_LTP'] < 0:
            item['filter'] = 'Short Build Up'
        elif item['change_in_OI'] < 0 and item['change_in_LTP'] > 0:
            item['filter'] = 'Short Covering'
        else:
            item['filter'] = 'None'

    # Get all unique filters
    unique_filters = set(item['filter'] for item in All_derivative_data)

    # Create a dictionary to store filtered data for each unique filter
    filtered_data_by_filter = {}

    for filter_param in unique_filters:
        filtered_data = [
            {'symbol_name': item['symbol_name'], 'percentage_change_in_OI': item['percentage_change_in_OI']}
            for item in All_derivative_data if item['filter'] == filter_param
        ]
        # Sort the filtered data based on percentage_change_in_OI in descending order
        sorted_data = sorted(filtered_data, key=lambda item: -item['percentage_change_in_OI'])
        filtered_data_by_filter[filter_param] = sorted_data

    return Response(filtered_data_by_filter)
