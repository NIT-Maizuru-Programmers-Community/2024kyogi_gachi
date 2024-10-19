import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する
param = {"token": "token1"}

with open('result.json', 'r') as file:
    json_data = json.load(file)

POST_URL = "http://localhost:8080/answer"


response = requests.post(POST_URL,params=param,json=json_data,verify=False)
# レスポンスボディを出力する
pprint.pprint(response)
print(response.text)
print("送信完了")
