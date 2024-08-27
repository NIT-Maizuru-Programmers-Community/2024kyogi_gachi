#output
import json
import threading

###############    仮    ###########
boardk=[[1,2,3],[1,3,1]]#盤面
turnk=1#ターン数
timek=21.1#時間
use_typek=5#使用した型
use_coordinatek=[1,1]#使用した型
move_direck=1#動かした方向
TorFk=24#正誤
###################################


def log_output(turn,time,use_type,use_coodenate,move_direc,TF):
    write_lock = threading.Lock()

    log ={
        turn:{ 
           'turn': turn, 
           'time': time, 
           'use_type':use_type, 
           'use_coodenate':use_coodenate, 
           'move_direc':move_direc, 
           'TF':TF
           }
    }
    
    with write_lock:
        with open('log.json', 'a') as f:
            if turn==1:
                f.write("[")
            json.dump(log, f,indent=3)
            if TF==0:
                 f.write("]")
            elif TF>0:
                 f.write(",")





