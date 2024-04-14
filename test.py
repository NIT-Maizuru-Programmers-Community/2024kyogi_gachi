board_width=6
board_height=4
board_start=[[2,2,0,1,0,3],[2,1,3,0,3,3],[0,2,2,1,0,3],[3,2,2,0,3,3]]
board_now=[[2,2,0,1,0,3],[2,1,3,0,3,3],[0,2,2,1,0,3],[3,2,2,0,3,3]]
board_goal=[[0,0,0,0,0,0],[1,1,1,2,2,2],[2,2,2,2,3,3],[3,3,3,3,3,3]]

general_patterns_p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_height=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_cells=[[[1]],[[1,1],[1,1]],[[1,1],[0,0]],[[1,0],[1,0]],[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
                        [[1,1,1,1],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0]],
                        [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]],
                        []]

class BoardReload():

    def __init__(self,p,x,y,s,board_now):

        self.p=p
        self.x=x
        self.y=y
        self.s=s
        self.board_now=board_now
        self.nukigata_width=0
        self.nukigata_height=0
        self.nukigata_x=0
        self.nukigata_y=0

    def cover_judge(self):
        if(self.x<0):
            self.nukigata_x=0
        else:self.nukigata_x=self.x
        if(self.y<0):
            self.nukigata_y=0
        else:self.nukigata_y=self.y
        
        if(self.x+general_patterns_width[self.p]<=board_width):
            if(self.x<0):
                self.nukigata_width=self.x+general_patterns_width[self.p]
            else:self.nukigata_width=general_patterns_width[self.p]
        else:self.nukigata_width=board_width-self.x

        if(self.y+general_patterns_height[self.p]<=board_height):
            if(self.y<0):
                self.nukigata_height=self.y+general_patterns_height[self.p]
            else:self.nukigata_height=general_patterns_height[self.p]
        else:self.nukigata_height=board_height-self.y

        print(self.nukigata_x,self.nukigata_y,self.nukigata_width,self.nukigata_height) #抜き型のx,y,width,height
            
    #def num_move(self):

board_reload=BoardReload(1,0,0,0,board_now)
board_reload.cover_judge()