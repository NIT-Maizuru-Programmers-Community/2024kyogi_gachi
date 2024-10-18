import sys
import os
import time
# 相対パスを使用して一つ上の階層のパスを追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import copy
import numpy as np
import cupy as cp  # CuPyをインポート
import random
import board_reload_gpu as board_reload_fujii
import judge as J
import general_patterns
import create_random_board

class MyAlgo:
    def __init__(self, board_height, board_width, special_cutter_quantity, cutter_size) -> None:
        self.height = board_height
        self.width = board_width
        self.cutter_size = cutter_size
        self.special_cutter_quantity = special_cutter_quantity
        self.board_op = board_reload_fujii.BoardOperation()
        self.log = []
    
    def algo(self, now_board, correct_board):
        self.now = now_board  # NumPy配列をCuPy配列に変換
        self.correct = correct_board  # NumPy配列をCuPy配列に変換

        def all_position():
            # すべての座標を探索
            recommended_action = [9999999, 0, 0, 0]  # distance, cutter_num, [x, y], move_direction
            for y in range(self.height):
                for x in range(self.width):
                    def check_pass_position():  # True: continue 
                        if random.random() > 0.2 or self.height * 0.8 < y:
                            return True
                        return False
                    
                    if check_pass_position():
                        continue
                    print("position=", x, y)
                    min_distance_data = self.force_search(x, y)
                    if recommended_action[0] > min_distance_data[0]:
                        recommended_action[0] = min_distance_data[0]
                        recommended_action[1] = min_distance_data[1]  # cutter_num
                        recommended_action[2] = [x ,y]
                        recommended_action[3] = min_distance_data[2]  # direction
            return [recommended_action[1], recommended_action[2], recommended_action[3], recommended_action[0]]
        
        recommended_action = all_position()
        self.log.append(recommended_action)

        return recommended_action

    # ある座標に対してスコアと最適な型と方向を求める
    def force_search(self, x, y):
        min_distance_data = [9999999, 0, 0]  # distance, cutter_num, move_direction
        for cutter_num_1 in range(25 + self.special_cutter_quantity):
            cutter_height = self.cutter_size[cutter_num_1][0]
            cutter_width = self.cutter_size[cutter_num_1][1]
            if cutter_height > self.height and cutter_width > self.width:
                break

            for move_direction in range(4):
                if not self.check_board_change([x, y], cutter_num_1, move_direction):
                    continue

                next_board = self.board_op.board_update(cutter_num_1, [x, y], move_direction, cp.asarray(self.now))
                total_distance = self.evaluation(next_board)
                
                if min_distance_data[0] > total_distance:
                    min_distance_data[0] = total_distance
                    min_distance_data[1] = cutter_num_1
                    min_distance_data[2] = move_direction
        return min_distance_data
    
    def check_board_change(self, position, cutter_num, direction):
        cutter_type = self.cutter_type(cutter_num)
        p_x, p_y = position
        cutter_height, cutter_width = self.cutter_size[cutter_num]
        is_changed = True

        if cutter_type == 0:
            if ((direction == 0 and (p_y + cutter_height) >= self.height)
                    or (direction == 1 and p_y == 0)
                    or (direction == 2 and (p_x + cutter_width) >= self.width)
                    or (direction == 3 and p_x == 0)):
                is_changed = False

        elif cutter_type == 1:
            if ((direction == 2 and (p_x + cutter_width) >= self.width)
                    or (direction == 3 and p_x == 0)):
                is_changed = False

        elif cutter_type == 2:
            if ((direction == 0 and (p_y + cutter_height) >= self.height)
                    or (direction == 1 and p_y == 0)):
                is_changed = False
        
        if is_changed:
            next_board = self.board_op.board_update(cutter_num, position, direction, cp.asarray(self.now))
            if cp.all(next_board == self.now):  # CuPyでの比較
                is_changed = False
            
        return is_changed

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
                manhattan_distance = find_closest_equal_value(cp.asnumpy(board), val, j, i)  # CuPyからNumPyへ変換
                total_distance += manhattan_distance ** 4
        
        return total_distance

    # 型の種類を判別する
    def cutter_type(self, cutter_num):  # 0:すべて１, 1:横, 2:縦, 3:一般抜型
        if cutter_num in [0, 1, 4, 7, 10, 13, 16, 19, 22]:
            return 0
        elif cutter_num in [2, 5, 8, 11, 14, 17, 20, 23]:
            return 1
        elif cutter_num < 25:
            return 2
        else:
            return 3


def main():
    start = time.perf_counter()

    cutters = general_patterns.general_patterns_cells
    cutter_size = []
    for i in range(len(cutters)):
        height = len(cutters[i])
        width = len(cutters[i][0])
        cutter_size.append([height, width])

    start_board, correct_board = create_random_board.create_board(10, 10)
    print(correct_board)

    height = len(start_board)
    width = len(start_board[0])
    my_algo = MyAlgo(height, width, 0, cutter_size)
    judge = J.Judgec()
    board_op = board_reload_fujii.BoardOperation()

    judge_result = False
    incorrect_total = []
    board = cp.asarray(start_board)
    correct_board = cp.asarray(correct_board)
    cnt = 1

    while not judge_result:
        print("cnt=", cnt)
        recommended_action = my_algo.algo(board, correct_board)  # CuPyからNumPyに変換
        print("recomm!=", recommended_action.tolist())
        # cutter = recommended_action[0]
        # posi = recommended_action[1]
        # direction = recommended_action[2]
        # rsl_board = board_op.board_update(cutter, posi, direction, cp.asarray(board))  # CuPyからNumPyに変換
        print("board=", board.tolist())
        judge_result, incorrect = judge.judge(board.tolist(), correct_board.tolist())  # CuPyからNumPyに変換
        incorrect_total.append(incorrect)
        cnt += 1
    
    print("log=", my_algo.log)
    print("incorrect_total=", incorrect_total)
    end = time.perf_counter()
    print(end - start)

main()
