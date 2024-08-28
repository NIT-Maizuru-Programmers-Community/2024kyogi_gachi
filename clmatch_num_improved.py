layer=2 #n層目
wide=5
height=5
goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]

now_board=[[1,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1]]

def fitnum(now_board,goal_board,layer,wide,height):
    completion=False
    p=[]
    x=[]
    y=[]
    s=[]
    ans=[]

    now_count=[0,0,0,0]  #現在の盤面におけるそれぞれの数字の数
    goal_count=[0,0,0,0] #正解の盤面におけるそれぞれの数字の数
    for i in range(wide): #各盤面における数字の数をカウント
        for j in range(4):
            if now_board[layer][i]==j:
                now_count[j]+=1
        for j in range(4):
            if goal_board[layer][i]==j:
                goal_count[j]+=1
    
    evalution_value=[0,0,0,0] #評価値
    for i in range(4): #過分、不足、満足を評価
        evalution_value[i]=now_count[i]-goal_count[i]

    if evalution_value[0]==0 and evalution_value[1]==0 and evalution_value[2]==0 and evalution_value[3]==0:
        completion=True
        return completion
    
    excess_index=[layer,0] #過分のインデックス
    for k in range(4): #過分のインデックス取得
        if evalution_value[k]>0:
            excess_index[1]=now_board[layer].index(k)
            break
    
    shortage_index=[0,0] #不足のインデックス
    for k in range(4): #不足のインデックス取得
        if evalution_value[k]<0:
            depth=0
            found=False
            while True:
                for i in range(depth): #左側処理
                    y_index = -excess_index[0] + 1 + i
                    x_index = excess_index[1] - depth + i
                    if(y_index < height and 0 <= x_index < wide and now_board[y_index][x_index] == k):
                        shortage_index[0]=y_index
                        shortage_index[1]=x_index
                        found=True
                        break
                if found:
                    break

                y_index=-excess_index[0]+depth+1 #中央処理
                x_index=excess_index[1]
                if(y_index < height and 0 <= x_index < wide and now_board[y_index][x_index] == k):
                    shortage_index[0]=y_index
                    shortage_index[1]=x_index
                    found=True
                    break
                if found:
                    break

                for i in range(depth): #右側処理
                    y_index=-excess_index[0]+depth-i
                    x_index=excess_index[1]+1+i
                    if(y_index < height and 0 <= x_index < wide and now_board[y_index][x_index] == k):
                        shortage_index[0]=y_index
                        shortage_index[1]=x_index
                        found=True
                        break
                if found:
                    break
                depth+=1
    
    move_num=shortage_index.copy()
    for i in range(abs(shortage_index[1]-excess_index[1])+abs(shortage_index[0]-excess_index[0])):
        if move_num[1]!=excess_index[1] and move_num[0]!=excess_index[0]:
            if move_num[1]<excess_index[1]:
                move_num[1]+=1
                p.append(0)
                x.append(move_num[1])
                y.append(move_num[0])
                s.append(3)
            if move_num[1]>excess_index[1]:
                move_num[1]-=1
                p.append(0)
                x.append(move_num[1])
                y.append(move_num[0])
                s.append(2)
        if move_num[1]==excess_index[1] and move_num[0]!=excess_index[0]:
            move_num[0]-=1
            p.append(0)
            x.append(move_num[1])
            y.append(move_num[0])
            s.append(0)
    
    for i in range(len(p)):
        t=[0,0,0,0]
        t[0]=p[i]
        t[1]=x[i]
        t[2]=y[i]
        t[3]=s[i]
        ans.append(t)



    return ans


ans=fitnum(now_board,goal_board,layer,wide,height)

#print(ans)