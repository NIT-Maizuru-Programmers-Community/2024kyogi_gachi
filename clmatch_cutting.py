from board_reload_fujii import BoardOperation
import numpy

#dir=1 #0:上 1:左
layer=2 #n層目

# goal_board=[[3,1,3,2,2],
#             [0,2,1,3,2],
#             [2,1,3,0,2],
#             [3,1,3,2,3],
#             [2,1,3,0,1]]

# now_board=[[3,2,3,2,1],
#            [3,2,0,1,2],
#            [0,1,3,2,2],
#            [2,1,3,2,3],
#            [0,1,3,0,1]]

width=3
height=3

def clmatch(now_board,goal_board,layer,width,height):

    def serch_goal(now_board_layer,place,goal_num):#goalと一致している場所を取得

        while(now_board_layer[place+1]!=goal_num):
            place=place+1
        
        return place+1






    operate_board=[]#ここに操作情報を追加

    if now_board[layer][0] != goal_board[layer][0]:
        goal_place=serch_goal(now_board[layer],0,goal_board[layer][0])

        operate_board.append([23,-256+goal_place,layer,2])



    for place in range(1,width):
        

    





        
    return (nowboard_log,now_board)

#print(clmatch(now_board,goal_board,layer,width,height))