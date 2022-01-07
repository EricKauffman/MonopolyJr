# This is a sample Python script.
"""
This is the notes section

Current main issue is the inability to keep track of who owns what and if that property is owned.
I noticed this when I tried to charge players rent

My current idea is to change the players to own properties in a list. Then have a dictionary to store
all of the properties with. The key on the property is going to correspond to who owns it
it might be 0 for no ownership. Then I will assign ownership

However this also needs to be accessible to the classes. When I do an action i need to be able to send the player
to a certain location. So I need to be able to access a dictionary of squares or something similar and say go to square
id 7 for example

I can return this id from the methods in my action class.

Do I want to run a check on everything every turn?
For example do I want to check to see if I have passed go? and therefore should I be doing that for every action?

This would require a pass go checker, something that is possible to create. But my worry here is that this game becomes
extremely memory extensive. The game would become very slow. However I think there is a way to store it all for later in
a dictionary

I need to solve the pass go issue and I think I will work on that later. The first step is going to be to solve what is
above. To create something to keep track of player ownership

"""
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# importing Classes
from Property import Property
from Square import Square
from Player import Player
from Action import Action

print('Start Successful!')

# global variables later defined in the create players function
num_players = 0
player_list = []
global player_name
p_curr_loc = 0


# start of the methods

# create players. ask user
def create_players():
    num_players = int(input("How many players? "))
    player_list = []
    for x in range(num_players):
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


# square checker
def square_checker():
    location_value = game_board[p_curr_loc].value
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


# create different types of squares aka properties
# 0 = Property: name, occupancy the number corresponds to owning players id, rent, id
COURT = Property(0, "Court Street", 0, 1, 0)
KING = Property(0, "King Street", 0, 1, 0)
STATE = Property(0, "State Street", 0, 2, 0)
COLONIAL = Property(0, "Colonial Street", 0, 2, 0)
MILL = Property(0, "Mill Street", 0, 2, 0)
COTTAGE = Property(0, "Cottage Street", 0, 2, 0)
WEST = Property(0, "West Street", 0, 3, 0)
NORTH = Property(0, "North Street", 0, 3, 0)
CHERRY = Property(0, "Cherry Street", 0, 3, 0)
ORCHARD = Property(0, "Orchard Street", 0, 3, 0)
SPRING = Property(0, "Spring Street", 0, 4, 0)
SUMMER = Property(0, "Summer Street", 0, 4, 0)
ELM = Property(0, "Elm Street", 0, 4, 0)
SPRUCE = Property(0, "Spruce Street", 0, 4, 0)
CENTER = Property(0, "Center Street", 0, 5, 0)
MAIN = Property(0, "Main Street", 0, 5, 0)
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

# create players
create_players()

test = False
while not test:

    turn = 0
    if turn > num_players:
        turn = 0

    # roll the dice
    roll_dice = Action.roll()
    # move the player
    if player_list[turn].location > 33:
        player_list[turn].location -= 33
    player_list[turn].location += roll_dice

    # checking for rent charge.
    rent()

    square_checker()

    x = 0
    for i in player_list:
        if player_list[i].balance <= 0:
            x = x + 1
            if num_players == x:
                test = False
        else:
            x = 0