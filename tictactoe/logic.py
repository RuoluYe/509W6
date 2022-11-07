# no input or output. logic in this file should be unit-testable.
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', '0', or None."""
    win = None
    n = len(board)
    player = None
    # check rows
    for i in range(n):
        win = True
        player = board[i][0] # get the player of  the first one of this row. 
        for j in range(n):
            if board[i][j] != player:
                win = False
                break # this row fail, check next row
        if win:
            return player
    #check columns
    for j in range(n):
        win = True
        player = board[0][j] # get the player as the first one of each column.
        for i in range(n):
            if board[i][j] != player:
                win = False
                break # this column fail, check next
        if win:
            return player
    # check diag
    player = board[0][0]
    #top left bottom right
    win = True
    for i in range(1,n):
        if board[i][i] != player:
            win = False
            break
    if win: 
        return player
    #top right bottom left
    player = board[0][2]
    win = True
    for i in range(1,n):
        if board[i][n-1-i] != player:
            win = False
            break
    if win:
        return player
    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X": return "0" 
    elif player == "0": return "X"
    else: return 'player given is not X or 0'

def numIsNotValid(num):
    """return true if number is less than 0 or larger than 2, check out of bound error"""
    return(num < 0 or num > 2)

def checkError(board, row, col):
    """ chekc error and return a error message"""
    if numIsNotValid(row) or numIsNotValid(col):
        return "Please input 1, 2, or 3 for row and column number."
    if board[row][col]:
        return "This spot is already taken! Pick another spot!"
    return None