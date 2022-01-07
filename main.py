# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# importing Classes
from Property import Property
from Square import Square
from Player import Player
from Action import Action

print('Start Successful!')

# global variables later defined in the create players function
global num_players
global player_list
global player_name
global p_curr_loc


# start of the methods

# create players. ask user
def create_players():
    num_players = int(input("How many players? "))
    player_list = []
    for x in range(num_players):
        print("X: ", x)
        player_name = input("Name:")
        # when creating players we are using a number as an ID. This is for future checking
        player = Player(x, player_name, 0, 10)
        player_list.insert(x, player)

    print(player_list[0].description())


# method for charging people rent
def rent():
    p_curr_loc = player_list[turn].location
    if p_curr_loc > 33:
        p_curr_loc -= 33
        player_list[turn].balance += 2


# create different types of squares aka properties
# 0 = Property: name, occupancy, rent
COURT = Property(0, "Court Street", False, 1)
KING = Property(0, "King Street", False, 1)
STATE = Property(0, "State Street", False, 2)
COLONIAL = Property(0, "Colonial Street", False,2)
MILL = Property(0, "Mill Street", False, 2)
COTTAGE = Property(0, "Cottage Street", False, 2)
WEST = Property(0, "West Street", False, 3)
NORTH = Property(0, "North Street", False, 3)
CHERRY = Property(0, "Cherry Street", False, 3)
ORCHARD = Property(0, "Orchard Street", False, 3)
SPRING = Property(0, "Spring Street", False, 4)
SUMMER = Property(0, "Summer Street", False, 4)
ELM = Property(0, "Elm Street", False, 4)
SPRUCE = Property(0, "Spruce Street", False, 4)
CENTER = Property(0, "Center Street", False, 5)
MAIN = Property(0, "Main Street", False, 5)
# 1 = Chance: draw chance card
chance = Square(1)
# 2 = RailRoad: Roll again
railroad = Square(2)
# 3 = Pay for supplies
tax = Square(3)
# 4 = Go to Lunch
lunch = Square(4)
# 5 = Pass Go
go = Square(5)
# 6 = lunch/free time
free = Square(6)

# create an set called game board. It is an array of squares
game_board = [go, chance, COURT, KING, chance, railroad, STATE, COLONIAL, tax, chance, free, MILL, COTTAGE, railroad,
              WEST, NORTH, free, chance, CHERRY, ORCHARD, chance, railroad, SPRING, SUMMER, tax, chance, lunch, ELM,
              SPRUCE, railroad, CENTER, MAIN]

# start of the logic
create_players()

test = False
while not test:

    turn = 0
    if turn > num_players:
        turn = 0

    # roll the dice
    roll_dice = Action.roll()
    # move the player
    player_list[turn].location += roll_dice
    # checking for rent charge.
    rent()

    location_value = game_board[p_curr_loc].value

    # property. There needs to be some logic here that checks to see if the property is owned,
    # and if yes pay that specific player rent. Otherwise buy the property and set that property to owned.

    if location_value == 0:
        if game_board[p_curr_loc].player:
            player_list[turn].balance -= game_board[p_curr_loc].rent

    # chance
    elif location_value == 1:
        pass
    # railroad
    elif location_value == 2:
        pass
    # tax
    elif location_value == 3:
        pass
    # lunch
    elif location_value == 4:
        pass
    # go
    elif location_value == 5:
        pass
    # free time
    elif location_value == 6:
        pass

    x = 0
    for i in player_list:
        if player_list[i].balance <= 0:
            x = x + 1
            if num_players == x:
                test = False
        else:
            x = 0