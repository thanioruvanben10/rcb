import requests
url = input ()
values = {'password': 'joinstreamhub'}

r = requests.post(url, data=values)
print (r.content)
