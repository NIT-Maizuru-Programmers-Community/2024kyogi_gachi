from board_reload_fujii import BoardOperation
import numpy

#dir=1 #0:上 1:左
layer=0 #n層目
goal_board=[[3,1,3,2,2],
            [0,2,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]

now_board=[[3,2,3,2,1],
           [3,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [0,1,3,0,1]]
width=5
height=5

def clmatch(now_board,goal_board,layer,width,height):

    unknown_x = 0 #未知部分の最初のx座標(=一致部の最後のx座標+1),最初はすべて未知
    unknown_y = 0
    cutter_num = 0
    goal_list = goal_board[layer]
    nowboard_log=[]

    print("HI!")

    #上方向

    while(unknown_x < width):

        now_list = now_board[layer]
        target=goal_list[unknown_x] #target
        c = unknown_x
        
        #unknown_x地点から,ゴールのものと一致するピース(target)が見つかるまでcをカウント
        while(now_list[c] != target):
            c += 1
        
        #(c-unknown_x)は不一致ピースの幅
        #不一致ピースの幅が0の場合はunknown_xを1ずらす
        if(c-unknown_x == 0):
            unknown_x += 1
            continue

        #不一致ピースの幅が0以外の場合,変更を加える必要があるので使用する抜き型を決定
        #2^nの抜き型を使用する,そのようなnを見つける関数
        def find_n(a):
            n = 0
            while 2 ** n <= a:
                n += 1

            return n - 1

        if(find_n(c-unknown_x)==0):
            cutter_num=0
        else:
            cutter_num=3*find_n(c-unknown_x)-2

        #now_boardを更新
        move=BoardOperation()
        now_board = move.board_update(cutter_num, [unknown_x, layer], 2, now_board)
        nowboard_log.append([cutter_num, [unknown_x, layer], 2])

        #unknown_xを更新するのは,ちょうど2^n=(c-unknown_x)を満たすような整数nだったとき
        if(2**find_n(c-unknown_x) == c-unknown_x):
            unknown_x+=int(2**find_n(c-unknown_x))

            #print(now_board)

    #左方向
#     if(dir == 1):

#         while(unknown_y < width):
#             for i in range(len(now_board)):
#                 now_list[i]=now_board[i][layer]
            
#             target=goal_list[unknown_y] #target
#             c = unknown_x
            
#             #unknown_x地点から,ゴールのものと一致するピース(target)が見つかるまでcをカウント
#             while(now_list[c] != target):
#                 c += 1
            
#             #(c-unknown_x)は不一致ピースの幅
#             #不一致ピースの幅が0の場合はunknown_xを1ずらす
#             if(c-unknown_x == 0):
#                 unknown_x += 1
#                 continue

#             #不一致ピースの幅が0以外の場合,変更を加える必要があるので使用する抜き型を決定
#             #2^nの抜き型を使用する,そのようなnを見つける関数
#             def find_n(a):
#                 n = 0
#                 while 2 ** n <= a:
#                     n += 1
    
#                 return n - 1

#             if(find_n(c-unknown_x)==0):
#                 cutter_num=0
#             else:
#                 cutter_num=3*find_n(c-unknown_x)-2

#             #now_boardを更新
#             move=BoardOperation()
#             now_board = move.board_update(cutter_num, [unknown_x, layer], 2, now_board)
#             nowboard_log.append([cutter_num, [unknown_x, layer], 2])


#             #unknown_xを更新するのは,ちょうど2^n=(c-unknown_x)を満たすような整数nだったとき
#             if(2**find_n(c-unknown_x) == c-unknown_x):
#                 unknown_x+=int(2**find_n(c-unknown_x))

#             #print(now_board)
        
    return (nowboard_log,now_board)

print(clmatch(now_board,goal_board,dir,layer,width,height))