class Gameboard:
    def __init__(self):
        self.board = []
        self.generate_board()

    def generate_board(self):
        row = 1
        column_header = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.board.append(column_header)
        for i in range(20):
            self.board.append(['0'] * 20)
            for j in self.board:
                if len(j) <= 20:
                    j.append(row)
            row += 1
    
    def display_board(self):
        for letter in self.board:
            print(letter)


game = Gameboard()
game.display_board()
