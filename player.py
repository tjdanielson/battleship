from fleet import Fleet
from gameboard import Gameboard

class Player:
    def __init__(self):
        self.fleet = Fleet()
        self.gameboard = Gameboard()
        self.attackboard = Gameboard()
    

    def place_fleet(self):
        for ship in self.fleet.ships:
            self.place_ship_on_board(ship, self.get_user_placements(ship))
        for i in self.gameboard.board:
            print(i)
        print('You have placed your ships, please see above board for ship placement!')

    def get_user_placements(self, ship):
        #TODO: handle user input (needs to come in like: A4) -- error handling for if it comes in backwards or totally invalid
        valid_placement = False
        while valid_placement == False:
            valid_input = False
            while valid_input == False:
                placement = input(f'Where would you like to place your {ship.name}? ').upper()
                letter = ord(placement[0]) - 65
                try:
                    number = int(placement[1:])
                    if letter > 19 or letter < 0 or number > 20 or number < 0:
                        print('Oops, looks like you\'re trying to place your ship outside of the range of the board. Please try again.')
                        valid_input = False
                    else:
                        valid_input = True
                except ValueError:
                    print('Oops! That isn\'t a valid placement. Please make sure you are entering a letter between A-T, then a number between 1-20 (IE - A10, R4, etc.')
                    valid_input = False
            orientation = input(f'Which way would you like your ship oriented? N, S, E, or W ').upper()
            while orientation != 'N' and orientation != 'E' and orientation != 'S' and orientation != 'W':
                orientation = input(f'Invalid entry - Please enter: N, S, E, or W ').upper()
            ship_placement = [letter, number, orientation]
            continue_looping = True
            while continue_looping == True:
                for count in range(0, ship.size):
                    if self.gameboard.board[number][letter] == '0 ':
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
                        break
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

    
    def attack(self, opponent):
        letter = 100
        number = 100
        while letter > 19 or letter < 0 or number > 20 or number < 0:
            attack = input(f'Where would you like to attack? ').upper()
            letter = ord(attack[0]) - 65
            number = int(attack[1:])
        if opponent.gameboard.board[number][letter] == '\U0001F4A3' or opponent.gameboard.board[number][letter] == '\U0001F4A8':
            print('You\'ve already attacked here! What a waste of a turn!')
        elif opponent.gameboard.board[number][letter] != '0 ':
            print('\U0001F4A3 You have hit a ship!!! \U0001F4A3')
            #decrement length of ship hit by 1
            for ship in opponent.fleet.ships:
                if ship.id == opponent.gameboard.board[number][letter]:
                    ship.size -= 1
                    if ship.size == 0:
                        print(f'You\'ve sunk my {ship.name}') 
                    break 
            self.attackboard.board[number][letter] = '\U0001F4A3'
        else:
            print('A swing and a miss')
            self.attackboard.board[number][letter] = '\U0001F4A8'
        

#tessa = Player()


            
   