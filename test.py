import numpy as np


# now_board_layer=[2,3,5,1,6,3,4]
# goal_num=6
# place=1
# while(now_board_layer[place+1]!=goal_num):
#         place=place+1     
# print(place+1)



first_board = np.random.randint(0, 4, (24, 24))
correct_board=first_board.tolist() #正解の盤面
shuffled_elements = np.random.permutation(first_board.flatten())
second_board = shuffled_elements.reshape(24, 24)
now_board=second_board.tolist() #現在の盤面


print(correct_board)
print(now_board)