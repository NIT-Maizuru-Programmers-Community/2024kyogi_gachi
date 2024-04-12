import json
import threading

def nukigata():
    for i in range(0,25):
        



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