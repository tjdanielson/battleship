from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.attack_board = ''
        self.player_board = ''
        self.gameboard = Gameboard()
        self.place_fleet()

    def place_fleet(self):
        for i in self.fleet.ships:
            #TODO: handle user input (needs to come in like A4)
            placement = input(f'Where would you like to place your {i.name}?')
            placement_list = []
            for letter in placement:
                placement_list.append(letter)
            self.gameboard

tessa = Player()


            
            


