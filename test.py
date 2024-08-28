y=0
x=2
height=256
excess_xy=(x,y)
xy_list=[]
depth=0
while(depth<5):
    for i in range(depth):
        xy_list.append((-y+1+i,x-depth+i))
    xy_list.append((-y+depth+1,x))
    for i in range(depth):
        xy_list.append((-y+depth-i,x+1+i))
        
    print(xy_list)
    xy_list=[]
    depth+=1

