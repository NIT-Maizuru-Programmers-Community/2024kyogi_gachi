goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1],
            [2,1,3,0,3]]#0:3,1:9,2:9,3:9

a=3
if a % 2==1:
    print("h偶数")

now_match_position=7
send_position=2
c=(now_match_position-send_position)//2 + (now_match_position-send_position)%2
print(c)





board_row=[list(x) for x in zip(*goal_board)]#行で参照のため転地

print(board_row)

#print(get_num(goal_board))
#tuple = [list(x) for x in zip(*goal_board)]#転地



