goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1],
            [2,1,3,0,3]]#0:3,1:9,2:9,3:9


board_row=[list(x) for x in zip(*goal_board)]#行で参照のため転地
print(board_row)


board_row_jisaku=[]#転置後のboard
for column in range(len(goal_board[0])):
    row_array=[]
    for row in range(len(goal_board)):
        row_array.append(goal_board[row][column])
    board_row_jisaku.append(row_array)

print(board_row_jisaku)

#print(get_num(goal_board))
#tuple = [list(x) for x in zip(*goal_board)]#転地



