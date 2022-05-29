import re
import requests

'''

Search for "anchor" in the network tab while the site is loading to obtain the url

anchor url should look like:
https://www.google.com/recaptcha/api2/anchor?ar=1&k=...

'''
ANCHOR_URL = input("1 = ")

def RecaptchaV3(ANCHOR_URL):
    url_base = input("\n2= ")
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = requests.Session()
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0]+'/'
    params = matches[1]
    res = client.get(url_base+'anchor', params=params)
    print(res)
    
# -------------------------------------------

ans = RecaptchaV3(ANCHOR_URL)

print(ans)

# If you are not sure how/where to use this token then this script is not for you :)
