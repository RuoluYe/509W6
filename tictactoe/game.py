### object Game and player
from Board import Board
import random

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Human("X")
        self.winner = None
        self.turn = 0
        
    def set_winner(self, player):
        if self.winner == None:
            self.winner = player
        else:
            print("!!!Multiple winner Error!!!")

    def check_winner(self):
        print("beginning check winner for turn" + str(self.turn))
        for i in range(3):
            thisRow = self.board.get_row(i)
            
            player = thisRow[0]
            if player == None:
                continue
            if thisRow[0] == thisRow[1] and thisRow[0] == thisRow[2]:
                self.set_winner(player)
                return True
                
        for i in range(3):
            thisCol = self.board.get_col(i)
            player = thisCol[0]
            if player == None:
                continue
            if thisCol[0] == thisCol[1] and thisCol[0] == thisCol[2]:
                self.set_winner(player)
                return True
        
        player = self.board.get(1,1)
        if player == None:
            return False
        diag1 = [self.board.get(0,0), self.board.get(2,2)]
        if diag1[0] == player and diag1[1] == player:
            self.set_winner(player)
            return True
        diag2 = [self.board.get(2,0), self.board.get(0,2)]
        if diag2[0] == player and diag2[1] == player:
            self.set_winner(player)
            return True
    
    def get_position(self):
        x = int(input("which coloumn? left(1), middle(2), or right(3): "))
        y = int(input("Which row? up(1), middle(2), or down(3): "))
        nums = [1,2,3]
        if (x not in nums) or (y not in nums):
            print("Please only enter 1,2, or 3 for your x & y input.")
            return self.get_position()
        if (self.board.is_filled(x-1,y-1)):
            print("Spot taken, please re-select!")
            return self.get_position()
        return [x, y]


    
       
class Player():
    def __init__(self, id) :
        self.id = id
    
    def __str__(self):
        return str(self.id)

    def other_player(self):
        """Given the character for a player, returns the other player."""
        assert self.id == "X" or self.id == "0", "Player must be 'X' or '0'"
        if self.id == "X": 
            self.id = "0" 
        else: 
            self.id = "X"
        
class Human(Player):
    pass
        
class Bot(Player):
    def bot_move(self, b: Board()):
        spots = b.get_empty_spot()
        return random.choice(spots)

class doubleGame(Game):
    def __init__(self):
        super().__init__()
        self.player2 = Human("0")
        self.currentPlayer = random.choice([self.player1, self.player2])
    
    def start(self):
        while self.winner is None:
            self.turn += 1
            print(self.board)
            
            print(str(self.currentPlayer) + ", your turn")
            
            positions = self.get_position()
            x, y = positions[0], positions[1]
            print(f"{self.currentPlayer} chose {positions[0]}, {positions[1]}")
            
            self.board.set(x - 1, y - 1, self.currentPlayer.id)
            
            self.currentPlayer.other_player()
            
            if self.turn > 3:
                self.check_winner()
            if self.turn == 9 and self.winner is None:
                break
        
        if self.winner:
            print(self.board)
            print("We have a winner, " + self.winner + "!")
        else:
            print("There is a tie")
        
class singleGame(Game):
    def __init__(self):
        super().__init__()
        self.player2 = Bot("0")
        self.human_turn = random.choice([True, False])
    
    
    def start(self):
        while self.winner is None:
            self.turn += 1
            if not self.human_turn:
                botMove = self.player2.bot_move(self.board)
                self.board.set(botMove[0], botMove[1], "0") # Bot.id
                print(f"Bot move to {botMove[0]+1},{botMove[1]+1}") 
                print(self.board)
            else:
                print("Your turn now! (((" + str(self.winner))
                
                positions = self.get_position()
                x = positions[0]
                y = positions[1] 
                print(f"You chose [{x}, {y}]")
            
                self.board.set(x - 1, y - 1, self.player1.id)
                print(self.board) 
        
            if self.turn > 3:
                self.check_winner()
            if self.turn == 9 and self.winner is None:
                break
            self.human_turn = not self.human_turn

            
        if self.winner:
            print("We have a winner, " + str(self.winner) + "!")
        else:
            print("There is a tie")
