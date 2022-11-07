# command line interface for the game. input & output here. 
import logic
import random

def board_view(board):
    line1 = str(board[0])
    line2 = str(board[1])
    line3 = str(board[2])
    output = line1 + "\n" + line2 + "\n" + line3
    return output

if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = random.choice(["X", "0"]) 
    turn = 1
    while winner == None:
        # show the board to the user
        print(player + ",take a turn!\n" + board_view(board))
        # input a move from the player
        print("which row (horizontal)?")
        row = int(input())-1
        print("Which column (vertical)?")
        col = int(input())-1
        msg = logic.checkError(board, row, col)
        if msg:
            print(msg)
            continue
        # update the board
        board[row][col] = player
        if turn > 4: #start evaluate winner
            winner = logic.get_winner(board)
        if turn == 9 and winner == None: #give it a stop
            break
        player = logic.other_player(player)
        turn += 1
            
    if winner: 
        print(board_view(board))
        print("Winner is " + winner + "! Congrats!")
    else:
        print("There is a tie.")
       

