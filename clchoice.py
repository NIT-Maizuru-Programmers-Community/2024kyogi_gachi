goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]#0:2,1:8,2:8,3:7

now_board=[[3,2,3,1,2],
           [1,2,0,1,2],
           [2,1,3,3,2],
           [2,1,3,2,3],
           [1,1,3,0,1]]

def clchoice(board,goal):

    def icchi(row1,row2):#now,goal
         def compare(hai1,hai2):#一致度確認一行の配列
             score=0
             for i in range(4):
                 if (hai1[i]<hai2[i]):
                     score=score+hai1[i]
                 if (hai1[i]>=hai2[i]):
                     score=score+hai2[i]
             return score
                 
         score_yoko=0
         score_tate=0
         for a in range(2):#0:横,1:縦
             for b in range(len(row1[0])):
                 for c in range(len(row1[0])):
                     if a==0:
                         score_yoko=score_yoko+compare(row1[a][b],row2[a][c])
                     else:
                         score_tate=score_tate+compare(row1[a][b],row2[a][c])
        
         if score_yoko < score_tate:
             return False
         if score_yoko > score_tate:
             return True
        
                         
                     
         


    def get_num(board):#配列の要素を取得
        board_element_yoko=[]
        board_element_tate=[]
        def count_num(youso):#入力された配列の要素を取得
            pisu=[0,0,0,0]
            for i in range(len(youso)):
                if youso[i]==0:
                    pisu[0]+=1

                if youso[i]==1:
                    pisu[1]+=1

                if youso[i]==2:
                    pisu[2]+=1

                if youso[i]==3:
                    pisu[3]+=1
            return pisu
        
        board_tate=[list(x) for x in zip(*board)]#縦で参照のため転地
        for ry in range(len(board)):
            board_element_yoko.append(count_num(board[ry]))
        for rt in range(len(board)):
            board_element_tate.append(count_num(board_tate[rt]))
        
        return [board_element_yoko,board_element_tate]
    
    now_element=get_num(board)
    goal_element=get_num(goal)

    return icchi(now_element,goal_element)#now,goal

                        
         
    


print(clchoice(goal_board,now_board))