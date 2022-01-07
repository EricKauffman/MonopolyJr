"""
id: for specifying the specific player and to use in its dictionary of properties
name: visual for user
location: keep track of where it is on the board
balance: keep track of how much money they have
"""


class Player:
    def __init__(self, p_id, name, location, balance):
        self.id = p_id
        self.name = name
        self.location = location
        self.balance = balance

    def description(self):
        return self.id, self.name, self.location, self.balance
