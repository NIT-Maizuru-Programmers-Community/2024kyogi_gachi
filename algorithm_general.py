#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ



import clmatch_num_cutting
import clmatch_cutting
import array_send
import board_reload_fujii
import copy
import time



class algorithm_tentative(board_reload_fujii.BoardOperation):

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def algo(self,now_board,goal_board,cut_type,width,height):
        self.now_board=now_board
        self.goal_board=goal_board
        self.use_cut_type=cut_type
        self.height=height
        self.wide=width
        self.array_operate_board=[]#ここに操作を追加
        self.operation_board = copy.deepcopy(self.now_board)
        just_type=[]#[抜き型番号,詰めれる距離,削った距離]
        general_usable=[]#[抜き型番号,幅,詰めれる距離,削った距離]



        #一般抜き型を使用できるように
        #just_typeを作成
        for just in range(25,len(cut_type)):
            just_cut=cut_type[just][0]
            cutter_distance=0
            sharpen_distance=0
            is_exist=False
            for sharpen in range(0,len(just_cut)):#削る距離カウント
                print(sharpen)
                if just_cut[sharpen]==1:
                    break
                sharpen_distance+=1

            if sharpen_distance==len(just_cut):#上全部が0の場合飛ばす
                continue

            for potential in range(sharpen_distance,len(just_cut)):#詰めれる距離カウント
                if just_cut[potential]==0:
                    break
                cutter_distance+=1

            for cutter in range(0,len(just_type)):
                if just_type[cutter][1]==cutter_distance:
                    is_exist=True

            if is_exist==False:
                just_type.append([just,cutter_distance,sharpen_distance])

        #general_usableを作成
        for just in range(0,len(cut_type)):
            general_cut=cut_type[just][0]
            cutter_distance=0
            sharpen_distance=0
            is_exist=False
            for sharpen in range(0,len(just_cut)):#削る距離カウント
                print(sharpen)
                if just_cut[sharpen]==1:
                    break
                sharpen_distance+=1
            
            if sharpen_distance==len(just_cut):#上全部が0の場合飛ばす
                continue






        

        for column in range(0,len(self.now_board)):
            #print(f"{column}層目")


            #一致度高いやつ寄せる
            self.array_operation=array_send.column_row_send(self.operation_board,self.goal_board,column)
            self.array_operate_board.extend(self.array_operation)
            #ボードの更新
            for turn_num in range(0,len(self.array_operation)):
                self.array_operation_position=[self.array_operation[turn_num][1],self.array_operation[turn_num][2]]
                self.operation_board=self.board_update(self.array_operation[turn_num][0], self.array_operation_position, self.array_operation[turn_num][3], self.operation_board)        


            #各要素の個数をそろえる
            self.element_operation=clmatch_num_cutting.fitnum(self.operation_board,self.goal_board,column,self.wide,self.height)
            self.array_operate_board.extend(self.element_operation[0])
            self.operation_board=copy.deepcopy(self.element_operation[1])


            #順番を一致させる
            self.match_operation=clmatch_cutting.clmatch(self.operation_board,self.goal_board,column,self.wide)
            self.array_operate_board.extend(self.match_operation[0])
            self.operation_board=copy.deepcopy(self.match_operation[1])
            #print(f"{self.operation_board}#順番を一致させる盤面")


        #print(self.array_operate_board)
        #print(self.array_execution_time)

        return (self.array_operate_board)
