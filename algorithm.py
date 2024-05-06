#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ

class karial:
    def algo(self,now_board,correct_board,cut_type):
        
        self.now=now_board
        self.correct=correct_board
        self.cut=cut_type

        self.use_type=5
        self.x=1
        self.y=-2
        self.shorten_direc=3
        return [self.use_type,self.x,self.y,self.shorten_direc]
