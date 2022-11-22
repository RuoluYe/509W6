### object Game and player
from Board import Board

class Game:
    def __init__(self, mode: int):
        self.mode = mode #1 for game bot, 2 for game b/w human
        self.board = Board()
        self.player1 = Human("X")
        self.player2 = None
        self.winner = None
        self.turn = 0
    
    def set_winner(self, player):
        if self.winner == None:
            self.winner = player
        else:
            print("!!!Multiple winner Error!!!")
            
    def get_winner(self):
        return self.winner

    def check_winner(self):
        while self.winner == None:
            for i in range(3):
                thisRow = self.board.get_row(i)
                
                player = thisRow[0]
                if player == None:
                    continue
                if thisRow[0] == thisRow[1] and thisRow[0] == thisRow[2]:
                    self.set_winner(player)
                    break
            if self.winner != None: break
                    
            for i in range(3):
                thisCol = self.board.get_col(i)
                player = thisCol[0]
                if player == None:
                    continue
                if thisCol[0] == thisCol[1] and thisCol[0] == thisCol[2]:
                    self.set_winner(player)
                    break
            if self.winner != None: break
           
            player = self.board[1][1]
            if player == None:
                break
            diag1 = [self.board[0][0], self.board[2][2]]
            if diag1[0] == player and diag1[1] == player:
                self.set_winner(player)
                break
            diag2 = [self.board[2][0], self.board[0][2]]
            if diag2[0] == player and diag2[1] == player:
                self.set_winner(player)
                break
    
    def start(self):
        pass
        
    
       
            
class singleGame(Game):
    def __init__(self, mode):
        super().__init__(mode = 1)
        self.player2 = Bot("0")
        
class singleGame(Game):
    def __init__(self, mode):
        super().__init__(mode = 1)
        self.player2 = Human("0")



class Player:
    def __init__(self, id) :
        self.id = id
        
class Human(Player):
    def __init__(self):
        super().__init__()
        
class Bot(Player):
    def __init__(self):
        super().__init__()

        