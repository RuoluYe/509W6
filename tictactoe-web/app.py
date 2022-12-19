from flask import Flask, render_template, request, redirect, url_for, session
from tempfile import mkdtemp
import random

class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def __str__(self):
        s = '-------\n'
        for row in self._rows:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + '|\n-------\n'
        return s
    
    def get(self, x: int, y: int):
        return self._rows[y][x]

    def is_filled(self, x, y):
        if self.get(x,y) is None:
            return False
        return True

    def set(self, x: int, y: int, value):
        self._rows[y][x] = value
        
    def get_row(self, row: int):
        return self._rows[row]
    
    def get_col(self, col: int): 
        # col = 1,2,or 3 for first,second or third column
        b = self._rows
        return [b[0][col], b[1][col], b[2][col]]
    
    def get_empty_spot(self):
        spots = []
        for y in range(3):
            for x in range(3):
                if self.get(x,y) is None:
                    spots.append([x,y])
        return spots 

app = Flask(__name__) #create a flask from this file
app.secret_key = "ttt"

@app.route('/', methods = ['GET', 'POST'])
def get_game_mode():
    session.pop("name", None)
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
    if "name" in session:
        name = session["name"]
        session
        return render_template('game.html', name = name)
    else:
        return redirect(url_for("get_game_mode"))


if __name__ == "__main__":
    app.run(debug = True)