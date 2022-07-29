import cloudscraper
from bs4 import BeautifulSoup

hijk = input("enter your link")
scraper = cloudscraper.create_scraper(allow_brotli=False)
lmno=scraper.get(hijk).text
soup4=BeautifulSoup(lmno,'html.parser')
print (soup4)
for pqrs in soup4.find_all('a',href=True):
    mag_reg= r"magnet:\?xt=urn:btih:[a-zA-Z0-9]*"
    tyvw=pqrs.findall(mag_reg)
    print("/Qbmirror ",tuvw)
