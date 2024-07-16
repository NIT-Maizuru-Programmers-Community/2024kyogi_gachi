#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ
import clmuch_num
import clmuch
import array_send
import board_reload_fujii

class karial(board_reload_fujii.BoardOperation):
    
    def algo(self,now_board,goal_board,cut_type):
        self.now=now_board
        self.goal=goal_board
        self.use_cut_type=cut_type



        
        self.operate_board=[]#ここに操作を追加
        self.operation_board=now_board

        for column in range(0,now_board):
            self.array_operation=array_send.column_row_send(now_board,goal_board,column)
            self.operate_board=self.operate_board.extend(self.array_operation)


            for turn_num in range(0,self.array_operation):
                self.array_operation_position=[self.array_operation[turn_num][1],self.array_operation[turn_num][2]]
                self.operation_board=self.board_update(self.array_operation[turn_num][0], self.array_operation_position, self.array_operation[turn_num][3], self.operation_board)




        

        return self.operate_board
