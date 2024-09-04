#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ

import numpy as np
import board_reload_fujii
import judge as J

class MyAlgo:
    def __init__(self, board_height, board_width, special_cutter_quantity) -> None:
        self.height = board_height
        self.width = board_width
        self.special_cutter_quantity = special_cutter_quantity
        self.board_op = board_reload_fujii.BoardOperation()
    
    def algo(self, now_board, correct_board):
        self.now = now_board
        self.correct = correct_board
        self.log = []

        def all_position():
            #すべての座標を探索
            recommended_action = [9999999, 0, 0, 0] #distance, cutter_num, [x, y], move_direction
            for y in range(self.height):
                for x in range(self.width):
                    min_distance_data =  self.force_search(x, y)
                    if recommended_action[0] > min_distance_data[0]:
                        recommended_action[0] = min_distance_data[0]
                        recommended_action[1] = min_distance_data[1]
                        recommended_action[2] = x ,y
                        recommended_action[3] = min_distance_data[2]
            return [recommended_action[1], recommended_action[2], recommended_action[3]]
        
        recommended_action = all_position()
        self.log.append(recommended_action)

        return recommended_action

    def force_search(self, x, y):
        min_distance_data = [9999999, 0, 0] #distance, cutter_num, move_direction
        for cutter_num_1 in range(25 + self.special_cutter_quantity):
            for move_direction in range(4):
                next_board = self.board_op.board_update(cutter_num_1, [x, y], move_direction, self.now)
                total_distance = self.evaluation(next_board)
                if min_distance_data[0] > total_distance:
                    min_distance_data[0] = total_distance
                    min_distance_data[1] = cutter_num_1
                    min_distance_data[2] = move_direction
        return min_distance_data

    def evaluation(self, board):
        def find_closest_equal_value(board, target_value, x, y):
            # ターゲット値と等しいすべてのインデックスを取得
            indices = np.argwhere(board == target_value) 
            min_manhattan_distance = 999

            for idx in indices:
                manhattan_distance = abs(idx[1] - x) + abs(idx[0] - y)
                if min_manhattan_distance > manhattan_distance:
                    min_manhattan_distance = manhattan_distance

            return min_manhattan_distance
        
        total_distance = 0
        for i in range(self.height):
            for j in range(self.width):
                val = self.correct[i][j]
                manhattan_distance = find_closest_equal_value(board, val, j, i)
                total_distance += manhattan_distance
        
        return total_distance


def main():
    start_board = [[0, 1], [2, 3]]
    correct_board = [[2, 1], [0, 3]]
    height = len(start_board)
    width = len(start_board[0])
    my_algo = MyAlgo(height, width, 0)
    judge = J.Judgec()
    board_op = board_reload_fujii.BoardOperation()

    judge_result = False
    incorrect_total = []
    board = start_board
    cnt = 1
    while judge_result != True:
        print(cnt)
        recommended_action = my_algo.algo(board, correct_board)
        board = board_op.board_update(recommended_action[0], recommended_action[1], recommended_action[2], board)
        judge_result, incorrect = judge.judge(board, correct_board)
        incorrect_total.append(incorrect)
        cnt += 1
    
    print(my_algo.log)
    print(incorrect_total)

main()
