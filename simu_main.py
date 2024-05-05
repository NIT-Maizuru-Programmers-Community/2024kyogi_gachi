import judge
import general_patterns
import output
import time
import algorithm
import sys
import board_reload_fujii


class simu(judge.Judgec,board_reload_fujii.BoardOperation,algorithm.karial):

    def set(self,start_time,turn):
        self.correct_board=[[1,1,1,1,1,1],
                            [2,2,2,2,2,3],
                            [3,3,3,3,3,2],
                            [2,2,2,2,2,2],
                            [1,1,1,1,1,1]] #正解の盤面


        self.now_board=[[1,1,1,1,1,1],
                        [2,2,2,2,2,2],
                        [3,3,3,3,3,3],
                        [2,2,2,2,2,2],
                        [1,1,1,1,1,1]]#現在の盤面






        self.use_type=general_patterns.general_patterns_cells.copy()#使用できる抜き型
        self.start=start_time
        self.turn=turn

        self.relord_judge_log()

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def relord_judge_log(self):

        self.call_algotithm=self.algo(self.now_board,self.correct_board,self.use_type)

        self.end = self.get_time()

        self.cutter_position=[self.call_algotithm[1],self.call_algotithm[2]]#使用した座標
        self.relord_board=self.board_update(self.call_algotithm[0],self.cutter_position,self.call_algotithm[3],self.now_board)
        #処理後の盤面取得(use_type,zahyou,move_direc,before_board)
        self.correct=self.judge(self.relord_board,self.correct_board)#正誤判定

        self.now_board=self.relord_board.copy()#盤面書き換え
        self.times=self.end-self.start#実行時間

        output.log_output(self.relord_board,self.turn,self.times,self.call_algotithm[0],self.cutter_position,self.call_algotithm[3],self.correct[1])
        #relord_board,turn,time,use_type,use_coodenate,move_direc,TF

        if self.correct[1]==0:
             sys.exit()


start_time = time.time()#開始時間
simul=simu()
simul.set(start_time,1)