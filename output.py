#output
import json

###############    仮    ###########
boardk=[[1,2,3],[1,3,1]]#盤面
turnk=1#ターン数
timek=21.1#時間
use_typek=5#使用した型
use_coordinatek=[1,1]#使用した型
move_direck=1#動かした方向
TorFk=24#正誤
###################################


def log_output(board,turn,time,use_type,use_coodenate,move_direc,TF):

    log = {
           'board': board, 
           'turn': turn, 
           'time': time, 
           'use_type':use_type, 
           'use_coodenate':use_coodenate, 
           'move_direc':move_direc, 
           'TF':TF
           }

    with open('log.json', 'w',) as f:
        json.dump(log, f,indent=3)


log_output(boardk,turnk,timek,use_typek,use_coordinatek,move_direck,TorFk)
