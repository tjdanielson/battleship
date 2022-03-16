from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.gameboard = Gameboard()
        self.place_fleet()

    def place_fleet(self):
        for ship in self.fleet.ships:
            #TODO: handle user input (needs to come in like: A4)
            placement = input(f'Where would you like to place your {ship.name}? ').upper()
            orientation = input(f'Which way would you like your ship oriented? N, S, E, or W ').upper()
            letter = ord(placement[0]) - 65
            number = int(placement[1:2])
            self.gameboard.board[number][letter] = ship.id
            if orientation == 'N':
                for count in range(1, ship.size):
                    number -= 1
                    self.gameboard.board[number][letter] = ship.id
        for i in self.gameboard.board:
            print(i)
            

tessa = Player()


            
            


