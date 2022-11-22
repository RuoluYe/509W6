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

    def is_filled(self, x, y):
        if self.get(x,y) is not None:
            print("Spot Taken! Please re-select:")
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
    