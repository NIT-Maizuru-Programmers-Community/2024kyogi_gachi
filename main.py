board_width=6
board_height=4
board_start=[[2,2,0,1,0,3],[2,1,3,0,3,3],[0,2,2,1,0,3],[3,2,2,0,3,3]]
board_now=[[2,2,0,1,0,3],[2,1,3,0,3,3],[0,2,2,1,0,3],[3,2,2,0,3,3]]
board_goal=[[0,0,0,0,0,0],[1,1,1,2,2,2],[2,2,2,2,3,3],[3,3,3,3,3,3]]

general_patterns_p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_height=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_cells=[[[1]],[[1,1],[1,1]],[[1,1],[0,0]],[[1,0],[1,0]],[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
                        [[1,1,1,1],[0,0,0,0],[1,1,1,1],[0,0,0,0]],[[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0]]]

class BoardReload():
    cover_count_x=0
    cover_count_y=0

    def __init__(self,p,x,y,s,board_now):

        self.p=p
        self.x=x
        self.y=y
        self.s=s
        self.board_now=board_now
        self.flame_board=[]
        self.flame_nukigata=[]


    def cover_judge(self):
                x=self.x
                y=self.y
                for i in range(general_patterns_width[self.p]):
                    x=x+i
                    y=self.y
                    for j in range(general_patterns_height[self.p]):
                        y=y+j
                        if x<board_width and y<board_height and x>=0 and y>=0:
                            
                            self.flame_board.append([x,y])
                            self.flame_nukigata.append([i,j])

                print(self.flame_board)
                print(self.flame_nukigata)
    
    def pull_out(self):
         self.cover_judge()


board_reload=BoardReload(general_patterns_p[7],-1,-1,0,board_now)
board_reload.cover_judge()
         


    

        