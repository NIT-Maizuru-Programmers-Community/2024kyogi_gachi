#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ
import sys
import os
# 相対パスを使用して一つ上の階層のパスを追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
from datetime import datetime
import copy
import numpy as np
import random
import board_reload_fujii
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
        self.now = copy.deepcopy(now_board)
        self.correct = correct_board

        def all_position():
            #すべての座標を探索
            recommended_action = [9999999, 0, 0, 0] #distance, cutter_num, [x, y], move_direction
            for y in range(self.height):
                for x in range(self.width):
                    
                    def check_pass_position(): #True: continue 
                        if random.random() > 0.2 or self.height * 0.7 < y:
                            return True
                        return False
                    
                    if check_pass_position():
                        continue
                    print("position=", x, y)
                    force_start = datetime.now()
                    min_distance_data =  self.force_search(x, y)
                    force_end = datetime.now()
                    print("force_time=", force_end - force_start)
                    #print("min_distance_data=", min_distance_data)
                    if recommended_action[0] > min_distance_data[0]:
                        recommended_action[0] = min_distance_data[0]
                        recommended_action[1] = min_distance_data[1] #cutter_num
                        recommended_action[2] = [x ,y]
                        recommended_action[3] = min_distance_data[2] #direction
            return [recommended_action[1], recommended_action[2], recommended_action[3], recommended_action[0]]
        
        recommended_action = all_position()
        self.log.append(recommended_action)

        return recommended_action

    #ある座標に対してスコアと最適な型と方向を求める
    def force_search(self, x, y):
        min_distance_data = [9999999, 0, 0] #distance, cutter_num, move_direction
        for cutter_num_1 in range(25 + self.special_cutter_quantity):
            if cutter_num_1 == 4:
                break
            cutter_height = self.cutter_size[cutter_num_1][0]
            cutter_width = self.cutter_size[cutter_num_1][1]
            if cutter_height > self.height and cutter_width > self.width:
                break

            for move_direction in range(4):
                if self.check_board_change([x, y], cutter_num_1, move_direction) == False: #変化のない操作はしないようにする
                    #print("skiped!!", "posi=", [x, y], "cutter=", cutter_num_1, "direction=", move_direction)
                    continue

                change_start = datetime.now()
                next_board = self.board_op.board_update(cutter_num_1, [x, y], move_direction, copy.deepcopy(self.now))
                change_end = datetime.now()
                print("change_time=", change_end - change_start)
                eval_start = datetime.now()
                total_distance = self.evaluation(next_board)
                eval_end = datetime.now()
                print("eval_time=", eval_end - eval_start)
                #print("total_distance=", total_distance)

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
        # else:
        #     next_board = self.board_op.board_update(cutter_num, position, direction, copy.deepcopy(self.now))
        #     if next_board == self.now:
        #         is_changed = False
        if is_changed == True:
            next_board = self.board_op.board_update(cutter_num, position, direction, copy.deepcopy(self.now))
            if next_board == self.now:
                is_changed = False
            
        return is_changed

    #すべてのセルの正解との距離を加算
    def evaluation(self, board):
        def find_closest_equal_value(board, target_value, x, y):
            # ターゲット値と等しいすべてのインデックスを取得
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
                find_start = datetime.now()
                val = self.correct[i][j]
                manhattan_distance = find_closest_equal_value(board, val, j, i)
                total_distance += manhattan_distance ** 4
                find_end = datetime.now()
                print("find_time=", find_end - find_start)
        
        return total_distance
    
    #型の種類を判別する
    def cutter_type(self, cutter_num): #0:すべて１, 1:横, 2:縦, 3:一般抜型
        if (cutter_num == 0 
                or cutter_num == 1 
                or cutter_num == 4 
                or cutter_num == 7 
                or cutter_num == 10 
                or cutter_num == 13
                or cutter_num == 16
                or cutter_num == 19
                or cutter_num == 22):
            return 0
        
        elif (cutter_num == 2
                or cutter_num == 5
                or cutter_num == 8
                or cutter_num == 11
                or cutter_num == 14
                or cutter_num == 17
                or cutter_num == 20
                or cutter_num == 23):
            return 1

        elif (cutter_num < 25):
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

    start_board, correct_board = create_random_board.create_board(20, 20)
    print(correct_board)

    height = len(start_board)
    width = len(start_board[0])
    my_algo = MyAlgo(height, width, 0, cutter_size)
    judge = J.Judgec()
    board_op = board_reload_fujii.BoardOperation()

    judge_result = False
    incorrect = height * width
    incorrect_total = []
    board = start_board
    cnt = 1
    score = 0
    next_score = score
    score_is_not_changed_cnt = 0

    while judge_result != True:
        print("cnt=", cnt)
        recommended_action = my_algo.algo(board, correct_board)
        print("recomm!=", recommended_action)
        cutter = recommended_action[0]
        posi = recommended_action[1]
        direction = recommended_action[2]
        next_score = recommended_action[3]

        if score != 0 and abs(score - next_score) <= 2 or incorrect < height * width / 3:
            score_is_not_changed_cnt += 1
            if score_is_not_changed_cnt == 5:
                break
        else:
            score_is_not_changed_cnt = 0
        score = next_score
        
        board = board_op.board_update(cutter, posi, direction, board)
        print("board=", board)
        judge_result, incorrect = judge.judge(board, correct_board)
        incorrect_total.append(incorrect)
        cnt += 1
    
    print("log=", my_algo.log)
    print("incorrect_total=", incorrect_total)
    end = time.perf_counter()
    print(end - start)

main()
