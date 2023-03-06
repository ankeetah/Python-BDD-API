import requests


cookie = {'visit-year': '2023'}

res = requests.get('https://httpbin.org/cookies', cookies=cookie)
print(res.text)
print(res.history)
print(res.status_code)

