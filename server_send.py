import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する


#param = {"token": "token1"}
param = {"token": "maizuru0478a4402bcf6769308a8d8fcafcf261bbb7ad87b911d2d0ee69a295d"}

# JSONファイルを開いて中身を読み込む
with open('result.json', 'r') as file:
    json_data = json.load(file)

POST_URL = "http://localhost:8080/answer"

# POSTリクエストを、リクエストボディ付きで送信する
response = requests.post(POST_URL,params=param,json=json_data,verify=False)
# レスポンスボディを出力する
pprint.pprint(response)
print(response.text)
print("送信完了")