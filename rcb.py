import requests
import cloudscraper
from bs4 import BeautifulSoup
import re
import time
'''

Search for "anchor" in the network tab while the site is loading to obtain the url

anchor url should look like:
https://www.google.com/recaptcha/api2/anchor?ar=1&k=...

'''
scraper = cloudscraper.create_scraper(allow_brotli=False)
a14=input("Enter Mx player url here: ")
a1=scraper.get(a14).text
soup4=BeautifulSoup(a1,'html.parser')
print(soup4)
a11=soup4.find_all("iframe")
print(a11)
