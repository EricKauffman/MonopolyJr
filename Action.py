import random


class Action:

    def free_property(self):
        pass

    def go_to_go(self):
        pass

    def go_to_pay(self):
        pass

    @staticmethod
    def roll():
        dice_sides = [1, 2, 3, 4, 5, 6]
        return random.choice(dice_sides)

    def pass_go(self):
        return 2

    def pick_chance(self):
        seq = [1, 2, 3]
        result = random.choice(seq)

        property_locations = [0, 2, 3, 5, 6, 7, 11, 12, 13, 14, 15, 18, 19, 21, 22, 23, 27, 28, 29, 30, 32, 33]

        # go to property
        if result == 1:
            return random.choice(property_locations)

        elif result == 2:
            pass
        elif result == 3:
            pass