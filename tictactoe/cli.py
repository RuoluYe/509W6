# command line interface for the game. input & output here. 
import logic
import random
from game import *

# def board_view(board):
#     line1 = str(board[0])
#     line2 = str(board[1])
#     line3 = str(board[2])
#     output = line1 + "\n" + line2 + "\n" + line3
#     return output

    

if __name__ == '__main__':
    _single = None
    while _single == None:
        print("Single(1) or Double(2) player?")
        mode = int(input())
        if mode == 1:
            _single = True
        elif mode == 2:
            _single = False 
        else: print("only enter 1 or 2")
    
    if _single:
        game = singleGame()
    else:
        game = doubleGame()
    
    game.start()
