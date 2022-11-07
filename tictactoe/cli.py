# command line interface for the game. input & output here. 
import logic
import random

if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = random.choice(["X", "0"]) 
    turn = 0
    while winner == None:
        turn += 1
        player = logic.other_player(player)
        print(player + ",take a turn!")
        # show the board to the user
        print(board)
        # input a move from the player
        print("which row (horizontal)?")
        row = int(input())-1
        print("Which column (vertical)?")
        col = int(input())-1
        # check is spot taken
        if board[row][col]:
            player = logic.other_player(player)
            print(player + " is here already! Pick another spot!")
            turn-=1
            continue
        # update the board
        board[row][col] = player
        if turn > 4: #start evaluate winner
            winner = logic.get_winner(board)
        if turn == 9 and winner == None: #give it a stop
            winner = "Tie"
            
    if winner == "Tie":
        print("There is a tie.")
    else:
        print("Winner is " + winner + "! Congrats!")
        