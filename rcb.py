import cloudscraper
from bs4 import BeautifulSoup
import re

hijk = input("enter your link")
scraper = cloudscraper.create_scraper(allow_brotli=False)
lmno=scraper.get(hijk).text
soup4=BeautifulSoup(lmno,'html.parser')
mag=re.compile(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]*")
for pqrs in soup4.find_all('a',href=True):
    j=str(pqrs)
    x=mag.findall(j)
    print(x)
