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
        #player attacks other player
        self.player_turn(self.player_one, self.player_two)
        # game tallies scores/health of ships to see where things stand, if player two is still alive, then:
        #round summary: print out a summary of
        #if either player has all ships sunk, game is over
        #display winner

    def player_turn(self, player, opponent):
        print('Player, it is your turn')
        print('Here is your attack board')
        #print attack board
        player.attack(opponent)
        for i in player.attackboard.board:
            print(i)

    def calculate_score(self):
        #calculates each players score
        pass

battle = Battlefield()
battle.run_game()