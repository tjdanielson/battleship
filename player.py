from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.gameboard = Gameboard()
        self.place_fleet()

    def place_fleet(self):
        for i in self.fleet.ships:
            #TODO: handle user input (needs to come in like: A4)
            placement = input(f'Where would you like to place your {i.name}?').upper()
            placement_list = []
            for letter in placement:
                placement_list.append(letter)
            placement_list[0] = ord(placement_list[0]) - 65
            placement_list[1] = int(placement_list[1])
            self.gameboard.board[placement_list[1]][placement_list[0]] = i.id
        for letter in self.gameboard.board:
            print(letter)
            

tessa = Player()


            
            


