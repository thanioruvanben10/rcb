import re
import requests

'''

Search for "anchor" in the network tab while the site is loading to obtain the url

anchor url should look like:
https://www.google.com/recaptcha/api2/anchor?ar=1&k=...

'''
ANCHOR_URL = input("1 = ")
ANCHOR_URL = ANCHOR_URL.replace('amp;','')

def RecaptchaV3(ANCHOR_URL):
    url_base = 'https://www.recaptcha.net/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    
    client = requests.Session()
    
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0]+'/'
    params = matches[1]
    
    res = client.get(url_base+'anchor', params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    
    params = dict(pair.split('=') for pair in params.split('&'))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    
    res = client.post(url_base+'reload', params=f'k={params["k"]}', data=post_data)
    
    print ("\n👉",res)
    
# -------------------------------------------

ans = RecaptchaV3(ANCHOR_URL)

print(ans)

