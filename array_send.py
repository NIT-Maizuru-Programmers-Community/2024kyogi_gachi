goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1],
            [2,1,3,0,3]]#0:3,1:9,2:9,3:9

now_board=[[3,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1],
           [2,1,3,0,3]]

soroeruretu=2

#寄せる動作を大会基準の配列で返す
def column_row_send(now_board,goal_board,send_position):#(現在の盤面,ゴール盤面,行か列か,何列目または何行目をそろえるのか)
    #send_directionがTrueなら行で揃える,Falseなら列で

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
    

    def count_column_row(board):#各要素数を1つの配列にまとめる,行または列で作成
        #行ならTrueで列ならFalse
        board_element=[]
        for column in range(len(board)):
            board_element.append(count_element(board[column]))
       
        return board_element


    def compare_element(array1,array2):#要素の一致数を取得
        score=0
        for i in range(4):
            if (array1[i]<array2[i]):
                score=score+array1[i]
            if (array1[i]>=array2[i]):
                score=score+array2[i]
        return score


    #揃えたいgoalと最も一致数が高いやつ探す(揃えたいnowの場所探す)
    def serch_most_match(now_element,goal_element,send_position):#入力はnowの要素数全部と任意のgoalの場所,列か行か
        match_score=[0,0]#[何列or何行目,一致数]
        #最も一致数が高いやつ探す
        for line in range(send_position,len(now_element)):#任意の揃えたい場所から最後まで
            now_element_score=compare_element(now_element[line],goal_element)#任意のnowの場所の一致数を取得
        if match_score[1] < now_element_score:
            match_score=[line,now_element_score]
        match_position=match_score[0]

        return match_position
    

    now_element=count_column_row(now_board)
    goal_element=count_element(goal_board[send_position])
    now_match_position=serch_most_match(now_element,goal_element,send_position)
    operate_array=[]#詰めるための操作を記録

    #False(0):列,True(1):行
    #0層に揃える場合
    if send_position==0:
        p=22#抜き型番号,全部1,256
        x=0#左端
        y=now_match_position-256
        s=0#上
        return [p,x,y,s]

    #1層以降
    #そろうまでループ
    while(now_match_position!=send_position):
        p=23##抜き型番号,横に1段ずつ,256
        x=0#左端
        if (now_match_position % 2==0 and send_position % 2==0) or (now_match_position % 2==1 and send_position % 2==1):#偶奇が一致してる
            y=send_position+1#そのままでかぶる
        else:
            y=send_position#そのままでもかぶらない
        s=0#上

        shorten_distance=(now_match_position-y)//2 + (now_match_position-y)%2#詰めた距離
        now_match_position -= shorten_distance#更新後
        operate_array.append([p,x,y,s])
     
    return operate_array
    

print(column_row_send(now_board,goal_board,soroeruretu))
#返り値はextendを使って追加して