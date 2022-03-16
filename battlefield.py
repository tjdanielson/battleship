from player import Player

class Battlefield:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
    
    def run_game(self):
        print('Player One: Place your fleet of ships!')
        self.player_one.place_fleet()
        print('Player Two: Place your fleet of ships!')
        self.player_two.place_fleet()