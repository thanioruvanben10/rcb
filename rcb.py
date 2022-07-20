import requests

url = input("Enter link: ")
password = input("Enter PWD: ")
Login = 'submit'
r = requests.post(url,data={
    'password': password
    })
print(r)
