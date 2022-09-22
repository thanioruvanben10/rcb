import base64
import re
import cloudscraper 
import concurrent.futures
from bs4  import BeautifulSoup
        

def expertlinks_scrape(url):
    client = cloudscraper.create_scraper(allow_brotli=False)    
    h = {
    'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = client.get(url, cookies={}, headers=h)
    print(res.text)
    url = re.findall('\&url=(.*?)"', res.text)[0]
    return base64.b64decode(url).decode('utf-8')
    

def atozcartoonist_bypasser(psa_url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(psa_url)
    soup = BeautifulSoup(r.text, "html.parser").find_all("a")
    links = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for link in soup:
            try:
                exit_gate = link.get("href")
                if "/redirect/" in exit_gate:
                    link = executor.submit(expertlinks_scrape, "https://www.atozcartoonist.com" + exit_gate)
                    links.append(link.result())
            except Exception as e:
                return (e)
    del links[-1]
    return "\n".join(links)

 
print(atozcartoonist_bypasser("https://www.atozcartoonist.com/2022/09/doraemon-nobitas-treasure-island-full-movie-in-hindi-tamil-telugu-download.html"))
