#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ
import judge
import board_reload_fujii
import general_patterns

class algo_kanefusa(board_reload_fujii.BoardOperation):
    def algo(self,now_board,correct_board,cut_type):
        
        self.now=now_board
        self.correct=correct_board
        self.cut=cut_type

        self.use_type=2
        self.x=0
        self.y=0
        self.shorten_direc=3
        incorrect=judge(now_board,correct_board)

        for p in range(25): #0~24
            for x in range(len(now_board[0])):
                for y in range(len(now_board)):
                    for d in range(4): #0~3
                        after_board=self.board_update(p,[x,y],d,now_board) #操作をする
                        if(judge(now_board,after_board)[0]<incorrect):
                            break
                    if(judge(now_board,after_board)[0]<incorrect):
                        break
                if(judge(now_board,after_board)[0]<incorrect):
                    break
            if(judge(now_board,after_board)[0]<incorrect):
                break

        self.use_type=p
        self.x=x
        self.y=y
        self.shorten_direc=d

        return [self.use_type,self.x,self.y,self.shorten_direc]