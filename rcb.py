import re
import requests

'''

Search for "anchor" in the network tab while the site is loading to obtain the url

anchor url should look like:
https://www.google.com/recaptcha/api2/anchor?ar=1&k=...

'''
new = input("1 = ")
ANCHOR_URL = new.replace('amp;','')
print ("🥰 : ",ANCHOR_URL)
def RecaptchaV3(ANCHOR_URL):
    url_base = 'https://www.google.com/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    
    client = requests.Session()
    
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    print ("\n matches = ",matches)
    url_base += matches[0]+'/'
    params = matches[1]
    res = client.get(url_base+'anchor', params=params)
    print ("\n res 1 = ",res.text)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    print ("\n token = ",token)
    params = dict(pair.split('=') for pair in params.split('&'))
    print ("\n params = ",params)
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    print ("\n post_data = ",post_data)
    res = client.post(url_base+'reload', params=f'k={params["k"]}', data=post_data)
    print ("\n res2 = ",res.text)
    
# -------------------------------------------

ans = RecaptchaV3(ANCHOR_URL)

print(ans)

