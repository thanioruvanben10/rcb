import requests, json
import os, sys
import base64

def load_config():
    global accesstoken, devid
    with open ("creds.txt", "r") as f:
        try:
            Creds = json.load(f)
            accesstoken = Creds['accesstoken']
            devid = Creds['deviceid']
        except json.JSONDecodeError:
            accesstoken = ''
            devid = ''    
    print("Access Token: ",accesstoken)
    print("devid: ",devid)

Request_URL = "https://apis-jiovoot.voot.com/playbackjv/v4/"
Meta_URL = "https://prod.media.jio.com/apis/common/v3/metamore/get/"
OTPSendURL = "https://auth-jiocinema.voot.com/userservice/apis/v4/loginotp/send"
OTPVerifyURL = "https://auth-jiocinema.voot.com/userservice/apis/v4/loginotp/verify"
IdURL = "https://cs-jv.voot.com/clickstream/v1/get-id"
GuestURL = "https://auth-jiocinema.voot.com/tokenservice/apis/v4/guest"

def get_accesstoken():
    id = requests.get(url=IdURL).json()['id']

    token = requests.post(url=GuestURL, json={
            'adId': id,
            "appName": "RJIL_JioCinema",
            "appVersion": "23.10.13.0-841c2bc7",
            "deviceId": id,
            "deviceType": "phone",
            "freshLaunch": True,
            "os": "ios"
        }, headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }).json()

    return token["authToken"], id

def login(mobile_number):
    accesstoken, id = get_accesstoken()
    
    send = requests.post(url=OTPSendURL, json={
            "number": base64.b64encode(f"+91{mobile_number}".encode()).decode(),
            "appVersion": "23.10.13.0-841c2bc7"
        }, headers = {
            'accesstoken': accesstoken,
            'appname': 'RJIL_JioCinema',
            'cache-control': 'no-cache',
            'devicetype': 'phone',
            'os': 'ios',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
})
    print(send.content)
    if 'karix' in str(send.content):
        OTP = input ('Enter OTP Received: ')
        verify = requests.post(url = OTPVerifyURL, headers = {
            'accesstoken': accesstoken,
            'appname': 'RJIL_JioCinema',
            'cache-control': 'no-cache',
            'devicetype': 'phone',
            'os': 'ios',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }, json={
            "appVersion": "23.10.13.0-841c2bc7",
            "deviceInfo": {
                "consumptionDeviceName": "iPhone",
                "info": {
                    "androidId": id,
                    "platform": {
                        "name": "iPhone OS"
                    },
                    "type": "iOS"
                }
            },
            "number": base64.b64encode(f"+91{mobile_number}".encode()).decode(),
            "otp": OTP
        })
        creds = json.loads(verify.content)
        load_creds(creds)
    else:
        print ("Wrong/Unregistered Mobile Number (ensure there's no +91 or 0 in the beginning)")
        sys.exit()

def load_creds(creds):
    try:
        accesstoken = creds['authToken']
        devid = creds['deviceId']
    except KeyError:
        print ("Wrong OTP, Try again!")
        sys.exit()
    Creds = {
        "accesstoken" : accesstoken,
        "deviceid" : devid
    }
    with open("creds.txt", "w") as f:
        f.write(json.dumps(Creds))
            
load_config()
if accesstoken == "" and devid == "":
    M_No = input ('Enter Mobile Number: ')
    login (M_No)
    load_config()
