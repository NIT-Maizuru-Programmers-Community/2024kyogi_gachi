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
    def __init__(self, board_height, board_width, special_cutter_quantity, cutter_size, correct_board) -> None:
        self.height = board_height
        self.width = board_width
        self.cutter_size = cutter_size
        self.special_cutter_quantity = special_cutter_quantity
        self.correct = correct_board
        self.board_op = board_reload_fujii.BoardOperation()
        self.log = []
    
    def algo(self, now_board, row):
        self.now = copy.deepcopy(now_board)
        self.row = row

        if self.correct[self.row] == self.now[self.row + 1]:
            return self.now, True

        def all_position():
            #すべての座標を探索
            recommended_action = [0, 0, [0, 0], 0] #distance, cutter_num, [x, y], move_direction
            for y in range(self.row, self.height):
                if y > self.row + 1:
                    continue
                for x in range(self.width):
                    
                    # print("position=", x, y)
                    #force_start = datetime.now()
                    max_correct_data =  self.force_search(x, y)
                    #print("min_distance_data= ", max_correct_data)
                    #force_end = datetime.now()
                    #print("force_time=", force_end - force_start)
                    #print("min_distance_data=", min_distance_data)
                    if recommended_action[0] < max_correct_data[0]:
                        recommended_action[0] = max_correct_data[0]
                        recommended_action[1] = max_correct_data[1] #cutter_num
                        recommended_action[2] = [x ,y]
                        recommended_action[3] = max_correct_data[2] #direction

            return [recommended_action[1], recommended_action[2], recommended_action[3], recommended_action[0]]

        def fill_blanks(now_board, log):
            def move_correct_y(x, y, target_y, next_board, log):
                dir_up = 0
                cutter_list, is_zero_distance = move_y(y, target_y)
                print("cutter list=", cutter_list, is_zero_distance)
                #y方向に1 or 2つ手前まで移動
                for cutter_size in cutter_list:
                    print("cutter_size= ", cutter_size)
                    cutter_num = self.search_cutter(cutter_size)
                    posi = [x, self.row + 2]
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                
                if is_zero_distance:
                    #y方向に1つ上に移動
                    posi = [x, self.row + 1]
                    cutter_num = 0
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                else:
                    #y方向に2つ上に移動
                    posi = [x, self.row + 1]
                    cutter_num = 3
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                return next_board, log
            
            def move_correct_y2(x, y, target_y, next_board, log):
                dir_up = 0
                cutter_list, is_zero_distance = move_y(y, target_y)
                print("cutter list=", cutter_list, is_zero_distance)
                #y方向に1 or 2つ手前まで移動
                for cutter_size in cutter_list:
                    print("cutter_size= ", cutter_size)
                    cutter_num = self.search_cutter(cutter_size)
                    posi = [x, self.row + 2]
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                
                if is_zero_distance:
                    #y方向に1つ上に移動
                    posi = [x, self.row]
                    cutter_num = 0
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                else:
                    #y方向に2つ上に移動
                    posi = [x, self.row]
                    cutter_num = 3
                    next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                    log.append([cutter_num, posi, dir_up])
                return next_board, log
            
            def move_y(y, target_y):
                print("y= ", y)
                print("target_y= ", target_y)
                #ターゲットの座標との間のセル数を算出
                distance_y = target_y - y - 1
                cutter_list = []
                while True:
                    cutter_size = 1

                    if distance_y <= 1:
                        if distance_y == 0:
                            is_zero_distance = True
                        else:
                            is_zero_distance = False
                        return cutter_list, is_zero_distance
                    
                    while distance_y >= cutter_size:
                        #print("cutter_size= ", cutter_size)
                        #print("distance_y", distance_y)
                        cutter_size *= 2

                    cutter_size /= 2
                    distance_y -= cutter_size
                    if cutter_size != 0:
                        cutter_list.append(int(cutter_size))
            
            def move_x_y(board, log, x, y, correct_line_num):
                next_board = board
                target_position = self.find_closest_equal_value(board, correct_line_num, x, y)
                #print("target posi= ", target_position)
                if target_position != None:
                    target_x = target_position[0]
                    target_y = target_position[1]
                    print("target posi=", target_position, target_x)
                    rlt = self.move_x(x, target_x)
                    if rlt != None:
                        posi_x = rlt[0]
                        dir = rlt[1]
                        posi = [posi_x, target_y]
                        cutter_num = 23 #上の行がすべて１の256
                        next_board = self.board_op.board_update(cutter_num, posi, dir, copy.deepcopy(board))
                        print("moved X board=", next_board)
                        log.append([cutter_num, posi, dir])
                    
                    print("before correct_move_y")
                    next_board, log = move_correct_y(x, y, target_y, next_board, log)
                    print("moved Y board=", next_board)
                    print("after correct_move_y")
                    cant_find_val = False
                else:
                    cant_find_val = True
                    next_board = board
                return [next_board, log, cant_find_val]
            
            def move_x_y2(x, y, board, log, correct_line_num):
                target_position = self.find_closest_equal_value(board, correct_line_num, x, y)
                if target_position != None:
                    target_x = target_position[0]
                    target_y = target_position[1]
                    rlt = self.move_x(x, target_x)
                    if rlt != None:
                        posi_x = rlt[0]
                        dir = rlt[1]
                        posi = [posi_x, target_y]
                        cutter_num = 23 #上の行がすべて１の256
                        next_board = self.board_op.board_update(cutter_num, posi, dir, copy.deepcopy(board))
                        #print([cutter_num, posi, dir])
                        log.append([cutter_num, posi, dir])
                    else:
                        next_board = board
                    #その行まで移動
                    next_board, log = move_correct_y2(x, y, target_y, next_board, log)
                    print(next_board)
                else:
                    print("no target")
                    posi = [x, y]
                    dir = 0
                    cutter_num = 0
                    next_board = self.board_op.board_update(cutter_num, posi, dir, copy.deepcopy(board))
                return [next_board, log]

            before_line_num = self.row + 1
            now_line = now_board[before_line_num]
            upper_line = now_board[self.row]
            correct_line = self.correct[self.row]

            #log = [] #cutter, posi, dir
            next_board = copy.deepcopy(now_board)
            cant_find_val = False
            #各列
            for column in range(self.width):
                print("fill column= ", column)
                if now_line[column] == correct_line[column]:
                    continue
                print("not skip")
                next_board, log, cant_find_val = move_x_y(next_board, log, column, before_line_num, correct_line[column])

            #y方向に1行入れ替え
            dir_up = 0
            next_board = self.board_op.board_update(23, [0, self.row], dir_up, copy.deepcopy(next_board))
            log.append([23, [0, self.row], dir_up])

            if cant_find_val == True:
                print("cant find val = True")
                while upper_line != correct_line:
                    print("cant find loop")
                    for column in range(self.width):
                        if upper_line[column] == correct_line[column]:
                            continue
                        next_board, log = move_x_y2(column, self.row, next_board, log, correct_line[column])
                        upper_line = next_board[self.row]
            return [next_board, log]
        
        all_posi_start = datetime.now()
        recommended_action = all_position()
        all_posi_end = datetime.now()
        print("all_posi_time=", all_posi_end - all_posi_start)

        first_maching_cells = self.evaluation(copy.deepcopy(self.now))
        print("recommended_action[3]= ", recommended_action[3])
        print("first_maching_cells= ", first_maching_cells)
        if first_maching_cells >= recommended_action[3] - 1:
            fill_start = datetime.now()
            next_board, self.log = fill_blanks(copy.deepcopy(self.now), self.log)
            fill_end = datetime.now()
            print("fill_time=", fill_end - fill_start)
            has_line_cmped = True
            print("filled")
        else:
            print("recommended", recommended_action)
            next_board = self.board_op.board_update(recommended_action[0], recommended_action[1], recommended_action[2], copy.deepcopy(self.now))
            self.log.append(recommended_action[0:3])
            if recommended_action[3] == self.width:
                #y方向に1行入れ替え
                dir_up = 0
                cutter_num = 23
                posi = [0, self.row]
                next_board = self.board_op.board_update(cutter_num, posi, dir_up, copy.deepcopy(next_board))
                self.log.append([cutter_num, posi, dir_up])
                has_line_cmped = True
            else:
                has_line_cmped = False
            print("recommend")

        #print("a-log= ", self.log)
        return next_board, has_line_cmped

    #ある座標に対してスコアと最適な型と方向を求める
    def force_search(self, x, y):
        min_distance_data = [0, 0, 0] #distance, cutter_num, move_direction
        for cutter_num_1 in range(25 + self.special_cutter_quantity):
            cutter_height = self.cutter_size[cutter_num_1][0]
            cutter_width = self.cutter_size[cutter_num_1][1]
            #行、列がはみ出す場合はスキップ
            if cutter_height > self.height - self.row or cutter_width > self.width:
                break

            for move_direction in range(4):
                if move_direction == 1:
                    continue
                if self.check_board_change([x, y], cutter_num_1, move_direction) == False: #変化のない操作はしないようにする
                    #print("skiped!!", "posi=", [x, y], "cutter=", cutter_num_1, "direction=", move_direction)
                    continue
                if move_direction != 0 and self.cutter_type(cutter_num_1) == 2 and cutter_num_1 != 3 and cutter_num_1 != 6:
                    continue


                # change_start = datetime.now()
                next_board = self.board_op.board_update(cutter_num_1, [x, y], move_direction, copy.deepcopy(self.now))
                # change_end = datetime.now()
                # print("change_time=", change_end - change_start)
                # eval_start = datetime.now()
                maching_cells = self.evaluation(next_board)
                #print("maching_cells= ", maching_cells)
                # eval_end = datetime.now()
                # print("eval_time=", eval_end - eval_start)
                #print("total_distance=", total_distance)

                if min_distance_data[0] < maching_cells:
                    min_distance_data[0] = maching_cells
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

    #特定の行でそろっている数を調べる
    def evaluation(self, new_board):
        correct_line = self.correct[self.row]
        new_line = new_board[self.row + 1]

        cnt = 0
        for i in range(len(correct_line)):
            if correct_line[i] == new_line[i]:
                cnt += 1
        return cnt

    def search_cutter(self, cutter_scale):#抜き型の番号決める
        #抜き型番号の決定
        if cutter_scale==128:
            return 21
        
        elif cutter_scale==64:
            return 18
        
        elif cutter_scale==32:
            return 15
        
        elif cutter_scale==16:
            return 12
        
        elif cutter_scale==8:
            return 9
        
        elif cutter_scale==4:
            return 6
        
        elif cutter_scale==2:
            return 3
        
        elif cutter_scale==1:
            return 0
    
    #x方向に動かす
    def move_x(self, x, target_x):
        print("x target_x= ", x, target_x)
        if x == target_x:
            return None
        
        if x < target_x:
            pos_x = -1 * (256 - (target_x - x))
            dir = 2
        elif x > target_x:
            pos_x = self.width - (x - target_x)
            dir = 3
        print("move X= ", pos_x, dir)
        return [pos_x, dir]



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
        
    
    def find_closest_equal_value(self, board, target_value, x, y):
        # ボードのサイズ
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        # 探索する距離の増加量を1ずつ増やしていく
        distance = 0
        # 訪問済みの位置を追跡するための集合
        visited = set()
        # 初期位置をキューに追加
        queue = [(x, y)]
        
        while queue:
            next_queue = []
            # 現在の距離に対応する全ての位置を探索
            for cx, cy in queue:
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                # ボードの範囲外の場合は無視
                if cx < 0 or cy < 0 or cx >= cols or cy >= rows:
                    continue
                # ターゲット値に一致する場合、その座標を返す
                if board[cy][cx] == target_value and cy > y:
                    return (cx, cy)
                # 次の距離で探索するための位置を追加
                next_queue.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])
            # 探索距離を1増やす
            distance += 1
            queue = next_queue
        # ターゲット値が見つからない場合は None を返す
        return None
    
    def move_final_row(self, board):
        def move_final_x(x, target_x):
            print("x= ", x)
            print("target_x= ", target_x)
            #ターゲットの座標との間のセル数を算出
            distance_x = target_x - x
            cutter_list = []
            while True:
                cutter_size = 1

                if distance_x == 0:
                    return cutter_list
                
                while distance_x >= cutter_size:
                    #print("cutter_size= ", cutter_size)
                    #print("distance_y", distance_y)
                    cutter_size *= 2

                cutter_size /= 2
                distance_x -= cutter_size
                if cutter_size != 0:
                    cutter_list.append(int(cutter_size))

        next_board = board
        correct_final_line = self.correct[self.height - 1]

        for column in range(self.width):
            correct_val = correct_final_line[column]
            now_final_line = next_board[self.height - 1]
            now_val = now_final_line[column]
            if correct_val == now_val:
                continue

            target_column = column
            target_val = now_val
            print("correct_final_line= ", correct_final_line)
            print("now_final_line= ", now_final_line)
            while correct_val != target_val:
                target_column += 1
                target_val = now_final_line[target_column]
            
            cutter_list = move_final_x(column, target_column)
            print("cutter_list= ", cutter_list)
            for cutter_size in cutter_list:
                cutter_num = self.search_cutter(cutter_size)
                if cutter_num != 0:
                    cutter_num -= 1
                print("cutter_num", cutter_num)
                posi = [column, self.height - 1]
                dir = 2
                next_board = self.board_op.board_update(cutter_num, posi, dir, copy.deepcopy(next_board))
                print("next_board= ", next_board)
                self.log.append([cutter_num, posi, dir])
        return next_board


def main():
    main_start = datetime.now()

    cutters = general_patterns.general_patterns_cells
    cutter_size = []
    for i in range(len(cutters)):
        height = len(cutters[i])
        width = len(cutters[i][0])
        cutter_size.append([height, width])

    start_board, correct_board = create_random_board.create_board(32, 32)
    print(correct_board)

    height = len(start_board)
    width = len(start_board[0])
    my_algo = MyAlgo(height, width, 0, cutter_size, correct_board)
    judge = J.Judgec()
    board_op = board_reload_fujii.BoardOperation()
    board = start_board

    
    for row in range(height-1):
        has_line_cmped = False
        while has_line_cmped == False:
            print("row= ", row)
            next_board, has_line_cmped = my_algo.algo(board, row)
            board = next_board
            print("now board=", board)
    board = my_algo.move_final_row(board)
    
    main_end = datetime.now()

    print("log=", my_algo.log)
    print("ans_board=", board)
    print("correct_board=", correct_board)
    rlt, _ = judge.judge(board, correct_board)
    if rlt == True:
        print("OK")
    else:
        print("NG")
    print("number-of-times= ", len(my_algo.log))
    print("main-time=", main_end - main_start)

main()