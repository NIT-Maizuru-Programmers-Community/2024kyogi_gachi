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

test=[1,1,2,3,2,0,1,2,2]
goal_board=[[1,2,3,2,1],
            [2,3,1,1,2],
            [2,1,3,0,2],
            [3,1,3,2,3],
            [2,1,3,0,1]]#0:2,1:8,2:8,3:7

#print(get_num(goal_board))
#tuple = [list(x) for x in zip(*goal_board)]#転地



