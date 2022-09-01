import re
import time
import requests
import cloudscraper
from urllib.parse import urlparse

url = input()
print("You Have Entered:")
print(url)
print("Checking Link!")

#Extra fit for site
if "redirect" in url:
    site = requests.get(url)
    url = site.url
else:
    url = url

# ==============================================
print("Bypassing Link...")
def droplink_bypass(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    resp = client.post(api, json={"type": "droplink", "url": url})
    res = resp.json()
    return res['url']

# ==============================================

print(droplink_bypass(url))
