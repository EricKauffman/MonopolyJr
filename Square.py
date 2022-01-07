# value is what will be used to determine the type of square the player lands on

class Square:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
