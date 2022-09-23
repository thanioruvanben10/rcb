import re
import json
import cloudscraper 
import concurrent.futures
from bs4 import BeautifulSoup
url = "https://inbbotlist.com/?O6Aux00kmbwApbsCadfEeFlgiHnikVE5UTXNOV29kcXpkdmR2dzdHMGZvYTR6RWppZERlb3JJQWlyUGdSZGNoS0lKYU1hdFlFU25uK0dPUFJUOEJ6NQ=="
def tmb_bypass(url):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        x = executor.submit(inbbotlist, url)
def inbbotlist(aurl):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    res = client.get(aurl, cookies={}, headers=h)
    value = re.findall(r'value=\"(.*?)\"',res.text)
    return res
