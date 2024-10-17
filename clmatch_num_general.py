from board_reload_fujii_general import BoardOperation

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

def fitnum(now_board,goal_board,layer,general_usable_column,cut_type,wide,height):

    def making_combination(cloce_distance):
        cutter_scale_array=[128,64,32,16,8,4,2,1]

        div_cloce_distance=cloce_distance #div_cloce_distanceを、定型(cutter_scale_array)で分割
        composition_list=[] #dic_cloce_distanceを構成する数字(定型)を格納

        #div_cloce_distanceを構成する数字(定型)をcomposition_listに格納
        while(div_cloce_distance!=0):
            scale_num=0
            while(cutter_scale_array[scale_num]>div_cloce_distance):
                scale_num+=1
            composition_list.append(cutter_scale_array[scale_num])
            div_cloce_distance-=cutter_scale_array[scale_num]
       
        num=0
        combination_list=[]
        #composition_listの各数字の組み合わせでできる数字をcombination_listに格納
        for i in range((1<<len(composition_list))):
            num=0
            for j in range(len(composition_list)):
                if((i>>j)&1):
                    if((str(bin(i)).count('1'))!=1):
                        num+=composition_list[j]
            
            #00...0の場合は考えない(00...1 ~ 11...1)
            if(num!=0):
                combination_list.append([num,num.bit_count()])

        bit_sort=sorted(combination_list, key=lambda x: x[1], reverse=True)#bitの1が多い順でソート
        combination_sort=[]
        for bit_pattern in bit_sort:
            combination_sort.append(bit_pattern[0])

        return combination_sort


    def search_cutter(cloce_distance):#抜き型の番号決める
        standard_combination=making_combination(cloce_distance)
        cutter_scale_array=[128,64,32,16,8,4,2,1]
        cutter_info=[]#[番号,一般(1)か定型か(0)]
        is_exist=False
        #just_type：[general_num,cutter_distance,sharpen_distance_left]
        #general_usable.append：[general_num,general_distance,cutter_distance,sharpen_distance_left]

        while is_exist==False:#定型の組み合わせの中に一般があるか参照
            for general in standard_combination:
                for usable in range(0,len(general_usable_column)):
                    if general==general_usable_column[usable][3]:#詰めれる距離参照
                        if cloce_distance>=general_usable_column[usable][2]:#幅参照
                            cutter_info.append([usable,1,general_usable_column[usable][3]])
                            cloce_distance=cloce_distance-general_usable_column[usable][3]
                            standard_combination=making_combination(cloce_distance)#bitの1が多い順にソート済み
                            break
                else:
                    continue
                break

            else:
                is_exist=True

            if is_exist==True:
                break 

        while(cloce_distance!=0):
            scale_num=0
            while(cutter_scale_array[scale_num]>cloce_distance):
                scale_num+=1
            
            if cutter_scale_array[scale_num]==128:
                cutter_info.append([21,0,128])
                
            if cutter_scale_array[scale_num]==64:
                cutter_info.append([18,0,64])
            
            if cutter_scale_array[scale_num]==32:
                cutter_info.append([15,0,32])
            
            if cutter_scale_array[scale_num]==16:
                cutter_info.append([12,0,16])
            
            if cutter_scale_array[scale_num]==8:
                cutter_info.append([9,0,8])
            
            if cutter_scale_array[scale_num]==4:
                cutter_info.append([6,0,4])
            
            if cutter_scale_array[scale_num]==2:
                cutter_info.append([3,0,2])
            
            if cutter_scale_array[scale_num]==1:
                cutter_info.append([0,0,1])

            cloce_distance-=cutter_scale_array[scale_num]             
        
        return cutter_info








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
    
    # def search_cutter(cloce_distance):#抜き型の番号決める
    #     cutter_scale_array=[128,64,32,16,8,4,2,1]
    #     cutter_number=[21,18,15,12,9,6,3,0]
    #     cutter_info=[]#ここに使用する抜型番号を追加
    #     #general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
    #     #general_patterns_p=    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 ,20 ,21 ,22 ,23 ,24 ]

    #     while(cloce_distance!=0):
    #         scale_num=0
    #         while(cutter_scale_array[scale_num]>cloce_distance):
    #             scale_num+=1
    #         cutter_info.append(cutter_number[scale_num])
    #         cloce_distance-=cutter_scale_array[scale_num]
        
    #     return cutter_info





    operate_board=[]#詰めるための操作を記録
    move=BoardOperation(cut_type)
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

        #y座標の1つ下まで持ってくる
        cloce_distance=shortage_index[0]-excess_index[0]-1#詰める距離
        goal_place=shortage_index[0]
        cutter_info=search_cutter(cloce_distance)

        for info in cutter_info:
            if info[1]==0:#定型
                p=info[0]
                x=excess_index[1]
                y=layer+1
                goal_place=goal_place-info[2]
            else:
                #[抜き型番号,何列目か,幅,詰めれる距離,削った距離]
                p=general_usable_column[info[0]][0]
                x=excess_index[1]-general_usable_column[info[0]][1]
                y=shortage_index[0]+general_usable_column[info[0]][2]+general_usable_column[info[0]][4]
                goal_place=goal_place-general_usable_column[info[0]][3]


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