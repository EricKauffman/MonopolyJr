class Player:
    def __init__(self, p_id, name, location, balance):
        self.id = p_id
        self.name = name
        self.location = location
        self.balance = balance

    def description(self):
        return self.id, self.name, self.location, self.balance
