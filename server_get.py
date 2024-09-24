import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する



def server_get():

    def make_board(board_str,height):#string型を分解して一個ずつのリストに
        board_list=[]#ここに追加

        for i in range(height):
            row_list=list(map(int,board_str[i]))#string型を一つずつ分解してintに

            board_list.append(row_list)
        
        return board_list




    param = {"token": "token1"}

    # get()メソッドでGETリクエストを送信する
    response = requests.get("http://localhost:8080/problem", params=param)

    get_data=vars(response)
    board = get_data['_content']
    board_data = json.loads(board)

    general_data=board_data['general']

    start_board_str=board_data['board']['start']#盤面のstring型のリスト
    goal_board_str=board_data['board']['goal']
    
    width=board_data['board']['width']
    height=board_data['board']['height']

    start_board=make_board(start_board_str,height)
    goal_board=make_board(goal_board_str,height)


    print(board_data)
    print(general_data)


# リクエスト時のURLを出力する
#pprint.pprint(vars(response))

server_get()