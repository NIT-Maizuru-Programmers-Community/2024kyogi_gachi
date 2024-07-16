d=[]

a=[[1,2,3,4,5,6]]
s=([[0, 1, 1, 2]], [[1, 2, 3], [1, 2, 3], [3, 2, 1]])

goal_board=[[3,1,3,2,2],
            [0,2,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3]
            ]

height=len(goal_board)
wide=len(goal_board[0])

print(height)
print(wide)

c=[[1,2,3]]
d.extend(a)
d.append(c)
#print(d)

