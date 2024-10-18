#アルゴリズム入れる用
#入力は(現在の盤面,正解の盤面,使用できる抜き型)がよい
#出力は(抜き型の番号,使用する座標(x),使用する座標(y),詰める方向)がよいよ



import clmatch_num_cutting
import clmatch_general
import array_send
from board_reload_fujii import BoardOperation
import copy



    
    
def algo_gene(now_board,goal_board,cut_type,wide,height):

    array_operate_board=[]#ここに操作を追加
    operation_board = copy.deepcopy(now_board)
    cutter_scale_array=[258,128,64,32,16,8,4,2,1]
    general_usable=[]#[抜き型番号,幅,詰めれる距離,削った距離]
    move=BoardOperation()
    



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
            


    for column in range(0,len(now_board)):
        print(f"{column}層目")

        #一致度高いやつ寄せる
        array_operation=array_send.column_row_send(operation_board,goal_board,column)
        array_operate_board.extend(array_operation)
        #ボードの更新
        for turn_num in range(0,len(array_operation)):
            array_operation_position=[array_operation[turn_num][1],array_operation[turn_num][2]]
            operation_board=move.board_update(array_operation[turn_num][0], array_operation_position, array_operation[turn_num][3], operation_board)        

        #各要素の個数をそろえる
        element_operation=clmatch_num_cutting.fitnum(operation_board,goal_board,column,wide,height)
        array_operate_board.extend(element_operation[0])
        operation_board=copy.deepcopy(element_operation[1])

        #順番を一致させる
        match_operation=clmatch_general.clmatch(operation_board,goal_board, column, wide, general_usable ,cut_type)
        array_operate_board.extend(match_operation[0])
        operation_board=copy.deepcopy(match_operation[1])

    if operation_board==goal_board:
        print("正解algo")
    else:
        print("不正解algo")

    return array_operate_board
