import numpy as np

class BoardOperation:
    def __init__(self):
        self.cutter = [
            [[1]],
            [[1, 1], [1, 1]],
            [[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]]
            ]

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
        if(self.cover_case == 10):
            print("cover case error")
        elif(self.cover_case != 0):
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

    def check_cover_case(self): #四隅がボード内かどうかを調べて型の位置を分類
        def is_inside(position): #指定した型の座標がボード内か判定
            if(position[0] < 0 
                    or position[1] < 0 
                    or position[0] + 1 > self.board_size[0] 
                    or position[1] + 1 > self.board_size[1]):
                return False
            else:
                return True
            
        inside = [True, True, True, True]
        over_left_upper = [False, False, False, True]
        over_left_lower = [False, True, False, False]
        over_right_upper = [False, False, True, False]
        over_right_lower = [True, False, False, False]
        over_upper = [False, False, True, True]
        over_lower = [True, True, False, False]
        over_left = [False, True, False, True]
        over_right = [True, False, True, False]

        corners_is_inside = []
        corners_is_inside.append(is_inside(self.cutter_LU_posi)) #左上

        corners_is_inside.append(is_inside([self.cutter_LU_posi[0] + self.cutter_size[0] - 1, 
                                            self.cutter_LU_posi[1]])) #右上
        
        corners_is_inside.append(is_inside([self.cutter_LU_posi[0], 
                                            self.cutter_LU_posi[1] + self.cutter_size[1] - 1])) #左下
        
        corners_is_inside.append(is_inside([self.cutter_LU_posi[0] + self.cutter_size[0] - 1,
                                            self.cutter_LU_posi[1] + self.cutter_size[1] - 1])) #右下

        if(corners_is_inside == inside):
            self.cover_case = 0
        elif(corners_is_inside == over_left_upper):
            self.cover_case = 1
        elif(corners_is_inside == over_left_lower):
            self.cover_case = 2
        elif(corners_is_inside == over_right_upper):
            self.cover_case = 3
        elif(corners_is_inside == over_right_lower):
            self.cover_case = 4
        elif(corners_is_inside == over_upper):
            self.cover_case = 5
        elif(corners_is_inside == over_lower):
            self.cover_case = 6
        elif(corners_is_inside == over_left):
            self.cover_case = 7
        elif(corners_is_inside == over_right):
            self.cover_case = 8
        elif(self.cutter_LU_posi[0] < 0 
                and self.cutter_LU_posi[0] + self.cutter_size[0] - 1 > self.board_size[0]
                and self.cutter_LU_posi[1] < 0
                and self.cutter_LU_posi[1] + self.cutter_size[1] - 1 > self.board_size[1]):
            self.cover_case = 9 #すべて覆い、ボードより大きい
        else:
            self.cover_case = 10 #かぶり箇所無し

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
        if(self.cover_case == 1):
            self.cutter_LU_posi = [0, 0]
        elif(self.cover_case == 2):
            self.cutter_LU_posi = [0, self.cutter_LU_posi[1]]
        elif(self.cover_case == 3):
            self.cutter_LU_posi = [self.cutter_LU_posi[0], 0]
        elif(self.cover_case == 4):
            self.cutter_LU_posi = self.cutter_LU_posi #変更なし
        elif(self.cover_case == 5):
            self.cutter_LU_posi = [self.cutter_LU_posi[0], 0]
        elif(self.cover_case == 6):
            self.cutter_LU_posi = self.cutter_LU_posi #変更なし
        elif(self.cover_case == 7):
            self.cutter_LU_posi = [0, self.cutter_LU_posi[1]]
        elif(self.cover_case == 8):
            self.cutter_LU_posi = self.cutter_LU_posi #変更なし
        elif(self.cover_case == 9):
            self.cutter_LU_posi = [0, 0]

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
                if(get_cutter_data([i, j]) == 1):
                    if(is_xy):
                        board_position = [self.cutter_LU_posi[0] + i, self.cutter_LU_posi[1] + j]
                    else:
                        board_position = [self.cutter_LU_posi[0] + j, self.cutter_LU_posi[1] + i]
                    pickup_data.append(get_board_data(board_position))
                    change_board_data(board_position, 4) #抜き取った位置をマーク=4

        if(is_xy):
            board_first_direction = self.cutter_size[0] + self.cutter_LU_posi[0]
            board_second_direction = self.board_size[1]
        else:
            board_first_direction = self.cutter_size[1] + self.cutter_LU_posi[1]
            board_second_direction = self.board_size[0]

        for i in range(board_first_direction): #上下左右に寄せて空いたところを埋める
            hole_count = 0
            for j in range(board_second_direction): #上下左右に寄せて空いたところをマークする
                data = get_board_data([i, j])
                if(data == 4):
                    hole_count += 1
                    change_board_data([i, j], 5) #移動済みをマーク=5
                elif(hole_count != 0):
                    change_board_data(distination_posi([i, j], hole_count), data)
                    change_board_data([i, j], 5) #移動済みをマーク=5

            for j in range(board_second_direction): #空いているところを埋める
                if(get_board_data([i, j]) == 5):
                    change_board_data([i, j], pickup_data.pop(0))

test_board = [
    [0, 1, 2],
    [3, 0, 1],
    [1, 2, 1]
]
test = BoardOperation()
board = test.board_update(2, [0, 0], 2, test_board)
print(board)