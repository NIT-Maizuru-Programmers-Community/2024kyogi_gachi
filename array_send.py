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

yoseruhoukou_kari=False
soroeruretu=3

#寄せる動作を大会基準の配列で返す
def column_row_send(now_board,goal_board,is_row,send_position):#(現在の盤面,ゴール盤面,行か列か,何列目または何行目をそろえるのか)
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
    

    def transposition(board):#転置
        board_row=[]
        for column in range(len(board[0])):
            row_array=[]
            for row in range(len(board)):
                row_array.append(board[row][column])
            board_row.append(row_array)
        
        return board_row


    def count_column_row(board,is_row):#各要素数を1つの配列にまとめる,行または列で作成
        #行ならTrueで列ならFalse
        board_element=[]
        if is_row==False:#列の場合
            for column in range(len(board)):
                board_element.append(count_element(board[column]))
        else:#行の場合
            board_row=transposition(board)#列と行入れ替え
            for row in range(len(board_row)):
                board_element.append(count_element(board_row[row]))
            
        return board_element

    
    def count_column_row_any(board,is_row,send_position):#任意の場所の各要素数を取得
        if is_row==False:#列の場合
            board_element_column_row=count_element(board[send_position])
        else:#行の場合
            board_row=transposition(board)#行で参照のため転置
            board_element_column_row=count_element(board_row[send_position])

        return board_element_column_row


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
    

    now_element=count_column_row(now_board,is_row)
    goal_element=count_column_row_any(goal_board,is_row,send_position)#goalの任意の場所の各要素数を取得
    now_match_position=serch_most_match(now_element,goal_element,send_position)
    print(f"{now_match_position}番目")
    operate_array=[]#詰めるための操作を記録

    #False(0):列,True(1):行
    #列:column(横方向)で寄せる場合
    #0層に揃える場合
    if send_position==0 and is_row==False:
        p=22#抜き型番号,全部1,256
        x=0#左端
        y=now_match_position-256#いい感じになる
        s=0#上
        return [p,x,y,s]
    elif send_position==0 and is_row==True:
        p=24#抜き型番号,全部1,256
        x=now_match_position-256#いい感じになるよ
        y=0#一番上
        s=2#左
        return [p,x,y,s]


    #1層以降
    if is_row==False:
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
            print(shorten_distance)

    else:#行:row(縦方向)で寄せる場合
        #そろうまでループ
        while(now_match_position!=send_position):
            p=24##抜き型番号,横に1段ずつ,256
            if (now_match_position % 2==0 and send_position % 2==0) or (now_match_position % 2==1 and send_position % 2==1):#偶奇が一致してる
                x=send_position+1#そのままでかぶる
            else:
                x=send_position#そのままでもかぶらない
            y=0#上端
            s=2#左

            shorten_distance=(now_match_position-x)//2 + (now_match_position-x)%2#詰めた距離
            now_match_position -= shorten_distance#更新後
            operate_array.append([p,x,y,s])
            print(shorten_distance)


    return operate_array
    

print(column_row_send(now_board,goal_board,yoseruhoukou_kari,soroeruretu))
#返り値はextendを使って追加して