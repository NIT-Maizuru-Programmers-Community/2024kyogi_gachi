layer=0 #n層目
goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]

now_board=[[3,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1]]

def fitnum(now_board,goal_board,layer,wide,height):
    now_0=0 #0の数
    now_1=0 #1の数
    now_2=0 #2の数
    now_3=0 #3の数
    goal_0=0
    goal_1=0 
    goal_2=0 
    goal_3=0
    for i in range(wide):
        if now_board[0][i]==0:
            now_0+=1
        if now_board[0][i]==1:
            now_1+=1
        if now_board[0][i]==2:
            now_2+=1
        if now_board[0][i]==3:
            now_3+=1
        if goal_board[0][i]==0:
            goal_0+=1
        if goal_board[0][i]==1:
            goal_1+=1
        if goal_board[0][i]==2:
            goal_2+=1
        if goal_board[0][i]==3:
            goal_3+=1

    new_0=now_0-goal_0
    new_1=now_1-goal_1
    new_2=now_2-goal_2
    new_3=now_3-goal_3

    for i in range(wide):
        if now_board[0][i]==0:
            if new_0>0