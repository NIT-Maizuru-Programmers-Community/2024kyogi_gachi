import sys
import os
# 相対パスを使用して一つ上の階層のパスを追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import copy
import numpy as np
import board_reload_fujii
import judge as J
import general_patterns

class MyAlgo:
    def __init__(self, board_height, board_width, special_cutter_quantity, cutter_size) -> None:
        self.height = board_height
        self.width = board_width
        self.cutter_size = cutter_size
        self.special_cutter_quantity = special_cutter_quantity
        self.board_op = board_reload_fujii.BoardOperation()
        self.log = []
    
    def algo(self, now_board, correct_board):
        self.now = copy.deepcopy(now_board)
        self.correct = correct_board

        def all_position():
            # すべての座標を探索（2手目の評価で選択）
            recommended_action = [9999999, 0, 0, 0]  # distance, cutter_num, [x, y], move_direction
            
            for y in range(self.height):
                for x in range(self.width):
                    min_distance_data = self.force_search_depth_2(x, y)
                    if recommended_action[0] > min_distance_data[0]:
                        recommended_action = min_distance_data
            return [recommended_action[1], recommended_action[2], recommended_action[3]]
        
        recommended_action = all_position()
        self.log.append(recommended_action)

        return recommended_action

    # ある座標に対して2手目のみの評価で最適な型と方向を求める
    def force_search_depth_2(self, x, y):
        min_distance_data = [9999999, 0, [x, y], 0]  # distance, cutter_num, [x, y], move_direction
        
        # 1手目の全候補を試す
        for cutter_num_1 in range(25 + self.special_cutter_quantity):
            cutter_height = self.cutter_size[cutter_num_1][0]
            cutter_width = self.cutter_size[cutter_num_1][1]
            if cutter_height > self.height or cutter_width > self.width:
                continue

            for move_direction_1 in range(4):
                next_board = self.board_op.board_update(cutter_num_1, [x, y], move_direction_1, copy.deepcopy(self.now))
                
                # 2手目の探索（評価を基に選択）
                for y2 in range(self.height):
                    for x2 in range(self.width):
                        for cutter_num_2 in range(25 + self.special_cutter_quantity):
                            cutter_height_2 = self.cutter_size[cutter_num_2][0]
                            cutter_width_2 = self.cutter_size[cutter_num_2][1]
                            if cutter_height_2 > self.height or cutter_width_2 > self.width:
                                continue

                            for move_direction_2 in range(4):
                                next_board_2 = self.board_op.board_update(cutter_num_2, [x2, y2], move_direction_2, copy.deepcopy(next_board))
                                total_distance_2 = self.evaluation(next_board_2)

                                if min_distance_data[0] > total_distance_2:
                                    min_distance_data = [total_distance_2, cutter_num_1, [x, y], move_direction_1]

        return min_distance_data

    # すべてのセルの正解との距離を加算
    def evaluation(self, board):
        def find_closest_equal_value(board, target_value, x, y):
            indices = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == target_value]
            min_manhattan_distance = float('inf')

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
    cutters = general_patterns.general_patterns_cells
    cutter_size = []
    for i in range(len(cutters)):
        height = len(cutters[i])
        width = len(cutters[i][0])
        cutter_size.append([height, width])

    start_board = [[0, 1, 2, 1], [3, 0, 1 ,0], [2, 3, 0, 2], [2, 3, 0, 2]]
    correct_board = [[0, 2, 0, 2], [2, 3, 0, 2], [1, 3, 1, 0], [2, 0, 1, 3]]
    height = len(start_board)
    width = len(start_board[0])
    my_algo = MyAlgo(height, width, 0, cutter_size)
    judge = J.Judgec()
    board_op = board_reload_fujii.BoardOperation()

    judge_result = False
    incorrect_total = []
    board = start_board
    cnt = 1

    while judge_result != True:
        print("cnt=", cnt)
        recommended_action = my_algo.algo(board, correct_board)
        print("recomm!=", recommended_action)
        cutter = recommended_action[0]
        posi = recommended_action[1]
        direction = recommended_action[2]
        board = board_op.board_update(cutter, posi, direction, board)
        print("board=", board)
        judge_result, incorrect = judge.judge(board, correct_board)
        incorrect_total.append(incorrect)
        cnt += 1
    
    print("log=", my_algo.log)
    print("incorrect_total=", incorrect_total)

main()