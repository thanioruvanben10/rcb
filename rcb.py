/exec import base64
import re
import cloudscraper 
import concurrent.futures
from bs4  import BeautifulSoup
def expertlinks_scrape(url):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {
    'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = client.get(url, cookies={}, headers=h)
    url = re.findall('\&url=(.*?)"', res.text)[0]
    print(base64.b64decode(url).decode('utf-8'))

def atozcartoonist_bypasser(psa_url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(psa_url)
    soup = BeautifulSoup(r.text, "html.parser").find_all(class_="gdlink")
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for link in soup:
            try:
                exit_gate = link.a.get("href")
                executor.submit(expertlinks_scrape, exit_gate)
            except Exception as e:
                print(e)

url = "https://themoviesboss.shop/tvshows/thai-cave-rescue-2022-season-1-all-episodes-donwload-hindi-multi-audio-nf-web-dl/"
atozcartoonist_bypasser(url)
