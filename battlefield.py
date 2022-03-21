from player import Player

class Battlefield:
    def __init__(self):
        self.display_instructions()
        self.player_one = Player()
        self.player_two = Player()
    
    def run_game(self):
        #both players put ships on board
        print(f'{self.player_one.name}: Place your fleet of ships!')
        self.player_one.place_fleet()
        print(f'{self.player_two.name}: Place your fleet of ships!')
        self.player_two.place_fleet()
        #players take turns:
        player_one_turn = True
        keep_playing = True
        while keep_playing == True:
            if player_one_turn == True:
                print(f'{self.player_one.name}, it is your turn')
                self.player_turn(self.player_one, self.player_two)
                player_one_turn = False
                if self.calculate_health(self.player_two) == 0:
                    player_two_health = 0
                    player_one_health = self.calculate_health(self.player_one)
                    keep_playing = False
                    break
            else:
                print(f'{self.player_two.name} it is your turn')
                self.player_turn(self.player_two, self.player_one)
                player_one_turn = True
                if self.calculate_health(self.player_one) == 0:
                    player_one_health = 0
                    player_two_health = self.calculate_health(self.player_two)
                    keep_playing = False
                    break
        self.display_winner(self.calculate_winner(player_one_health, player_two_health))

    def display_instructions(self):
        print('Welcome to Two Player Battleship!!!')
        print('Instructions:')
        print('1. Players will first take turns placing their ships on their boards')
        print('2. Once ship placement has been done, players will alternate turns attacking the other players\' ships')
        print('3. If you hit a ship - the other player\'s ship will lose health')
        print('4. When one (or both) players drop to zero health (AKA - all ships have been sunk), the player with remaining ships on the board WINS!')
        print('READY....SET.....GO!')
        print('*****************************************************************')
    
    
    def player_turn(self, player, opponent):
        print(f'{player.name}: Here is your attack board:')
        for i in player.attackboard.board:
            print(i)
        player.attack(opponent)
        
    def calculate_health(self, player):
        player_health = 0
        for ship in player.fleet.ships:
            player_health += ship.size
        return player_health

    def calculate_winner(self, player_one_health, player_two_health):
        if player_one_health > 0 and player_two_health > 0:
            return False
        else:
            if player_one_health == 0 and player_two_health == 0:
                return 'TIE'
            elif player_one_health == 0:
                return self.player_two.name
            else:
                return self.player_one.name

    
    def display_winner(self, outcome):
        print('THE WINNER IS.....')
        print(f'{outcome}!!!!!!')


battle = Battlefield()
battle.run_game()