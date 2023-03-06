import json
import json
import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName': 'Rahul Shetty'},)
# print(response.text)
# print(len(response.text))
# type(response.text)
#
# dicy = json.loads(response.text)
# print(len(dicy))
# print(dicy[70]['book_name'])

finny = response.json()
print(type(finny))
print(finny)
print(finny[89]['book_name'])
print(response.status_code)
assert response.status_code == 200
print(response.headers['Content-type'])
for book in finny:
    if book['isbn'] == 'bcz888df':
        print(book)
