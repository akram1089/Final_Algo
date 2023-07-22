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
from django.http import JsonResponse
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

    df = pd.DataFrame(all_list).head(50)
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


def base(request):

    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    all_list = []
    for d in data['data']:
        if d['symbol'] != 'NIFTY 50':
            all_list.append({
                'symbol': d['symbol'],
                'pChange': d['pChange']
            })

    # Randomly select 10 symbols from the top 50
    random_symbols = random.sample(all_list, 10)

    df = pd.DataFrame(random_symbols)
    symbols = df.to_dict(orient='records')

    return render(request, 'base.html', {'symbols': symbols})


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
    url = "https://trendlyne.com/futures-options/api-filter/futures/27-jul-2023-next/oi_gainers/"

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


def admin_login(request):
    return render(request, "admin_login.html")


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
    url = "https://trendlyne.com/futures-options/api-filter/futures/27-jul-2023-next/oi_gainers/"

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
    url_date = "https://webapi.niftytrader.in/webapi/Resource/nifty50-date-List"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    response_date = requests.get(url_date, headers=headers)
    data_date = response_date.json()
    all_dates = []
    for date in data_date["resultData"]["date"]:
        all_dates.append(date)

    return all_dates


def contributors_data(request):
    try:
        selected_date = request.GET.get('date')
        selected_filter = request.GET.get('filter', 'nifty50')
        if not selected_date:
            # Set initial selected date
            # Replace this with your code to fetch all available dates
            all_dates = get_all_dates()
            if all_dates:
                selected_date = all_dates[1]

        print("Selected Date:", selected_date)
        print("Selected Filter:", selected_filter)

        url = f'https://webapi.niftytrader.in/webapi/Resource/{selected_filter}-float-data?Date={selected_date}'
        url_date = f"https://webapi.niftytrader.in/webapi/Resource/{selected_filter}-date-List"
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

            all_dates = data_date.get("resultData", {}).get("date", [])
            if not all_dates:
                error_dict = {
                    "error": "No dates available"
                }
                return JsonResponse(error_dict, status=500)

            print(all_dates[1])

            date_max = data_date.get("resultData", {}).get("max_date")

            stocks_data = data.get("resultData", {}).get("startdate", [])
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
        oi_percent_change = (oi_change / future["prev_oi"]) * 100
        change_price = future["last_price"] - future["prev_close"]
        change_percent = (change_price / future["prev_close"]) * 100
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
    return render(request,"stock_future.html")




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




from django.http import JsonResponse
import requests
import datetime

def fetch_option_data_with_spot_price(request):
    selected_symbol = request.GET.get('symbol')
    selectedDate = request.GET.get('selectedDate')
    print(selected_symbol)
    print(selectedDate)

 
    url = f"https://webapi.niftytrader.in/webapi/option/fatch-option-chain?symbol={selected_symbol}&expiryDate={selectedDate}"
    url_symbol_list = "https://webapi.niftytrader.in/webapi/symbol/psymbol-list"
    url_india_vix = "https://webapi.niftytrader.in/webapi/Other/other-symbol-spot-data?symbol=INDIA+VIX" 
    url_spot_data = f"https://webapi.niftytrader.in/webapi/symbol/today-spot-data?symbol={'NIFTY+50' if selected_symbol == 'nifty' else selected_symbol}"

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
        date_str = options_date.split("T")[0]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = datetime.datetime.strftime(
            date_obj, "%Y-%m-%d")
        All_dates.append(formatted_date)

    total_puts_change_oi= 0
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
    return render(request,'stock_option_chain.html')

def option_dashboard(request):
    return render(request,'option_dashboard.html')