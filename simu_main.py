import judge
import general_patterns
import output
import time
import algorithm
import board_reload_fujii
import numpy as np


class simu(judge.Judgec,algorithm.algorithm_tentative,board_reload_fujii.BoardOperation):

    def set(self):
        first_board = np.random.randint(0, 4, (256, 256))
        self.correct_board=first_board.tolist() #正解の盤面
        shuffled_elements = np.random.permutation(first_board.flatten())
        second_board = shuffled_elements.reshape(256, 256)
        self.now_board=second_board.tolist() #現在の盤面
        self.use_type=general_patterns.general_patterns_cells.copy()#使用できる抜き型

        self.relord_judge_log()

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def relord_judge_log(self):

        self.start_time = time.time()#開始時間
        self.call_algotithm=self.algo(self.now_board,self.correct_board,self.use_type)#アルゴリズム呼び出し,
        self.end_time = time.time()#終了時間
        print(f"{len(self.call_algotithm)}手かかりました")


        #print(self.now_board)
        for turn in range(1,len(self.call_algotithm)+1):
            #self.end = self.get_time()
            self.turn_algorithm=self.call_algotithm[turn-1]#そのターンの操作

            self.cutter_position=[self.turn_algorithm[1],self.turn_algorithm[2]]#使用した座標

            self.relord_board=self.board_update(self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.now_board)
            #処理後の盤面取得( cutter_num, cutter_LU_posi, move_direction, board):
            #print(f"{self.relord_board}self.relord_board")

            self.correct=self.judge(self.relord_board,self.correct_board)#正誤判定

            self.now_board=self.relord_board.copy()#盤面書き換え
            
            self.time=self.end_time-self.start_time
            #実行時間

            output.log_output(self.relord_board,turn,self.time,self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.correct[1])
            #relord_board,turn,time,use_type,use_coodenate,move_direc,TF

        



simul=simu()
simul.set()