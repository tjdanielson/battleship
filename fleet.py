from ship import Ship

class Fleet:
    def __init__(self):
        self.ships = []
        self.create_fleet()

    def create_fleet(self):
        destroyer = Ship('Destroyer', 2)
        submarine = Ship('Submarine', 3)
        battleship1 = Ship('Battleship 1', 4)
        battleship2 = Ship('Battleship 2', 4)
        aircraft_carrier = Ship('Aircraft Carrier', 5)
        self.ships.extend([destroyer, submarine, battleship1, battleship2, aircraft_carrier])
        # for i in self.ships:
        #     print(i.name)
        #     print(i.size)


