from flask import Flask, render_template, request, redirect, url_for
from tempfile import mkdtemp
import random
from flask_session import Session

app = Flask(__name__) #create a flask from this file


@app.route('/', methods = ['GET', 'POST'])
def get_game_mode():
    if request.method == 'POST':
        name = request.form["single user name"]
        return render_template('game.html', name = name)
    else: 
        return render_template('index.html')


@app.route('/game', methods = ["POST", "GET"])
def game():
    return render_template('game.html')


@app.route('/debug', methods = ['GET', 'POST'])
def debug():
    return render_template('debug.html', request = request)

if __name__ == "__main__":
    app.run(debug = True)