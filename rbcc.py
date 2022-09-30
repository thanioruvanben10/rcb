import requests, json
import os, sys

OTPSendURL = "https://prod.media.jio.com/apis/common/v3/login/sendotp"
OTPVerifyURL = "https://prod.media.jio.com/apis/common/v3/login/verifyotp"

def login(mobile_number):
    send = requests.post(url = OTPSendURL, headers = {
    'authority': 'prod.media.jio.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'origin': 'https://www.jiocinema.com',
    'referer': 'https://www.jiocinema.com/',
    },
     data = '{"number":"+91' + mobile_number +'"}'
    )
    if 'success' in str(send.content):
        OTP = input ('Enter OTP Received: ')
        verify = requests.post(url = OTPVerifyURL, headers = {
        'authority': 'prod.media.jio.com',
        'pragma': 'no-cache',
        'origin': 'https://www.jiocinema.com',
        'referer': 'https://www.jiocinema.com/',
        'deviceid': '1727391720'
        },
        data = '{"number":"+91' + mobile_number + '","otp":"' + OTP + '"}')
        creds = json.loads(verify.content)
        load_creds(creds)
    else:
        print ("Wrong/Unregistered Mobile Number (ensure there's no +91 or 0 in the beginning)")
        sys.exit()

def load_creds(creds):
    try:
        ssotoken = creds['ssoToken']
        uniqueID = creds['uniqueId']
    except KeyError:
        print ("Wrong OTP, Try again!")
        sys.exit()
    Creds = {
        "ssotoken" : ssotoken,
        "uniqueID" : uniqueID
    }
    print(json.dumps(Creds))

M_No = input ('Enter Mobile Number: ')
login (M_No)
