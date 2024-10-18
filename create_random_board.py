import numpy as np
import general_patterns

def create_board(height ,width):
    first_board = np.random.randint(0, 4, (height, width))
    correct_board=first_board.tolist() #正解の盤面
    shuffled_elements = np.random.permutation(first_board.flatten())
    second_board = shuffled_elements.reshape(height, width)
    now_board=second_board.tolist() #現在の盤面
    return correct_board, now_board