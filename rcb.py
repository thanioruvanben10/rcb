import cloudscraper, requests
from bs4 import BeautifulSoup

url = input("Enter Url : ")

def rocklinks_bypass(url):
        RLDOMAIN ="https://share.techymedies.com"
        client = cloudscraper.create_scraper(allow_brotli=False)
        code = url.split("/")[-1]
        final_url = f"{RLDOMAIN}/{code}" 
        resp = client.get(final_url)
        soup = BeautifulSoup(resp.content, "html.parser")
        try: inputs = soup.find(id="go-link").find_all(name="input")
        except: return "Incorrect Link"
        data = { input.get('name'): input.get('value') for input in inputs }
        h = { "x-requested-with": "XMLHttpRequest" }
        time.sleep(5)
        r = client.post(f"{RLDOMAIN}/links/go", data=data, headers=h)
        return r.json()['url']

print(rocklinks_bypass(url))
