# command line interface for the game. input & output here. 
import logic
import random
from game import Game

# def board_view(board):
#     line1 = str(board[0])
#     line2 = str(board[1])
#     line3 = str(board[2])
#     output = line1 + "\n" + line2 + "\n" + line3
#     return output

def get_game_mode(): #return true if is single
    """change game mode"""
    

if __name__ == '__main__':
    _mode = None
    while _mode == None:
        print("Single(1) or Double(2) player?")
        mode = int(input())
        if mode == 1:
            _mode = True
        elif mode == 2:
            _mode = False 
        else: print("only enter 1 or 2")
    
    game = Game(_mode)
    game.start()
    
        
    # if winner: 
    #     print(board_view(board))
    #     print("Winner is " + winner + "! Congrats!")
    # else:
    #     print("There is a tie.")
       

