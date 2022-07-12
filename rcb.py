import requests
import cloudscraper
from bs4 import BeautifulSoup
import re
import time


a13=input("Enter Mx player url here: ")
x = int(input())
y = int(input())
for x in range(x,y+1):
   a11=a13+str(x)
   x+=1
   print(a11)
