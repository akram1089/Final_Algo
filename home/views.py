from .models import Watchlist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
import datetime
from .models import Only_buyers
from .models import Stock_Low_Data
from .models import StockData
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import logging
import random
# from datetime import datetime
from collections import defaultdict
from decimal import Decimal
from .models import Entrance
from .models import SecurityBan
from .models import TradedVolume
from .models import Top_Loser
from .models import Top_Gainer
from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError, JsonResponse
import uuid
import json
from django.shortcuts import render, redirect, HttpResponse
import pandas as pd
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages  #
from django.contrib.auth import get_user_model
from .models import ChartData
from home.helper import send_forget_password_mail
User = get_user_model()


# def home(request):
#     url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
#     headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()

#     all_list = []
#     for d in data['data']:
#         if d['symbol'] != 'NIFTY 50':
#             all_list.append({
#                 'symbol': d['symbol'],
#                 'pChange': d['pChange']
#             })

#     # Randomly select 10 symbols from the top 50
#     random_symbols = random.sample(all_list, 10)

#     df = pd.DataFrame(random_symbols)
#     symbols = df.to_dict(orient='records')

#     return render(request, 'home.html', {'symbols': symbols})


def contact_us(request):
    return render(request, "contact_us.html")


# def features(request):
#     url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
#     headers = {
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()

#     all_list = []
#     for d in data['data']:
#         if d['symbol'] != 'NIFTY 50':
#             all_list.append({
#                 'symbol': d['symbol'],
#                 'pChange': d['pChange']
#             })

#     # Randomly select 10 symbols from the top 50
#     random_symbols = random.sample(all_list, 10)

#     df = pd.DataFrame(random_symbols)
#     symbols = df.to_dict(orient='records')

#     return render(request, 'features.html', {'symbols': symbols})

def home(request):
    return render(request, 'home.html')


def features(request):
    return render(request, 'features.html')


def use_cases_strategy(request):
    return render(request, "use_cases_strategy.html")


def use_cases_invester(request):
    return render(request, "use_cases_invester.html")


def Strategy_builder_straddle(request):
    return render(request, "Strategy_builder_straddle.html")


def Futures_Buildup(request):
    return render(request, "Futures_Buildup.html")


def financial_result(request):
    return render(request, "financial_result.html")


def reports(request):
    return render(request, "reports.html")


def stock_scanner(request):
    return render(request, "stock_scanner.html")


def rocket_call(request):
    return render(request, "rocket_call.html")


# def fetch_top_gainers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()

#     top_gainers = []
#     for stock in data['FOSec']['data']:
#         symbol = stock['symbol']
#         previous_close = stock['prev_price']
#         current_price = stock['ltp']

#         if symbol and previous_close and current_price:
#             gain_percentage = round(
#                 ((current_price - previous_close) / previous_close) * 100, 2)
#             top_gainers.append({
#                 "symbol": symbol,
#                 "gain_percentage": gain_percentage
#             })

#     top_gainers.sort(key=lambda x: x['gain_percentage'], reverse=True)
#     return top_gainers[:10]


# def fetch_top_losers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=loosers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()

#     top_losers = []
#     for stock in data['FOSec']['data']:
#         symbol_loser = stock['symbol']
#         previous_close = stock['prev_price']
#         current_price = stock['ltp']

#         if symbol_loser and previous_close and current_price:
#             loss_percentage = round(
#                 ((previous_close - current_price) / previous_close) * 100, 2)
#             top_losers.append({
#                 "symbol_loser": symbol_loser,
#                 "loss_percentage": loss_percentage
#             })

#     top_losers.sort(key=lambda x: x['loss_percentage'], reverse=True)
#     return top_losers[:10]


# def fetch_top_gainers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=gainers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)

#     try:
#         data = response.json()
#     except ValueError:
#         data = None

#     top_gainers = []
#     if data and 'FOSec' in data and 'data' in data['FOSec']:
#         for stock in data['FOSec']['data']:
#             symbol = stock['symbol']
#             previous_close = stock['prev_price']
#             current_price = stock['ltp']

#             if symbol and previous_close and current_price:
#                 gain_percentage = round(
#                     ((current_price - previous_close) / previous_close) * 100, 2)
#                 top_gainers.append({
#                     "symbol": symbol,
#                     "gain_percentage": gain_percentage
#                 })

#     top_gainers.sort(key=lambda x: x['gain_percentage'], reverse=True)
#     return top_gainers[:10]


# def fetch_top_losers():
#     url = "https://www.nseindia.com/api/live-analysis-variations?index=loosers"
#     headers = {
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
#         "Connection": "keep-alive"
#     }
#     response = requests.get(url, headers=headers)

#     try:
#         data = response.json()
#     except ValueError:
#         data = None

#     top_losers = []
#     if data and 'FOSec' in data and 'data' in data['FOSec']:
#         for stock in data['FOSec']['data']:
#             symbol = stock['symbol']
#             previous_close = stock['prev_price']
#             current_price = stock['ltp']

#             if symbol and previous_close and current_price:
#                 loss_percentage = round(
#                     ((previous_close - current_price) / previous_close) * 100, 2)
#                 loss_percentage_with_sign = f"-{loss_percentage}"
#                 top_losers.append({
#                     "symbol": symbol,
#                     "loss_percentage": loss_percentage_with_sign
#                 })

#     top_losers.sort(key=lambda x: x['loss_percentage'], reverse=True)
#     return top_losers[:10]


def get_chart_data():
    try:
        url = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Create a DataFrame from the data
        df = pd.DataFrame(data['data'])

        # Convert totalTradedVolume column to numeric
        df['totalTradedVolume'] = pd.to_numeric(df['totalTradedVolume'])

        # Sort DataFrame by totalTradedVolume in descending order
        df_sorted = df.sort_values(by='totalTradedVolume', ascending=False)

        # Filter the top 10 rows
        top_10 = df_sorted.head(10)

        # Get the symbol and total traded volume as lists
        symbols_volume = top_10['symbol'].tolist()
        traded_volumes = top_10['totalTradedVolume'].tolist()

        # Save the data into the database
        TradedVolume.objects.all().delete()
        for volume in traded_volumes:
            traded_volume = TradedVolume(trade_volume=str(volume))
            traded_volume.save()

        return symbols_volume, traded_volumes
    except requests.exceptions.RequestException:
        # Fetch data from the database if unable to fetch from the API
        traded_volumes = TradedVolume.objects.all().order_by(
            '-trade_volume')[:10]
        symbols_volume = [str(volume) for volume in traded_volumes]

        return symbols_volume, [float(volume.trade_volume) for volume in traded_volumes]


# def dashboard(request):
#     symbols_volume, traded_volumes = get_chart_data()

    # try:
    #     top_losers = fetch_top_losers()
    #     symbols = [loser['symbol'] for loser in top_losers]
    #     loss_percentages = [loser['loss_percentage'] for loser in top_losers]

    #     Top_Loser.objects.all().delete()
    #     Top_Loser.objects.create(top_losers=", ".join(symbols))

    # except Exception as e:

    #     top_loser_data = Top_Loser.objects.first()
    #     if top_loser_data:
    #         symbols = top_loser_data.top_losers.split(", ")
    #         loss_percentages = []
    #     else:
    #         symbols = []
    #         loss_percentages = []

    # context = {
    #     'symbols_losers': symbols,
    #     'loss_percentages': loss_percentages,
    # }
    # try:
    #     top_gainers = fetch_top_gainers()
    #     symbols = [gainer['symbol'] for gainer in top_gainers]
    #     gain_percentages = [gainer['gain_percentage']
    #                         for gainer in top_gainers]

    #     Top_Gainer.objects.all().delete()
    #     Top_Gainer.objects.create(top_gainers=", ".join(symbols))

    # except Exception as e:

    #     top_gainer_data = Top_Gainer.objects.first()
    #     if top_gainer_data:
    #         symbols = top_gainer_data.top_gainers.split(", ")
    #         gain_percentages = []
    #     else:
    #         symbols = []
    #         gain_percentages = []

    # context = {
    #     'symbols': symbols,
    #     'gain_percentages': gain_percentages,
    # }

    # url = "https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings"

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Accept-Encoding": "gzip, deflate, br",
    # }

    # response = requests.get(url, headers=headers)

    # try:
    #     data = response.json()
    # except json.JSONDecodeError as e:
    #     print("Error decoding JSON:", str(e))
    #     data = None

    # if data is not None:

    #     sorted_data = sorted(data['data'], key=lambda x: x['avgInOI'])

    #     top_symbols_lowest = sorted_data[:10]

    #     symbols_lowest = [symbol_data['symbol']
    #                       for symbol_data in top_symbols_lowest]
    #     avgInOI_values_lowest = [symbol_data['avgInOI']
    #                              for symbol_data in top_symbols_lowest]

    #     sorted_data = sorted(
    #         data['data'], key=lambda x: x['avgInOI'], reverse=True)

    #     top_symbols_highest_positive = [
    #         symbol_data for symbol_data in sorted_data if symbol_data['avgInOI'] > 0][:10]

    #     symbols_highest_positive = [symbol_data['symbol']
    #                                 for symbol_data in top_symbols_highest_positive]
    #     avgInOI_values_highest_positive = [
    #         symbol_data['avgInOI'] for symbol_data in top_symbols_highest_positive]

    #     chart_data = ChartData(data_json=json.dumps(data))
    #     chart_data.save()

    #     context = {
    #         'symbols_lowest': symbols_lowest,
    #         'avgInOI_values_lowest': avgInOI_values_lowest,
    #         'symbols_highest_positive': symbols_highest_positive,
    #         'avgInOI_values_highest_positive': avgInOI_values_highest_positive,
    #         # 'symbols': symbols,
    #         # 'gain_percentages': gain_percentages,
    #         # 'symbols_losers': symbols,
    #         # 'loss_percentages': loss_percentages,
    #         'symbols_volume': symbols_volume,
    #         'traded_volumes': traded_volumes,
    #     }

    #     return render(request, 'dashboard.html', context)
    # else:

    #     chart_data = ChartData.objects.last()
    #     if chart_data:
    #         data = json.loads(chart_data.data_json)

    #         sorted_data = sorted(data['data'], key=lambda x: x['avgInOI'])

    #         top_symbols_lowest = sorted_data[:10]

    #         symbols_lowest = [symbol_data['symbol']
    #                           for symbol_data in top_symbols_lowest]
    #         avgInOI_values_lowest = [symbol_data['avgInOI']
    #                                  for symbol_data in top_symbols_lowest]

    #         sorted_data = sorted(
    #             data['data'], key=lambda x: x['avgInOI'], reverse=True)

    #         top_symbols_highest_positive = [
    #             symbol_data for symbol_data in sorted_data if symbol_data['avgInOI'] > 0][:10]

    #         symbols_highest_positive = [symbol_data['symbol']
    #                                     for symbol_data in top_symbols_highest_positive]
    #         avgInOI_values_highest_positive = [
    #             symbol_data['avgInOI'] for symbol_data in top_symbols_highest_positive]

    #         context = {
    #             'symbols_lowest': symbols_lowest,
    #             'avgInOI_values_lowest': avgInOI_values_lowest,
    #             'symbols_highest_positive': symbols_highest_positive,
    #             'avgInOI_values_highest_positive': avgInOI_values_highest_positive,
    #             # 'symbols': symbols,
    #             # 'gain_percentages': gain_percentages,
    #             # 'symbols_losers': symbols,
    #             # 'loss_percentages': loss_percentages,
    #             'symbols_volume': symbols_volume,
    #             'traded_volumes': traded_volumes,
    #         }
    #         return render(request, 'dashboard.html', context)
    #     else:
    #         return HttpResponse("No data available.")


def help_support(request):
    return render(request, "help_support.html")


def learning_center(request):
    return render(request, "learning_center.html")


def blog(request):
    return render(request, "blog.html")


def my_strategies(request):
    return render(request, "my_strategies.html")


def my_portfolio(request):
    return render(request, "my_portfolio.html")


def broking_details(request):
    return render(request, "broking_details.html")


def courses_details(request):
    return render(request, "courses_details.html")


def reset_password(request):
    return render(request, "reset_password.html")


def Open_interest_analysis(request):
    if request.method == "POST":
        symbol = request.POST['symbols']
        expiry_dates = request.POST["expiryDates"]
        print(symbol, expiry_dates)
        if expiry_dates == "":
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol='+symbol
            print(url)
            headers = {
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
            }
            session = requests.Session()

            data = session.get(url, headers=headers).json()["records"]["data"]
            ocdata = []

            for i in data:
                for j, k in i.items():
                    if j == "CE" or j == "PE":
                        info = k
                        info['instrumentType'] = j
                        ocdata.append(info)
            dataopt = pd.DataFrame(ocdata)
            datashort = dataopt.head(100)
            json_records = datashort.reset_index().to_json(orient='records')
            data = []
            data = json.loads(json_records)
            return render(request, "Open_interest_analysis.html", {"dataframe": data})

        else:
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol='+symbol
            print(url)
            headers = {
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
            }
            session = requests.Session()

            data = session.get(url, headers=headers).json()["records"]["data"]
            ocdata = []

            for i in data:
                for j, k in i.items():
                    if j == "CE" or j == "PE":
                        info = k
                        info['instrumentType'] = j
                        ocdata.append(info)
            dataopt = pd.DataFrame(ocdata)
            filtered_data_open = dataopt[dataopt['expiryDate'] == str(
                expiry_dates)]
            if not filtered_data_open.empty:
                print(filtered_data_open)
                filtered_datas = filtered_data_open.head(100)
                print(filtered_datas)
                json_records = filtered_datas.reset_index().to_json(orient='records')
                data_filter = []
                data_filter = json.loads(json_records)

            else:
                print("No data available for the specified expiry date.")
            return render(request, 'Open_interest_analysis.html', {"dataframe": data_filter})

    else:
        url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        print(url)
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        session = requests.Session()

        data = session.get(url, headers=headers).json()["records"]["data"]
        ocdata = []

        for i in data:
            for j, k in i.items():
                if j == "CE" or j == "PE":
                    info = k
                    info['instrumentType'] = j
                    ocdata.append(info)
        dataopt = pd.DataFrame(ocdata)
        datashort = dataopt.head(100)
        json_records = datashort.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
    return render(request, "Open_interest_analysis.html", {"dataframe": data})


