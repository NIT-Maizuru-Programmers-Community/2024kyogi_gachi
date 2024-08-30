from board_reload_fujii import BoardOperation

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

    def count_element(board_array):#入力された1行または列の各要素数を取得
        element=[0,0,0,0]
        for i in range(len(board_array)):
            if board_array[i]==0:
                element[0]+=1

            if board_array[i]==1:
                element[1]+=1

            if board_array[i]==2:
                element[2]+=1

            if board_array[i]==3:
                element[3]+=1
        return element
    
    def search_cutter(cloce_distance):#抜き型の番号決める
        cutter_scale_array=[128,64,32,16,8,4,2,1]
        #print(f"{cloce_distance}cloce_distance")

        #general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
        #general_patterns_p=    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 ,20 ,21 ,22 ,23 ,24 ]
        scale_num=0
        while(cutter_scale_array[scale_num]>cloce_distance):
            scale_num+=1
        #print(f"{scale_num}scale_num")
        
        cutter_scale=cutter_scale_array[scale_num]#抜き型の大きさ
        #print(f"{cutter_scale}cutter_scale")

        #抜き型番号の決定
        if cutter_scale==128:
            return [21,128]
        
        if cutter_scale==64:
            return [18,64]
        
        if cutter_scale==32:
            return [15,32]
        
        if cutter_scale==16:
            return [12,16]
        
        if cutter_scale==8:
            return [9,8]
        
        if cutter_scale==4:
            return [6,4]
        
        if cutter_scale==2:
            return [3,2]
        
        if cutter_scale==1:
            return [0,1]




    operate_board=[]#詰めるための操作を記録
    move=BoardOperation()
    now_count=count_element(now_board[layer])  #現在の盤面におけるそれぞれの数字の数
    goal_count=count_element(goal_board[layer]) #正解の盤面におけるそれぞれの数字の数

    # completion=False
    # if evalution_value[0]==0 and evalution_value[1]==0 and evalution_value[2]==0 and evalution_value[3]==0:
    #     completion=True
    #     return completion

    
    while now_count!=goal_count:
    
        evalution_value=[0,0,0,0] #評価値
        for i in range(4): #過分、不足、満足を評価
            evalution_value[i]=now_count[i]-goal_count[i]


        excess_index=[layer,0] #過分のインデックス
        for k in range(4): #過分のインデックス取得
            if evalution_value[k]>0:
                excess_index[1]=now_board[layer].index(k)
                break

        shortage_index=[0,0] #不足のインデックス
        for k in range(4): #不足のインデックス取得
            if evalution_value[k]<0:
                for i in range(layer+1,height):
                    for j in range(wide):
                        if now_board[i][j]==k:
                            shortage_index[0]=i
                            shortage_index[1]=j
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break


        if shortage_index[1]!=excess_index[1]:
            p=23
            y=shortage_index[0]
            if shortage_index[1]<excess_index[1]:
                s=3#右に寄せる
                x=shortage_index[1]+wide-excess_index[1]
            else:
                s=2#左に寄せる
                x=shortage_index[1]-excess_index[1]-1
            
            now_board = move.board_update(p, [x, y], s, now_board)#ボードの更新
            operate_board.append([p,x,y,s])


        while shortage_index[0]!=excess_index[0]+1:

            cloce_distance=shortage_index[0]-excess_index[0]-1#詰める距離
            cutter_num_scale=search_cutter(cloce_distance)

            p=cutter_num_scale[0]
            x=excess_index[1]
            y=excess_index[0]-1
            s=0
            shortage_index[0]=shortage_index[0]-cutter_num_scale[1]

            now_board = move.board_update(p, [x, y], s, now_board)#ボードの更新
            operate_board.append([p,x,y,s])

        #目的地の1つ下まで詰めるため、1つ上に
        p=0
        x=excess_index[1]
        y=excess_index[0]
        s=0

        now_board = move.board_update(p, [x, y], s, now_board)#ボードの更新
        operate_board.append([p,x,y,s])

        now_count=count_element(now_board[layer])  #現在の盤面におけるそれぞれの数字の数

    return [operate_board,now_board]


#ans=fitnum(now_board,goal_board,layer,wide,height)
#print(ans[0])

#print(ans)