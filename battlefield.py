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
        outcome = self.calculate_winner(self.player_one, self.player_two)
        while self.calculate_winner(self.player_one, self.player_two) == False:
            if player_one_turn == True:
                print('Player one, it is your turn')
                self.player_turn(self.player_one, self.player_two)
                player_one_turn = False
            else:
                print('Player two, it is your turn')
                self.player_turn(self.player_two, self.player_one)
                player_one_turn = True
        self.display_winner(outcome)

    def player_turn(self, player, opponent):
        print('Here is your attack board:')
        for i in player.attackboard.board:
            print(i)
        player.attack(opponent)
        

    def calculate_winner(self, player_one, player_two):
        player_one_health = 0
        player_two_health = 0
        for ship in player_one.fleet.ships:
            player_one_health += ship.size
        for ship in player_two.fleet.ships:
            player_two_health += ship.size
        if player_one_health > 0 and player_two_health > 0:
            return False
        else:
            if player_one_health == 0 and player_two_health == 0:
                return 'TIE'
            elif player_one_health == 0:
                return player_two
            else:
                return player_one

    def display_winner(self, outcome):
        print('THE WINNER IS.....')
        print(f'{outcome}!!!!!!')


battle = Battlefield()
battle.run_game()