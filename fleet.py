from ship import Ship

class Fleet:
    def __init__(self):
        self.ships = []
        self.create_fleet()

    def create_fleet(self):
        destroyer = Ship('Destroyer', 3, 'D ')
        submarine = Ship('Submarine', 2, 'S ')
        battleship1 = Ship('Battleship 1', 4, 'B1')
        battleship2 = Ship('Battleship 2', 4, 'B2')
        aircraft_carrier = Ship('Aircraft Carrier', 5, 'A ')
        self.ships.extend([destroyer, submarine, battleship1, battleship2, aircraft_carrier])
    

    def display_fleet_health(self):
        for ship in self.ships:
                print(f'Ship: {ship.name} Health: {ship.size}')
        print('**********************************************************')


