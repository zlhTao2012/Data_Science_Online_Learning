__author__ = 'Linghuan'
# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals

def new_game():
    global state, list_combined, expose, Turns

    state = 0

    Turns = 0

    expose = ['Down'] * 16

    list_1 = [num + 1 for num in range(8)]

    list_2 = [num + 1 for num in range(8)]

    random.shuffle(list_1)

    random.shuffle(list_2)

    list_combined = list_1 + list_2

    #print list_combined


# define event handlers

def mouseclick(pos):
    global expose, state, list_combined, n_th_card, prior_n, prior_2_n, Turns

    click_pos = list(pos)

    n_th_card = click_pos[0] // 50

    # add game state logic here

    if state == 0:

        expose[n_th_card] = 'Up'

        prior_n = n_th_card

        state = 1

    elif expose[n_th_card] == 'Down':

        if state == 1:

            expose[n_th_card] = 'Up'

            state = 2

            Turns += 1

        else:

            expose[n_th_card] = 'Up'

            state = 1

            if list_combined[prior_2_n] != list_combined[prior_n]:
                expose[prior_2_n] = 'Down'

                expose[prior_n] = 'Down'



        prior_2_n = prior_n

        prior_n = n_th_card



    label.set_text("Turns = " + str(Turns))


# cards are logically 50x100 pixels in size
def draw(canvas):
    global expose, list_combined

    canvas.draw_line((0, 0), (0, 100), 4, 'Yellow')

    canvas.draw_line((0, 0), (800, 0), 4, 'Yellow')

    canvas.draw_line((0, 100), (800, 100), 4, 'Yellow')

    for i in range(16):

        canvas.draw_line(((i + 1) * 50, 0), ((i + 1) * 50, 100), 4, 'Yellow')

        if expose[i] == 'Up':

            canvas.draw_text(str(list_combined[i]), ((i * 50 + 20), 50), 25, 'Red')

        else:

            canvas.draw_text('', ((i * 50 + 25), 50), 12, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0 ")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric