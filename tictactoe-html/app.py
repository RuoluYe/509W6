from flask import Flask, render_template, session
from collections import namedtuple
from tempfile import mkdtemp

app = Flask(__name__) #create a flask from this file

@app.route('/')
def index():
    return render_template("index.html")

# Post = namedtuple('Post', ['title'])
# user_to_post = {
#     'Alice': [
#         Post('hi alice')
#     ],
#     'bob': [
#         Post('Hi bob')
#     ]
# }

@app.route('/user/<name>')
def profile(name):
    posts = user_to_posts[name]
    return render_template('profile.html', name=name, post = post)

@app.route('/game/<game_id>')
def show_game(game_id):
    return 'facts about game '+ game_id

# @app.route('/')
# def index():
#     return """
#         <link rel = "stylesheet" href="/static/style.css">
#         <div>
#         Hello Page 
#         </div>
#     """

