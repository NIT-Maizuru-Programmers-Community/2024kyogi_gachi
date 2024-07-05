from board_reload_fujii import BoardOperation
dir=0 #0:上 1:左
layer=0 #n層目
goal_board=[[3,1,3,2,2],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]

now_board=[[3,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1]]
width=5
height=5

def clmatch(now_board,goal_board,dir,layer,width,height):

    unknown_x = 0 #未知部分の最初のx座標(=一致部の最後のx座標+1),最初はすべて未知
    cutter_num = 0
    goal_list = goal_board[layer]
    if(dir == 0):
        while(unknown_x - 1 != width):

            now_list = now_board[layer]
            target=goal_list[unknown_x] #target
            c = unknown_x
            
            #unknown_x地点から、一致するピースが見つかるまでcをカウント
            while(now_list[c] != target):
                c += 1
            
                #(c-unknown_x)は不一致ピースの幅
                #不一致ピースの幅が0の場合はunknown_xを1ずらす
                if(c-unknown_x == 0):
                    unknown_x += 1
                    break

                #不一致ピースの幅が0以外の場合,変更を加える必要があるので使用する抜き型を決定
                n=0
                while(2**n <c-unknown_x):
                    n+=1
                n-=1
                if(n==0):
                    cutter_num=1
                else:cutter_num=3*n-1

                #now_boardを更新
                move=BoardOperation()
                now_board = move.board_update(cutter_num, [unknown_x, layer], 2, now_board)
            

                #unknown_xを更新
                unknown_x+=2**n
            print("HI")
            

    #now_board[0][0]=10
    print(now_board)
    return 0

clmatch(now_board,goal_board,dir,layer,width,height)