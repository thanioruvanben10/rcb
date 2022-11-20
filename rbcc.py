import requests,json

Request_URL = "https://prod.media.jio.com/apis/common/v3/playbackrights/get/"
Meta_URL = "https://prod.media.jio.com/apis/common/v3/metamore/get/"
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
        print (creds)
    else:
        print ("Wrong/Unregistered Mobile Number (ensure there's no +91 or 0 in the beginning)")
        sys.exit()

M_No = input ('Enter Mobile Number: ')
login (M_No)
