from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.attack_board = ''
        self.player_board = ''
        self.gameboard = Gameboard()

    def place_fleet(self):
        for i in self.Fleet():
            placement = input(f'Where would you like to place your {i.name}?')
            


