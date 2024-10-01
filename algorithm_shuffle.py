#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ



import clmatch_num_cutting
import clmatch_cutting
import array_send
import board_reload_fujii
import copy
import time



class algorithm_tentative(board_reload_fujii.BoardOperation):

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def algo(self,now_board,goal_board,cut_type,width,height):
        self.now_board=now_board
        self.goal_board=goal_board
        self.use_cut_type=cut_type
        self.height=height
        self.wide=width

        
        self.array_operate_board=[[24,0,0,1],[23,0,0,0]]#ここに操作を追加
        self.operation_board = copy.deepcopy(self.now_board)
        

        for column in range(0,len(self.now_board)):
            #print(f"{column}層目")


            self.array_operation=array_send.column_row_send(self.operation_board,self.goal_board,column)#一致度高いやつ寄せる
            self.array_operate_board.extend(self.array_operation)
            #print(f"{self.array_operation}#一致度高いやつ寄せる")

            
            #print(len(self.array_execution_time))

            for turn_num in range(0,len(self.array_operation)):#ボードの更新
                self.array_operation_position=[self.array_operation[turn_num][1],self.array_operation[turn_num][2]]
                self.operation_board=self.board_update(self.array_operation[turn_num][0], self.array_operation_position, self.array_operation[turn_num][3], self.operation_board)        
            #print(f"{self.operation_board}#一致度高いやつ寄せる盤面")


            #各要素の個数をそろえる
            self.element_operation=clmatch_num_cutting.fitnum(self.operation_board,self.goal_board,column,self.wide,self.height)#ボード情報の取得
            # print(f"{len(self.array_execution_time)}self.element_operation")
            self.array_operate_board.extend(self.element_operation[0])
            #print(f"{self.element_operation}#各要素の個数をそろえる")
            self.operation_board=copy.deepcopy(self.element_operation[1])



            
            
            #print(f"{self.operation_board}#各要素の個数をそろえる盤面")




            self.match_operation=clmatch_cutting.clmatch(self.operation_board,self.goal_board,column,self.wide)#順番を一致させる
            #self.match_operation=clmatch.clmatch(self.operation_board,self.goal_board,column,self.wide,self.height)#順番を一致させる

            
            # print(f"{len(self.array_execution_time)}self.match_operation")
            # print(f"{len(self.match_operation[0])}リストながさ")


            self.array_operate_board.extend(self.match_operation[0])
            #print(f"{self.match_operation}#順番を一致させる")
            # for turn_num in range(0,len(self.match_operation[0])):#ボードの更新
            #     self.array_operation_position=[self.match_operation[0][turn_num][1],self.match_operation[0][turn_num][2]]
            #     self.operation_board=self.board_update(self.match_operation[0][turn_num][0], self.array_operation_position, self.match_operation[0][turn_num][3], self.operation_board)
            self.operation_board=copy.deepcopy(self.match_operation[1])

            #print(f"{self.operation_board}#順番を一致させる盤面")

        #print(self.array_operate_board)
        #print(self.array_execution_time)

        return (self.array_operate_board)
