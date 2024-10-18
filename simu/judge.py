class Judgec:
    def judge(self,update_bord,correct_bord):
        #更新されたボードをupdate_bord、正解のボードをcorrect_bord
        incorrect_total=0
        if update_bord==correct_bord:
            return [True,0]
        
        for tate in range(len(update_bord)):
            for yoko in range(len(update_bord[0])):
                
                if update_bord[tate][yoko]!=correct_bord[tate][yoko]:
                    incorrect_total+=1

        return [False,incorrect_total]