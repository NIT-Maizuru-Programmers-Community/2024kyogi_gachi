import json
import threading

json_open = open('test.json' ,'r')
json_load = json.load(json_open)







print(json_load)



def log():
    print("log")


# 出力
def output(type,dir):

    write_block=threading.Lock()

    path_B='output.json'
    action={
        "actions": [
          {
            "type": type,
            "dir": dir
          }
        ]
      }
    
    with write_block:
        with open(path_B,'w')as f:
            json.dump(action,f)





 

