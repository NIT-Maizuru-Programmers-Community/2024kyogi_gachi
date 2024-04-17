import judge
import general_patterns
import output



seikai=[[1,2,3],[3,2,2],[1,2,2]]
nukigata=general_patterns.general_patterns_cells.copy()
zahyou=[1,2]
houkou=1
before_board=[[1,3,3],[1,2,3],[3,2,2]]


class relord_kari:
    def relord(self):#nukigata,zahyou,houkou,before_boardを入力
        self.nukigata=general_patterns.general_patterns_cells.copy()
        self.zahyou=[1,2]
        self.houkou=1
        self.before_board=[[1,3,3],[1,2,3],[3,2,2]]
        self.after_board=[[2,2,3],[2,1,1],[2,1,2]] 

        return self.after_board
       


class simu(judge.Judgec,relord_kari):
    seikai=[[1,2,3],[3,2,2],[1,2,2]]

    
    def relord_judge(self):
        self.relord_board=self.relord()
        self.correct=self.judge(self.relord_board,seikai)


    def kair(self):
        print("kyogi")


simul=simu()#nukigata,zahyou,houkou,before_boardを入力



#output.log_output(relord_board,turn,time,use_type,use_coodenate,move_direc,TF)










