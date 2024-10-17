cutter_scale_array=[258,128,64,32,16,8,4,2,1]
general_usable_coumn=[]#[抜き型番号,何列目か,幅,詰めれる距離,上の削った距離]
cut_type=[[[1,1,1,1,0],
           [1,1,0,1,0],
           [1,1,1,1,0]],

          [[1,0,1,1,0],
           [1,0,1,0,0],
           [1,0,1,1,0],
           [0,1,1,0,0],
           [0,1,1,0,0]
           ]]


#一般を使える形に横
for general_num in range(0,len(cut_type)): #一般は25から
    general_cut=cut_type[general_num]#今回のループで扱う抜き型

    for column in range(0, len(general_cut[0])):#各列を見ていく
        cutter_distance=0#詰める距離
        sharpen_distance=0#最初の距離
        sharpen_distance_under=0#下の削る距離
        between_count=0#間の距離
        general_distance=cutter_distance+between_count#幅
        is_exist=False

        for sharpen in general_cut:#上側の削る距離カウント
            if sharpen[column]==1:
                break
            sharpen_distance+=1
        
        if sharpen_distance==len(general_cut):#上全部が0の場合飛ばす
            continue

        for sharpen in reversed(general_cut):#下側の削る距離カウント
            if sharpen[column]==1:
                break
            sharpen_distance_under+=1

        while general_distance+sharpen_distance!=len(general_cut)-sharpen_distance_under:#左の削る距離+詰める距離+間の距離==抜き型の大きさ-右側の削る距離
            is_exist=False#while内部でのis_existの再定義
            is_exist_standard=False
            
            for cutter in range(general_distance+sharpen_distance,len(general_cut)-sharpen_distance_under):#詰めれる距離カウント
                if general_cut[cutter][column]==0:
                    break
                cutter_distance+=1
            general_distance=cutter_distance+between_count

            for i in range(0,len(cutter_scale_array)):#定型と同じ距離詰めるなら省く
                if cutter_scale_array[i]==cutter_distance:
                    is_exist_standard=True
                    break
            
            if (is_exist_standard==False):#general_usableを追加
                for search in range(0,len(general_usable_coumn)):#同じ長さのやつがないか探す
                    if general_usable_coumn[search][2]==cutter_distance:#幅詰める距離が同じ場合、幅がより小さいものを取得
                        is_exist=True
                        if general_usable_coumn[search][1] > general_distance:
                            general_usable_coumn[search]=[general_num,column,general_distance,cutter_distance,sharpen_distance]
                            #[抜き型番号,何列目,詰める距離,上の削った距離]
                        else:
                            break
                
                if is_exist==False:
                    general_usable_coumn.append([general_num,column,general_distance,cutter_distance,sharpen_distance])
            
        
            for between in range(general_distance+sharpen_distance,len(general_cut)-sharpen_distance_under):#間カウント
                if general_cut[between][column]==1:
                    break
                between_count+=1
            general_distance=cutter_distance+between_count

print(general_usable_coumn)
print(f"general_usableは{len(general_usable_coumn)}")