### object Game
import random
import logic
from Board import Board

class Game:
    def __init__(self, mode: int):
        self.mode = mode #1 for game bot, 2 for game b/w human
        self.board = Board()
        self.player1 = Human(1)
        self.winner = None
    
    def get_winner(self):
        return self.winner

    def check_winner(self, player):
        if [(self.board[0] == player)]

class singleGame(Game):
    def __init__(self, mode):
        super().__init__(mode = 1)
        self.player2 = Bot()

    
    
    
        
    
     

class Player:
    def __init__(self) :
        pass
class Human(Player):
    def __init__(self):
        super().__init__()
class Bot(Player):
    def __init__(self):
        super().__init__()

        