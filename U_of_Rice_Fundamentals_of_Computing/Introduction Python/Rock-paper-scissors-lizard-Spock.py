__author__ = 'Linghuan'

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import simplegui
import random

def rpsls(name):
    print 'Play chooses', name

    comp_number = random.randrange(0,5,1)

    if comp_number == 0:
        comp ='rock'
        print 'Computer chooses', comp

    elif comp_number == 1:
        comp='Spock'
        print 'Computer chooses', comp

    elif comp_number == 2:
        comp='paper'
        print 'Computer chooses', comp

    elif comp_number == 3:
        comp='lizard'
        print 'Computer chooses', comp

    elif comp_number == 4:
        comp='scissors'
        print 'Computer chooses', comp


    if name == 'rock':
        player_number = 0

        if 4 > player_number - comp_number > 0 or player_number - comp_number == -4:
            print 'Player wins!'
            print ''

        if -4 < player_number - comp_number < 0 or player_number - comp_number == 4:
            print 'Computer wins!'
            print ''

        if player_number - comp_number == 0:
            print 'Player and computer tie!'
            print ''

    elif name == 'Spock':
        player_number = 1


        if 4 > player_number - comp_number > 0 or player_number - comp_number == -4:
            print 'Player wins!'
            print ''

        if -4 < player_number - comp_number < 0 or player_number - comp_number == 4:
            print 'Computer wins!'
            print ''

        if player_number - comp_number == 0:
            print 'Player and computer tie!'
            print ''

    elif name == 'paper':
        player_number = 2


        if 4 > player_number - comp_number > 0 or player_number - comp_number == -4:
            print 'Player wins!'
            print ''

        if -4 < player_number - comp_number < 0 or player_number - comp_number == 4:
            print 'Computer wins!'
            print ''

        if player_number - comp_number == 0:
            print 'Player and computer tie!'
            print ''


    elif name == 'lizard':
        player_number = 3


        if 4 > player_number - comp_number > 0 or player_number - comp_number == -4:
            print 'Player wins!'
            print ''

        if -4 < player_number - comp_number < 0 or player_number - comp_number == 4:
            print 'Computer wins!'
            print ''

        if player_number - comp_number == 0:
            print 'Player and computer tie!'
            print ''

    elif name == 'scissors':
        player_number = 4

        if 4 > player_number - comp_number > 0 or player_number - comp_number == -4:
            print 'Player wins!'
            print ''

        if -4 < player_number - comp_number < 0 or player_number - comp_number == 4:
            print 'Computer wins!'
            print ''

        if player_number - comp_number == 0:
            print 'Player and computer tie!'
            print ''


    else:

        print 'Please enter correct choice, and try again!'
        print ''




# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


