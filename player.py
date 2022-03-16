from turtle import pos
from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.gameboard = Gameboard()
        self.place_fleet()

    def place_fleet(self):
        for ship in self.fleet.ships:
            self.place_ship_on_board(ship, self.get_user_placements(ship))
        for i in self.gameboard.board:
            print(i)
        print('You have placed your ships, please see above board for ship placement!')

    def get_user_placements(self, ship):
        #TODO: handle user input (needs to come in like: A4) -- error handling for if it comes in backwards or totally invalid
        letter = 100
        number = 100
        orientation = ''
        valid_placement = False
        while valid_placement == False:
            while letter > 19 or letter < 0 or number > 20 or number < 0:
                placement = input(f'Where would you like to place your {ship.name}? ').upper()
                letter = ord(placement[0]) - 65
                number = int(placement[1:])
            while orientation != 'N' and orientation != 'E' and orientation != 'S' and orientation != 'W':
                orientation = input(f'Which way would you like your ship oriented? N, S, E, or W ').upper()
            ship_placement = [letter, number, orientation]
            continue_looping = True
            while continue_looping == True:
                for count in range(0, ship.size):
                    if self.gameboard.board[number][letter] == '0':
                        valid_placement = True
                        if orientation == 'N':
                            number -= 1
                        elif orientation == 'S':
                            number += 1
                        elif orientation == 'E':
                            letter += 1
                        elif orientation == 'W':
                            letter -= 1
                    else:
                        continue_looping = False
                        valid_placement = False
                        print(f'Placement conflict! Either you have gone off the board or placed your {ship.name} on top of another ship. Please try placing your {ship.name} somewhere else.')
                continue_looping = False
        return ship_placement

    
    def place_ship_on_board(self, ship, ship_placement):
        number = ship_placement[1]
        letter = ship_placement[0]
        orientation = ship_placement[2]
        for count in range(0, ship.size):
            if orientation == 'N':
                self.gameboard.board[number][letter] = ship.id
                number -= 1
            elif orientation == 'S':
                self.gameboard.board[number][letter] = ship.id
                number += 1
            elif orientation == 'E':
                self.gameboard.board[number][letter] = ship.id
                letter += 1
            elif orientation == 'W':
                self.gameboard.board[number][letter] = ship.id
                letter -= 1
        return self.gameboard.board

tessa = Player()


            
   