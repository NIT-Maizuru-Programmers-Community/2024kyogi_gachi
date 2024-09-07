import requests
import pprint

# リクエストパラメータを辞書型で設定する
param = {"token": "token1"}

# get()メソッドでGETリクエストを送信する
response = requests.get("http://localhost:8000/problem", params=param)

# リクエスト時のURLを出力する
pprint.pprint(vars(response))