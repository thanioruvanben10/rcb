import requests
url = input ()
values = {'user': 'admin',
          'password': 'joinstreamhub'}

r = requests.post(url, data=values)
print (r.content)
