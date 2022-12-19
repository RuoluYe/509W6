import unittest
import logic
from game import *

class TestLogic(unittest.TestCase):
    # def test_get_winner(self):
    #     board = [
    #         ['X', None, '0'],
    #         [None, 'X', '0'],
    #         ['X', '0', 'X'],
    #     ]
    #     self.assertEqual(logic.get_winner(board), 'X')
        
    #     board = [
    #         ['X', '0', 'X'],
    #         ['0', '0', '0'],
    #         [None, None, 'X']
    #     ]
    #     self.assertEqual(logic.get_winner(board), '0')

    #     board = [
    #         ['X', '0', 'X'],
    #         ['X', '0', '0'],
    #         ['0', 'X', 'X']
    #     ]
    #     self.assertEqual(logic.get_winner(board), None)

    #     # TODO: Test all functions from logic.py!
    # def test_other_player(self):
    #     self.assertEqual(logic.other_player('X'), '0')
    #     self.assertEqual(logic.other_player('0'), 'X')
    
    # def test_numIsNotValid(self):
    #     self.assertEqual(logic.numIsNotValid(2), False)
    #     self.assertEqual(logic.numIsNotValid(-1), True)
    #     self.assertEqual(logic.numIsNotValid(4), True)
    #     self.assertEqual(logic.numIsNotValid(1), False)
    #     self.assertEqual(logic.numIsNotValid(3), True)
    #     self.assertEqual(logic.numIsNotValid(0), False)

    
    # # def test_checkError(self):
    #     board = [
    #         ['X', None, '0'],
    #         [None, 'X', '0'],
    #         ['X', '0', 'X'],
    #     ]
    #     row = 1
    #     col = 3
    #     self.assertEqual(logic.checkError(board,row,col), "Please input 1, 2, or 3 for row and column number.")
    #     col = 2
    #     self.assertEqual(logic.checkError(board,row,col), "This spot is already taken! Pick another spot!")
    #     col = 0
    #     self.assertEqual(logic.checkError(board,row,col), None)
        
    def test_board_check_winner(self):
        b = Game()
        b.board.set(0,0,'X')
        b.board.set(1,1, 'X')
        b.board.set(2,2, 'X')
        b.check_winner()
        self.assertEqual(b.winner, "X")
            # ['X', None, none],
            # [None, 'X', none],
            # [none, none, x],
        b = Game()
        b.board.set(1,1, '0')
        b.board.set(1,0, '0')
        b.board.set(1,2, '0')
        b.check_winner()
        self.assertEqual(b.winner, "0")
        b = Game()
        b.board.set(0,0, '0')
        b.board.set(1,0, '0')
        b.board.set(2,0, '0')
        b.check_winner()
        self.assertEqual(b.winner, "0")
        
    def test_get_position(self):
        b = singleGame()
        self.assertEqual(b.get_position(), [1,1])# input 1, 1
        self.assertEqual(b.get_position(), [2,2])# input 2, 2


        
        
    
        
if __name__ == '__main__':
    unittest.main()
