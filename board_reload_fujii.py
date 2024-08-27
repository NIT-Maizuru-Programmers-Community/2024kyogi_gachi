import numpy as np
import general_patterns

class BoardOperation:
    def __init__(self):
        # self.cutter = [
        #     [[1]],
        #     [[1, 1], [1, 1]],
        #     [[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
        #     [[1, 0], [1, 0]],
        #     [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
        #     ]
        self.cutter = general_patterns.general_patterns_cells

    def board_update(self, cutter_num, cutter_LU_posi, move_direction, board):
        self.cutter_num = cutter_num
        self.cutter_LU_posi = cutter_LU_posi #LU = left-upper
        self.move_direction = move_direction
        self.board = board
        self.cutter_data = np.array(self.cutter[self.cutter_num])

        #サイズを取得
        self.set_cutter_size()
        self.set_board_size()
        #型とボードの重なり方を調べる
        self.check_cover_case()
        #print(f"case={self.cover_case}")
        if(self.cutterPosi_is_error):
            print("cover case error!!")
        self.reshape_cutter_size()
        self.update_cutter_position()
        
        #ボードの操作
        self.change_board()

        #更新後のボードを出力
        return self.board

    def set_cutter_size(self): #型のサイズを取得
        self.cutter_size = [len(self.cutter[self.cutter_num][0]), 
                            len(self.cutter[self.cutter_num])]
    
    def set_board_size(self): #ボードのサイズを取得
        self.board_size = [len(self.board[0]), len(self.board)]
    
    def is_inside(self, position): #指定した型の座標がボード内か判定
        if(position[0] < 0 
                or position[1] < 0 
                or position[0] + 1 > self.board_size[0] 
                or position[1] + 1 > self.board_size[1]):
            return False
        else:
            return True

    def check_cover_case(self): #四隅がボード内かどうかを調べて型の位置を分類
        ctr_lu = self.cutter_LU_posi
        ctr_ll = [ctr_lu[0], ctr_lu[1] + self.cutter_size[1] - 1]
        ctr_ru = [ctr_lu[0] + self.cutter_size[0] - 1, ctr_lu[1]]
        ctr_rl = [ctr_ru[0], ctr_ru[1] + self.cutter_size[1] - 1]
        
        if(ctr_lu[0] < 0 and ctr_ll[0] < 0 and ctr_ru[0] < 0 and ctr_rl[0] < 0
                or ctr_lu[1] < 0 and ctr_ll[1] < 0 and ctr_ru[1] < 0 and ctr_rl[1] < 0
                or (ctr_lu[0] > self.board_size[0] - 1) and (ctr_ll[0] > self.board_size[0] - 1) and (ctr_ru[0] > self.board_size[0] - 1) and (ctr_rl[0] > self.board_size[0] - 1)
                or (ctr_lu[1] > self.board_size[1] - 1) and (ctr_ll[1] > self.board_size[1] - 1) and (ctr_ru[1] > self.board_size[1] - 1) and (ctr_rl[1] > self.board_size[1] - 1)):
            self.cutterPosi_is_error = True
        else:
            self.cutterPosi_is_error = False

    def reshape_cutter_size(self): #型のサイズを変更
        reshape_left = 0
        reshape_right = 0
        reshape_upper = 0
        reshape_lower = 0

        if(self.cutter_LU_posi[0] < 0): #上下左右それぞれどのぐらい削るかを算出
            reshape_left = self.cutter_LU_posi[0] * -1
        if(self.cutter_LU_posi[0] + self.cutter_size[0] - 1 > self.board_size[0] - 1):
            reshape_right = (self.cutter_LU_posi[0] + self.cutter_size[0] - 1) - (self.board_size[0] - 1)
        if(self.cutter_LU_posi[1] < 0):
            reshape_upper = self.cutter_LU_posi[1] * -1
        if(self.cutter_LU_posi[1] + self.cutter_size[1] - 1 > self.board_size[1] - 1):
            reshape_lower = (self.cutter_LU_posi[1] + self.cutter_size[1] - 1) - (self.board_size[1] - 1)

        self.cutter_data = self.cutter_data[reshape_upper:self.cutter_size[1] - reshape_lower, 
                                            reshape_left:self.cutter_size[0] - reshape_right]
        self.cutter_size = [len(self.cutter_data[0]), len(self.cutter_data)]

    def update_cutter_position(self): #型の指定位置を更新
        if(self.cutter_LU_posi[0] < 0):
            self.cutter_LU_posi[0] = 0
        if(self.cutter_LU_posi[1] < 0):
            self.cutter_LU_posi[1] = 0

    def change_board(self): #型を適用してボードを更新
        def get_board_data(position): #ボードの指定した座標にある値を返す
            return self.board[position[1]][position[0]]
        
        def get_cutter_data(position): #型の指定した座標にある値を返す
            return self.cutter_data[position[1]][position[0]]
        
        def change_board_data(position, data): #ボードの値を変更する              
            self.board[position[1]][position[0]] = data

        def distination_posi(position, rate):
            if(self.move_direction == 0):
                xy = [0, -1]
            elif(self.move_direction == 1):
                xy = [0, 1]
            elif(self.move_direction == 2):
                xy = [-1, 0]
            else:
                xy = [1, 0]
            return [position[0] + xy[0] * rate, position[1] + xy[1] * rate]

        direction_upper = 0
        direction_lower = 1

        if(self.move_direction == direction_upper or self.move_direction == direction_lower):
            is_xy = True #走査が縦方向かどうか
            cutter_first_direction = self.cutter_size[0]
            cutter_second_direction = self.cutter_size[1]
        else:
            is_xy = False
            cutter_first_direction = self.cutter_size[1]
            cutter_second_direction = self.cutter_size[0]

        pickup_data = [] #型の1の場所を抜き取る
        for i in range(cutter_first_direction):
            for j in range(cutter_second_direction):
                if(is_xy and get_cutter_data([i, j]) == 1):
                    board_position = [self.cutter_LU_posi[0] + i, self.cutter_LU_posi[1] + j]
                    pickup_data.append(get_board_data(board_position))
                    change_board_data(board_position, 4) #抜き取った位置をマーク=4
                elif(not is_xy and get_cutter_data([j, i]) == 1):
                    board_position = [self.cutter_LU_posi[0] + j, self.cutter_LU_posi[1] + i]
                    pickup_data.append(get_board_data(board_position))
                    change_board_data(board_position, 4) #抜き取った位置をマーク=4

        if(is_xy): #上下左右の指定によって走査する方向を決定する
            board_first_start = self.cutter_LU_posi[0]
            board_first_direction = self.cutter_size[0] + self.cutter_LU_posi[0]
            board_line_size = self.board_size[1]
        else:
            board_first_start = self.cutter_LU_posi[1]
            board_first_direction = self.cutter_size[1] + self.cutter_LU_posi[1]
            board_line_size = self.board_size[0]
        if(self.move_direction == 0 or self.move_direction == 2):
            if(is_xy):
                board_second_end = self.board_size[1]
            else:
                board_second_end = self.board_size[0]
            board_second_start = 0
            board_second_step = 1
        else:
            if(is_xy):
                board_second_start = self.board_size[1] - 1
            else:
                board_second_start = self.board_size[0] - 1
            board_second_end = -1
            board_second_step = -1

        for i in range(board_first_start, board_first_direction): #上下左右に寄せて空いたところを埋める
            hole_count = 0
            if(is_xy):
                x = i
            else:
                y = i

            for j in range(board_second_start, board_second_end, board_second_step): #上下左右に寄せて空いたところをマークする
                if(is_xy):
                    y = j
                else:
                    x = j

                data = get_board_data([x, y])
                #print(f"posi=[{x},{y}], data={self.board}")
                if(data == 4):
                    hole_count += 1
                    change_board_data([x, y], 5) #移動済みをマーク=5
                elif(hole_count != 0):
                    new_position = distination_posi([x, y], hole_count)
                    if(self.is_inside(new_position)):
                        change_board_data(new_position, data)
                        change_board_data([x, y], 5) #移動済みをマーク=5
                    else:
                        break
            #print(self.board)
            for line in range(board_line_size): #空いているところを埋める
                if(is_xy):
                    y = line
                else:
                    x = line
                if(get_board_data([x, y]) == 5):
                    change_board_data([x, y], pickup_data.pop(0))

# test_board = [
#     [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
#     [2, 2, 2, 2]
# ]
# test = BoardOperation()
# board = test.board_update(1, [0, 0], 0, test_board)
# print(board)