def signUp(request):
    if request.method == "POST":
        fname = request.POST["name"]
        email = request.POST["email"]
        phone_code = request.POST["phone_code"]
        mobile = request.POST["mobile"]
        country_id = request.POST.get("country_id", "")
        state_id = request.POST.get("state_id", "")
        password = request.POST["password"]
        Cofirm_password = request.POST["Cofirm_password"]
        if User.objects.filter(email=email):
            messages.error(request, 'Email already being taken')
            return redirect('/')
        else:
            Mysignup = User.objects.create_user(
                full_name=fname,
                email=email,
                Mobile_number=mobile,
                password=password,
                confirm_password=Cofirm_password,
                Country=country_id,
                State=state_id,
                Phone_code=phone_code,
            )
            Mysignup.save()

            # Picture=Display_picture(image=images)
            # Picture.save()
            messages.success(
                request, 'You have successfully signed up , please login with correct credential')
            redirect('/')
    return render(request, 'home.html')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        Email = request.POST['email']
        password = request.POST['password']
        print(Email, password)
        user = authenticate(email=Email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                messages.success(
                    request, 'You are successfully logged in as Admin')
                return redirect("/admin_panel")
            else:
                messages.success(request, 'You are successfully logged in')
                return redirect("/")
        else:
            messages.error(request, 'Invalid credential')
            return redirect("/")


def logout_user(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect("/")


def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        if User.objects.filter(email=email):
            token = str(uuid.uuid4())
            profile_email = User.objects.get(email=email)
            profile_email.forget_password_token = token
            profile_email.save()
            send_forget_password_mail(email, token)
            messages.success(
                request, 'An email has been sent you to ,please check the mail box')
            return redirect('/')

        else:
            messages.success(request, 'Sorry your email is not registered')
            return redirect('/')

    return render(request, 'reset_password.html')


def change_pass(request, token):

    profile_email = User.objects.filter(
        forget_password_token=token).first()

    print(profile_email)
    context = {'user_id': profile_email.id}

    if request.method == 'POST':
        l_pass = request.POST['new_pass']
        cpass = request.POST['confirm_pass']
        user_id = request.POST.get('user_id')
        print(l_pass, cpass)

        if l_pass != cpass:
            messages.error(request, 'both should  be equal.')
            return redirect(f'/change_pass/{token}/')

        else:
            change_pass = User.objects.get(id=user_id)
            change_pass.password = l_pass
            change_pass.confirm_password = cpass
            change_pass.set_password(l_pass)
            change_pass.save()
            messages.success(request, 'Your password has been changed.')

            return redirect('/')

    return render(request, 'change_pass.html', context)


def get_option_chain(request):
    if request.method == 'GET':
        symbol = request.GET.get('symbol')

        if symbol == 'NIFTY':
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        elif symbol == 'BANKNIFTY':
            url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
        else:
            return JsonResponse({'success': False, 'message': 'Invalid symbol'})

        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            option_data = response.json()
            expiry_dates = option_data['records']['expiryDates']
            print(expiry_dates)
            return JsonResponse({'expiry_dates': expiry_dates})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'success': False, 'message': 'Error fetching option chain data'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


def tests(request):
    data = {
        "data": [
            {
                "Unnamed: 0": 0,
                "fivedayoichange": 8.76,
                "fivedaypricechange": -0.02,
                "futuresPrice": 18631.55,
                "ivchange": 3.36,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.93,
                "onedaypricechange": -0.42,
                "shorttermoutlook": "-",
                "ticker": "NIFTY",
                "volper": 60.71,
                "volumechange": 106.87
            },
            {
                "Unnamed: 0": 1,
                "fivedayoichange": 8.72,
                "fivedaypricechange": 0.02,
                "futuresPrice": 44117.95,
                "ivchange": -2.73,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.72,
                "onedaypricechange": -0.07,
                "shorttermoutlook": "-",
                "ticker": "BANKNIFTY",
                "volper": 68.25,
                "volumechange": 102.76
            },
            {
                "Unnamed: 0": 2,
                "fivedayoichange": 7.42,
                "fivedaypricechange": -1.81,
                "futuresPrice": 508.1,
                "ivchange": -2.2,
                "mediumtermoutlook": "-",
                "onedayoichange": 1.53,
                "onedaypricechange": -1.52,
                "shorttermoutlook": "-",
                "ticker": "AARTIIND",
                "volper": 10.71,
                "volumechange": 102.07
            },
            {
                "Unnamed: 0": 3,
                "fivedayoichange": -0.07,
                "fivedaypricechange": 2.89,
                "futuresPrice": 4138.05,
                "ivchange": -1.29,
                "mediumtermoutlook": "-",
                "onedayoichange": -0.07,
                "onedaypricechange": 0.77,
                "shorttermoutlook": "-",
                "ticker": "ABB",
                "volper": 0.0,
                "volumechange": 78.52
            }
        ]
    }
    data1 = []
    for d in data["data"]:
        data1.append(d)

    return render(request, 'tests.html', {'data1': data1})


def Algo_market_place(request):
    return render(request, "Algo_market_place.html")


def market_wide_position(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/ban-list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    date = []
    for d in data['resultData']['date']:
        date.append(d)

    date_str = ''.join(date)

    securities_ban_result = data['resultData']['securities_ban_result']
    possible_entrants_result = data['resultData']['possible_entrants_result']

    SecurityBan.objects.all().delete()
    Entrance.objects.all().delete()

    securityban_df = pd.DataFrame(securities_ban_result)
    entrance_df = pd.DataFrame(possible_entrants_result)

    for _, row in securityban_df.iterrows():
        SecurityBan.objects.create(
            symbol_name=row['symbol_name'],
            current_percent=row['current_percent']
        )

    for _, row in entrance_df.iterrows():
        Entrance.objects.create(
            Entrance_symbol_name=row['symbol_name'],
            Entrance_precent=row['current_percent']
        )

    securityban_data = SecurityBan.objects.all()
    entrance_data = Entrance.objects.all()

    if not securityban_data:

        securityban_data = SecurityBan.objects.all()

    if not entrance_data:

        entrance_data = Entrance.objects.all()

    labels = []
    chart_data = []

    entrance_labels = []
    entrance_chart_data = []

    for data in securityban_data:
        labels.append(data.symbol_name)
        chart_data.append(data.current_percent)

    decimal_places = 2
    normalized_list = [round(float(d), decimal_places) for d in chart_data]

    for data in entrance_data:
        entrance_labels.append(data.Entrance_symbol_name)
        entrance_chart_data.append(data.Entrance_precent)

    normalized_list_entrance = [
        round(float(d), decimal_places) for d in entrance_chart_data]
    url = "https://webapi.niftytrader.in/webapi/Resource/ban-list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    all_list = []
    for d in data["resultData"]["all_list_result"]:
        all_list.append(d)

    df = pd.DataFrame(all_list).head(25)
    # Select only "symbol_name" and "current_percent" columns
    df = df[["symbol_name", "current_percent"]]

    # Prepare the data for Chart.js
    all_labels = df["symbol_name"].tolist()
    all_values = df["current_percent"].tolist()

    context = {
        'labels': labels,
        'Entrance_labels': entrance_labels,
        'chart_data': normalized_list,
        'normalized_list_entrance': normalized_list_entrance,
        'date_str': date_str,
        "all_labels": all_labels,
        "all_values": all_values,
    }

    return render(request, "market_wide_position.html", context)


def dii_fii(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/fii-cash-month?Date=2023-06"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Create a list to store merged data
    merged_data = defaultdict(float)

    # Merge records with the same created_at value and perform arithmetic addition on net_value
    for d in data["resultData"]["data"]:
        created_at = d["created_at"]
        net_value = float(d["net_value"])
        merged_data[created_at] += net_value

    # Convert the merged data to a DataFrame
    df = pd.DataFrame(merged_data.items(), columns=["created_at", "net_value"])

    # Sort the DataFrame by created_at in descending order
    df.sort_values("created_at", ascending=False, inplace=True)

    # Format the created_at column
    df["created_at"] = pd.to_datetime(df["created_at"]).dt.strftime("%Y-%m-%d")

    # Prepare the data for Chart.js
    labels = df["created_at"].tolist()
    values = df["net_value"].tolist()
    print(labels, values)

    filtered_data_fpi = [
        (datetime.datetime.strptime(
            item["created_at"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"), item["net_value"])
        for item in data["resultData"]["data"]
        if item["category"] == "FII/FPI"
    ]

    # Convert the filtered data to a DataFrame
    dfii = pd.DataFrame(filtered_data_fpi, columns=["created_at", "net_value"])

    # Sort the DataFrame by created_at in descending order
    dfii.sort_values("created_at", ascending=False, inplace=True)

    # Prepare the data for Chart.js
    labels_fii = dfii["created_at"].tolist()
    values_fii = dfii["net_value"].tolist()

    filtered_data_fii = [
        (datetime.datetime.strptime(
            item["created_at"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"), item["net_value"])
        for item in data["resultData"]["data"]
        if item["category"] == "DII"  # Filter for "DII" category
    ]

    # Convert the filtered data to a DataFrame
    dii_df = pd.DataFrame(filtered_data_fii, columns=[
                          "created_at", "net_value"])

    # Sort the DataFrame by created_at in descending order
    dii_df.sort_values("created_at", ascending=False, inplace=True)

    # Prepare the data for Chart.js
    labels_dii = dii_df["created_at"].tolist()
    values_dii = dii_df["net_value"].tolist()

    context = {
        'labels': labels,
        'labels_fii': labels_fii,
        'values': values,
        'values_fii': values_fii,
        "labels_dii": labels_dii,
        "values_dii": values_dii

    }

    return render(request, 'dii_fii.html', context)





def option_strategies(request):
    return render(request, 'option_strategies.html')


def strategy_builder(request):
    return render(request, 'strategy_builder.html')


# def chart_topgainer(request):

#     url = "https://trendlyne.com/futures-options/api-filter/futures/29-jun-2023-near/oi_losers/"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     response_oi_loser = requests.get(url, headers=headers)
#     data_oi_loser = response_oi_loser.json()

#     # Extract the name and value data_oi_loser
#     name_value_list = [(item[0]["name"], item[7]) for item in data_oi_loser["tableData"]]

#     # Create a pandas DataFrame
#     df_oi_loser = pd.DataFrame(name_value_list, columns=["name", "value"])

#     # Select the top 10 rows
#     top_10_df_oi_loser = df_oi_loser.head(10)

#     # Prepare data for Chart.js
#     labels_oi_loser = top_10_df_oi_loser["name"].tolist()
#     values_oi_loser = top_10_df_oi_loser["value"].tolist()

#     context = {
#         "labels_oi_loser": labels_oi_loser,
#         "values_oi_loser": values_oi_loser,
#     }

#     return render(request, 'chart_topgainer.html',context)


def dashboard(request):

    url = "https://etmarketsapis.indiatimes.com/ET_Stats/gainers?pagesize=25&exchange=nse&pageno=1&sort=intraday&sortby=percentchange&sortorder=desc&marketcap=largecap&duration=1d"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Create a pandas DataFrame
    df = pd.DataFrame(data["searchresult"])

    # Select the desired columns
    df = df[["companyShortName", "percentChange"]]

    top_10 = df.head(10)

    # Prepare data for Chart.js
    top_gainer_labels = top_10["companyShortName"].tolist()
    top_gainer_values = top_10["percentChange"].tolist()

    url = "https://etmarketsapis.indiatimes.com/ET_Stats/losers?pagesize=25&exchange=nse&pageno=1&sort=intraday&sortby=percentchange&sortorder=asc&marketcap=largecap&duration=1d"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_losers = requests.get(url, headers=headers)
    data_losers = response_losers.json()

    # Create a pandas DataFrame
    df_losers = pd.DataFrame(data_losers["searchresult"])

    # Select the desired columns
    df_losers = df_losers[["companyShortName", "percentChange"]]

    # Get the top 10 losers
    top_10_losers = df_losers.head(10)

    # Prepare data for Chart.js
    looser_labels = top_10_losers["companyShortName"].tolist()
    looser_values = top_10_losers["percentChange"].tolist()
    url = "https://trendlyne.com/futures-options/api-filter/futures/28-sep-2023-near/oi_gainers/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_oi = requests.get(url, headers=headers)
    data_oi = response_oi.json()

    # Extract the name and value data_oi
    name_value_list = [(item[0]["name"], item[7])
                       for item in data_oi["tableData"]]

    # Create a pandas DataFrame
    df_oi = pd.DataFrame(name_value_list, columns=["name", "value"])

    # Get the top 10 rows
    top_10_df_oi = df_oi.head(10)

    # Prepare data for Chart.js
    labels_oi_gainer = top_10_df_oi["name"].tolist()
    values_oi_losers = top_10_df_oi["value"].tolist()
    url = "https://trendlyne.com/futures-options/api-filter/futures/27-jul-2023-next/oi_losers/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_oi_loser = requests.get(url, headers=headers)
    data_oi_loser = response_oi_loser.json()

    # Extract the name and value data_oi_loser
    name_value_list = [(item[0]["name"], item[7])
                       for item in data_oi_loser["tableData"]]

    # Create a pandas DataFrame
    df_oi_loser = pd.DataFrame(name_value_list, columns=["name", "value"])

    # Select the top 10 rows
    top_10_df_oi_loser = df_oi_loser.head(10)

    # Prepare data for Chart.js
    labels_oi_loser = top_10_df_oi_loser["name"].tolist()
    values_oi_loser = top_10_df_oi_loser["value"].tolist()

    context = {
        "looser_labels": looser_labels,
        "looser_values": looser_values,
        "top_gainer_labels": top_gainer_labels,
        "top_gainer_values": top_gainer_values,
        "labels_oi_gainer": labels_oi_gainer,
        "values_oi_losers": values_oi_losers,
        "labels_oi_loser": labels_oi_loser,
        "values_oi_loser": values_oi_loser,
    }
    print(context)

    return render(request, 'dashboard.html', context)


def market_glance(request):
    return render(request, "market_glance.html")


def holiday(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/bse-nse-holiday"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    filtered_data_holiday = []

    for d in data["resultData"]["holiday1"]:
        filtered_data_holiday.append({
            "srno": d["srno"],
            "date": d["date"],
            "day": d["day"],
            "description": d["description"]
        })

    df = pd.DataFrame(filtered_data_holiday)
    table_data = df.to_dict(orient='records')

    context = {
        'table_data': table_data
    }
    return render(request, "holiday.html", context)


def lot_size(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/fno-lot-size"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    table_data = []
    for d in data["resultData"]["data"]:
        underlying = d["underlying"]
        symbol = d["symbol"]
        month_data_str = d["month_data"]
        month_data = eval(month_data_str)
        row_data = [underlying, symbol] + list(month_data.values())
        table_data.append(row_data)

    headers = ["Underlying", "Symbol"] + list(month_data.keys())

    context = {
        "headers": headers,
        "table_data": table_data,
    }

    return render(request, "lot_size.html", context)


def market_heavy(request):
    return render(request, "market_heavy.html")


def bulk_deal_data(request):
    if request.method == 'GET':
        selected_date = request.GET.get('date')

        url = "https://webapi.niftytrader.in/webapi/Resource/bulk-deal-data"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        deal_dates = pd.to_datetime(
            data["resultData"]['deal_dates']).strftime('%Y-%m-%d').tolist()

        deal_data = pd.DataFrame(data["resultData"]['deal_data'])

        deal_data['created_at'] = pd.to_datetime(
            deal_data['created_at']).dt.strftime('%Y-%m-%d')

        if selected_date:

            selected_date = datetime.datetime.strptime(
                selected_date, '%Y-%m-%d')
            deal_data = deal_data[deal_data['created_at']
                                  == selected_date.date().strftime('%Y-%m-%d')]

        deal_data = deal_data.to_dict(orient='records')

        return JsonResponse({'deal_dates': deal_dates, 'deal_data': deal_data}, json_dumps_params={'indent': 2})


def bulk_deal_data_page(request):
    return render(request, 'bulk_deal_data.html')


def base_dashboard1(request):
    url = "https://webapi.niftytrader.in/webapi/symbol/stock-index-data"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    nifty50_data = data['resultData'].get('nifty50', '')
    niftybank_data = data['resultData'].get('niftybank', '')
    finnity_data = data['resultData'].get('finnity', '')

    nifty50_difference = nifty50_data.get(
        'last_trade_price', 0) - nifty50_data.get('prev_price', 0)
    niftybank_difference = niftybank_data.get(
        'last_trade_price', 0) - niftybank_data.get('prev_price', 0)
    finnity_difference = finnity_data.get(
        'last_trade_price', 0) - finnity_data.get('prev_price', 0)

    nifty50_percentage = (nifty50_difference /
                          nifty50_data.get('prev_price', 1)) * 100
    niftybank_percentage = (niftybank_difference /
                            niftybank_data.get('prev_price', 1)) * 100
    finnity_percentage = (finnity_difference /
                          finnity_data.get('prev_price', 1)) * 100

    stock_data = {
        'nifty50_data': nifty50_data,
        'nifty50_value': nifty50_difference,
        'nifty50_percentage': nifty50_percentage,
        'niftybank_data': niftybank_data,
        'niftybank_value': niftybank_difference,
        'niftybank_percentage': niftybank_percentage,
        'finnity_data': finnity_data,
        'finnity_value': finnity_difference,
        'finnity_percentage': finnity_percentage,
    }
    return JsonResponse(stock_data)


def global_market(request):
    url = "https://webapi.niftytrader.in/webapi/usstock/global-market"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    country_data = {}

    for item in data['resultData']:
        country = item['country']
        if country in country_data:
            country_data[country].append(item)
        else:
            country_data[country] = [item]

    tables_data = []
    for country, items in country_data.items():
        table_data = {
            'country': country,
            'items': items
        }
        tables_data.append(table_data)

    return JsonResponse({'tables': tables_data})


def dashboard1(request):
    return render(request, 'dashboard1.html')


def market_actions(request):
    url = "https://webapi.niftytrader.in/webapi/symbol/top-gainers-data"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "resultData" in data:
        result_data = data["resultData"]
        tables = []

        for category, items in result_data.items():
            if category == "topWatchList":
                continue  # Skip the "topWatchList" category

            df = pd.DataFrame(items)
            table = {
                "category": category,
                "data": df.to_dict(orient="records")
            }
            tables.append(table)

        return JsonResponse({"tables": tables})
    else:
        return JsonResponse({"error": "No data found in the response."})


def ban_list_dashboard(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/ban-list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    securities_ban_result = data['resultData']['securities_ban_result']
    possible_entrants_result = data['resultData']['possible_entrants_result']
    possible_exits_result = data['resultData']['possible_exits_result']

    # Convert data to pandas DataFrames for optimization
    securities_ban_df = pd.DataFrame(securities_ban_result)
    possible_entrants_df = pd.DataFrame(possible_entrants_result)
    possible_exits_df = pd.DataFrame(possible_exits_result)

    # Convert DataFrames back to JSON format
    securities_ban_result = securities_ban_df.to_dict(orient='records')
    possible_entrants_result = possible_entrants_df.to_dict(orient='records')
    possible_exits_result = possible_exits_df.to_dict(orient='records')

    result = {
        'securities_ban_result': securities_ban_result,
        'possible_entrants_result': possible_entrants_result,
        'possible_exits_result': possible_exits_result
    }

    return JsonResponse(result)

# from django.http import JsonResponse
# import requests
# from .models import StockListing

# def stock_listing(request):
#     url = "https://www.nseindia.com/api/new-listing-today?index=RecentListing"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }

#     try:
#         response = requests.get(url, headers=headers)
#         data = response.json()

#         sme_records = [record for record in data["data"] if record["instrument"] == "SME"]

#         equity_records = [record for record in data["data"] if record["instrument"] == "Equity"]

#         # Update the StockListing model with new data
#         stock_listing, _ = StockListing.objects.get_or_create(pk=1)
#         stock_listing.sme_records = sme_records
#         stock_listing.equity_records = equity_records
#         stock_listing.save()

#     except requests.exceptions.RequestException:
#         # If the API does not respond, fetch the data from the StockListing model
#         try:
#             stock_listing = StockListing.objects.get(pk=1)
#             sme_records = stock_listing.sme_records if stock_listing else []
#             print(sme_records)
#             equity_records = stock_listing.equity_records if stock_listing else []
#         except StockListing.DoesNotExist:
#             sme_records = []
#             equity_records = []

#     return JsonResponse({"sme_records": sme_records, "equity_records": equity_records})

@csrf_exempt
def admin_login(request):
    return render(request, "admin_login.html")

@csrf_exempt
def admin_signup(request):
    if request.method == "POST":
        fname = request.POST["name"]
        email = request.POST["email"]
        phone_code = request.POST["phone_code"]
        mobile = request.POST["mobile"]
        country_id = request.POST.get("country_id", "")
        state_id = request.POST.get("state_id", "")
        password = request.POST["password"]
        Cofirm_password = request.POST["Cofirm_password"]
        if User.objects.filter(email=email):
            messages.error(request, 'Email already being taken')
            return redirect('/')
        else:
            Mysignup = User.objects.create_superuser(
                full_name=fname,
                email=email,
                Mobile_number=mobile,
                password=password,
                confirm_password=Cofirm_password,
                Country=country_id,
                State=state_id,
                Phone_code=phone_code,
            )
            Mysignup.save()

            # Picture=Display_picture(image=images)
            # Picture.save()
            messages.success(
                request, 'You have successfully signed up as Admin , please login with Admin credential')
            redirect('/admin_login')
    return render(request, "admin_signup.html")


def admin_reset(request):
    return render(request, "admin_reset.html")


def manage_user(request):
    User_check = User.objects.all()
    return render(request, "manage_user.html", {"User_check": User_check})


def delete_user(request, id):
    if request.method == "POST":
        Del_user = User.objects.filter(id=id)
        Del_user.delete()
        messages.success(request, "A user has been deleted")
        return redirect("manage_user")


# import requests
# from django.http import JsonResponse

# def oi_gainers(request):
#     url = "https://trendlyne.com/futures-options/api-filter/futures/29-jun-2023-near/oi_gainers/"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }
#     response_oi = requests.get(url, headers=headers)
#     data_oi = response_oi.json()

#     return JsonResponse(data_oi)


# def oi_losers(request):
#     url = "https://trendlyne.com/futures-options/api-filter/futures/29-jun-2023-near/oi_losers/"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive"
#     }
#     response_oi_loser = requests.get(url, headers=headers)
#     data_oi_loser = response_oi_loser.json()

#     return JsonResponse(data_oi_loser)


def volume_shocker(request):
    url = "https://etmarketsapis.indiatimes.com/ET_Stats/volumeshocker?pagesize=25&exchange=nse&pageno=1&sortby=volume&sortorder=desc&avgvolumeover=DAY_3&marketcap=largecap"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    volume_data = data["searchresult"]
    return JsonResponse(volume_data, safe=False)

# views.py


def oi_gainers(request):
    url = "https://trendlyne.com/futures-options/api-filter/futures/28-sep-2023-near/oi_gainers/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_oi = requests.get(url, headers=headers)
    data_oi = response_oi.json()

    # Extract the desired values from data_oi
    name_values_list = [
        (
            item[0]["name"],  # name
            item[1],  # price
            item[2],  # Date Chang
            item[3],  # Volume Contracts
            item[4],  # % Volume Contracts
            item[5],  # TTV
            item[6],  # OI
            item[7],  # %OI
            item[8],  # Basis
            item[9],  # COC
            item[10],  # Spot
            item[11]  # Build Up
        )
        for item in data_oi["tableData"]
    ]

    # Prepare the data as a dictionary
    response_data = {
        "data": name_values_list,
        "columns": [
            "name",
            "price",
            "Date Change",
            "Volume Contracts",
            "% Volume Contracts",
            # "TTV",
            "OI",
            "%OI",
            "Basis",
            "COC",
            "Spot",
            "Build Up"
        ]
    }

    return JsonResponse(response_data)


def oi_losers(request):
    url = "https://trendlyne.com/futures-options/api-filter/futures/27-jul-2023-next/oi_losers/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_oi = requests.get(url, headers=headers)
    data_oi = response_oi.json()

    # Extract the desired values from data_oi
    name_values_list = [
        (
            item[0]["name"],  # name
            item[1],  # price
            item[2],  # Date Chang
            item[3],  # Volume Contracts
            item[4],  # % Volume Contracts
            item[5],  # TTV
            item[6],  # OI
            item[7],  # %OI
            item[8],  # Basis
            item[9],  # COC
            item[10],  # Spot
            item[11]  # Build Up
        )
        for item in data_oi["tableData"]
    ]

    # Prepare the data as a dictionary
    response_data = {
        "data": name_values_list,
        "columns": [
            "name",
            "price",
            "Date Chang",
            "Volume Contracts",
            "% Volume Contracts",
            # "TTV",
            "OI",
            "%OI",
            "Basis",
            "COC",
            "Spot",
            "Build Up"
        ]
    }

    return JsonResponse(response_data)


# from datetime import datetime


def admin_panel(request):
    User_check = User.objects.all()
    return render(request, "admin_panel.html", {"User_check": User_check})


def put_call_ratio_chart(request):
    trade = request.GET.get('trade', 'nifty')  # Default value is 'nifty'
    print(trade)
    url = f"https://webapi.niftytrader.in/webapi/option/oi-pcr-data?reqType={trade}pcr&reqDate="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    pcr_values = []
    index_close_values = []
    time_values = []
    for result in data['resultData']["oiDatas"]:
        pcr_values.append(result['pcr'])
        index_close_values.append(result['index_close'])
        time_value = datetime.datetime.strptime(
            result['time'], "%Y-%m-%dT%H:%M:%S")
        time_values.append(time_value.strftime("%H:%M"))

    context = {
        'pcr_values': pcr_values,
        'index_close_values': index_close_values,
        'time_values': time_values,
    }

    return JsonResponse(context)


def put_call_ratio(request):
    return render(request, "put_call_ratio.html")


def Edit_user_data(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        edit_fullname = request.POST.get('edit_fullname', '')
        edit_email = request.POST.get('edit_email', '')
        phone_code_edit = request.POST.get('phone_code_edit', '')
        mobile_edit = request.POST.get('mobile_edit', '')
        edit_country = request.POST.get('edit_country', '')
        edit_state = request.POST.get('edit_state', '')
        edit_status = request.POST.get('edit_status', '')

        if edit_status == 'Active':
            user.is_active = True
        elif edit_status == 'Inactive':
            user.is_active = False

        user.save()

        user.full_name = edit_fullname
        user.email = edit_email
        user.phone_code = phone_code_edit
        user.mobile_number = mobile_edit
        user.country = edit_country
        user.state = edit_state
        user.save()

        messages.success(request, 'Data has been successfully edited')
        return redirect('admin_panel')

    return render(request, 'admin_panel.html')


def feedback_management(request):
    return render(request, "feedback_management.html")


def payments_details(request):
    return render(request, "payments_details.html")


def stock_analysis(request):
    return render(request, "stock_analysis.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def filtered_oi_data(request):
    # Retrieve the selected expiry date
    expiry_date = request.GET.get("expiry_date")
    arg = request.GET.get("arg")  # Retrieve the arg parameter
    print(arg)  # Print the value of arg to the console

    nifty_value = None
    spot_value = None

    if arg:
        arg_dict = json.loads(arg)
        nifty_value = arg_dict.get("nifty")
        spot_value = arg_dict.get("spot")

    oi_url = f"https://webapi.niftytrader.in/webapi/option/oi-data?reqType={nifty_value}&reqDate={expiry_date}"
    print(oi_url)

    dates_url = f"https://webapi.niftytrader.in/webapi/option/oi-data?reqType={nifty_value}&reqDate="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    oi_response = requests.get(oi_url, headers=headers)
    oi_data = oi_response.json()

    dates_response = requests.get(dates_url, headers=headers)
    dates_data = dates_response.json()

    spot_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={spot_value}"

    spot_response = requests.get(spot_url, headers=headers)
    spot_data = spot_response.json()

    result_data = spot_data.get("resultData")
    if result_data is not None:
        spot_price = result_data.get("last_trade_price")
        change_value = result_data.get("change_value")  # Added change_value
        change_per = result_data.get("change_per")  # Added change_per

        if spot_price is not None:
            closest_prices = []
            calls_oi = []
            puts_oi = []

            oi_datas = oi_data.get("resultData", {}).get("oiDatas", [])

            for result in oi_datas:
                price = result.get("strike_price")
                if price is not None:
                    closest_prices.append(price)
                    calls_oi.append(result.get("calls_oi", 0))
                    puts_oi.append(result.get("puts_oi", 0))

            closest_prices, calls_oi, puts_oi = zip(
                *sorted(
                    zip(closest_prices, calls_oi, puts_oi),
                    key=lambda x: abs(x[0] - spot_price)
                )
            )

            bar_count = request.GET.get("bar_count")
            if bar_count:
                if bar_count == "all":
                    closest_prices = closest_prices
                    calls_oi = calls_oi
                    puts_oi = puts_oi
                else:
                    bar_count = int(bar_count)
                    closest_prices = closest_prices[:bar_count]
                    calls_oi = calls_oi[:bar_count]
                    puts_oi = puts_oi[:bar_count]

            dates = []
            for result in dates_data.get("resultData", {}).get("oiExpiryDates", []):
                date_str = result.split("T")[0]
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                formatted_date = datetime.datetime.strftime(
                    date_obj, "%Y-%m-%d")
                dates.append(formatted_date)

            context = {
                'spot_price': spot_price,
                'change_value': change_value,  # Added change_value
                'change_per': change_per,  # Added change_per
                'closest_prices': closest_prices,
                'calls_oi': calls_oi,
                'puts_oi': puts_oi,
                'dates': dates
            }
            return JsonResponse(context)

    return JsonResponse({'message': 'Data not available'})


def filtered_oi_change_data(request):
    # Retrieve the selected expiry date
    expiry_date = request.GET.get("expiry_date")
    arg = request.GET.get("arg")  # Retrieve the arg parameter
    print(arg)  # Print the value of arg to the console

    nifty_value = None
    spot_value = None

    if arg:
        arg_dict = json.loads(arg)
        nifty_value = arg_dict.get("nifty")
        spot_value = arg_dict.get("spot")
    oi_url = f"https://webapi.niftytrader.in/webapi/option/oi-change-data/?reqType={nifty_value}&reqDate={expiry_date}"

    dates_url = f"https://webapi.niftytrader.in/webapi/option/oi-change-data/?reqType={nifty_value}&reqDate="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    oi_response = requests.get(oi_url, headers=headers)
    oi_data = oi_response.json()

    dates_response = requests.get(dates_url, headers=headers)
    dates_data = dates_response.json()
    print(spot_value)

    spot_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={spot_value}"

    spot_response = requests.get(spot_url, headers=headers)
    spot_data = spot_response.json()

    result_data = spot_data.get("resultData")
    if result_data is not None:
        spot_price = result_data.get("last_trade_price")
        change_value = result_data.get("change_value")  # Added change_value
        change_per = result_data.get("change_per")
        if spot_price is not None:
            closest_prices = []
            calls_oi = []
            puts_oi = []

            oi_datas = oi_data.get("resultData", {}).get("oiDatas", [])

            for result in oi_datas:
                price = result.get("strike_price")
                if price is not None:
                    closest_prices.append(price)
                    calls_oi.append(result.get("calls_change_oi", 0))
                    puts_oi.append(result.get("puts_change_oi", 0))

            closest_prices, calls_oi, puts_oi = zip(
                *sorted(
                    zip(closest_prices, calls_oi, puts_oi),
                    key=lambda x: abs(x[0] - spot_price)
                )
            )

            bar_count = request.GET.get("bar_count")
            if bar_count:
                if bar_count == "all":
                    closest_prices = closest_prices
                    calls_oi = calls_oi
                    puts_oi = puts_oi
                else:
                    bar_count = int(bar_count)
                    closest_prices = closest_prices[:bar_count]
                    calls_oi = calls_oi[:bar_count]
                    puts_oi = puts_oi[:bar_count]

            dates = []
            for result in dates_data.get("resultData", {}).get("oiExpiryDates", []):
                date_str = result.split("T")[0]
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                formatted_date = datetime.datetime.strftime(
                    date_obj, "%Y-%m-%d")
                dates.append(formatted_date)

            context = {
                'spot_price': spot_price,
                'closest_prices': closest_prices,
                'change_value': change_value,  # Added change_value
                'change_per': change_per,  #
                'calls_oi': calls_oi,
                'puts_oi': puts_oi,
                'dates': dates
            }
            return JsonResponse(context)

    return JsonResponse({'message': 'Data not available'})


def scale_stacking_chart(request):
    symbol_pain = request.GET.get('symbol', 'nifty')
    print(symbol_pain)  # Get the selected symbol from the request parameters

    url = f"https://webapi.niftytrader.in/webapi/Option/symbol-max-pain-data?symbol={symbol_pain}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    result_data = data.get("resultData", [])
    if result_data:
        df = pd.DataFrame(result_data)
        df["strike_price"] = df["strike_price"].astype(
            str)  # Convert "strike_price" column to strings
        df = df[df["strike_price"] != "pp"]  # Filter out "pp" values
        df = df[df["strike_price"] != "cp"]  # Filter out "cp" values
        # Filter out "strike_price" headers
        df = df[~df["strike_price"].str.startswith("strike_price")]

        labels = df["strike_price"].tolist()
        pp_values = df["pp"].tolist()
        cp_values = df["cp"].tolist()

        chart_data = {
            'labels': labels,
            'pp_values': pp_values,
            'cp_values': cp_values
        }

        return JsonResponse(chart_data)
    else:
        return JsonResponse({'message': 'No data available'})


def pcr_volume(request):
    pcr_args = request.GET.get('trade', 'niftyvolumepcr')

    url = f"https://webapi.niftytrader.in/webapi/option/oi-volume-data?reqType={pcr_args}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    timestamps = []
    pcr_index_close = []
    pcr = []

    for pcrdata in data["resultData"]:
        timestamp = pcrdata["time"]
        time_parts = timestamp.split("T")[1].split(
            ":")[:2]  # Extract hours and minutes
        formatted_time = ":".join(time_parts)
        timestamps.append(formatted_time)
        pcr.append(pcrdata["pcr"])
        pcr_index_close.append(pcrdata["index_close"])

    chart_data = {
        'pcr_values': pcr,
        'time_values': timestamps,
        'index_close_values': pcr_index_close,
    }

    return JsonResponse(chart_data)


def nifty_tracker(request):
    return render(request, "nifty_tracker.html")


def get_52_week_data(request):
    url = "https://www.nseindia.com/api/live-analysis-52Week?index=high"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Convert the JSON data to a string
        api_response = json.dumps(data)

        if response.status_code == 200:
            # Delete the previous saved data
            StockData.objects.all().delete()

            # Create a new entry with the updated API response
            StockData.objects.create(api_response=api_response)

            return JsonResponse(data, safe=False)
        else:
            try:
                # Retrieve the saved API response from the database
                saved_data = StockData.objects.first()
                saved_response = saved_data.api_response

                # Convert the string back to JSON
                saved_json = json.loads(saved_response)

                return JsonResponse(saved_json, safe=False)
            except AttributeError:
                # Return an empty JSON response if no saved data is available
                return JsonResponse([], safe=False)
    except requests.exceptions.RequestException:
        # Handle the case when the API request fails
        try:
            # Retrieve the saved API response from the database
            saved_data = StockData.objects.first()
            saved_response = saved_data.api_response

            # Convert the string back to JSON
            saved_json = json.loads(saved_response)

            return JsonResponse(saved_json, safe=False)
        except AttributeError:
            # Return an empty JSON response if no saved data is available
            return JsonResponse([], safe=False)


def get_52_week_low_data(request):
    url = "https://www.nseindia.com/api/live-analysis-52Week?index=low"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Convert the JSON data to a string
        api_response = json.dumps(data)

        if response.status_code == 200:
            # Delete the previous saved data
            Stock_Low_Data.objects.all().delete()

            # Create a new entry with the updated API response
            Stock_Low_Data.objects.create(api_response_low=api_response)

            return JsonResponse(data, safe=False)
        else:
            try:
                # Retrieve the saved API response from the database
                saved_data = Stock_Low_Data.objects.first()
                saved_response = saved_data.api_response_low

                # Convert the string back to JSON
                saved_json = json.loads(saved_response)

                return JsonResponse(saved_json, safe=False)
            except AttributeError:
                # Return an empty JSON response if no saved data is available
                return JsonResponse([], safe=False)
    except requests.exceptions.RequestException:
        # Handle the case when the API request fails
        try:
            # Retrieve the saved API response from the database
            saved_data = Stock_Low_Data.objects.first()
            saved_response = saved_data.api_response_low

            # Convert the string back to JSON
            saved_json = json.loads(saved_response)

            return JsonResponse(saved_json, safe=False)
        except AttributeError:
            # Return an empty JSON response if no saved data is available
            return JsonResponse([], safe=False)


def only_buyers(request):
    url = "https://www.nseindia.com/api/live-analysis-price-band-hitter"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Convert the JSON data to a string
        api_response = json.dumps(data)

        if response.status_code == 200:
            # Delete the previous saved data
            Only_buyers.objects.all().delete()

            # Create a new entry with the updated API response
            Only_buyers.objects.create(api_response_buyers=api_response)

            return JsonResponse(data, safe=False)
        else:
            try:
                # Retrieve the saved API response from the database
                saved_data = Only_buyers.objects.first()
                saved_response = saved_data.api_response_buyers

                # Convert the string back to JSON
                saved_json = json.loads(saved_response)

                return JsonResponse(saved_json, safe=False)
            except AttributeError:
                # Return an empty JSON response if no saved data is available
                return JsonResponse([], safe=False)
    except requests.exceptions.RequestException:
        # Handle the case when the API request fails
        try:
            # Retrieve the saved API response from the database
            saved_data = Only_buyers.objects.first()
            saved_response = saved_data.api_response_buyers

            # Convert the string back to JSON
            saved_json = json.loads(saved_response)

            return JsonResponse(saved_json, safe=False)
        except AttributeError:
            # Return an empty JSON response if no saved data is available
            return JsonResponse([], safe=False)


def index(request):
    return render(request, 'index.html')


def get_data_buildup(request):
    buildup_type = request.GET.get('buildup_type', 'all')

    if buildup_type == 'all':
        urls = [
            "https://trendlyne.com/futures-options/api-filter/futures/31-aug-2023-next/long_build_up/",
            "https://trendlyne.com/futures-options/api-filter/futures/31-aug-2023-next/short_build_up/",
            "https://trendlyne.com/futures-options/api-filter/futures/31-aug-2023-next/long_unwinding/",
            "https://trendlyne.com/futures-options/api-filter/futures/31-aug-2023-next/short_covering/"
        ]
    else:
        urls = [
            f"https://trendlyne.com/futures-options/api-filter/futures/31-aug-2023-next/{buildup_type}/"
        ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    data = []

    for url in urls:
        response = requests.get(url, headers=headers)
        data_oi = response.json()

        # Extract the desired values from data_oi
        name_values_list = [
            (
                item[0]["name"],  # name
                item[1],  # price
                item[2],  # Date Chang
                item[3],  # Volume Contracts
                item[4],  # % Volume Contracts
                item[6],  # OI
                item[7],  # %OI
                item[8],  # Basis
                item[9],  # COC
                item[10],  # Spot
                item[11]  # Build Up
            )
            for item in data_oi["tableData"]
        ]

        data.extend(name_values_list)

    response_data = {
        "buildup_type": buildup_type,
        "data": data,
        "columns": [
            "Name",
            "Price",
            "Date Change",
            "Volume Contracts",
            "% Volume Contracts",
            "OI",
            "%OI",
            "Basis",
            "COC",
            "Spot",
            "Build Up"
        ]
    }

    return JsonResponse(response_data)


def watch_list(request):
    return render(request, "watch_list.html")


def port_folio_management(request):
    return render(request, "port_folio_management.html")


def new_options_data(request):
    symbol_name_url = "https://webapi.niftytrader.in/webapi/symbol/psymbol-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response_symbol = requests.get(symbol_name_url, headers=headers)
    data_option_symbol_name = response_symbol.json()

    all_symbol_names = ["nifty", "banknifty", "finifty", "---"] + [op_symbol_name["symbol_name"]
                                                                   for op_symbol_name in data_option_symbol_name["resultData"]]

    symbol = request.GET.get("symbol_op", "nifty")

    date = request.GET.get("date_op", "")
    print(symbol)
    print(date)

    url = f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={symbol}&expiryDate={date}"
    print(url)

    response = requests.get(url, headers=headers)
    data_option_chain = response.json()
    Symbol_expiry_date_op = []
    Symbol_data_op = []

    for dates_all in data_option_chain["resultData"]["opExpiryDates"]:
        formatted_date = dates_all[:10]
        Symbol_expiry_date_op.append(formatted_date)

    for symbol_data_all in data_option_chain["resultData"]["opDatas"]:
        Symbol_data_op.append(symbol_data_all)

    spot_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol=NIFTY+50"
    spot_response = requests.get(spot_url, headers=headers)
    spot_json = spot_response.json()
    spot__price = spot_json["resultData"]["last_trade_price"]

    data = {
        "Symbol_expiry_date_op": Symbol_expiry_date_op,
        "Symbol_data_op": Symbol_data_op,
        "symbol_names": all_symbol_names,
        "spot__price": spot__price,
    }

    # Change symbol_names to lowercase
    data["symbol_names"] = [symbol.lower() for symbol in all_symbol_names]

    return JsonResponse(data, safe=False)


def options_simulator(request):
    return render(request, "options_simulator.html")


def admin_report(request):
    return render(request, "admin_report.html")


def feedback(request):
    return render(request, "feedback.html")


def stock_list(request):
    stock_url = "https://webapi.niftytrader.in/webapi/Symbol/stock-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    stock_data = requests.get(stock_url, headers=headers)
    stock_json = stock_data.json()

    All_stocks = []
    for stock in stock_json["resultData"]:
        stock_info = {
            "symbol_name": stock["symbol_name"],
            "today_close": stock["today_close"],
            "change_percent": stock["change_percent"]
        }
        All_stocks.append(stock_info)

    return JsonResponse(All_stocks, safe=False)


def performance_chart(request):
    today = datetime.datetime.now().date()
    yesterday = today - datetime.timedelta(days=0)
    ts2 = str(int(datetime.datetime(yesterday.year,
              yesterday.month, yesterday.day).timestamp()))

    # Get the 'days' parameter from the request, defaulting to 20 if not provided
    d_days = int(request.GET.get('days', '20'))
    ts1 = str(
        int((datetime.datetime.now() - datetime.timedelta(days=d_days+1)).timestamp()))

    interval = '1d'
    history_data = request.GET.get('historical_symbols', '%5ENSEI')
    events = 'history'
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + history_data + '?period1=' \
          + ts1 + '&period2=' + ts2 + '&interval=' + interval + \
        '&events=' + events + '&includeAdjustedClose=true'
    try:
        stockdata = pd.read_csv(url)
        stockdata['Date'] = pd.to_datetime(stockdata['Date'])
        stockdata = stockdata.dropna()
        dates = stockdata['Date'].dt.strftime('%b-%d').tolist()
        closes = stockdata['Close'].tolist()
        opens = stockdata['Open'].tolist()
        differences = []
        prev_close_today_open_diff = []
        prev_close_today_open_diff_minus_diff = []
        prev_open = opens[:-1]  # Store previous open values
        prev_close = closes[:-1]
        prev_close_today_close = []
        prev_close_today_open_diff_minus_diff_main = []
        # Store previous close values

        for i in range(len(closes)):
            if i > 0:
                difference = closes[i] - closes[i-1]
                prev_close_today_open = closes[i-1] - opens[i]
                prev_close_today_close_inner = closes[i-1] - closes[i]
                prev_close_today_close.append(prev_close_today_close_inner)
                if difference is not None and prev_close_today_open is not None:
                    prev_close_today_open_diff.append(prev_close_today_open)
                    prev_close_today_open_diff_minus_diff.append(
                        prev_close_today_open)
                    prev_close_today_open_diff_minus_diff_main.append(
                        abs(prev_close_today_open) - abs(difference))
            else:
                difference = None
            differences.append(difference)
        dates = dates[1:]
        closes = closes[1:]
        opens = opens[1:]
        differences = differences[1:]
        data = {
            'dates': dates,
            'closes': closes,
            'opens': opens,
            'differences': differences,
            'prev_close_today_open_diff': prev_close_today_open_diff,
            'prev_close_today_open_diff_minus_diff': prev_close_today_open_diff_minus_diff,
            'prev_open': prev_open,
            'prev_close': prev_close,
            'prev_dates': dates[1:],
            'prev_close_today_close': (prev_close_today_close),
            'prev_close_today_open_diff_minus_diff_main': prev_close_today_open_diff_minus_diff_main
        }

        return JsonResponse(data)
    except:
        return JsonResponse({'error': 'Failed to fetch stock data'})


def blog_news_data(request):
    url = "https://newsapi.org/v2/top-headlines?country=In&category=business&apiKey=71c44e5689f5421b99dc55f6217b25ca"
    cricket_news = requests.get(url).json()
    a = cricket_news['articles']
    data = []
    for i in range(len(a)):
        f = a[i]
        data.append({
            'title': f['title'],
            'description': f['description'],
            'imageUrl': f['urlToImage'],
            'url': f['url'],
            'source': f['source'],
            'publishedAt': f['publishedAt']
        })
    return JsonResponse(data, safe=False)


def blog_news(request):
    return render(request, "blog_news.html")


def contributor(request):
    return render(request, "contributor.html")


def get_all_dates():
    url_date = "https://webapi.niftytrader.in/webapi/Resource/contrubutors-date-list?symbol=nifty"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date = requests.get(url_date, headers=headers)
    data_date = response_date.json()
    all_dates = []
    for date in data_date["resultData"]["start_date"]:
        all_dates.append(date)
    print(all_dates)     

    return all_dates


def contributors_data(request):
    try:
        selected_date = request.GET.get('date')
        selected_filter = request.GET.get('filter', 'nifty')
        if not selected_date:
            # Set initial selected date
            # Replace this with your code to fetch all available dates
            all_dates = get_all_dates()
            print(all_dates)
            if all_dates:
                selected_date = all_dates[1]

        print("Selected Date:", selected_date)
        print("Selected Filter:", selected_filter)


        url = f'https://webapi.niftytrader.in/webapi/Resource/contributors-data?symbol={selected_filter}&expiryDate={selected_date}'
        url_date = f"https://webapi.niftytrader.in/webapi/Resource/contrubutors-date-list?symbol={selected_filter}"
        print(url)
        print(url_date)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        response_date = requests.get(url_date, headers=headers)

        if response.status_code == 200 and response_date.status_code == 200:
            data = response.json()
            data_date = response_date.json()

            all_dates = data_date.get("resultData", {}).get("start_date", [])
            if not all_dates:
                error_dict = {
                    "error": "No dates available"
                }
                return JsonResponse(error_dict, status=500)

            # print(all_dates[1])

            date_max = data_date.get("resultData", {}).get("max_date")

            stocks_data = data.get("resultData", {}).get("contributor_data", [])
            stocks_data_ltp = data.get("resultData", {}).get("enddate", [])
            # print(date_max)

            # print(stocks_data_ltp)

            stocks_data_symbol = [stock["symbol_name"]
                                  for stock in stocks_data]

            filtered_data = [
                stock for stock in stocks_data_ltp if stock["symbol_name"] in stocks_data_symbol]

            for stock in stocks_data:
                for filtered_stock in filtered_data:
                    if stock["symbol_name"] == filtered_stock["symbol_name"]:
                        stock["last_trade_price"] = filtered_stock["last_trade_price"]
                        break

            # positive_price_difference = [stock for stock in stocks_data if stock["price_difference"] >= 0]
            # negative_price_difference = [stock for stock in stocks_data if stock["price_difference"] < 0]

            data_dict = {
                "all_dates": all_dates,
                "date_max": date_max,
                "stocks_data": stocks_data,


            }
            # print(stocks_data)

            return JsonResponse(data_dict)

        else:
            error_dict = {
                "error": "Invalid API response"
            }
            return JsonResponse(error_dict, status=500)

    except requests.exceptions.RequestException as e:
        error_dict = {
            "error": str(e)
        }
        return JsonResponse(error_dict, status=500)
    except (KeyError, ValueError) as e:
        error_dict = {
            "error": "Invalid API response format"
        }
        return JsonResponse(error_dict, status=500)


def future_data_chart(request):
    selected_symbol = request.GET.get('symbol', "NIFTY")
    print(selected_symbol)
    psymbol_url = "https://webapi.niftytrader.in/webapi/symbol/psymbol-list"
    future_url = f"https://webapi.niftytrader.in/webapi/symbol/future-expiry-data?symbol={selected_symbol}"
    spot_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={selected_symbol}"
    chart_url = f"https://webapi.niftytrader.in/webapi/symbol/future-expiry-chart-data?symbol={selected_symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    psymbol_response = requests.get(psymbol_url, headers=headers)
    future_response = requests.get(future_url, headers=headers)
    spot_response = requests.get(spot_url, headers=headers)
    chart_response = requests.get(chart_url, headers=headers)

    psymbol_data = psymbol_response.json()
    future_data = future_response.json()
    spot_data = spot_response.json()
    chart_data = chart_response.json()
    # print(chart_data)

    All_symbol = []
    for psymbol in psymbol_data["resultData"]:
        All_symbol.append(psymbol["symbol_name"])
  
    future_expiry_list = []
    for future in future_data["resultData"]:
        oi_change = future["oi"] - future["prev_oi"]
        print(oi_change)
        
        # Check if prev_oi is zero to avoid division by zero
        if future["prev_oi"] != 0:
            oi_percent_change = (oi_change / future["prev_oi"]) * 100
        else:
            oi_percent_change = 0  # Set to 0 or handle as appropriate for your use case
        
        print(oi_percent_change)
        
        change_price = future["last_price"] - future["prev_close"]
        
        # Check if prev_close is zero to avoid division by zero
        if future["prev_close"] != 0:
            change_percent = (change_price / future["prev_close"]) * 100
        else:
            change_percent = 0  # Set to 0 or handle as appropriate for your use case
        
        future_expiry_list.append({
            "expiry": future["expiry"],
            "oi": future["oi"],
            "prev_oi": future["prev_oi"],
            "oi_change": oi_change,
            "oi_percent_change": oi_percent_change,
            "last_price": future["last_price"],
            "change_price": change_price,
            "change_percent": change_percent,
            "high": future["high"],
            "low": future["low"]
        })


    spot_symbol_list = spot_data["resultData"]["symbol_name"]
    spot_price_list = spot_data["resultData"]["last_trade_price"]
    spot_change_list = spot_data["resultData"]["change_per"]

    chart_data_list = []

    for chart in chart_data["resultData"]:
        chart_data_list.append(chart)

    # Assuming you have three dictionaries in chart_data_list
    if len(chart_data_list) >= 3:
        chart1 = chart_data_list[0]
        chart2 = chart_data_list[1]
        chart3 = chart_data_list[2]

    print(chart1)
    print(chart2)
    print(chart3)

    data = {
        "All_symbol": All_symbol,
        "future_expiry_list": future_expiry_list,
        "spot_symbol_list": spot_symbol_list,
        "spot_price_list": spot_price_list,
        "spot_change_list": spot_change_list,
        "chart_data_list": chart_data_list,
        "chart1": chart1,
        "chart2": chart2,
        "chart3": chart3,
    }

    return JsonResponse(data)


def stock_future(request):
    return render(request, "stock_future.html")


def get_news_data(request):
    filter = request.GET.get('filter', 'WorldNews')
    language = request.GET.get('language', 'English')

    url = f"https://webapi.niftytrader.in/webapi/Other/rss-feeds-data?NewsType={filter}&lanType={language}"
    print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return JsonResponse(data)


def chart_topgainer(request):
    return render(request, "chart_topgainer.html")


def fetch_option_data_with_spot_price(request):
    selected_symbol = request.GET.get('symbol','NIFTY')
    selectedDate = request.GET.get('selectedDate')
    print(selected_symbol)
    print(selectedDate)

    url = f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={selected_symbol}&expiryDate={selectedDate}"

    url_symbol_list = "https://webapi.niftytrader.in/webapi/symbol/psymbol-list"
    url_india_vix = "https://webapi.niftytrader.in/webapi/Other/other-symbol-spot-data?symbol=INDIA+VIX"
    url_spot_data = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={selected_symbol}"
    

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    response_url = requests.get(url_symbol_list, headers=headers)
    response_india_vix = requests.get(url_india_vix, headers=headers)
    response_spot_data = requests.get(url_spot_data, headers=headers)

    data = response.json()
    symbol_data = response_url.json()
    india_vix_data = response_india_vix.json()
    india_spot_data = response_spot_data.json()

    total_put_volume = 0
    total_call_volume = 0
    All_option_data = []
    All_dates = []
    All_symbols = []
    India_vix_data = india_vix_data["resultData"]
    india_spot_data = india_spot_data["resultData"]

    for symbol in symbol_data['resultData']:
        All_symbols.append(symbol["symbol_name"])

    for options_date in data['resultData']["opExpiryDates"]:
        if options_date is not None and isinstance(options_date, str):
            date_str = options_date.split("T")[0]
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            print(options_date)
            print(formatted_date)
            All_dates.append(formatted_date)
    print(All_dates)        

    total_puts_change_oi = 0
    total_calls_change_oi = 0

    for options_data in data['resultData']["opDatas"]:
        All_option_data.append(options_data)
        put_volume = options_data["puts_volume"]
        call_volume = options_data["calls_volume"]
        puts_change_oi = options_data["puts_change_oi"]
        calls_change_oi = options_data["calls_change_oi"]

        total_put_volume += put_volume
        total_call_volume += call_volume

        total_puts_change_oi += puts_change_oi
        total_calls_change_oi += calls_change_oi

    # Check if total_put_volume is zero to avoid division by zero
    if total_put_volume != 0:
        put_call_ratio = total_call_volume / total_put_volume
    else:
        put_call_ratio = 0  # Set a default value or handle it differently

    if total_puts_change_oi != 0:
        oi_pcr = total_calls_change_oi / total_puts_change_oi
    else:
        oi_pcr = 0  # Set a default value or handle it differently

    print(oi_pcr)
    response_data = {
        "india_spot_data": india_spot_data,
        "India_vix_data": India_vix_data,
        "All_symbols": All_symbols,
        "All_dates": All_dates,
        "All_option_data": All_option_data,
        "total_put_volume": total_put_volume,
        "total_call_volume": total_call_volume,
        "put_call_ratio": put_call_ratio,
        "oi_pcr": oi_pcr,

    }

    return JsonResponse(response_data)


def stock_option_chain(request):
    return render(request, 'stock_option_chain.html')


def option_dashboard(request):
    return render(request, 'option_dashboard.html')


def breakout_data(request):
    url = "https://webapi.niftytrader.in/webapi/Resource/nse-break-out-data"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data["resultData"])

    # Convert the DataFrame to a list of dictionaries
    data_dict = df.to_dict(orient='records')

    # If you want to return the data as JSON
    return JsonResponse(data_dict, safe=False)


def volume_socker(request):
    return render(request, 'volume_socker.html')


def get_gainers_data_separate(request):

    range_type = request.GET.get('range_type')
    print(range_type)

    url = f"https://webapi.niftytrader.in/webapi/Symbol/top-gainers-historical-data?range_type=gainers&range_days={range_type}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    top_gainers_stock = pd.DataFrame(data["resultData"])

    # You can now manipulate the data using pandas functions if needed

    return JsonResponse(top_gainers_stock.to_dict(orient="records"), safe=False)


def top_gainers(request):
    return render(request, 'top_gainer.html')


def get_gainers_data_separate(request):

    range_type = request.GET.get('range_type')
    print(range_type)

    url = f"https://webapi.niftytrader.in/webapi/Symbol/top-gainers-historical-data?range_type=gainers&range_days={range_type}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    top_gainers_stock = pd.DataFrame(data["resultData"])

    # You can now manipulate the data using pandas functions if needed

    return JsonResponse(top_gainers_stock.to_dict(orient="records"), safe=False)


def top_loosers(request):
    return render(request, 'top_loosers.html')


def get_loosers_data_separate(request):

    range_type = request.GET.get('range_type')
    print(range_type)

    url = f"https://webapi.niftytrader.in/webapi/Symbol/top-gainers-historical-data?range_type=loosers&range_days={range_type}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    top_gainers_stock = pd.DataFrame(data["resultData"])

    # You can now manipulate the data using pandas functions if needed

    return JsonResponse(top_gainers_stock.to_dict(orient="records"), safe=False)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_gap_data(request):
    date = request.GET.get('date')
    print(date)
    gap_date_url = "https://webapi.niftytrader.in/webapi/Resource/gap-analysis-date-list"
    gap_data_url = f"https://webapi.niftytrader.in/webapi/Resource/gap-analysis?Date={date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    gap_date_response = requests.get(gap_date_url, headers=headers)
    gap_data_response = requests.get(gap_data_url, headers=headers)
    gap_date = gap_date_response.json()
    gap_data = gap_data_response.json()

    gap_up_all_data = gap_data["resultData"]["gap_up_stocks"]
    gap_down_all_data = gap_data["resultData"]["gap_down_stocks"]

    data = {
        "gap_dates": gap_date["resultData"],
        "gap_up_stocks": gap_up_all_data,
        "gap_down_stocks": gap_down_all_data,
    }

    return Response(data)


def gap_up_gap_down(request):
    return render(request, 'gap_up_gap_down.html')




# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_to_watchlist(request):
    if request.method == "POST":
        data = request.POST
        symbol_name = data.get("symbol_name")
        prev_high = data.get("prev_high")
        today_low = data.get("today_low")
        today_high = data.get("today_high")
        change_value = data.get("change_value")
        change_percent = data.get("change_percent")
        prev_close = data.get("prev_close")
        today_volume = data.get("today_volume")
        print(symbol_name)
        existing_item = Watchlist.objects.filter(
            user=request.user,
            symbol_name=symbol_name
        ).first()
        if existing_item:
            return JsonResponse({'message1': f' {symbol_name} already exists in your watch list'})
        else:
            # Save the data to the Watchlist model
            watchlist_entry = Watchlist(
                # Assuming the user is authenticated and you're using Django's built-in User model
                user=request.user,
                symbol_name=symbol_name,
                prev_high=prev_high,
                today_low=today_low,
                today_high=today_high,
                change_value=change_value,
                change_percent=change_percent,
                prev_close=prev_close,
                today_volume=today_volume,
            )
            watchlist_entry.save()

            return JsonResponse({'message2': f' {symbol_name} added to your watch list'})
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_watchlist_item(request, item_id):
    print(item_id)
    try:
        # Retrieve the symbol_name before deleting the watchlist item
        symbol_name = Watchlist.objects.filter(user=request.user, symbol_name=item_id).values_list('symbol_name', flat=True).first()

        # Delete the watchlist item with the given item_id from the database
        Watchlist.objects.filter(user=request.user, symbol_name=item_id).delete()

        # Return a success message along with the symbol_name
        return JsonResponse({'message': f' {symbol_name} remove from your watchlist'})
    except Exception as e:
        # Return an error message if the item deletion fails
        return JsonResponse({'error': 'Error occurred while deleting item'})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Watchlist

@csrf_exempt
def get_watchlist_data(request):
    if request.user.is_authenticated:
        user_watchlist = Watchlist.objects.filter(user=request.user)
        watchlist_data = []
        print(user_watchlist)
        for item in user_watchlist:
            watchlist_url = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={item.symbol_name}"
            chart_watchlist_url = f"https://webapi.niftytrader.in/webapi/Symbol/symbol-ltp-chart?symbol={item.symbol_name}"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            watchlist_response = requests.get(watchlist_url, headers=headers)
            chart_watchlist_response = requests.get(chart_watchlist_url, headers=headers)

            watchlist_data_url = watchlist_response.json()
            chart_watchlist_data = chart_watchlist_response.json()
            watch_list = watchlist_data_url["resultData"]
            chart_data = chart_watchlist_data["resultData"]

            # Combine watch_list and chart_data into a single dictionary
            symbol_data = {
               
                'watch_list': watch_list,
                'chart_data': chart_data
            }
            watchlist_data.append(symbol_data)

        return JsonResponse({"watchlist_data": watchlist_data})
    else:
        return JsonResponse({"watchlist_data": []})



@api_view(['GET'])
def get_intraday_breakout_data(request):
    instraday_url = "https://webapi.niftytrader.in/webapi/Resource/nse-break-out-data"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    instra_breakout_response = requests.get(instraday_url, headers=headers)
    intra_breakout_data = instra_breakout_response.json()
    main_intra_breakout_data = intra_breakout_data["resultData"]
    return JsonResponse(main_intra_breakout_data, safe=False)


def intraday_breakouts(request):
    return render(request ,"intraday_breakouts.html")




import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def opening_clue_data_view(request):
    opening_clue_url = "https://webapi.niftytrader.in/webapi/Resource/open-analysis"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    
    opening_clue_response = requests.get(opening_clue_url, headers=headers)
    opening_clue_data = opening_clue_response.json()
    result_data = opening_clue_data["resultData"]
    
    return Response(result_data)

def opening_price_clues(request):
    return render(request ,"opening_price_clues.html")



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Border_FetchedData
import requests
import random
import pandas as pd
import json

@api_view(['GET'])
def base_api_border_top(request):
    prited_data = Border_FetchedData.objects.all()
    print(prited_data)
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        all_list = []
        for d in data['data']:
            if d['symbol'] != 'NIFTY 50':
                all_list.append({
                    'symbol': d['symbol'],
                    'lastPrice': d['lastPrice'],
                    'pChange': d['pChange']
                })

        # Randomly select 10 symbols from the top 50
        random_symbols = random.sample(all_list, 50)

        df = pd.DataFrame(random_symbols)
        symbols = df.to_dict(orient='records')

        # Convert the data to JSON and save it in the database
        Border_FetchedData.objects.all().delete()  # Delete previous data
        fetched_data = Border_FetchedData(data=json.dumps(symbols))  # Convert to JSON string
        fetched_data.save()

        return Response(symbols)
    else:
        # If data couldn't be fetched, return the saved data from the database
        try:
            fetched_data = Border_FetchedData.objects.latest('id')
            data = json.loads(fetched_data.data)  # Convert JSON string back to Python objects
            # Return the data as JSON response
            return Response(data)
        except Border_FetchedData.DoesNotExist:
            return Response({"message": "Data not available."}, status=404)



from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_derivative_data(request):
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

    for i, item in enumerate(All_derivative_data):
        oi = item['oi']
        prev_oi = item['prev_oi']
        last_price = item['last_price']
        prev_close = item['prev_close']


        item['change_in_OI'] = oi - prev_oi
        item['change_in_LTP'] = last_price - prev_close


        if prev_oi != 0:
            item['percentage_change_in_OI'] = (item['change_in_OI'] / prev_oi) * 100
        else:
            item['percentage_change_in_OI'] = 0

        if prev_close != 0:
            item['percentage_change_in_LTP'] = (item['change_in_LTP'] / prev_close) * 100
        else:
            item['percentage_change_in_LTP'] = 0


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

    filter_param = request.GET.get('filter')

    if filter_param:

        filtered_data = [item for item in All_derivative_data if item['filter'] == filter_param]
    else:
        filtered_data = All_derivative_data

    return Response(filtered_data)


def derivative_summary(request):
    return render(request ,"derivative_summary.html")


# Import necessary modules
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Define the view function
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



    All_derivative_data = data.get("resultData", [])



    for item in All_derivative_data:
        oi = item.get('oi', 0)
        prev_oi = item.get('prev_oi', 0)
        last_price = item.get('last_price', 0)
        prev_close = item.get('prev_close', 0)

        item['change_in_OI'] = oi - prev_oi
        item['change_in_LTP'] = last_price - prev_close

        if prev_oi != 0:
            item['percentage_change_in_OI'] = (item['change_in_OI'] / prev_oi) * 100
        else:
            item['percentage_change_in_OI'] = 0

        if prev_close != 0:
            item['percentage_change_in_LTP'] = (item['change_in_LTP'] / prev_close) * 100
        else:
            item['percentage_change_in_LTP'] = 0

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
            {'symbol_name': item['symbol_name'], 'percentage_change_in_OI': item['percentage_change_in_OI'],'percentage_change_in_LTP':item['percentage_change_in_LTP']}
            for item in All_derivative_data if item['filter'] == filter_param
        ]
        # Sort the filtered data based on percentage_change_in_OI in descending order
        sorted_data = sorted(filtered_data, key=lambda item: -item['percentage_change_in_OI'])
        filtered_data_by_filter[filter_param] = sorted_data

    return Response(filtered_data_by_filter)

from django.http import JsonResponse
import requests
from .models import VolumeGainer

def nse_volume_shocker(request):
    url = "https://www.nseindia.com/api/live-analysis-volume-gainers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        sorted_data = sorted(data['data'], key=lambda x: x['pChange'], reverse=True)


        filtered_data = [{'symbol': item['symbol'], 'pChange': item['pChange']} for item in sorted_data]

        VolumeGainer.objects.all().delete()
     
        volume_gainer_obj = VolumeGainer(data_json=json.dumps(filtered_data))
        volume_gainer_obj.save()

        return JsonResponse(filtered_data, safe=False)
    except requests.exceptions.RequestException as e:
        volume_gainer_obj = VolumeGainer.objects.first()
        if volume_gainer_obj:
            data = json.loads(volume_gainer_obj.data_json)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)







from django.http import JsonResponse
import requests
from .models import MostActiveStock

def nse_most_active_stock(request):
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        All_most_active_value = []
        for value_data in data["data"]:
            symbol = value_data["symbol"]
            totalTradedValue = value_data["totalTradedValue"]
            if symbol != 'NIFTY 50':
                All_most_active_value.append({"symbol": symbol, "totalTradedValue": totalTradedValue})

   
        All_most_active_value = sorted(All_most_active_value, key=lambda x: x["totalTradedValue"], reverse=True)

        MostActiveStock.objects.all().delete()
        most_active_stock_obj = MostActiveStock(data_json=json.dumps(All_most_active_value))
        most_active_stock_obj.save()

        return JsonResponse(All_most_active_value, safe=False)

    except requests.exceptions.RequestException as e:
        most_active_stock_obj = MostActiveStock.objects.first()
        if most_active_stock_obj:
            data = json.loads(most_active_stock_obj.data_json)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)






from django.http import JsonResponse
import requests
from .models import MostSpreadStock

def nse_most_spread_stock(request):
    url = "https://www.nseindia.com/api/liveEquity-derivatives?index=top20_spread_contracts"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)

        All_most_spread_value = []
        for value_data in data["data"]:
            symbol = value_data["symbol"]
            spread = value_data["spread"]
            All_most_spread_value.append({"symbol": symbol, "spread": spread})


        All_most_spread_value = sorted(All_most_spread_value, key=lambda x: x["spread"], reverse=True)

        MostSpreadStock.objects.all().delete()
        most_spread_stock_obj = MostSpreadStock(data_json=json.dumps(All_most_spread_value))
        most_spread_stock_obj.save()

        return JsonResponse(All_most_spread_value, safe=False)

    except requests.exceptions.RequestException as e:
        most_spread_stock_obj = MostSpreadStock.objects.first()
        if most_spread_stock_obj:
            data = json.loads(most_spread_stock_obj.data_json)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)


def dashboard_news_feed(request):
    url = "https://webapi.niftytrader.in/webapi/other/dashboard-rss-feeds"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    return JsonResponse(data)



# from django.shortcuts import render
# import pandas as pd
# import yfinance as yf
# import numpy as np
# from django.http import JsonResponse

# def fetch_stock_data(ticker, start_date, end_date):
#     data = yf.download(ticker, start=start_date, end=end_date)
#     return data

# def strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital):
#     # Check if the expiration_date is in the stock_data DataFrame
#     if expiration_date not in stock_data.index:
#         raise ValueError(f"Expiration date {expiration_date} is not available in the stock_data.")

#     # Buy the call and put options at the specified strike prices and expiration date
#     call_option = stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0] - call_strike
#     put_option = put_strike - stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0]

#     # Calculate total investment cost
#     total_cost = call_option + put_option

#     # Compute the profit/loss for each trading day
#     stock_data['Strangle_PnL'] = stock_data['Open'] - (stock_data['Open'].shift(1) + total_cost)

#     # Calculate cumulative PnL
#     stock_data['Cumulative_PnL'] = stock_data['Strangle_PnL'].cumsum()

#     # Calculate the number of contracts we can buy with initial capital
#     num_contracts = int(initial_capital // total_cost)

#     # Calculate the final PnL
#     final_pnl = num_contracts * stock_data.iloc[-1]['Strangle_PnL']

#     # Calculate max profit and max loss
#     max_profit = np.inf if call_strike > stock_data['Open'].max() else final_pnl
#     max_loss = -total_cost

#     # Calculate breakeven points
#     breakeven_upper = call_strike + total_cost
#     breakeven_lower = put_strike - total_cost

#     # Calculate reward-risk ratio
#     reward_risk_ratio = max_profit / abs(max_loss)

#     return stock_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio

# def strangle_chart(request):
#     # Define the parameters
#     ticker = '^NSEI'
#     start_date = '2023-07-20'
#     end_date = '2023-07-31'
#     call_strike = 20000  # Adjust this to the desired call strike price
#     put_strike = 19500  # Adjust this to the desired put strike price
#     expiration_date = '2023-07-27'  # Adjust this to the desired expiration date
#     initial_capital = 10000  # Adjust this to your desired initial capital

#     # Fetch historical stock data
#     stock_data = fetch_stock_data(ticker, start_date, end_date)

#     # Run the strangle backtest
#     try:
#         backtest_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio = strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital)
#     except ValueError as e:
#         error_message = str(e)
#         return render(request, 'strangle_app/strangle_chart.html', {'error_message': error_message})

#     # Create JSON representation of stock_data for the chart
#     stock_data_json = stock_data.reset_index().to_json(orient='records')

#     context = {
#         'stock_data_json': stock_data_json,
#         'final_pnl': final_pnl,
#         'max_profit': max_profit,
#         'max_loss': max_loss,
#         'breakeven_upper': breakeven_upper,
#         'breakeven_lower': breakeven_lower,
#         'reward_risk_ratio': reward_risk_ratio,
#     }

#     return render(request, 'strangle_app/strangle_chart.html', context)

# def strangle_chart_data(request):
#     # Define the parameters
#     ticker = '^NSEI'
#     start_date = '2023-07-20'
#     end_date = '2023-07-31'
#     call_strike = 20000  # Adjust this to the desired call strike price
#     put_strike = 19500  # Adjust this to the desired put strike price
#     expiration_date = '2023-07-27'  # Adjust this to the desired expiration date
#     initial_capital = 10000  # Adjust this to your desired initial capital

#     # Fetch historical stock data
#     stock_data = fetch_stock_data(ticker, start_date, end_date)

#     # Run the strangle backtest
#     try:
#         backtest_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio = strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital)
#     except ValueError as e:
#         return JsonResponse({'error': str(e)})

#     # Create JSON representation of stock_data for the chart
#     stock_data_json = stock_data.reset_index().to_dict(orient='records')

#     data = {
#         'stock_data': stock_data_json,
#         'final_pnl': final_pnl,
#         'max_profit': max_profit,
#         'max_loss': max_loss,
#         'breakeven_upper': breakeven_upper,
#         'breakeven_lower': breakeven_lower,
#         'reward_risk_ratio': reward_risk_ratio,
#     }

#     return JsonResponse(data)



# from django.shortcuts import render
# from django.http import JsonResponse
# import pandas as pd
# import yfinance as yf
# import numpy as np

# def fetch_stock_data(ticker, start_date, end_date):
#     data = yf.download(ticker, start=start_date, end=end_date)
#     return data

# def strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital):
#     # Check if the expiration_date is in the stock_data DataFrame
#     if expiration_date not in stock_data.index:
#         raise ValueError(f"Expiration date {expiration_date} is not available in the stock_data.")

#     # Buy the call and put options at the specified strike prices and expiration date
#     call_option = stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0] - call_strike
#     put_option = put_strike - stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0]

#     # Calculate total investment cost
#     total_cost = call_option + put_option

#     # Compute the profit/loss for each trading day
#     stock_data['Strangle_PnL'] = stock_data['Open'] - (stock_data['Open'].shift(1) + total_cost)

#     # Calculate cumulative PnL
#     stock_data['Cumulative_PnL'] = stock_data['Strangle_PnL'].cumsum()

#     # Calculate the number of contracts we can buy with initial capital
#     num_contracts = int(initial_capital // total_cost)

#     # Calculate the final PnL
#     final_pnl = num_contracts * stock_data.iloc[-1]['Strangle_PnL']

#     # Calculate max profit and max loss
#     max_profit = np.inf if call_strike > stock_data['Open'].max() else final_pnl
#     max_loss = -total_cost

#     # Calculate breakeven points
#     breakeven_upper = call_strike + total_cost
#     breakeven_lower = put_strike - total_cost

#     # Calculate reward-risk ratio
#     reward_risk_ratio = max_profit / abs(max_loss)

#     return stock_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio

#     # ... (same as before)

# def strangle_chart(request):
#     # Define the parameters (same as before)
#     ticker = '^NSEI'
#     start_date = '2023-07-20'
#     end_date = '2023-07-31'
#     call_strike = 20000  # Adjust this to the desired call strike price
#     put_strike = 19500  # Adjust this to the desired put strike price
#     expiration_date = '2023-07-27'  # Adjust this to the desired expiration date
#     initial_capital = 10000  # Adjust this to your desired initial capital

#     # Fetch historical stock data
#     stock_data = fetch_stock_data(ticker, start_date, end_date)

#     # Run the strangle backtest
#     try:
#         backtest_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio = strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital)
#     except ValueError as e:
#         return JsonResponse({'error_message': str(e)})

#     # Convert Infinity and NaN to None in the backtest data
#     backtest_data.replace([np.inf, -np.inf, np.nan], [None, None, None], inplace=True)

#     # Convert the date values to a more readable format
#     backtest_data['BacktestDate'] = backtest_data.index.strftime('%Y-%m-%d')

#     # Create a dictionary for each row in the DataFrame (orient='records') and store them in a list
#     stock_data_json = backtest_data.to_dict(orient='records')

#     context = {
#         'stock_data_json': stock_data_json,
#         'final_pnl': final_pnl,
#         'max_profit': max_profit.item() if np.isfinite(max_profit) else None,
#         'max_loss': max_loss.item(),
#         'breakeven_upper': breakeven_upper.item(),
#         'breakeven_lower': breakeven_lower.item(),
#         'reward_risk_ratio': reward_risk_ratio.item() if np.isfinite(reward_risk_ratio) else None,
#     }

#     return JsonResponse(context)





# from django.shortcuts import render
# import pandas as pd
# import yfinance as yf
# from django.http import JsonResponse

# def fetch_stock_data(ticker, start_date, end_date):
#     data = yf.download(ticker, start=start_date, end=end_date)
#     return data

# def straddle_backtest(stock_data, call_strike, put_strike, initial_capital):
#     # Buy the call and put options at the specified strike prices
#     stock_data['Call_PnL'] = stock_data['Open'] - call_strike
#     stock_data['Put_PnL'] = put_strike - stock_data['Open']

#     # Calculate the total investment cost
#     total_cost = stock_data['Call_PnL'].abs() + stock_data['Put_PnL'].abs()

#     # Calculate the profit/loss for each trading day
#     stock_data['Straddle_PnL'] = stock_data['Call_PnL'] + stock_data['Put_PnL']

#     # Calculate cumulative PnL
#     stock_data['Cumulative_PnL'] = stock_data['Straddle_PnL'].cumsum()

#     # Calculate max profit and max loss
#     max_profit = stock_data['Straddle_PnL'].max()
#     max_loss = stock_data['Straddle_PnL'].min()

#     # Calculate breakevens
#     breakeven_upper = call_strike + total_cost.min()
#     breakeven_lower = put_strike - total_cost.min()

#     # Calculate reward-risk ratio
#     reward_risk_ratio = max_profit / max_loss

#     # Calculate the final PnL
#     final_pnl = stock_data.iloc[-1]['Cumulative_PnL']

#     return stock_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio

# def straddle_view(request):
#     return render(request, 'straddle_app/straddle.html')

# def get_straddle_backtest_data(request):
#     ticker = 'RELIANCE.NS'
#     start_date = '2023-01-01'
#     end_date = '2023-12-31'
#     call_strike = 2500  # Set the desired call strike price
#     put_strike = 2500  # Set the desired put strike price
#     initial_capital = 100000  # Set your desired initial capital

#     stock_data = fetch_stock_data(ticker, start_date, end_date)

#     try:
#         backtest_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio = straddle_backtest(stock_data, call_strike, put_strike, initial_capital)
#     except ValueError as e:
#         return JsonResponse({'error': str(e)})

#     # Reset the index and convert the Date column to string format for the chart
#     backtest_data.reset_index(inplace=True)
#     backtest_data['Date'] = backtest_data['Date'].dt.strftime('%Y-%m-%d')

#     chart_data = backtest_data[['Date', 'Open', 'Straddle_PnL', 'Cumulative_PnL']].to_dict(orient='records')

#     data = {
#         'chart_data': chart_data,
#         'final_pnl': final_pnl,
#         'max_profit': max_profit,
#         'max_loss': max_loss,
#         'breakeven_upper': breakeven_upper,
#         'breakeven_lower': breakeven_lower,
#         'reward_risk_ratio': reward_risk_ratio,
#     }

#     return JsonResponse(data)








# from django.http import JsonResponse
# import numpy as np

# def call_payoff(sT, strike_price, premium):
#     return np.where(sT > strike_price, sT - strike_price, 0) - premium

# def put_payoff(sT, strike_price, premium):
#     return np.where(sT < strike_price, strike_price - sT, 0) - premium

# def straddle_payoff(request):
#     spot_price = 19479.65
#     strike_price_long_put = 19550
#     premium_long_put = 193.25 
#     strike_price_long_call = 19550
#     premium_long_call = 203.8
#     sT = np.arange(0, 2 * spot_price, 1)

#     payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
#     payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
#     payoff_straddle = payoff_long_call + payoff_long_put

#     max_profit = "Unlimited"
#     max_loss = min(payoff_straddle)

#     data = {
#         'sT': sT.tolist(),
#         'payoff_long_call': payoff_long_call.tolist(),
#         'payoff_long_put': payoff_long_put.tolist(),
#         'payoff_straddle': payoff_straddle.tolist(),
#         'max_profit': max_profit,
#         'max_loss': max_loss,
#     }
#     return JsonResponse(data)





# views.py
from django.shortcuts import render
import requests

def fetch_expiry_data_option_strategies(symbol):
    stock_url = "https://webapi.niftytrader.in/webapi/Option/option-simulator-expiry-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    payload = {
        "symbol": symbol,
    }

    stock_data = requests.post(stock_url, json=payload, headers=headers)
    stock_json = stock_data.json()
    
    Option_strategies_expiry_date = stock_json['resultData']["expiry_all"]
    
    return Option_strategies_expiry_date



# views.py
from django.shortcuts import render
import requests


def fetch_expiry_data(symbol):
    stock_url = "https://webapi.niftytrader.in/webapi/Option/option-simulator-expiry-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    payload = {
        "symbol": symbol,
    }

    stock_data = requests.post(stock_url, json=payload, headers=headers)
    stock_json = stock_data.json()
    
    Option_strategies_expiry_date = stock_json['resultData']["expiry_all"]
    
    # Convert date format from "2023-10-26T00:00:00" to "2023-10-26"
    formatted_expiry_dates = [datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d') for date in Option_strategies_expiry_date]
    
    return formatted_expiry_dates



# views.py
from django.http import JsonResponse

def get_expiry_data(request, symbol):
    Option_strategies_expiry_date = fetch_expiry_data(symbol)
    return JsonResponse(Option_strategies_expiry_date, safe=False)





from django.http import JsonResponse

def option_simulator_data(request):
    if request.method == 'POST':
        index = request.POST.get('index')
        expiry_date = request.POST.get('expiryDate')
        start_date = request.POST.get('startDate')

        # Perform further processing with the received data

        response_data = {
            'message': 'Data received successfully!',
            'index': index,
            'expiry_date': expiry_date,
            'start_date': start_date,
        }
        print(response_data)

        return JsonResponse(response_data)
    else:
        # Handle GET requests if needed
        # For this example, we only handle POST requests
        return JsonResponse({'error': 'Invalid request method.'})


from django.http import JsonResponse
import numpy as np
import json

def calculate_long_straddle(call_premium, put_premium, strike_price, stock_price_min, stock_price_max, stock_price_step):
    def long_straddle(call_premium, put_premium, strike_price, stock_price_range):
        call_profit = np.maximum(stock_price_range - strike_price, 0) - call_premium
        put_profit = np.maximum(strike_price - stock_price_range, 0) - put_premium
        total_profit = call_profit + put_profit
        return total_profit

    # Define the stock price range for analysis
    stock_price_range = np.arange(stock_price_min, stock_price_max + stock_price_step, stock_price_step)

    # Calculate the profit or loss for each stock price in the range
    profits = long_straddle(call_premium, put_premium, strike_price, stock_price_range)

    # Create a dictionary to store the data
    data = {
        'stock_price_range': stock_price_range.tolist(),
        'profits': profits.tolist()
    }

    return data

def straddle_data(request):
    # Define option prices and strike price
    call_premium = 146.8
    put_premium = 91.6
    strike_price = 19850

    # Define the stock price range for analysis
    stock_price_min = 19000
    stock_price_max = 21000
    stock_price_step = 50

    # Calculate the long straddle data
    data = calculate_long_straddle(call_premium, put_premium, strike_price, stock_price_min, stock_price_max, stock_price_step)

    # Return the data as a JSON response
    return JsonResponse(data)




import requests
from django.http import JsonResponse

def option_simulator_data(request):
    if request.method == 'GET':
        index = request.GET.get('index', "Nifty")
        print(index)
        expiry_date = request.GET.get('expiryDate')
        start_date = request.GET.get('startDate')
        createTime = request.GET.get('createTime', "09:20:00")
        print(index, expiry_date, start_date, createTime)

        spot_url = f'https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={index}'
        stock_url = "https://webapi.niftytrader.in/webapi/Option/option-simulator-expiry-data"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        payload = {
            "symbol": index,
            "expiryDate": expiry_date,
            "createdAt": start_date,
            "createdTime": createTime
        }

        stock_data = requests.post(stock_url, json=payload, headers=headers)
        stock_json = stock_data.json()

        spot_data = requests.get(spot_url, headers=headers)
        spot_json = spot_data.json()
        print(spot_json["resultData"])

        return JsonResponse({
            "stock_data": stock_json["resultData"],
            "spot_data": spot_json["resultData"]
        }, safe=False)


def long_call_option(request):
    return render(request,'long_call_option.html')
def long_put_option(request):
    return render(request,'long_put_option.html')
def covered_call(request):
    return render(request,'covered_call.html')
def short_call_option(request):
    return render(request,'short_call_option.html')
def synthetic_long_call(request):
    return render(request,'synthetic_long_call.html')
def covered_put(request):
    return render(request,'covered_put.html')
def long_combo(request):
    return render(request,'long_combo.html')
def long_straddle(request):
    return render(request,'long_straddle.html')
def short_straddle(request):
    return render(request,'short_straddle.html')
def pretective_call(request):
    return render(request,'pretective_call.html')
def aaaa(request):
    return render(request,'aaaa.html')









def option_strategy_optimizer(request):
    return render(request,'option_strategy_optimizer.html')



import requests
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_stock_symbol(request):
    stock_url = "https://webapi.niftytrader.in/webapi/symbol/psymbol-list"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    stock_data = requests.get(stock_url, headers=headers)
    stock_json = stock_data.json()

    nifty_stocks = []
    other_stocks = []

    for stock in stock_json["resultData"]:
        stock_info = {
            "symbol_name": stock["symbol_name"],
        }
        
        if stock_info["symbol_name"] in ["NIFTY", "BANKNIFTY", "FINNIFTY"]:
            nifty_stocks.append(stock_info)
        else:
            other_stocks.append(stock_info)

    # Create DataFrame
    df = pd.DataFrame(other_stocks)

    # Serialize DataFrame data
    response_data = df.to_dict(orient='records')

    return Response(response_data)



# stocks/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_option_strategy_optimizer_spot_data(request):
    selected_option = request.GET.get('selected_option',"NIFTY")
    print(selected_option)
    strategy_stop_url=f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={selected_option}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    stock_data = requests.get(strategy_stop_url, headers=headers)
    stock_json = stock_data.json()
    # Do something with the selected_option, process the data, and prepare a response
    response_data = {
        'spot_data': stock_json,
        # Add more data as needed
    }
    return Response(response_data)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_option_strategy_optimizer_option_data(request):
    selected_option = request.GET.get('selected_option',"NIFTY")
    selected_option_date = request.GET.get('selected_expiry')
    print(selected_option,selected_option_date)
    strategy_option_url=f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={selected_option}&expiryDate={selected_option_date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    stock_data = requests.get(strategy_option_url, headers=headers)
    stock_json = stock_data.json()
    # Do something with the selected_option, process the data, and prepare a response
    response_data = {
        'option_data': stock_json,
        # Add more data as needed
    }
    return Response(response_data)
@api_view(['GET'])
def option_strategies_expiry(request):
    # selected_option = request.GET.get('selected_option',"NIFTY")
    # selected_option_date = request.GET.get('selected_expiry')
    # print(selected_option,selected_option_date)
    selected_option = request.GET.get("selected_option")
    print(selected_option)
    strategy_expiry_url=f"https://webapi.niftytrader.in/webapi/Option/option-strategy-expiry-list?symbol={selected_option}"
    strategy_strike_url=f"https://webapi.niftytrader.in/webapi/Symbol/symbol-strike-price-list?symbol={selected_option}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    expiry_data = requests.get(strategy_expiry_url, headers=headers)
    strike_data = requests.get(strategy_strike_url, headers=headers)
    expiry_json = expiry_data.json()
    strike_json = strike_data.json()
    final_expiry_json = expiry_json["resultData"]
    final_strike_json = strike_json["resultData"]



    # Do something with the selected_option, process the data, and prepare a response
    response_date = {
        'option_date': final_expiry_json,
        'option_strike': final_strike_json,
        # Add more data as needed
    }
    return Response(response_date)



import numpy as np
from django.http import JsonResponse
from django.shortcuts import render

def get_payoff_data(request):
    spot_price = 19400
    strike_price_long_put = 19400
    premium_long_put = 50
    strike_price_long_call = 19400
    premium_long_call = 90
    sT = np.arange(18800, 2 * spot_price, 50)

    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 18800) - premium

    payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)

    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 18800) - premium

    payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)

    payoff_straddle = payoff_long_call + payoff_long_put

    data = {
        'sT': sT.tolist(),
        'payoff_long_call': payoff_long_call.tolist(),
        'payoff_long_put': payoff_long_put.tolist(),
        'payoff_straddle': payoff_straddle.tolist(),
    }

    return JsonResponse(data)



import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def filter_iv_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Parse the JSON data from the request body

            # Define the URLs for sending requests
            filter_data_url = "https://webapi.niftytrader.in/webapi/Option/option-strategy-filter-data"
            iv_data_url = "https://webapi.niftytrader.in/webapi/Option/option-strategy-iv-data"

            # Define headers for the requests
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            # Create the payload structure for the POST request to filter_data_url
            stock_payload = {
                "getFrom": data[0]['selectedOption'],
                "data": []
            }

            # Create the payload structure for the POST request to iv_data_url
            iv_payload = {
                "data": []
            }

            # Loop through the received data and create payload items
            for item in data:
                selectedOption = item.get('selectedOption')
                optionSide = item.get('optionSide')
                option_lot_size = item.get('option_lot_size')
                expiryDate = item.get('expiryDate')
                strikePrice = item.get('strikePrice')
                action = item.get('action')
                quantity = item.get('quantity')
                conditionOrder = item.get('conditionOrder')
                ltpValue = item.get('ltpValue')

                # Create an item for the stock payload
                stock_payload_item = {
                    "symbol": selectedOption,
                    "optionType": optionSide,
                    "expiry": expiryDate,
                    "strikePrice": strikePrice,
                    "position": action,
                    "quantity": quantity,
                    "conditionOrder": conditionOrder,
                    "iv": 0,
                    "tradedPrice": ltpValue
                }

                stock_payload["data"].append(stock_payload_item)
                print(stock_payload_item)

                # Create an item for the IV payload
                
                iv_payload_item = {
                    "optionType": optionSide,
                    "strikePrice": strikePrice,
                    "symbol": selectedOption,
                    "expiry": expiryDate,
                    "quantity": quantity,
                    "position": action,
                    "conditionOrder": conditionOrder,
                    "unitPrice": ltpValue,
                    "lotSize": option_lot_size
                }

                iv_payload["data"].append(iv_payload_item)

            # Send POST requests to retrieve data from two different URLs
            stock_data = requests.post(filter_data_url, json=stock_payload, headers=headers)
            iv_data = requests.post(iv_data_url, json=iv_payload, headers=headers)

            # Convert the responses to JSON
            stock_json = stock_data.json()
            iv_json = iv_data.json()

            # print("Stock Data:")
            # print(json.dumps(stock_json, indent=4))
            # print("===================")

            # print("IV Data:")
            # print(json.dumps(iv_json, indent=4))
            # print("===================")
            response_data = {
                "stock_data": stock_json,
                "iv_data": iv_json
            }

            return JsonResponse(response_data) 

             # Send a response back to the frontend
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


import requests
def bse_spot_data(request):
    url_date = "https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol=SENSEX&exchange=bse"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date = requests.get(url_date, headers=headers)
    data_date = response_date.json()
    

 

    return JsonResponse(data_date["resultData"])


def option_strategy_tester(request):
    return render(request,"option_strategy_tester.html")




def contact_us(request):
    return render(request, "contact-us.html")
def vertical(request):
    return render(request, "vertical.html")
def annotation(request):
    return render(request, "annotation.html")




from django.http import JsonResponse
from .models import ContactUs

@csrf_exempt
def customer_contact(request):
    if request.method == "GET":
        first_name = request.GET.get("firstname")
        last_name = request.GET.get("lastname")
        email = request.GET.get("email")
        phone_number = request.GET.get("phone")
        messages = request.GET.get("message")

        if not all([first_name, last_name, email, phone_number, messages]):
            error_message = "All fields are required."
            return JsonResponse({"error_message": error_message}, status=400)

        try:
            new_contact = ContactUs(
                Contact_first_name=first_name,
                Contact_last_name=last_name,
                Contact_phone_number=phone_number,
                Contact_email=email,
                Contact_messages=messages
            )
            new_contact.save()

            success_message = "Thank you for contacting us."
            return JsonResponse({"success_message": success_message})

        except Exception as e:
            error_message = f"An error occurred while contacting us: {str(e)}"
            return JsonResponse({"error_message": error_message}, status=500)

    # Handle GET request if needed
    return JsonResponse({"error_message": "Invalid request method."}, status=405)



def bse_option_chain(request):
    return render(request, "bse_option_chain.html")


def bse_option_chain_spotprice(request):
    url_date = "https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol=SENSEX&exchange=bse"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date = requests.get(url_date, headers=headers)
    data_date = response_date.json()
    all_data=data_date["resultData"]
    
    return JsonResponse(all_data)

def bse_option_expiry(request):
    url = "https://webapi.niftytrader.in/webapi/symbol/symbol-expiry-list?symbol=sensex&exchange=BSE"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date_expiry = requests.get(url, headers=headers)
    expiry_data = response_date_expiry.json()
    all_expiry_data=expiry_data
    
    return JsonResponse(all_expiry_data)
def bse_table_data(request):
    if request.method == "GET":
        dates_option = request.GET.get("dates_option")
        # symbols_value = request.GET.get("symbol_data")
        print(dates_option)
        # print(symbols_value)
        url=f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol=SENSEX&expiryDate={dates_option}&exchange=BSE"
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
        response_table_data = requests.get(url,headers=headers)
        table_option_data = response_table_data.json()
        all_table_option_data = table_option_data["resultData"]

    return JsonResponse(all_table_option_data)



from .models import Customer_feedback

def customer_feedback(request):
    return render(request, "customer_feedback.html")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def customer_feedback_data(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'You must be logged in to submit feedback.'}, status=401)

        usr = request.user
        data = json.loads(request.body.decode('utf-8'))

        first_star = data.get("first_star")
        second_star = data.get("second_star")
        rating1_10 = data.get("rating1_10")
        review = data.get("review")
        yes_no = data.get("yes_no")
        frnd_recommend = yes_no.lower() == "yes"
        
        # print(usr, first_star, second_star, rating1_10, review, yes_no)

        new_feedback = Customer_feedback(
            user=usr,
            ui_exp=first_star,
            helpful_exp=second_star,
            rating_scale=rating1_10,
            suggestion=review,
            frnd_recommend=frnd_recommend
        )

        new_feedback.save()

        return JsonResponse({'message': 'Thank you for your feedback!'})


from django.http import JsonResponse
from .models import Customer_feedback

def format_feedback_data(request):
    all_feedback = Customer_feedback.objects.all()
    
    feedback_list = []
    for feedback in all_feedback:
      
        feedback_data = {
            'User': feedback.user.email,  
            'UI Experience': feedback.ui_exp,
            'Helpful Experience': feedback.helpful_exp,
            'Rating (1-10)': feedback.rating_scale,
            'Review': feedback.suggestion,
            'Friend Recommend': feedback.frnd_recommend
        }
        feedback_list.append(feedback_data)

    return JsonResponse(feedback_list, safe=False)


def event_tracker(request):
    return render(request , "event_tracker.html")

@csrf_exempt
def event_tracker_dates(request):

        day = request.POST.get("all_date","day")
        print(day)
       
        url = f"https://www.moneysukh.com/api/markets/Eventcal/{day}"
        print(url)
        
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
       }
        response_date = requests.get(url, headers=headers)
        all_datas = response_date.json()
        all_event_data= all_datas
        print(all_event_data)
        return JsonResponse(all_event_data,safe=False)




from .models import Subscriber
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime 

@csrf_exempt
def subscribe_to_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("send_email")
        # print(email)
        if email:
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'message_already': 'You are already subscribed.'})
            else:
                new_subscriber = Subscriber(email=email)
                new_subscriber.subscribed_at = datetime.datetime.now()
             
   
                new_subscriber.save()
                
                subject = 'Subscription Confirmation'
                message = 'Thank you for subscribing to our newsletter!'
                from_email = 'tufailakram8190@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)
                
                return JsonResponse({'message': 'You have successfully subscribed to our newsletter!'})
        else:
            return JsonResponse({'error': 'Invalid email address.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

from django.http import JsonResponse
from .models import Subscriber

def get_subscribers(request):
    subscribers = Subscriber.objects.all().values('email', 'subscribed_at')
    subscribers_list = list(subscribers)
    return JsonResponse({'subscribers': subscribers_list})


def subscribers_management(request):
    return render(request, 'subscribers_management.html')


def event_tracker(request):
    return render(request , "event_tracker.html")


@csrf_exempt
def event_tracker_dates(request):
    
        days = request.POST.get("all_date", "day")
       
        url = f"https://www.moneysukh.com/api/markets/Eventcal/{days}"
        print(url)
        
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
       }
        response_date = requests.get(url, headers=headers)
        all_datas = response_date.json()
        all_event_data= all_datas
        print(all_event_data)
        return JsonResponse(all_event_data)


@csrf_exempt
def events_table_data(request):
    if request.method == "POST":
     from_date = request.POST.get("from_date")
     to_date = request.POST.get("to_date")
     originalValue = request.POST.get("originalValue")
   
     
 
     url = f"https://www.moneysukh.com/api/markets/CorporateAction/{originalValue}/{from_date}/{to_date}/-/-"
     print(url)
     headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
       }
     response_card_data = requests.get(url , headers)
     all_data = response_card_data.json()
     all_table_data = all_data

     return JsonResponse(all_table_data,safe=False)


def broker_management(request):
    return render(request , "broker_management.html")

import datetime
from django.http import JsonResponse
from .models import ZerodhaAPIConfig
from django.contrib.auth.decorators import login_required

@login_required
def save_zerodha_config(request):
    user = request.user  # Get the currently logged-in user

    if not user.is_authenticated:
        return JsonResponse({'message': 'Please login first'})

    if request.method == 'POST':
        app_name = request.POST.get('app_name')
        api_key = request.POST.get('api_key')
        secret_key = request.POST.get('secret_key')

        # Check if an API configuration with the same api_key and secret_key exists for this user
        existing_config = ZerodhaAPIConfig.objects.filter(user=user, api_key=api_key, secret_key=secret_key).first()

        if existing_config:
            return JsonResponse({'message': 'API is already in use'})

        api_data = ZerodhaAPIConfig(
            user=user,  # Associate the user with the configuration
            app_name=app_name,
            api_key=api_key,
            secret_key=secret_key,
            api_added_at=datetime.datetime.now()
        )
        api_data.save()

        return JsonResponse({'message': 'Data saved successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)






import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ZerodhaAPIConfig

@login_required
def get_zerodha_config(request):
    user = request.user  # Get the currently logged-in user

    # Get the current date
    current_date = datetime.date.today()

    # Retrieve data for the logged-in user sorted by 'api_added_at' field in descending order
    data = ZerodhaAPIConfig.objects.filter(user=user).order_by('-api_added_at').values()

    # Create a list comprehension to modify the data and add 'connected' status
    modified_data = [
        {
            **item,
            'connected': 'Connected' if item['access_token'] and item['api_added_at'].date() == current_date else 'Please connect'
        }
        for item in data
    ]

    return JsonResponse(modified_data, safe=False)




from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ZerodhaAPIConfig

@csrf_exempt
@login_required
def delete_zerodha_config(request, item_id):
    if request.method == 'POST':
        try:
            # Attempt to delete the item from the database only if it belongs to the logged-in user
            item = ZerodhaAPIConfig.objects.get(pk=item_id, user=request.user)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except ZerodhaAPIConfig.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)






from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ZerodhaAPIConfig
import datetime
from kiteconnect import KiteConnect

@csrf_exempt
@login_required
def edit_access_token(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')
        access_token = request.POST.get('access_token')

        try:
            api_config = ZerodhaAPIConfig.objects.get(pk=unique_id, user=request.user)

            # Retrieve api_secret and request_token from the database
            api_secret = api_config.secret_key
            request_token = access_token

            # Create a KiteConnect instance and generate a new access_token
            kite = KiteConnect(api_key=api_config.api_key)
            data = kite.generate_session(request_token, api_secret=api_secret)
            new_access_token = data["access_token"]

            # Update the API configuration with the new access_token and timestamp
            api_config.access_token = new_access_token
            api_config.api_added_at = datetime.datetime.now()
            api_config.save()

            return JsonResponse({'message': 'Access token updated successfully'})
        except ZerodhaAPIConfig.DoesNotExist:
            return JsonResponse({'message': 'API configuration not found'}, status=404)

    return JsonResponse({'message': 'Invalid request'}, status=400)














def zerodha_place(request):
    return render(request , "zerodha_place.html")


from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ipo_return_data(request):
    market = request.GET.get('market', 'nse')
    duration = request.GET.get('duration', '1M')

    stock_url = f"https://www.moneysukh.com/api/markets/returnipo/{market}/{duration}/-/-"
     

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        stock_data = requests.get(stock_url, headers=headers)

        if stock_data.status_code == 200:
            stock_json = stock_data.json()
            return JsonResponse(stock_json)
        else:
            return JsonResponse({"error": f"Failed to fetch data. Status Code: {stock_data.status_code}"}, status=500)

    except requests.RequestException as e:
        return JsonResponse({"error": f"An error occurred: {e}"}, status=500)




def ipo_dashboard(request):
    return render(request , "ipo_dashboard.html")





import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def best_performers(request):
    market = request.GET.get('market', 'NSE')
    segment = request.GET.get('segment', 'sme')
   


    api_url = f"https://www.moneysukh.com/api/markets/BestPerformers/{market}/{segment}/-"
    
    headers = {
        "User-Agent": "Your User Agent",  # Set your user agent here
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Unable to fetch data from the API"}, status=500)



import requests
from django.http import JsonResponse

def draft_prospectus(request):
    draft_type = request.GET.get('draft_type','sebi')


    api_url = f"https://www.moneysukh.com/api/markets/DraftProspectus/{draft_type}/-"

    headers = {
        "User-Agent": "Your User Agent",  # Set your user agent here
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Unable to fetch data from the API"}, status=500)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import os
from kiteconnect import KiteConnect
from .models import ZerodhaAPIConfig

@csrf_exempt
def kiteOrder(request):
    if request.method == 'POST':
        try:
            dataTrade = json.loads(request.body)
            print(dataTrade)
            logging.basicConfig(level=logging.DEBUG)

            # Retrieve API keys and access token from the database
            zerodha_config = ZerodhaAPIConfig.objects.first()  # Assuming you have only one configuration

            if not zerodha_config:
                return JsonResponse({'error': 'API configuration not found'}, status=500)

            api_key = zerodha_config.api_key
            api_secret = zerodha_config.secret_key
            access_token = zerodha_config.access_token
            print(f"API Key: {api_key}")
            print(f"Access Token: {access_token}")


            kite = KiteConnect(api_key=api_key)

            if access_token:
                kite.set_access_token(access_token)
            else:
                # If the access token is not available, generate a new one
                print(kite.login_url())
                request_token = input("Enter the request token after logging in: ")

                data = kite.generate_session(request_token, api_secret=api_secret)
                access_token = data["access_token"]
                kite.set_access_token(access_token)

                # Save the access token securely for future use
                zerodha_config.access_token = access_token
                zerodha_config.save()

            # Now you can use the saved access token to interact with the API

            try:
                profile = kite.profile()['user_name']
                print(profile)
                order_ids = []

                for order_data in dataTrade:
                    tradingsymbol = order_data['tradingsymbol']
                    isRadioChecked = order_data['isRadioChecked']
                    quantity = int(order_data['Quantity'])
                    price = float(order_data['price'])
                    print(tradingsymbol)
                    print(quantity)
                    print(price)
                    print(isRadioChecked)
                    transaction_type = kite.TRANSACTION_TYPE_SELL if order_data['sell_buy_indicator'] == 'SELL' else kite.TRANSACTION_TYPE_BUY
                    order_type = kite.ORDER_TYPE_LIMIT if order_data['isRadioChecked'] == 'limit' else kite.ORDER_TYPE_MARKET

                    # Place a market order
                    order_id = kite.place_order(
                        tradingsymbol=tradingsymbol,
                        exchange=kite.EXCHANGE_NFO,
                        transaction_type=transaction_type,
                        quantity=quantity,
                        price=price,
                        variety=kite.VARIETY_REGULAR,  
                        order_type=order_type,
                        product=kite.PRODUCT_NRML,  # Modify this if needed
                        validity=kite.VALIDITY_DAY
                    )
                    order_ids.append(order_id)
                    logging.info("Order placed for {}. ID is: {}".format(tradingsymbol, order_id))

                if all(order_ids):
                    response_data = {'message': 'Orders placed successfully', 'order_ids': order_ids}
                    return JsonResponse(response_data)
                else:
                    return JsonResponse({'error': 'Some orders failed to place'}, status=500)

            except Exception as e:
                logging.error("Order placement failed: {}".format(str(e)))
                order_failed="Order placement failed: {}".format(str(e))
                return JsonResponse({'error':order_failed})

            # Return a response if needed (only if there are no exceptions)
            response_data = {'message': 'Data received successfully'}
            return JsonResponse(response_data)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from kiteconnect import KiteConnect

@csrf_exempt
def quote_data_zerodha(request):
    zerodha_config = ZerodhaAPIConfig.objects.first() 
    api_key = zerodha_config.api_key
    api_secret = zerodha_config.secret_key
    access_token = zerodha_config.access_token
    
    kite = KiteConnect(api_key=api_key)
    
    if access_token:
        kite.set_access_token(access_token)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            trading_quote = data.get('trading_quote')
            zerodha_trading_symbol = data.get('zerodha_trading_symbol')
            
            ohlc_data = kite.ohlc(zerodha_trading_symbol["tradingsymbol"])
            ohlc = ohlc_data[zerodha_trading_symbol["tradingsymbol"]]
            
            # Calculate net change and change percentage
            nifty_ltp = ohlc['last_price']
            open_price = ohlc['ohlc']['open']
            close_price = ohlc['ohlc']['close']
            net_change = nifty_ltp - close_price
            percentage_change = (net_change / open_price) * 100
            
            profile = kite.profile()['user_name']
            user_id = kite.profile()['user_id']
            margins = kite.margins(segment='equity')

# Extract available cash balance
            available_cash = margins['available']['cash']

  
            # Create a list to store the quotes
            quotes_data = []
            
            for item in trading_quote:
                combinedString = item.get('combinedString')
                stock_symbol = f'NFO:{combinedString}'  # Create the instrument symbol
                
                # Fetch the quote for the stock symbol
                stock_quote = kite.quote(stock_symbol)
                
                # Append the stock_quote to the quotes_data list
                quotes_data.append(stock_quote)
            
            # Add combined_data to the quotes_data list as a separate element
            quotes_data.append({
                'combined_data': {
                    "available_cash":available_cash,
                    "symbol_spot":zerodha_trading_symbol["tradingsymbol"],
                    'nifty_ltp': nifty_ltp,
                    'percentage_change': percentage_change,
                    'profile': profile,
                    'user_id': user_id
                }
            })
            
            # Return the quotes_data list as a JSON response
            return JsonResponse(quotes_data, safe=False)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)


def mutual_fund(request):
    return render(request , "mutual_fund.html")

import requests
from django.http import JsonResponse
@csrf_exempt
def category_performance(request):
    if request.method == "POST":
        category = request.POST.get("category")
        times = request.POST.get("times_date")
        print(category,times)
        url = f"https://www.moneysukh.com/api/markets/MFActivityChart/{category}/{times}/GROWTH/-"
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
            all_data = response.json()
            return JsonResponse(all_data)
        except requests.exceptions.RequestException as e:
            # Handle any exceptions, e.g., connection error or invalid response
            error_message = {"error": str(e)}
            return JsonResponse(error_message, status=500)  # Return a 500 Internal Server Error

    # Handle other HTTP methods (e.g., GET, PUT, DELETE) if needed
    return JsonResponse({"error": "Unsupported HTTP method"}, status=405)  # Method Not Allowed




@csrf_exempt
def ipo_watch(request):
    if request.method == "POST":
        ipo_data = request.POST.get("all_data", "1")
        url = f"https://www.moneysukh.com/api/markets/Forthcoming/{ipo_data}/8/-/-/-/-"
        print(url)
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
         }
        response_data = requests.get(url , headers)
        datas = response_data.json()
        get_all_data = datas
    return JsonResponse(get_all_data)

@csrf_exempt
def new_listed_ipo(request):
    if request.method == "POST":
      new_listed = request.POST.get("all_listed_data", "BSE/main")
      url = f"https://www.moneysukh.com/api/markets/Newlisting/{new_listed}/8"
      print(url)
      headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
      }
      response_ipo_data = requests.get(url , headers)
      datas = response_ipo_data.json()
      get_listed_ipo_data = datas
      return JsonResponse(get_listed_ipo_data)


@csrf_exempt
def basic_allotment(request):
    url_data = "https://www.moneysukh.com/api/markets/BasisofAllotment/-"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date = requests.get(url_data, headers=headers)
    data_date = response_date.json()
    all_data=data_date
     
    return JsonResponse(all_data)


@csrf_exempt
def ipo_news(request):
    url = "https://www.moneysukh.com/api/markets/News/28/117/-/100"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_data = requests.get(url , headers=headers)
    news_data = response_data.json()
    all_news = news_data
    return JsonResponse(all_news)

def ipo_deepak(request):
    return render(request , "ipo_deepak.html")

import requests
from django.http import JsonResponse
from django.shortcuts import render

def news_details(request, sno, heading):
    # Construct the API URL with Sno as a parameter
    api_url = f"https://www.moneysukh.com/api/markets/News/-/-/{sno}/-"

    # Define headers for the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    try:
        # Make an API request to fetch the news details with headers
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        news_data = response.json()
        
        # If "data" key exists, remove "Ind_code" from each dictionary inside it
        if "data" in news_data:
            data = news_data["data"]
            for item in data:
                if "Ind_code" in item:
                    del item["Ind_code"]
            # Update the "data" key with the modified data
            news_data["data"] = data
        
        print(news_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

    # Render the HTML template with the modified news_data
    return render(request, 'news_details.html', {'news_data': news_data["data"]})





def option_index_statregy_executor(request):
    return render(request,'option_index_statregy_executor.html')