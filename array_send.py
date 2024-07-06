goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]#0:2,1:8,2:8,3:7

now_board=[[3,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1]]

yoseruhoukou_kari=True#行:row(縦方向)
soroeruretu=0

#寄せる動作を大会基準の配列で返す
def column_row_send(now_board,goal_board,send_direction):#(現在の盤面,ゴール盤面,行か列か)
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
    

    def count_column_row(board):#行ごとと列ごとの各要素数を1つの配列に
        board_element_column=[]
        board_element_row=[]
        board_row=[list(x) for x in zip(*board)]#行で参照のため転地
        for column in range(len(board)):
            board_element_column.append(count_element(board[column]))
        for row in range(len(board)):
            board_element_row.append(count_element(board_row[row]))
        
        return [board_element_column,board_element_row]
    
    def compare_element(array1,array2):#要素の一致数を取得
            score=0
            for i in range(4):
                if (array1[i]<array2[i]):
                    score=score+array1[i]
                if (array1[i]>=array2[i]):
                    score=score+array2[i]
            return score
    
    def serch_match_line(now_board,goal_board):
         for line in range()




    def serch_most_match(now_element,goal_element,send_position):#揃えたいgoalと最も一致数が高いやつ探す,入力はnowの要素数全部と任意のgoalの場所
         print("shine")
    


    
    now_element=count_column_row(now_board)
    goal_element=count_column_row(goal_board)

    #False(0):列,True(1):行
    #列:column(横方向)で寄せる場合
    for i in range(len):


