#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ

import clmatch_num
import clmatch
import array_send
import board_reload_fujii
import copy
import time


class karial(board_reload_fujii.BoardOperation):

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def algo(self,now_board,goal_board,cut_type,start_time):
        self.now_board=now_board
        self.goal_board=goal_board
        self.use_cut_type=cut_type
        self.start_time=start_time

        
        self.array_operate_board=[]#ここに操作を追加
        self.array_execution_time=[]#実行時間リスト
        self.operation_board = copy.deepcopy(self.now_board)
        

        for column in range(0,len(self.now_board)):
            #print(f"{column}層目")


            self.array_operation=array_send.column_row_send(self.operation_board,self.goal_board,column)#一致度高いやつ寄せる
            self.array_operate_board.extend(self.array_operation)
            #print(f"{self.array_operation}#一致度高いやつ寄せる")

            #実行時間の取得
            self.end = self.get_time()
            self.times=self.end-self.start_time
            if self.array_operation:
                for _ in range(len(self.array_operation)):
                    self.array_execution_time.append(self.times)
            #print(len(self.array_execution_time))

            for turn_num in range(0,len(self.array_operation)):#ボードの更新
                self.array_operation_position=[self.array_operation[turn_num][1],self.array_operation[turn_num][2]]
                self.operation_board=self.board_update(self.array_operation[turn_num][0], self.array_operation_position, self.array_operation[turn_num][3], self.operation_board)        
            #print(f"{self.operation_board}#一致度高いやつ寄せる盤面")


            self.is_element_correct=False
            self.height=len(self.goal_board)
            self.wide=len(self.goal_board[0])
            while self.is_element_correct==False:#各要素の個数をそろえる
                self.element_operation=clmatch_num.fitnum(self.operation_board,self.goal_board,column,self.wide,self.height)#ボード情報の取得


                
                # print(f"{len(self.array_execution_time)}self.element_operation")

                if self.element_operation ==True:
                    self.is_element_correct=self.element_operation
                else:
                    #実行時間の取得
                    self.end = self.get_time()
                    self.times=self.end-self.start_time
                    for _ in range(len(self.element_operation)):
                        self.array_execution_time.append(self.times)

                    self.array_operate_board.extend(self.element_operation)
                    #print(f"{self.element_operation}#各要素の個数をそろえる")
                    for turn_num in range(0,len(self.element_operation)):#ボードの更新
                        self.array_operation_position=[self.element_operation[turn_num][1],self.element_operation[turn_num][2]]
                        self.operation_board=self.board_update(self.element_operation[turn_num][0], self.array_operation_position, self.element_operation[turn_num][3], self.operation_board)
            
            #print(f"{self.operation_board}#各要素の個数をそろえる盤面")



            self.match_operation=clmatch.clmatch(self.operation_board,self.goal_board,column,self.wide,self.height)#順番を一致させる

            #実行時間の取得
            self.end = self.get_time()
            self.times=self.end-self.start_time
            if self.match_operation[0]:
                for _ in range(len(self.match_operation[0])):
                    self.array_execution_time.append(self.times)
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

        return (self.array_operate_board,self.array_execution_time)
