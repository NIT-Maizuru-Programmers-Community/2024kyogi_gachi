import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する


def server_send(operate_board,algorithm_turn):
    param = {"token": "token1"}

    output_operate_board=[]#辞書型を追加
    for turn in range(algorithm_turn):
        opperate_data={"p":operate_board[turn][0],"x":operate_board[turn][1],"y":operate_board[turn][2],"s":operate_board[turn][3]}
        output_operate_board.append(opperate_data)

    data ={
        "n":algorithm_turn,
        "ops":output_operate_board
    }

    POST_URL = "http://localhost:8080/answer"

    # POSTリクエストを、リクエストボディ付きで送信する
    response = requests.post(POST_URL,params=param,json=data,verify=False)

    # レスポンスボディを出力する
    pprint.pprint(response)
    print(response.text)
    print("送信完了")