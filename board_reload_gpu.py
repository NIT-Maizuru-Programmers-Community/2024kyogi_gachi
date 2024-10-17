import cupy as cp
import general_patterns

class BoardOperation:
    def __init__(self):
        self.cutter = general_patterns.general_patterns_cells

    def board_update(self, cutter_num, cutter_LU_posi, move_direction, board):
        self.cutter_num = cutter_num
        self.cutter_LU_posi = cutter_LU_posi  # LU = left-upper
        self.move_direction = move_direction
        self.board = board  # cupy配列で受け取る
        self.cutter_data = cp.array(self.cutter[self.cutter_num])

        # サイズを取得
        self.set_cutter_size()
        self.set_board_size()
        # 型とボードの重なり方を調べる
        self.check_cover_case()

        if self.cutterPosi_is_error:
            print("cover case error!!")
            return self.board  # エラーの場合、変更せず元のボードを返す

        self.reshape_cutter_size()
        self.update_cutter_position()

        # ボードの操作
        self.change_board()

        # 更新後のボードを返す（cupy配列）
        return self.board

    def set_cutter_size(self):
        # 型のサイズを取得
        self.cutter_size = [len(self.cutter[self.cutter_num][0]), len(self.cutter[self.cutter_num])]

    def set_board_size(self):
        # ボードのサイズを取得
        self.board_size = [self.board.shape[1], self.board.shape[0]]

    def is_inside(self, position):
        # 指定した型の座標がボード内か判定（cupy対応）
        return not (position[0] < 0 or position[1] < 0 
                    or position[0] + 1 > self.board_size[0] 
                    or position[1] + 1 > self.board_size[1])

    def check_cover_case(self):
        # 型の四隅がボード内かどうかを調べて分類
        ctr_lu = self.cutter_LU_posi
        ctr_ll = [ctr_lu[0], ctr_lu[1] + self.cutter_size[1] - 1]
        ctr_ru = [ctr_lu[0] + self.cutter_size[0] - 1, ctr_lu[1]]
        ctr_rl = [ctr_ru[0], ctr_ru[1] + self.cutter_size[1] - 1]

        if (ctr_lu[0] < 0 and ctr_ll[0] < 0 and ctr_ru[0] < 0 and ctr_rl[0] < 0
                or ctr_lu[1] < 0 and ctr_ll[1] < 0 and ctr_ru[1] < 0 and ctr_rl[1] < 0
                or ctr_lu[0] > self.board_size[0] - 1 and ctr_ll[0] > self.board_size[0] - 1
                or ctr_lu[1] > self.board_size[1] - 1 and ctr_ll[1] > self.board_size[1] - 1):
            self.cutterPosi_is_error = True
        else:
            self.cutterPosi_is_error = False

    def reshape_cutter_size(self):
        # 型のサイズを変更
        reshape_left = max(-self.cutter_LU_posi[0], 0)
        reshape_right = max(self.cutter_LU_posi[0] + self.cutter_size[0] - self.board_size[0], 0)
        reshape_upper = max(-self.cutter_LU_posi[1], 0)
        reshape_lower = max(self.cutter_LU_posi[1] + self.cutter_size[1] - self.board_size[1], 0)

        self.cutter_data = self.cutter_data[reshape_upper:self.cutter_size[1] - reshape_lower,
                                            reshape_left:self.cutter_size[0] - reshape_right]
        self.cutter_size = [self.cutter_data.shape[1], self.cutter_data.shape[0]]

    def update_cutter_position(self):
        # 型の指定位置を更新
        self.cutter_LU_posi[0] = max(self.cutter_LU_posi[0], 0)
        self.cutter_LU_posi[1] = max(self.cutter_LU_posi[1], 0)

    def change_board(self):
        # 型を適用してボードを更新 (cupy版)
        def get_board_data(position):
            # cupy配列から指定した座標にある値を返す
            return self.board[position[1], position[0]]

        def get_cutter_data(position):
            # 型の指定した座標にある値を返す
            return self.cutter_data[position[1], position[0]]

        def change_board_data(position, data):
            # ボードの値を変更する
            self.board[position[1], position[0]] = data

        def distination_posi(position, rate):
            if self.move_direction == 0:
                xy = [0, -1]
            elif self.move_direction == 1:
                xy = [0, 1]
            elif self.move_direction == 2:
                xy = [-1, 0]
            else:
                xy = [1, 0]
            return [position[0] + xy[0] * rate, position[1] + xy[1] * rate]

        # pickup_dataをcupyで処理
        pickup_data = []
        for i in range(self.cutter_size[0]):
            for j in range(self.cutter_size[1]):
                if get_cutter_data([i, j]) == 1:
                    board_position = [self.cutter_LU_posi[0] + i, self.cutter_LU_posi[1] + j]
                    pickup_data.append(get_board_data(board_position))
                    change_board_data(board_position, 4)  # マーク=4

        # 寄せて空いたところを埋める（cupy対応）
        for i in range(self.cutter_LU_posi[0], self.cutter_LU_posi[0] + self.cutter_size[0]):
            hole_count = 0
            for j in range(self.cutter_LU_posi[1], self.cutter_LU_posi[1] + self.cutter_size[1]):
                data = get_board_data([i, j])
                if data == 4:
                    hole_count += 1
                    change_board_data([i, j], 5)
                elif hole_count != 0:
                    new_position = distination_posi([i, j], hole_count)
                    if self.is_inside(new_position):
                        change_board_data(new_position, data)
                        change_board_data([i, j], 5)

        # 空いているところを埋める
        for i in range(len(pickup_data)):
            x, y = divmod(i, self.cutter_size[0])
            if get_board_data([x, y]) == 5:
                change_board_data([x, y], pickup_data[i])

# 使用例: cupy配列でボードを生成し、計算を行う
# test_board = cp.array([
#     [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
#     [2, 2, 2, 2]
# ])
# test = BoardOperation()
# board = test.board_update(1, [0, 0], 0, test_board)
# print(cp.asnumpy(board))  # CPU上で確認するためにnumpy配列に戻して出力
