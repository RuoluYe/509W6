# command line interface for the game. input & output here. 
import logic
import random

def board_view(board):
    line1 = str(board[0])
    line2 = str(board[1])
    line3 = str(board[2])
    output = line1 + "\n" + line2 + "\n" + line3
    return output

def get_game_mode(): #return true if is single
    """change game mode"""
    isSingle = None
    while isSingle == None:
        print("Single(1) or Double(2) player?")
        mode = int(input())
        if mode == 1:
            isSingle = True
        elif mode == 2:
            isSingle = False 
        else: print("only enter 1 or 2")
    return isSingle

if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = random.choice(["X", "0"]) 
    turn = 1
    # get game mode first
    isSingle = get_game_mode()
    
    if isSingle:
        
    
    # else :
    #     while winner == None:
    #         # show the board to the user
    #         print(player + ",take a turn!\n" + board_view(board))

    #         # input a move from the player
    #         print("Which row (horizontal)? Please input 1, 2 or 3")
    #         row = int(input())-1
    #         print("Which column (vertical)? Please input 1, 2, 3")
    #         col = int(input())-1
    #         msg = logic.checkError(board, row, col)

    #         if msg: # if error message exist, print and continue
    #             print(msg)
    #             continue
    #         # update the board
    #         board[row][col] = player

    #         if turn > 4: #start evaluate winner after 4 turns
    #             winner = logic.get_winner(board)
    #         if turn == 9 and winner == None: # give it a stop at turn 9
    #             break
    #         # update counter
    #         player = logic.other_player(player)
    #         turn += 1
            
    if winner: 
        print(board_view(board))
        print("Winner is " + winner + "! Congrats!")
    else:
        print("There is a tie.")
       

