import base64
import re,json
import cloudscraper 
import concurrent.futures
from bs4 import BeautifulSoup
def expertlinks_scrape(url):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {
    'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = client.get(url, cookies={}, headers=h)
    return json.loads(res.text)
    
def atozcartoonist_bypasser(psa_url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(psa_url)
    soup = BeautifulSoup(r.text, "html.parser").find_all(class_="gdlink")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for link in soup:
            try:
                tuvw =link.get('href')
                x = executor.submit(expertlinks_scrape, tuvw)
                return x
            except Exception as e:
                print(e)
x = "https://themoviesboss.shop/tvshows/thai-cave-rescue-2022-season-1-all-episodes-donwload-hindi-multi-audio-nf-web-dl/"
y = atozcartoonist_bypasser(x)
print(y)
