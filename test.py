cutter_scale_array=[128,64,32,16,8,4,2,1]
cutter_info=[]#[番号,一般(1)か定型か(0)]
is_exist=False
#just_type：[general_num,cutter_distance,sharpen_distance_left]
#general_usable.append：[general_num,general_distance,cutter_distance,sharpen_distance_left]





def making_combination(cloce_distance):
        cutter_scale_array=[128,64,32,16,8,4,2,1]

        div_cloce_distance=cloce_distance #div_cloce_distanceを、定型(cutter_scale_array)で分割
        composition_list=[] #dic_cloce_distanceを構成する数字(定型)を格納

        #div_cloce_distanceを構成する数字(定型)をcomposition_listに格納
        while(div_cloce_distance!=0):
            scale_num=0
            while(cutter_scale_array[scale_num]>div_cloce_distance):
                scale_num+=1
            composition_list.append(cutter_scale_array[scale_num])
            div_cloce_distance-=cutter_scale_array[scale_num]
       
        num=0
        combination_list=[]
        #composition_listの各数字の組み合わせでできる数字をcombination_listに格納

        for i in range((1<<len(composition_list))):
            num=0
            for j in range(len(composition_list)):
                if((i>>j)&1):
                    if((str(bin(i)).count('1'))!=1):
                        num+=composition_list[j]
            
            #00...0の場合は考えない(00...1 ~ 11...1)
            if(num!=0):
                combination_list.append([num,num.bit_count()])

        bit_sort=sorted(combination_list, key=lambda x: x[1], reverse=True)#bitの1が多い順でソート
        combination_sort=[]
        for bit_pattern in bit_sort:
            combination_sort.append(bit_pattern[0])

        return combination_sort

#print(making_combination(45))
cloce_distance=45
standard_combination=[21, 20, 17, 5]
general_usable=[[0, 3, 3, 0], [2, 6, 6, 3], [1, 5, 5, 0]]
standard_combination=making_combination(cloce_distance)

cutter_scale_array=[128,64,32,16,8,4,2,1]
cutter_info=[]#[番号,一般(1)か定型か(0)]
is_exist=False
#just_type：[general_num,cutter_distance,sharpen_distance_left]
#general_usable.append：[general_num,general_distance,cutter_distance,sharpen_distance_left]

while is_exist==False:#定型の組み合わせの中に一般があるか参照
    for general in standard_combination:
        for usable in range(0,len(general_usable)):
            if general==general_usable[usable][2]:#詰めれる距離参照
                if cloce_distance>=general_usable[usable][1]:#幅参照
                    print("あったよー")
                    cutter_info.append([general_usable[usable][0],1,general_usable[usable][2]])
                    cloce_distance=cloce_distance-general_usable[usable][2]
                    standard_combination=making_combination(cloce_distance)#bitの1が多い順にソート済み
                    break
        else:
            continue
        break

    else:
        is_exist=True

    if is_exist==True:
        print("なかったよー")
        break 

while(cloce_distance!=0):
    scale_num=0
    while(cutter_scale_array[scale_num]>cloce_distance):
        scale_num+=1
    
    if cutter_scale_array[scale_num]==128:
        cutter_info.append([20,0,128])
        
    if cutter_scale_array[scale_num]==64:
        cutter_info.append([17,0,64])
    
    if cutter_scale_array[scale_num]==32:
        cutter_info.append([14,0,32])
    
    if cutter_scale_array[scale_num]==16:
        cutter_info.append([11,0,16])
    
    if cutter_scale_array[scale_num]==8:
        cutter_info.append([8,0,8])
    
    if cutter_scale_array[scale_num]==4:
        cutter_info.append([5,0,4])
    
    if cutter_scale_array[scale_num]==2:
        cutter_info.append([2,0,2])
    
    if cutter_scale_array[scale_num]==1:
        cutter_info.append([0,0,1])

    cloce_distance-=cutter_scale_array[scale_num]             
        



print(cutter_info)