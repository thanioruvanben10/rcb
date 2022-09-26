import base64
import re
import json
import cloudscraper
import requests
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
    #if "inbbotlist" in newurl:
        #with concurrent.futures.ThreadPoolExecutor() as executor:
            #xy = executor.submit(expertlinks_scrape_, newurl)
    return code

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
    with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                tuvw =link.get('href')
                x = executor.submit(expertlinks_scrape, tuvw)
            except Exception as e:
                print(e)

x = "https://gplinks.co/HwsEUBZ0"
atozcartoonist_bypasser(x)
