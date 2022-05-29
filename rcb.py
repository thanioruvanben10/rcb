import re
import requests

'''

Search for "anchor" in the network tab while the site is loading to obtain the url

anchor url should look like:
https://www.google.com/recaptcha/api2/anchor?ar=1&k=...

'''
ANCHOR_URL = input("1 = ")
ANCHOR_URL = ANCHOR_URL.replace('amp;','')
print (ANCHOR_URL)

