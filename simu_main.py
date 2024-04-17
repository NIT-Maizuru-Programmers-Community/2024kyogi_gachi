import judge
import general_patterns
import output
import time




seikai=[[1,2,3],[3,2,2],[1,2,2]]
use_type=general_patterns.general_patterns_cells.copy()
zahyou=[1,2]
move_direc=1
before_board=[[1,3,3],[1,2,3],[3,2,2]]
turn=4


class relord_kari:
    def relord(self,nukigata,zahyou,houkou,before_board):#nukigata,zahyou,houkou,before_boardを入力
        self.nukigata=general_patterns.general_patterns_cells.copy()
        self.zahyou=[1,2]
        self.houkou=1
        self.before_board=[[1,3,3],[1,2,3],[3,2,2]]
        self.after_board=[[2,2,3],[2,1,1],[2,1,2]] 

        return self.after_board
       


class simu(judge.Judgec,relord_kari):
    seikai=[[1,2,3],[3,2,2],[1,2,2]]

    
    def relord_judge_log(self,use_type,zahyou,move_direc,before_board):

        self.start = time.perf_counter()

        self.relord_board=self.relord(use_type,zahyou,move_direc,before_board)
        self.correct=self.judge(self.relord_board,seikai)

        self.end = time.perf_counter()

        output.log_output(self.relord_board,turn,self.end-self.start,use_type,zahyou,move_direc,self.correct[1])
        #relord_board,turn,time,use_type,use_coodenate,move_direc,TF

        return [self.relord_board,self.correct]




simul=simu()

relo_jud=simul.relord_judge_log(use_type,zahyou,move_direc,before_board)



#output.log_output(relord_board,turn,time,use_type,use_coodenate,move_direc,TF)












