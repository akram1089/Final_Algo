from urllib.parse import parse_qs, urlparse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyotp import TOTP
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint

USER_ID = "7DB863"
API_KEY = 'a6c092df-00a3-4e61-86ad-8cf0b0a72de3'
SECRET_KEY = 'ghjv4yytiu'
TOTP_KEY = 'SAIVSYRK2BQZ6QUY5QJ7ZVQA5DUGN7L3'
MOBILE_NO = '9885443405'
PIN = '747474'
RURL = 'https://optionperks.com/my_portfolio'

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
    return json_response['access_token']

def run_selenium():
    AUTH_URL = f'https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={API_KEY}&redirect_uri={RURL}'

    chrome_options = Options()
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--log-level=1')
    chrome_options.add_argument('--headless')  # Uncomment this line if you want to run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_argument("--enable-logging")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(AUTH_URL)
    print("got the web driver ")

    try:
        # Wait for mobile number input field to be visible
        mobile_num_input_xpath = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div/div/div/div/div/div/input"))
        )
        mobile_num_input_xpath.send_keys(MOBILE_NO)

        # Click on the submit button after entering mobile number
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div/button"))
        )
        submit_button.click()

        time.sleep(1)  # Add a delay of 1 second

        # Wait for OTP input field to be visible
        otp_input_xpath = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]/div/div/div/input"))
        )
        totp = TOTP(TOTP_KEY)
        token = totp.now()

        time.sleep(1)  # Add a delay of 1 second

        # Enter OTP
        print(token)
        otp_input_xpath.send_keys(token)

        # Click on the verify OTP button
        verify_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/form/div[2]/button"))
        )
        verify_button.click()

        time.sleep(2)  # Add a delay of 1 second

        # Wait for 2FA input field to be visible
        twofa_input_xpath = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div/div/div/div/div/input"))
        )
        print(PIN)
        twofa_input_xpath.send_keys(PIN)

        # Click on the submit 2FA button
        submit_2fa_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]/form/button"))
        )
        submit_2fa_button.click()

        # Wait for redirection to the specified URL
        WebDriverWait(browser, 15).until(EC.url_contains(RURL))
        print(browser.current_url)
        code = parse_qs(urlparse(browser.current_url).query)['code'][0]
        print(code)

        return code

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Save screenshot
        browser.save_screenshot("screenshot_final.png")
        browser.quit()

# Run Selenium to get the code and then obtain the access token
code = run_selenium()
if code:
    access_token = get_access_token(code)
    print(access_token)
    
    # Configure OAuth2 access token for authorization: OAUTH2
    configuration = upstox_client.Configuration()
    configuration.access_token = access_token

    # Create an instance of the API class
    api_instance = upstox_client.UserApi(upstox_client.ApiClient(configuration))
    api_version = 'api_version_example' # str | API Version Header

    try:
        # Get profile
        api_response = api_instance.get_profile(api_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_profile: %s\n" % e)
else:
    print("Error retrieving code.")
