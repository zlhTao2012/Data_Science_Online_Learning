__author__ = 'Linghuan'

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import simplegui
import random

def name_to_number(name):

    if name == 'rock':
        player = 0


    elif name == 'Spock':
        player = 1


    elif name == 'paper':
        player = 2


    elif name == 'lizard':
        player = 3


    elif name == 'scissors':
        player = 4


    return player


def number_to_name(number):


    if number == 0:
        comp ='rock'


    elif number == 1:
        comp='Spock'


    elif number == 2:
        comp='paper'


    elif number == 3:
        comp='lizard'


    elif number == 4:
        comp='scissors'

    print 'Computer chooses', comp

    return comp

def rpsls(player_choice):

    print ''

    print 'Player chooses', player_choice

    name_to_number(player_choice)

    number = random.randrange(0,5,1)

    number_to_name(number)



    diff = (name_to_number(player_choice) - number)%5

    if diff == 1 or diff == 2:
        print 'Player wins!'

    elif diff == 3 or diff == 4:
        print 'Computer wins!'

    else:
        print 'Player and computer tie!'


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
