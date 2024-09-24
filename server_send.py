import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する


def server_send():
    param = {"token": "token1"}

    with open('result.json', 'r') as json_file:
        data = json.load(json_file)

    POST_URL = "http://localhost:8080/answer"

    # POSTリクエストを、リクエストボディ付きで送信する
    response = requests.post(POST_URL,params=param,json=data,verify=False)

    # レスポンスボディを出力する
    pprint.pprint(response)
    print(response.text)