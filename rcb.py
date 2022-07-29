import cloudscraper
from bs4 import BeautifulSoup

hijk = input("enter your link")
scraper = cloudscraper.create_scraper(allow_brotli=False)
lmno=scraper.get(hijk).text
soup4=BeautifulSoup(lmno,'html.parser')
print (soup4)
for pqrs in soup4.find_all(href=True):
    tuvw =pqrs.get('href')
    print("/Qbmirror +",tuvw)
