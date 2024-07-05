import pygame as py
from pygame.locals import *
import sys
import random
import json
import threading
import numpy as np

py.init()    # Pygameを初期化
turn = 1
path_B = 'log.json'

write_block = threading.Lock()
load_block = threading.Lock()

WIDTH, HEIGHT = 1200, 800

Masu_size = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)  
YELLOW = (255, 255, 0)  
RED = (255, 0, 0) 
BLUE = (0, 0, 255)  

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("a")
screen.fill(WHITE)

botton_y = 650
botton_x_next = 850
botton_x_back = 150

button = py.Rect(botton_x_next, botton_y, 120, 50)  # creates a rect object
button2 = py.Rect(botton_x_back, botton_y, 120, 50)  # creates a rect object

#STEP1.フォントの用意  
font = py.font.SysFont(None, 60)
    
#STEP2.テキストの設定
text1 = font.render("NEXT", True, (0,0,0))
text2 = font.render("BACK", True, (0,0,0))






running = True
while running:
    with load_block:
        json_open = open(path_B, 'r')
        BOARD = json.load(json_open)
        

    board_date = BOARD[turn-1][str(turn)]["board"]
    board_turn =  BOARD[turn-1][str(turn)]["turn"]
    TF =  BOARD[turn-1][str(turn)]["TF"]
    time =  BOARD[turn-1][str(turn)]["time"]


    board = np.array(board_date)
    board_size = board.shape
    board_y = board_size[0]
    board_x = board_size[1]
    
    turn_text = font.render(f"turn:{board_turn}", True, (0,0,0))
    TF_text = font.render(f"TF:{(100-TF)}%", True, (0,0,0))
    time_text = font.render(f"time:{time}s", True, (0,0,0))

    for y in range(board_y):
        for x in range(board_x):
            if board_date[y][x] == 0:  
                py.draw.rect(screen, RED, (x * Masu_size, y * Masu_size, Masu_size, Masu_size))

            elif board_date[y][x] == 1:
                py.draw.rect(screen, BLUE, (x * Masu_size, y * Masu_size, Masu_size, Masu_size))

            elif board_date[y][x] == 2:
                py.draw.rect(screen, YELLOW, (x * Masu_size, y * Masu_size, Masu_size, Masu_size))

            elif board_date[y][x] == 3:
                py.draw.rect(screen, GREEN, (x * Masu_size, y * Masu_size, Masu_size, Masu_size))
    
    py.draw.rect(screen, (255, 0, 0), button)
    py.draw.rect(screen, (0, 255, 0), button2)

    screen.blit(text1, (botton_x_next, botton_y))
    screen.blit(text2,(botton_x_back, botton_y))

    screen.blit(turn_text,(500, 600))
    screen.blit(TF_text,(500, 650))
    screen.blit(time_text,(500, 700))


    
    py.display.flip()
    for event in py.event.get():
        if event.type == py.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                turn= turn+1
            if button2.collidepoint(event.pos):
                turn = turn-1
    
    screen.fill(WHITE)




py.quit()
sys.exit()