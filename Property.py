# import the squares class. Property will be a sub class of square.
from Square import Square
# this class also needs to be updated to hold a player, or no player at all

class Property(Square):
    def __init__(self, value, name, player, rent):
        super().__init__(value)
        self.name = name
        self.player = player
        self.rent = rent

    # Instance method
    def description(self):
        return print(self.value, self.name, self.player, self.rent)

