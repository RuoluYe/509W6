import unittest
import logic

class TestLogic(unittest.TestCase):
    def test_get_winner(self):
        board = [
            ['X', None, '0'],
            [None, 'X', '0'],
            ['X', '0', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        
        board = [
            ['X', '0', 'X'],
            ['0', '0', '0'],
            [None, None, 'X']
        ]
        self.assertEqual(logic.get_winner(board), '0')

        board = [
            ['X', '0', 'X'],
            ['X', '0', '0'],
            ['0', 'X', 'X']
        ]
        self.assertEqual(logic.get_winner(board), None)


        # TODO: Test all functions from logic.py!
    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), '0')
        self.assertEqual(logic.other_player('0'), 'X')
    
    def test_numIsNotValid(self):
        self.assertEqual(logic.numIsNotValid(2), False)
        self.assertEqual(logic.numIsNotValid(-1), True)
        self.assertEqual(logic.numIsNotValid(4), True)
        self.assertEqual(logic.numIsNotValid(1), False)
        self.assertEqual(logic.numIsNotValid(3), True)
        self.assertEqual(logic.numIsNotValid(0), False)

    
    def test_checkError(self):
        board = [
            ['X', None, '0'],
            [None, 'X', '0'],
            ['X', '0', 'X'],
        ]
        row = 1
        col = 3
        self.assertEqual(logic.checkError(board,row,col), "Please input 1, 2, or 3 for row and column number.")
        col = 2
        self.assertEqual(logic.checkError(board,row,col), "This spot is already taken! Pick another spot!")
        col = 0
        self.assertEqual(logic.checkError(board,row,col), None)
        
if __name__ == '__main__':
    unittest.main()
