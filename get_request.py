import requests
import json

response=requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName":"Rahul Shetty2"})
# print(response.text)
# print(type(response.text))
# dict_responce=json.loads(response.text) #Instead of loads method, using respons.json
# print(type(dict_responce))
# print(dict_responce[0]["book_name"])
json_responce=response.json()
print(type(json_responce))
print(response.status_code)