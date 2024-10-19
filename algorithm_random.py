#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ



import clmatch_num_cutting
import clmatch_general
import array_send
import board_reload_fujii
import copy
import time
import random



class algorithm_tentative(board_reload_fujii.BoardOperation):

    def get_time(self):
        self.now_time=time.time()
        return self.now_time
    
    def algo_rand(self,now_board,goal_board,cut_type,width,height):
        self.now_board=now_board
        self.goal_board=goal_board
        self.use_cut_type=cut_type
        self.height=height
        self.wide=width
        self.random_x=random.randint(0,(self.wide/2))
        self.random_y=random.randint(0,(self.height/2))
        self.random_s=random.choice([2, 3])
        self.array_operate_board=[24,self.random_x,self.random_y,self.random_s]#ここに操作を追加
        self.operation_board = copy.deepcopy(self.now_board)
        cutter_scale_array=[258,128,64,32,16,8,4,2,1]
        general_usable=[]#[抜き型番号,幅,詰めれる距離,削った距離]
        self.operation_board = self.board_update(24,(self.random_x,self.random_y),self.random_s,self.operation_board)



        #一般を使える形に
        #一般を使える形に
        for general_num in range(25,len(cut_type)): #一般は25から

            general_cut=cut_type[general_num][0]#今回のループの一番上
            cutter_distance=0#詰める距離
            sharpen_distance_left=0#左側の削る距離
            sharpen_distance_right=0#右側の削る距離
            between_count=0#間の距離
            general_distance=cutter_distance+between_count#幅
            is_exist=False

            for sharpen in range(0,len(general_cut)):#左側の削る距離カウント
                if general_cut[sharpen]==1:
                    break
                sharpen_distance_left+=1
            
            if sharpen_distance_left==len(general_cut):#上全部が0の場合飛ばす
                continue

            for sharpen in reversed(general_cut):#右側の削る距離カウント
                if sharpen==1:
                    break
                sharpen_distance_right+=1

            while general_distance+sharpen_distance_left!=len(general_cut)-sharpen_distance_right:#左の削る距離+詰める距離+間の距離==抜き型の大きさ-右側の削る距離
                is_exist=False#while内部でのis_existの再定義
                is_exist_standard=False

                for cutter in range(general_distance+sharpen_distance_left,len(general_cut)-sharpen_distance_right):#詰めれる距離カウント
                    if general_cut[cutter]==0:
                        break
                    cutter_distance+=1
                general_distance=cutter_distance+between_count

                for i in range(0,len(cutter_scale_array)):#定型と同じ距離詰めるなら省く
                    if cutter_scale_array[i]==cutter_distance:
                        is_exist_standard=True
                        break
                
                if (is_exist_standard==False):#general_usableを追加
                    for search in range(0,len(general_usable)):#同じ長さのやつがないか探す
                        if general_usable[search][2]==cutter_distance:#幅詰める距離が同じ場合、幅がより小さいものを取得
                            is_exist=True
                            if general_usable[search][1] > general_distance:
                                general_usable[search]=[general_num,general_distance,cutter_distance,sharpen_distance_left]
                            else:
                                break
                    
                    if is_exist==False:
                        general_usable.append([general_num,general_distance,cutter_distance,sharpen_distance_left])
                
            
                for between in range(general_distance+sharpen_distance_left,len(general_cut)-sharpen_distance_right):#間カウント
                    if general_cut[between]==1:
                        break
                    between_count+=1
                general_distance=cutter_distance+between_count
        
        print(f"general_usableは{len(general_usable)}")
                
        

        for column in range(0,len(self.now_board)):
            print(f"{column}層目")

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
            self.match_operation=clmatch_general.clmatch(self.operation_board, self.goal_board, column, self.wide, general_usable ,self.use_cut_type)
            self.array_operate_board.extend(self.match_operation[0])
            self.operation_board=copy.deepcopy(self.match_operation[1])

        if self.operation_board==self.goal_board:
            print("正解algo")
            print(self.random_x)
            print(self.random_y)
            print(self.random_s)
        else:
            print("不正解algo")

        return self.array_operate_board
