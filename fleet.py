from ship import Ship

class Fleet:
    def __init__(self):
        self.ships = []
        self.create_fleet()

    def create_fleet(self):
        destroyer = Ship('Destroyer', 1, 'D ')
        #submarine = Ship('Submarine', 2, 'S ')
        # battleship1 = Ship('Battleship 1', 4, 'B ')
        # battleship2 = Ship('Battleship 2', 4, 'B ')
        # aircraft_carrier = Ship('Aircraft Carrier', 5, 'A ')
        self.ships.extend([destroyer])
        # for i in self.ships:
        #     print(i.name)
        #     print(i.size)


