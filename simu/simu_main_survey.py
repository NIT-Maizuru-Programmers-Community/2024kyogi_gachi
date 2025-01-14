import simu.judge as judge
import standard_patterns
import simu.output as output
import time
import simu.algorithm_survey as algorithm_survey
import board_reload_fujii
import numpy as np



#logへの出力を無くしたバージョン
#どこに何手かかったかを見やすく
#継承するクラスのファイル名を変更してアルゴリズム変更
class simu(judge.Judgec,algorithm_survey.algorithm_tentative,board_reload_fujii.BoardOperation):

    def set(self):
        first_board = np.random.randint(0, 4, (50, 50))
        self.correct_board=first_board.tolist() #正解の盤面

        shuffled_elements = np.random.permutation(first_board.flatten())
        second_board = shuffled_elements.reshape(50, 50)
        self.now_board=second_board.tolist() #現在の盤面

        self.wide=len(self.correct_board[0])
        self.height=len(self.correct_board)
        self.use_type=standard_patterns.standard_patterns_cells.copy()#使用できる抜き型

        self.relord_judge_log()

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def relord_judge_log(self):

        self.start_time = time.time()#開始時間
        self.call_algotithm=self.algo(self.now_board,self.correct_board,self.use_type,self.wide,self.height)#アルゴリズム呼び出し
        self.end_time = time.time()#終了時間
        self.time=self.end_time-self.start_time#実行時間

        self.operate_time=self.call_algotithm[2]

        print(f"{len(self.call_algotithm[0])}手かかりました")

        print(f"array_sendは{self.call_algotithm[1][0]}手かかりました")
        print(f"array_sendは{self.operate_time[0]}秒かかりました")
        
        print(f"clmatch_num_cuttingは{self.call_algotithm[1][1]}手かかりました")
        print(f"clmatch_num_cuttingは{self.operate_time[1]}秒かかりました")

        print(f"clmatch_cuttingは{self.call_algotithm[1][2]}手かかりました")
        print(f"clmatch_cuttingは{self.operate_time[2]}秒かかりました")


        print(f"{self.time}秒かかりました")
        


        #print(self.now_board)
        # for turn in range(1,len(self.call_algotithm[0])+1):
        #     #self.end = self.get_time()
        #     self.turn_algorithm=self.call_algotithm[0][turn-1]#そのターンの操作
        #     self.cutter_position=[self.turn_algorithm[1],self.turn_algorithm[2]]#使用した座標
        #     self.relord_board=self.board_update(self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.now_board)
        #     self.now_board=self.relord_board.copy()#盤面書き換え
            

        # if self.now_board==self.correct_board:
        #     print("正解")

        



simul=simu()
simul.set()