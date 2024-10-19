import requests
import pprint
import json

# リクエストパラメータを辞書型で設定する



def server_get():

    def make_list(board_str,height):#string型を分解して一個ずつのリストに
        board_list=[]#ここに追加
        for i in range(height):
            row_list=list(map(int,board_str[i]))#string型を一つずつ分解してintに
            board_list.append(row_list)
        return board_list


    param = {"token": "maizuru0478a4402bcf6769308a8d8fcafcf261bbb7ad87b911d2d0ee69a295d"}
    #トークン↓
    #maizuru0478a4402bcf6769308a8d8fcafcf261bbb7ad87b911d2d0ee69a295d

    # get()メソッドでGETリクエストを送信する
    response = requests.get("http://172.29.1.2:80/problem", params=param)

    get_data=vars(response)
    board = get_data['_content']
    board_data = json.loads(board)

    general_data=board_data['general']
    start_board_str=board_data['board']['start']#盤面のstring型のリスト
    goal_board_str=board_data['board']['goal']
    
    width=board_data['board']['width']
    height=board_data['board']['height']

    general_number=general_data['n']#一般抜型の個数
    general_data_patterns=general_data['patterns']#一般抜き型の情報が格納

    #一般抜型を取得
    general_patterns=[]#ここに一般抜型を追加
    for general in range(general_number):
        pattern_data=general_data_patterns[general]#patternsのdataを取得
        pattern_height=pattern_data['height']
        pattern=make_list(pattern_data['cells'],pattern_height)
        general_patterns.append(pattern)


    start_board=make_list(start_board_str,height)
    goal_board=make_list(goal_board_str,height)

    print("取得完了")

    return start_board,goal_board,general_patterns,width,height


# リクエスト時のURLを出力する
#pprint.pprint(vars(response))

#print(server_get())