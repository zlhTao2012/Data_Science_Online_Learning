__author__ = 'Linghuan'

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math



Game_mode = 0

# helper function to start and restart the game
def new_game():

    global secret_number, guess_number, guess_allow, Game_mode

    guess_number = 0

    if Game_mode == 0:

        high = 100

        secret_number = random.randrange(0,100)

        print ""
        print "New game. Range is from 0 to 100."

    if Game_mode == 1:

        high = 1000

        secret_number = random.randrange(0,1000)

        print""
        print "New game. Range is from 0 to 1000."

    guess_allow = math.ceil(math.log(high - 0 + 1, 2))

    print "Guess number is", str(int(guess_number))+"."
    print "You have", str(int(guess_allow)), "time(s) to guess."

# define event handlers for control panel

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    global secret_number, guess_number, guess_allow, Game_mode

    Game_mode = 1

    guess_number = 0

    guess_allow = math.ceil(math.log(1000 - 0 + 1, 2))

    secret_number = random.randrange(0,1000)

    print ""
    print "New game. Range is from 0 to 1000."
    print "Guess number is", str(int(guess_number))+"."
    print "You have 7 time(s) to guess."
    print ""

def range100():

    # button that changes the range to [0,100) and starts a new game

    global secret_number, guess_number, guess_allow, Game_mode

    Game_mode = 0

    guess_number = 0

    guess_allow = math.ceil(math.log(100 - 0 + 1, 2))

    secret_number = random.randrange(0, 100)

    print ""
    print "New game. Range is from 0 to 100."
    print "Guess number is", str(int(guess_number))+"."
    print "You have 7 time(s) to guess."
    print ""



def input_guess(guess):

    global guess_number, guess_allow

    print ""
    print "Guess was", guess

    guess_numeric = float(guess)

    # main game logic goes here

    if guess_numeric > secret_number:
        print "Lower"

    if guess_numeric < secret_number:
        print "Higher"

    if guess_numeric == secret_number:
        print "Correct"



    guess_number = guess_number + 1

    guess_left = guess_allow - guess_number

    if guess_left > 0 and guess_numeric != secret_number:

        print "Guess number is", str(int(guess_number))+"."
        print "You have", str(int(guess_left)), "time(s) to guess."
        print ""

    elif guess_left >= 0 and guess_numeric == secret_number:

        print "Congratulation!"
        print ""
        new_game()

    else:

        print "You lose!"
        print ""

        new_game()

# create frame

frame = simplegui.create_frame('testing', 80, 150, 150)

frame.add_button('Range is [0, 100).', range100, 150)

frame.add_button('Range is [0, 1000).', range1000, 150)


# register event handlers for control elements and start frame

frame.add_input('Guess the number', input_guess, 150)

frame.start()


# call new_game
new_game()
