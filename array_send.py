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

yoseruhoukou_kari=True#行:row(縦方向)
soroeruretu=3

#寄せる動作を大会基準の配列で返す
def column_row_send(now_board,goal_board,send_direction,send_position):#(現在の盤面,ゴール盤面,行か列か,何列目または何行目をそろえるのか)
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
    

    def count_column_row(board,send_direction):#各要素数を1つの配列にまとめる,行または列で作成
        #行ならTrueで列ならFalse

        if send_direction==False:#列の場合
            board_element_column=[]

            for column in range(len(board)):
                board_element_column.append(count_element(board[column]))

            return board_element_column
        
        if send_direction==True:#行の場合
            board_element_row=[]
            board_row=[list(x) for x in zip(*board)]#行で参照のため転地

            for row in range(len(board_row)):
                board_element_row.append(count_element(board_row[row]))
            
            return board_element_row

    

    def count_column_row_any(board,send_direction,send_position):#任意の場所の各要素数を取得

        if send_direction==False:#列の場合
            board_element_column=count_element(board[send_position])
            
            return board_element_column
        
        if send_direction==True:#行の場合
            board_row=[list(x) for x in zip(*board)]#行で参照のため転地
            board_element_row=count_element(board_row[send_position])

            return board_element_row


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
            print(now_element_score)

            if match_score[1] < now_element_score:
                match_score=[line,now_element_score]
        
        match_position=match_score[0]

        return match_position
    

    
    now_element=count_column_row(now_board,send_direction)
    goal_element=count_column_row_any(goal_board,send_direction,send_position)#goalの任意の場所の各要素数を取得

    now_match_position=serch_most_match(now_element,goal_element,send_position)
    print(now_match_position)


    #False(0):列,True(1):行
    #列:column(横方向)で寄せる場合




column_row_send(now_board,goal_board,yoseruhoukou_kari,soroeruretu)