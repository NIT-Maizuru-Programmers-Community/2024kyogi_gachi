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
        cutter_number=[21,18,15,12,9,6,3,0]
        cutter_info=[]#ここに使用する抜型番号を追加
        #general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
        #general_patterns_p=    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 ,20 ,21 ,22 ,23 ,24 ]

        while(cloce_distance!=0):
            scale_num=0
            while(cutter_scale_array[scale_num]>cloce_distance):
                scale_num+=1
            cutter_info.append(cutter_number[scale_num])
            cloce_distance-=cutter_scale_array[scale_num]
        
        return cutter_info





    operate_board=[]#詰めるための操作を記録
    move=BoardOperation()
    now_count=count_element(now_board[layer])  #現在の盤面におけるそれぞれの数字の数
    goal_count=count_element(goal_board[layer]) #正解の盤面におけるそれぞれの数字の数
    evalution_value=[0,0,0,0] #評価値
    for i in range(4): #過分、不足、満足を評価
        evalution_value[i]=now_count[i]-goal_count[i]

    # completion=False
    # if evalution_value[0]==0 and evalution_value[1]==0 and evalution_value[2]==0 and evalution_value[3]==0:
    #     completion=True
    #     return completion



    
    while evalution_value[0]!=0 or evalution_value[1]!=0 or evalution_value[2]!=0 or evalution_value[3]!=0:
        excess_index=[layer,0] #過分のインデックス
        for k in range(4): #過分のインデックス取得
            if evalution_value[k]>0:
                excess_index[1]=now_board[layer].index(k)
                break
        
        #print(f"{excess_index}excess_index")

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
        
        #print(f"{shortage_index}shortage_index")
        #print(now_board)


        if shortage_index[1]!=excess_index[1]:#x座標揃える
            p=23
            y=shortage_index[0]
            if shortage_index[1]<excess_index[1]:
                s=3#右に寄せる
                x=shortage_index[1]+wide-excess_index[1]
            else:
                s=2#左に寄せる
                x=-256+shortage_index[1]-excess_index[1]
            
            now_board = move.board_update(p, [x, y], s, now_board)#ボードの更新
            operate_board.append([p,x,y,s])
        #print(f"{now_board}x座標揃える")


        #y座標の1つ下まで持ってくる
        cloce_distance=shortage_index[0]-excess_index[0]-1#詰める距離
        cutter_num_scale=search_cutter(cloce_distance)

        for cutter in cutter_num_scale:
            p=cutter
            x=excess_index[1]
            y=excess_index[0]+1
            s=0

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
        for i in range(4): #過分、不足、満足を評価
            evalution_value[i]=now_count[i]-goal_count[i]
        #print(f"{evalution_value}evalution_value")

    return [operate_board,now_board]


# ans=fitnum(now_board,goal_board,layer,wide,height)
# print(ans[0])

#print(ans)