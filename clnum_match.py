dir=0 #0:上 1:下 2:左 3:右
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

def fitnum(now_board,goal_board,dir,layer,wide,height):
    now_num0=0
    now_num1=0 #1の個数
    now_num2=0 #2の個数
    now_num3=0 #3の個数
    goal_num0=0
    goal_num1=0 
    goal_num2=0 
    goal_num3=0
    for i in range(wide):
        if now_board[layer,i]==0:
            now_num0+=1
        if now_board[layer,i]==1:
            now_num1+=1
        if now_board[layer,i]==2:
            now_num2+=1
        if now_board[layer,i]==3:
            now_num3+=1
        if goal_board[layer,i]==0:
            goal_num0+=1
        if goal_board[layer,i]==1:
            goal_num1+=1
        if goal_board[layer,i]==2:
            goal_num2+=1
        if goal_board[layer,i]==3:
            goal_num3+=1
    