import judge
import general_patterns
import output
import time
import algorithm
import board_reload_fujii


class simu(judge.Judgec,algorithm.karial,board_reload_fujii.BoardOperation):

    def set(self):
        self.correct_board=[[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]#正解の盤面
        self.now_board=[[1,1,1],[2,2,2],[3,3,3],[1,1,1],[2,2,2],[3,3,3]]#現在の盤面
        self.use_type=general_patterns.general_patterns_cells.copy()#使用できる抜き型

        self.relord_judge_log()

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def relord_judge_log(self):

        self.start_time = time.time()#開始時間
        self.call_algotithm_time=self.algo(self.now_board,self.correct_board,self.use_type,self.start_time)#アルゴリズム呼び出し
        #print(self.call_algotithm_time[0])

        #print(self.now_board)
        for turn in range(1,len(self.call_algotithm_time[0])+1):
            #self.end = self.get_time()
            self.turn_algorithm=self.call_algotithm_time[0][turn-1]#そのターンの操作

            self.cutter_position=[self.turn_algorithm[1],self.turn_algorithm[2]]#使用した座標

            self.relord_board=self.board_update(self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.now_board)
            #処理後の盤面取得( cutter_num, cutter_LU_posi, move_direction, board):
            #print(f"{self.relord_board}self.relord_board")

            self.correct=self.judge(self.relord_board,self.correct_board)#正誤判定

            self.now_board=self.relord_board.copy()#盤面書き換え
            

            self.times=self.call_algotithm_time[1][turn-1]
            #実行時間

            output.log_output(turn,self.times,self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.correct[1])
            #relord_board,turn,time,use_type,use_coodenate,move_direc,TF

        



simul=simu()
simul.set()