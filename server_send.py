import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する


param = {"token": "token1"}

data ={
    "n":4,
    "ops":[
        {
            "p":1,
            "x":1,
            "y":1,
            "s":1
        },
        {
            "p":0,
            "x":0,
            "y":0,
            "s":0
        },
        {
            "p":2,
            "x":2,
            "y":2,
            "s":2
        },
        {
            "p":3,
            "x":3,
            "y":3,
            "s":3 
        }

    ]
    }


POST_URL = "http://localhost:8080/answer"

# POSTリクエストを、リクエストボディ付きで送信する
response = requests.post(POST_URL,params=param,json=data,verify=False)

# レスポンスボディを出力する
pprint.pprint(response)
print(response.text)