import base64
import re
import json
import requests 
import cloudscraper 
import concurrent.futures
from bs4 import BeautifulSoup
def expertlinks_scrape(url):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {
    'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = requests.get(url, cookies={}, headers=h)
    value = re.findall(r'value=\"(.*?)\"',res.text)
    code = base64.b64decode(value[1]).decode('utf-8')
    coderes = json.loads(code)
    newurl = coderes['linkr']
    if "inbbotlist" in newurl:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            xy = executor.submit(expertlinks_scrape_, newurl)

def expertlinks_scrape_(url):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {
    'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = requests.get(url, cookies={}, headers=h)
    value = re.findall(r'value=\"(.*?)\"',res.text)
    result = base64.b64decode(value[0]).decode('utf-8')
    print(result)

def atozcartoonist_bypasser(psa_url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = requests.get(psa_url)
    soup = BeautifulSoup(r.text, "html.parser").find_all(class_="gdlink")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for link in soup:
            try:
                tuvw =link.get('href')
                x = executor.submit(expertlinks_scrape, tuvw)
            except Exception as e:
                print(e)

x = "https://themoviesboss.shop/tvshows/thai-cave-rescue-2022-season-1-all-episodes-donwload-hindi-multi-audio-nf-web-dl/"
atozcartoonist_bypasser(x)
