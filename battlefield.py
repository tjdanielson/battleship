from player import Player

class Battlefield:
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
    
    def run_game(self):
        #both players put ships on board
        print('Player One: Place your fleet of ships!')
        self.player_one.place_fleet()
        print('Player Two: Place your fleet of ships!')
        self.player_two.place_fleet()
        #players take turns:
        player_one_turn = True
        keep_playing = True
        while keep_playing == True:
            if player_one_turn == True:
                print('Player one, it is your turn')
                self.player_turn(self.player_one, self.player_two)
                player_one_turn = False
                if self.calculate_health(self.player_two) == 0:
                    player_two_health = 0
                    player_one_health = self.calculate_health(self.player_one)
                    keep_playing = False
                    break
            else:
                print('Player two, it is your turn')
                self.player_turn(self.player_two, self.player_one)
                player_one_turn = True
                if self.calculate_health(self.player_one) == 0:
                    player_one_health = 0
                    player_two_health = self.calculate_health(self.player_two)
                    keep_playing = False
                    break
        self.display_winner(self.calculate_winner(player_one_health, player_two_health))

    def player_turn(self, player, opponent):
        print('Here is your attack board:')
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
                return 'PLAYER TWO'
            else:
                return 'PLAYER ONE'

    
    def display_winner(self, outcome):
        print('THE WINNER IS.....')
        print(f'{outcome}!!!!!!')


battle = Battlefield()
battle.run_game()