import simu.judge as judge
import standard_patterns
import output_server
import time
import algo_func
import kanefusa
import numpy as np
import server_get
import copy



#サーバーとの送受信ができる


#cd "C:\Users\ryory\Desktop\procom\2024年度\procon-server"
#"C:\Users\taker\Downloads\procon-server"
#procon-server_win.exe -c input.json -l :8080 -start 1s


#コマンドプロンプトで上のコマンドを実行してからmainを実行

def set(x,y,n):
    
    first_board = np.random.randint(0, 4, (x, y))
    correct_board=first_board.tolist() #正解の盤面
    shuffled_elements = np.random.permutation(first_board.flatten())
    second_board = shuffled_elements.reshape(x, y)
    now_board=second_board.tolist() #現在の盤面
    use_type=standard_patterns.standard_patterns_cells.copy()#使用できる抜き型
    wide=len(correct_board[0])
    height=len(correct_board)

    general=kanefusa.generate_random_lists(n)
    
    use_type.extend(general)

    return now_board,correct_board,use_type,wide,height


# now_board,correct_board,general_patterns,width,height=server_get.server_get()
# #現在の盤面,正解の盤面,一般抜型,横の大きさ,縦の大きさ
# use_type=copy.deepcopy(standard_patterns.standard_patterns_cells)#使用できる定型抜き型
# use_type.extend(general_patterns)#使用できる定型抜き型


now_board,correct_board,use_type,width,height=set(100,100,25)   
#x,y,n 

start_time = time.time()#開始時間
call_algotithm=algo_func.algo_gene(now_board,correct_board,use_type,width,height)#アルゴリズム呼び出し
algorithm_turn=len(call_algotithm)#かかった手数

#output_server.log_output(call_algotithm,algorithm_turn)

end_time = time.time()#終了時間
time_action=end_time-start_time#かかった時間





print(f"{algorithm_turn}手かかりました")
print(f"{time_action}秒かかりました")


# for turn in range(1,self.algorithm_turn+1):
#     self.turn_algorithm=self.call_algotithm[turn-1]#そのターンの操作
#     self.cutter_position=[self.turn_algorithm[1],self.turn_algorithm[2]]#使用した座標
#     self.relord_board=self.board_update(self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.now_board)
#     self.correct=self.judge(self.relord_board,self.correct_board)#正誤判定
#     self.now_board=self.relord_board.copy()#盤面書き換え
#     output.log_output(self.relord_board,turn,self.time,self.turn_algorithm[0],self.cutter_position,self.turn_algorithm[3],self.correct[1])
    




