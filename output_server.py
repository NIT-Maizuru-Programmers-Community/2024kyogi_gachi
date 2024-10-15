#output
import json
import threading



def log_output(operate_board,algorithm_turn):
    write_lock = threading.Lock()
    output_operate_board=[]#辞書型を追加
    for turn in range(algorithm_turn):
        opperate_data={"p":operate_board[turn][0],"x":operate_board[turn][1],"y":operate_board[turn][2],"s":operate_board[turn][3]}
        output_operate_board.append(opperate_data)

    result ={
        "n":algorithm_turn,
        "ops":output_operate_board
    }
    



    with open('result.json', mode="wt", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    
    
    #return True
    