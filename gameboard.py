class Gameboard:
    def __init__(self, owner):
        self.owner = owner
        self.board = [[0] * 20 for i in range(20)]

    def display_board(self):
        for i in self.board:
            print(i)

# game = Gameboard('tessa')
# game.display_board()