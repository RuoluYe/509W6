### class object for board. 
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

    def isFilled(self, x, y):
        if self.get(x,y) is None:
            return False
        return True

    def set(self, x: int, y: int, value):
        self._rows[y-1][x-1] = value


    def get_winner(self):
        """Return the winner, if no one wins, return None"""
        n = len(self._rows)
        for x in range(n):
            player = self.get(x,0)
            if player == self.get(x,1) and self.get(x,2) == player:
                return player
    