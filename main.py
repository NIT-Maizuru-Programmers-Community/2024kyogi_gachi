import judge
import standard_patterns
import output_server
import output
import time
import algorithm
import algorithm_general
import board_reload_fujii
import numpy as np
import server_get
import copy
import server_send



#サーバーとの送受信ができる


#cd "C:\Users\ryory\Desktop\procom\2024年度\procon-server"
#procon-server_win.exe -c input.json -l :8080 -start 1s


#コマンドプロンプトで上のコマンドを実行してからmainを実行
class simu(judge.Judgec,algorithm_general.algorithm_tentative,board_reload_fujii.BoardOperation):

    def set(self):
        self.now_board,self.correct_board,self.general_patterns,self.width,self.height=server_get.server_get()
        #現在の盤面,正解の盤面,一般抜型,横の大きさ,縦の大きさ
        self.use_type=copy.deepcopy(standard_patterns.standard_patterns_cells)#使用できる定型抜き型
        self.use_type.extend(self.general_patterns)#使用できる定型抜き型

        self.algorithm_execution()

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def algorithm_execution(self):
        self.start_time = time.time()#開始時間

        self.call_algotithm=self.algo(self.now_board,self.correct_board,self.use_type,self.width,self.height)#アルゴリズム呼び出し
        self.algorithm_turn=len(self.call_algotithm)#かかった手数

        #output_server.log_output(self.call_algotithm,self.algorithm_turn)
        output_server.log_output(self.call_algotithm,self.algorithm_turn)#serverに送信

        self.end_time = time.time()#終了時間
        self.time=self.end_time-self.start_time#かかった時間

        print(f"{self.algorithm_turn}手かかりました")
        print(f"{self.time}秒かかりました")


        # for turn in range(1,self.algorithm_turn+1):
        #     self.turn_algorithm=self.call_algotithm[turn-1]#そのターンの操作
        #     self.cutter_position=[self.turn_algorithm[1],self.turn_algorithm[2]]#使用した座標
        #     self.relord_board=self.board_update(self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.now_board)
        #     self.correct=self.judge(self.relord_board,self.correct_board)#正誤判定
        #     self.now_board=self.relord_board.copy()#盤面書き換え
        #     output.log_output(self.relord_board,turn,self.time,self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.correct[1])
            

        



simul=simu()
simul.set()