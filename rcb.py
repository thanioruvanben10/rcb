import requests

url = input("Enter link: ")
password = input("Enter PWD: ")
Login = 'Login'
r = requests.post(url,allow_redirects=False,data={
    'password': password,
    })
print(r)
