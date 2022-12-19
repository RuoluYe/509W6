from flask import Flask, render_template, request, redirect, url_for, session
from tempfile import mkdtemp
import random

app = Flask(__name__) #create a flask from this file
app.secret_key = "ttt"

@app.route('/', methods = ['GET', 'POST'])
def get_game_mode():
    session.pop("name", None)
    session.pop("board", None)
    if request.method == 'POST':
        name = request.form["single user name"]
        session["name"]= name
        
        return redirect(url_for("game"))
        # return render_template('game.html', name = name)
    else: 
        if "user" in session:
            return redirect(url_for("game"))
        else:
            
            return render_template('index.html')


@app.route('/game', methods = ["POST", "GET"])
def game():
    if "board" not in session:
            person = random.choice(["X","0"])
            session["board"] = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]
            session["turn"] = person
            session["winner"] = False
            session["draw"] = False
    
    winner = get_winner(session["board"])

        
    if "name" in session:
        name = session["name"]
        return render_template('game.html', name = name,  game = session["board"], turn = session["turn"], winner = winner)
    else:
        return redirect(url_for("get_game_mode"))

def get_winner(board):
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

@app.route('/debug')
def debug():
    turn = 1
    if "turn" in session:
        turn = session["turn"]
    return render_template('debug.html', game = session["board"], turn = turn)

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "0"
    else:
        session["turn"] = "X"
    return redirect(url_for('game'))
    
if __name__ == "__main__":
    app.run(debug = True)
    
    