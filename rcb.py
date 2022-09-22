# ThaniOruvan - Python script for bypassing atozcartoonist.com poorly developed site and get direct links
# Copyright (c) 2022 dakshy/atozcartoonist-bypasser
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    print (res.text)
    url = re.findall('\&url=(.*?)"', res.text)[0]
    print(base64.b64decode(url).decode('utf-8'))

def atozcartoonist_bypasser(psa_url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    r = client.get(psa_url)
    soup = BeautifulSoup(r.text, "html.parser").find_all(class_="gdlink")
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for link in soup:
            try:
                tuvw =link.get('href')
                print (tuvw)
                executor.submit(expertlinks_scrape, tuvw)
            except Exception as e:
                print(e)

x = "https://themoviesboss.shop/tvshows/thai-cave-rescue-2022-season-1-all-episodes-donwload-hindi-multi-audio-nf-web-dl/"
y = atozcartoonist_bypasser(x)
