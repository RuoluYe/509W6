### object Game and player
from board import Board
import random
import pandas as pd

class Game:
    def __init__(self):
        self.board = Board()
        self.winner = None
        self.turn = 0
        self.savedGames: pd.DataFrame = self.read_games()
        self.savedMoves: pd.DataFrame = self.read_moves()
        self.player1 = Bot()
        self.player2 = Bot()
        self.currentPlayer = self.player1

    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else: 
            self.currentPlayer = self.player1

    def finish(self):
        if self.winner:
            print(self.board)
            id = str(self.winner) 
            if id == "X": 
                self.winner = self.player1
            else:
                self.winner = self.player2
             
            print("We have a winner, " + self.winner.name + "!")
        else:
            print("There is a tie")
        self.add_game()
        self.savedGames.to_csv("game.csv")
        self.savedMoves.to_csv("move.csv")

        
        
    def read_games(self):
        try:
            return pd.read_csv("game.csv")
        except FileNotFoundError:
            return pd.DataFrame(columns=[
                "Game ID",
                "Player 1",
                "Player 2",
                "Winner",
                "Turns taken",
        ])
    def read_moves(self):
        try:
            return pd.read_csv("moves.csv")
        except FileNotFoundError:
            return pd.DataFrame(columns=[
                "Game ID",
                "Turn",
                "Player",
                "Position",
            ])
    
    def add_game(self):
        length = len(self.savedGames)
        self.savedGames.loc[length] = {
        "Game ID": length+1,
        "Player 1": self.player1.name, 
        "Player 2": self.player2.name, 
        "Winner": self.winner.name,
        "Turns taken": self.turn,
    }
        
    def add_move(self, player, position):
        game_id = len(self.savedGames)
        moves = self.read_moves()
        moves.loc[len(moves)] = {
            "Game ID": game_id,
            "Turn": self.turn,
            "Player": player,
            "Position": position,
        }   
         
    def set_winner(self, player):
        if self.winner == None:
            self.winner = player
        else:
            print("Multiple winner Error!")

        
    def check_winner(self):
        
        def check_winner_helper(positions):
            player = positions[0]
            if player == None:
                return False
            if positions[0] == positions[1] and positions[0] == positions[2]:
                self.set_winner(player)
                return True
            return False
            
        for i in range(3):
            if self.winner == None:
                thisRow = self.board.get_row(i)
                thisCol = self.board.get_col(i)
                check_winner_helper(thisRow)
                check_winner_helper(thisCol)
        
        player = self.board.get(1,1)
        if self.winner != None:
            return True
        elif player == None: 
            return False
        else:
            diag1 = [self.board.get(0,0), self.board.get(2,2)]
            if diag1[0] == player and diag1[1] == player:
                self.set_winner(player)
                return True
            diag2 = [self.board.get(2,0), self.board.get(0,2)]
            if diag2[0] == player and diag2[1] == player:
                self.set_winner(player)
                return True 
    
    def start(self):
        while self.winner is None:
            self.turn += 1
            print(self.board)

            if self.currentPlayer.type == "Human":
                print("Your turn now!" +
                      str(self.currentPlayer.name))                
            
            move = self.currentPlayer.get_move(self.board)
            x = move[0]
            y = move[1]
            self.board.set(x, y, self.currentPlayer.id)
            self.add_move(self.currentPlayer.name, move)
        
            if self.turn > 3:
                self.check_winner()
            if self.turn == 9 and self.winner is None:
                break
            self.other_player()
        
        self.finish()
        
class Player():
    def __init__(self, id = None) :
        self.id = id
    
    def __str__(self):
        return str(self.id)


        
class Human(Player):
    name = input("Please input your name:")
    type = "Human"
    def get_move(self, board):
        x = int(input("which coloumn? left(1), middle(2), or right(3): "))
        y = int(input("Which row? up(1), middle(2), or down(3): "))
        nums = [1,2,3]
        if (x not in nums) or (y not in nums):
            print("Please only enter 1,2, or 3 for your x & y input.")
            return self.get_move()
        if (board.is_filled(x-1,y-1)):
            print("Spot taken, please re-select!")
            return self.get_move()
        print(f"{self.name} chose {x}, {y}")
        return [x-1, y-1]
        
class Bot(Player):
    name = "Bot"
    type = "Bot"
    def get_move(self, board):
        spots = board.get_empty_spot()
        spot = random.choice(spots)
        print(f"Bot move to {spot[0]+1},{spot[1]+1}") 
        return spot


class doubleGame(Game):
    def __init__(self):
        super().__init__()
        self.player1 = Human("X")
        self.player2 = Human("0")
        self.currentPlayer = random.choice([self.player1, self.player2])
        
 
        
 
class singleGame(Game):
    def __init__(self):
        super().__init__()
        self.player1 = Human("X")
        self.player2 = Bot("0")
        self.currentPlayer = random.choice([self.player1,  self.player2])
        
            

