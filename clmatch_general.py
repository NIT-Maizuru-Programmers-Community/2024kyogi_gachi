from board_reload_fujii import BoardOperation

#dir=1 #0:上 1:左
layer=0 #n層目
width=5

goal_board=[[3,1,3,2,2,1,2,3,3],
            [0,2,1,3,2,1,1,1,1],
            [2,1,3,0,2,1,1,1,1],
            [3,1,3,2,3,1,1,1,1],
            [2,1,3,0,1,1,1,1,1]]

now_board=[[3,2,3,2,1,3,3,2,1],
           [3,2,0,1,2,1,1,1,1],
           [0,1,3,2,2,1,1,1,1],
           [2,1,3,2,3,1,1,1,1],
           [0,1,3,0,1,1,1,1,1]]


def clmatch(now_board,goal_board,just_type,general_usable,layer,width):

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

    def search_goal(now_board_layer,start_place,goal_num):#goalと一致している場所を取得

        while(now_board_layer[start_place+1]!=goal_num):
            start_place=start_place+1
        
        return start_place+1
    

    def search_cutter(cloce_distance,standard_combination):#抜き型の番号決める
        cutter_scale_array=[128,64,32,16,8,4,2,1]
        scale_num=0


        #just_type：[general_num,cutter_distance,sharpen_distance_left]
        #general_usable.append：[general_num,general_distance,cutter_distance,sharpen_distance_left]

        for i in range(len(just_type)):
            if(just_type[i][1] == cloce_distance):
                return just_type[i][1]

        for i in range(len(just_type)):
            if(just_type[i][1] in standard_combination):
                return just_type[i][0]
            
        for i in range(len(general_usable)):
            if((general_usable[i][2] in standard_combination)and(general_usable[i][1]<cloce_distance)):
                return general_usable[i][0]

        while(cutter_scale_array[scale_num]>cloce_distance):
            scale_num+=1
        
        cutter_scale=cutter_scale_array[scale_num] #抜き型の大きさ

        #抜き型番号の決定
        if cutter_scale==128:
            return 20
        
        if cutter_scale==64:
            return 17
        
        if cutter_scale==32:
            return 14
        
        if cutter_scale==16:
            return 11
        
        if cutter_scale==8:
            return 8
        
        if cutter_scale==4:
            return 5
        
        if cutter_scale==2:
            return 2
        
        if cutter_scale==1:
            return 0
        

        

    operate_board=[]#ここに操作情報を追加
    move=BoardOperation()

    if now_board[layer][0] != goal_board[layer][0]:#1回目の処理
        goal_place=search_goal(now_board[layer],0,goal_board[layer][0])
        now_board = move.board_update(23, [-256+goal_place, layer], 2, now_board)#ボードの更新

        operate_board.append([23,-256+goal_place,layer,2])


    for place in range(1,width-1):
        while(now_board[layer][place]!=goal_board[layer][place]):
            goal_place=search_goal(now_board[layer],place,goal_board[layer][place])

            cloce_distance=goal_place-place #詰める距離
            standard_combination=making_combination(cloce_distance)#bitの1が多い順にソート済み

            p=search_cutter(cloce_distance,standard_combination)
            x=place
            y=layer
            s=2
            now_board = move.board_update(p, [x, y], s, now_board)#ボードの更新
            operate_board.append([p,x,y,s])
        
    return (operate_board,now_board)

#print(clmatch(now_board,goal_board,layer,width))