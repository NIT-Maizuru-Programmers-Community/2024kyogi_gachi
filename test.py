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
        self.flame_board=[]
        self.flame_nukigata=[]
        self.cover_judge()

    def cover_judge(self):
                
                x=self.x
                y=self.y
                for i in range(0,general_patterns_width[self.p]):
                    x=self.x+i
                    y=self.y
                    for j in range(0,general_patterns_height[self.p]):
                        y=self.y+j
                        if x<board_width and y<board_height and x>=0 and y>=0:
                            self.flame_board.append([x,y])
                            self.flame_nukigata.append([i,j])

    def num_move(self):
        nuki=self.flame_board
        nuki_line=int
        depth=int

        if(self.s==0):
             nuki_line = [i for i in self.flame_board if i[0] == self.flame_board[0][0]]
             nuki_depth = [i for i in self.flame_board if i[1] == self.flame_board[0][1]]
             depth=board_height-self.flame_board[0][0]
             move_count=[]*len(nuki_line)
             tyousei=self.flame_board[0]
             for i in range(nuki_line[0][1],nuki_line[len(nuki_line)-1][1]+1): #(列)回繰り返す
                   for j in range(nuki_depth[0][0],nuki_depth[len(nuki_depth)-1][0]+1): #(深さ)回繰り返す
                        if(general_patterns_cells[self.p][i-tyousei[0]][j-tyousei[1]]==1):
                             move_count[i]=3
                             print(move_count)
                             
                  

board_reload=BoardReload(1,1,1,0,board_now)
board_reload.num_move()
#print(board_reload.cover_judge())