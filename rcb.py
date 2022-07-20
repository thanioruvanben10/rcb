import requests

url = input("Enter link: ")
password = input("Enter PWD: ")
Login = 'Login'
r = requests.post(url, allow_redirects=True, data={
    'password': password,
    'Login': Login
    })
print(r)
