import requests
import pprint

# リクエストパラメータを辞書型で設定する
param = {"token": "token1"}

# get()メソッドでGETリクエストを送信する
response = requests.get("http://localhost:8080/problem", params=param)


get_data = vars(response) 
# リクエスト時のURLを出力する
#pprint.pprint(vars(response))
print(get_data)