import time
import requests 
import re
import cloudscraper 
from bs4  import BeautifulSoup


def try2link_bypass(url):
	client = cloudscraper.create_scraper(allow_brotli=False)
	
	url = url[:-1] if url[-1] == '/' else url
	
	params = (('d', int(time.time()) + (60 * 4)),)
	r = client.get(url, params=params, headers= {'Referer': 'https://newforex.online/'})
	
	soup = BeautifulSoup(r.text, 'html.parser')
	inputs = soup.find(id="go-link").find_all(name="input")
	data = { input.get('name'): input.get('value') for input in inputs }	
	time.sleep(7)
	
	headers = {'Host': 'try2link.com', 'X-Requested-With': 'XMLHttpRequest', 'Origin': 'https://try2link.com', 'Referer': url}
	
	bypassed_url = client.post('https://try2link.com/links/go', headers=headers,data=data)
	return bypassed_url.json()["url"]
		

def psa_bypasser(url):
	client = cloudscraper.create_scraper(allow_brotli=False)	
	h = {
	'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
	}
	res = client.get(url, cookies={}, headers=h)
	print("RESULT : ",res.text)
			
 
site = requests.get("https://gplinks.co/HwsEUBZ0")
urlx = site.url
print ("URLX : ",urlx)
psa_bypasser(urlx)
