cutter_scale_array=[258,128,64,32,16,8,4,2,1]
just_type=[]#[抜き型番号,詰めれる距離,削った距離]
general_usable=[]#[抜き型番号,幅,詰めれる距離,削った距離]
cut_type=[[[1,1,1,0,0,0,0,1,1],[1,1,1,0,0,0,0,1,1]],[[1,1,1],[0,0,0]],[[1,1,1,1],[0,0,0,1]]]


#一般を使える形に
for general_num in range(0,len(cut_type)): #一般は25から

    general_cut=cut_type[general_num][0]#今回のループの一番上
    cutter_distance=0#詰める距離
    sharpen_distance_left=0#左側の削る距離
    sharpen_distance_right=0#右側の削る距離
    between_count=0#間の距離
    general_distance=cutter_distance+between_count#幅
    is_exist=False
    is_exist_just=False

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
        is_exist_just=False

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
        
        if (is_exist_standard==False) and (cutter_distance==general_distance):
            #just_typeを追加
            for search in range(0,len(just_type)):#同じ長さのやつがないか探す
                if just_type[search][1]==cutter_distance:
                    is_exist_just=True
                    break

            if is_exist_just==False:
                just_type.append([general_num,cutter_distance,sharpen_distance_left])

    
        for between in range(general_distance+sharpen_distance_left,len(general_cut)-sharpen_distance_right):#間カウント
            if general_cut[between]==1:
                break
            between_count+=1
        general_distance=cutter_distance+between_count




print(f"just_type{just_type}")
print(f"general_usable{general_usable}")