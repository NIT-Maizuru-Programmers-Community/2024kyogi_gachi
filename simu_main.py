import judge
import general_patterns
import output
import time
import algorithm




class relord_kari:
    def relord(self,nukigata,zahyou,houkou,before_board):#nukigata,zahyou,houkou,before_boardを入力
        self.nukigata=general_patterns.general_patterns_cells.copy()
        self.zahyou=[1,2]
        self.houkou=1
        self.before_board=[[1,3,3],[1,2,3],[3,2,2]]
        self.after_board=[[2,2,3],[2,1,1],[2,1,2]] 

        return self.after_board
       

class simu(judge.Judgec,relord_kari,algorithm.karial):

    def __init__(self,start_time,turn):
        self.correct_board=[[1,2,3],[3,2,2],[1,2,2]]#正解の盤面
        self.now_board=[[1,2,3],[3,2,2],[1,2,2]]#現在の盤面
        self.use_type=general_patterns.general_patterns_cells.copy()#使用できる抜き型

        self.start=start_time
        self.turn=turn

        self.relord_judge_log()


    
    def relord_judge_log(self):

        self.call_algotithm=self.algo(self.now_board,self.correct_board,self.use_type)

        self.end = time.time()

        self.relord_board=self.relord(self.call_algotithm[0],[self.call_algotithm[1],self.call_algotithm[2]],self.call_algotithm[3],self.now_board)
        #処理後の盤面取得(use_type,zahyou,move_direc,before_board)

        self.correct=self.judge(self.relord_board,self.now_board)#正誤判定

        self.now_board=self.relord_board.copy()#盤面書き換え
        self.coordinate=[self.call_algotithm[1],self.call_algotithm[2]]#使用した座標
        self.times=self.start-self.end#実行時間



        output.log_output(self.relord_board,self.turn,self.times,self.call_algotithm[0],self.coordinate,self.call_algotithm[3],self.correct[1])
        #relord_board,turn,time,use_type,use_coodenate,move_direc,TF


start_time = time.time()#開始時間

turn=1


simul=simu(start_time,turn)
turn+=1

    






#output.log_output(relord_board,turn,time,use_type,use_coodenate,move_direc,TF)












