import time
import cloudscraper
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# eg: https://gplinks.co/XXXX
url = "https://gplinks.co/yXS5"

# =======================================
ANCHOR_URL = "https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LezO6kUAAAAAGAYpazfxwlPpBVljyiMIhj0kLA7&co=aHR0cHM6Ly93d3cuY2FzYWRhYmViaWRhLmNvbS5icjo0NDM.&hl=pt-BR&v=4rwLQsl5N_ccppoTAwwwMrEN&size=invisible&cb=vvcfcwwb7aum"

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
    answer = re.findall(r'"rresp","(.*?)"', res.text)[0]
    return answer

def gplinks_bypass(url: str):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    res = client.head(url)
    header_loc = res.headers['location']
    param = header_loc.split('postid=')[-1]
    req_url = f'{p.scheme}://{p.netloc}/{param}'

    p = urlparse(header_loc)
    ref_url = f'{p.scheme}://{p.netloc}/'

    h = { 'referer': ref_url }
    res = client.get(req_url, headers=h, allow_redirects=False)

    bs4 = BeautifulSoup(res.content, 'html.parser')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }
    ans = RecaptchaV3(ANCHOR_URL)
    data['_Token[unlocked]']=ans
    h = {
        'referer': ref_url,
        'x-requested-with': 'XMLHttpRequest',
    }
    time.sleep(10)
    res = client.post(final_url, headers=h, data=data)
    try:
        return res.json()['url'].replace('\/','/')
    except: return 'Something went wrong :('

# =======================================

print(gplinks_bypass(url))
