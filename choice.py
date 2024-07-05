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


def column_row_choice(now_board,goal_board):#列or行の選択,行ならTrueで列ならFalseで返す
#行:row(縦方向),列:column(横方向)
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
    

    def count__column_row(board):#行ごとと列ごとの要素数を1つの配列に
        board_element_column=[]
        board_element_row=[]
        board_tate=[list(x) for x in zip(*board)]#行で参照のため転地
        for column in range(len(board)):
            board_element_column.append(count_element(board[column]))
        for row in range(len(board)):
            board_element_row.append(count_element(board_tate[row]))
        
        return [board_element_column,board_element_row]
    

    def compare_element(array1,array2):#一致数確認,
            score=0
            for i in range(4):
                if (array1[i]<array2[i]):
                    score=score+array1[i]
                if (array1[i]>=array2[i]):
                    score=score+array2[i]
            return score
    

    def match_check(now,goal):#nowの要素数1つとgoalの要素数全部
        score_match=0
        for goal_length in range(len(goal)):
            score_match=score_match+compare_element(now,goal[goal_length])
        return score_match

    goal_element=count__column_row(goal_board)
    now_board_tposition=[list(x) for x in zip(*now_board)]#行と列入れ替え
    column_score=0
    row_score=0

    for column_number in range(len(now_board[0])):#列の要素数の一致数
        now_column=count_element(now_board[column_number]) 
        column_score=column_score+match_check(now_column,goal_element[0])
    
    for row_number in range(len(now_board_tposition[0])):#行の要素数の一致度
        now_row=count_element(now_board_tposition[row_number]) 
        row_score=row_score+match_check(now_row,goal_element[1])
    
    if column_score < row_score:
        is_column_row=False
    if column_score > row_score:
        is_column_row=True

    return is_column_row

print(column_row_choice(now_board,goal_board))