cutter_scale_array=[128,64,32,16,8,4,2,1]
cloce_distance=19 #間隔（幅）

div_cloce_distance=cloce_distance #div_cloce_distanceを、定型(cutter_scale_array)で分割
composition_list=[] #dic_cloce_distanceを構成する数字(定型)を格納

#div_cloce_distanceを構成する数字(定型)をcomposition_listに格納
while(div_cloce_distance!=0):
    scale_num=0
    while(cutter_scale_array[scale_num]>div_cloce_distance):
        scale_num+=1
    composition_list.append(cutter_scale_array[scale_num])
    div_cloce_distance-=cutter_scale_array[scale_num]

print(composition_list)

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
        combination_list.append(num)

print(combination_list)