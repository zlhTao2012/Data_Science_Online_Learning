__author__ = 'Linghuan'

# Implementation of classic arcade game Pong

import simplegui
import random
import math


# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = 1
RIGHT = 0



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos # these are vectors stored as lists

    ball_vel_loc= [0,0]

    if direction == RIGHT:
        ball_vel_loc[0] += random.randrange(12, 24)
        ball_vel_loc[1] += random.randrange(6, 18)

    else:
        ball_vel_loc[0] -= random.randrange(12, 24)
        ball_vel_loc[1] += random.randrange(6, 18)

    ball_pos = [sum(x) for x in zip(ball_pos, ball_vel_loc)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global ball_pos, ball_vel
    global direction
    score1 = 0
    score2 = 0


    paddle1_pos = [[0,199-40],[8,199-40],[8,199+40],[0,199+40]]
    paddle1_vel = [0,0]
    paddle2_pos = [[WIDTH-8,199-40],[WIDTH,199-40],[WIDTH,199+40],[WIDTH-8,199+40]]
    paddle2_vel = [0,0]

   # ball_pos=[299,399]

   # ball_vel=[5,0.01]

    ball_pos=[299,199]

    ball_vel=[0,0]
    if random.randrange(0,2) == 0:
        sign1 = -1
    else:
        sign1 = 1

    if random.randrange(0,2) == 0:
        sign2 = -1
    else:
        sign2 = 1

    ball_vel[0] = 3.5*sign1
    ball_vel[1] = random.randrange(2,7)*sign2



def draw(canvas):
    global score1, score2
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] + BALL_RADIUS >= HEIGHT or ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = - ball_vel[1]
        ball_pos = [sum(x) for x in zip(ball_pos, ball_vel)]
        if ball_pos[1] > 379:
            ball_pos[1] = 381
        if ball_pos[1] < 20:
            ball_pos[1] = 18

    else:
        ball_pos = [sum(x) for x in zip(ball_pos, ball_vel)]

        if ((ball_pos[1] + BALL_RADIUS >= paddle1_pos[1][1] and ball_pos[1] - BALL_RADIUS < paddle1_pos[1][1]) or (ball_pos[1] - BALL_RADIUS >= paddle1_pos[1][1] and ball_pos[1] + BALL_RADIUS <= paddle1_pos[2][1]) or (ball_pos[1] - BALL_RADIUS <= paddle1_pos[2][1] and ball_pos[1] + BALL_RADIUS > paddle1_pos[2][1])) and ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
            spawn_ball(RIGHT)
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1

        if (paddle1_pos[1][1] < ball_pos[1] + BALL_RADIUS or ball_pos[1] - BALL_RADIUS > paddle1_pos[2][1]) and ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
            score2 += 1

            ball_pos=[299,199]

            ball_vel=[0,0]

            paddle1_pos = [[0,199-40],[8,199-40],[8,199+40],[0,199+40]]
            paddle1_vel = [0,0]
            paddle2_pos = [[WIDTH-8,199-40],[WIDTH,199-40],[WIDTH,199+40],[WIDTH-8,199+40]]
            paddle2_vel = [0,0]

            if random.randrange(0,2) == 0:
                sign2 = -1
            else:
                sign2 = 1

            ball_vel[0] = 3.5
            ball_vel[1] = random.randrange(2,7)*sign2


        if ((ball_pos[1] + BALL_RADIUS >= paddle2_pos[0][1] and ball_pos[1] - BALL_RADIUS < paddle2_pos[0][1]) or (ball_pos[1] - BALL_RADIUS >= paddle2_pos[0][1] and ball_pos[1] + BALL_RADIUS <= paddle2_pos[3][1]) or (ball_pos[1] - BALL_RADIUS <= paddle2_pos[3][1] and ball_pos[1] + BALL_RADIUS > paddle2_pos[3][1])) and WIDTH - (ball_pos[0] + BALL_RADIUS) < PAD_WIDTH:
            spawn_ball(LEFT)
            ball_vel[0] = -ball_vel[0]*1.1
            ball_vel[1] = ball_vel[1]*1.1


        if (paddle2_pos[0][1] < ball_pos[1] + BALL_RADIUS or ball_pos[1] - BALL_RADIUS > paddle2_pos[3][1]) and WIDTH - (ball_pos[0] + BALL_RADIUS) < PAD_WIDTH:
            score1 += 1

            ball_pos=[299,199]

            ball_vel=[0,0]


            paddle1_pos = [[0,199-40],[8,199-40],[8,199+40],[0,199+40]]
            paddle1_vel = [0,0]
            paddle2_pos = [[WIDTH-8,199-40],[WIDTH,199-40],[WIDTH,199+40],[WIDTH-8,199+40]]
            paddle2_vel = [0,0]

            if random.randrange(0,2) == 0:
                sign2 = -1
            else:
                sign2 = 1

            ball_vel[0] = -3.5
            ball_vel[1] = random.randrange(2,7)*sign2




    print ball_pos
    print ball_vel
    print paddle1_pos
    print paddle2_pos

    # draw ball
    canvas.draw_circle(ball_pos, 20, 1, 'Green', 'White')



    # update paddle's vertical position, keep paddle on the screen

    paddle1_pos[0] = [sum(x) for x in zip(paddle1_pos[0], paddle1_vel)]
    paddle1_pos[1] = [sum(x) for x in zip(paddle1_pos[1], paddle1_vel)]
    paddle1_pos[2] = [sum(x) for x in zip(paddle1_pos[2], paddle1_vel)]
    paddle1_pos[3] = [sum(x) for x in zip(paddle1_pos[3], paddle1_vel)]
    if paddle1_pos[0][1] < 0:
        paddle1_pos[0] = [0,0]
        paddle1_pos[1] = [8,0]
        paddle1_pos[2] = [8,80]
        paddle1_pos[3] = [0,80]
    if paddle1_pos[3][1] > HEIGHT:
        paddle1_pos[0] = [0,399-80]
        paddle1_pos[1] = [8,399-80]
        paddle1_pos[2] = [8,399]
        paddle1_pos[3] = [0,399]
    paddle1_vel = [0,0]



    paddle2_pos[0] = [sum(x) for x in zip(paddle2_pos[0], paddle2_vel)]
    paddle2_pos[1] = [sum(x) for x in zip(paddle2_pos[1], paddle2_vel)]
    paddle2_pos[2] = [sum(x) for x in zip(paddle2_pos[2], paddle2_vel)]
    paddle2_pos[3] = [sum(x) for x in zip(paddle2_pos[3], paddle2_vel)]
    if paddle2_pos[0][1] < 0:
        paddle2_pos[0] = [599-8,0]
        paddle2_pos[1] = [599,0]
        paddle2_pos[2] = [599,80]
        paddle2_pos[3] = [599-8,80]
    if paddle2_pos[3][1] > HEIGHT:
        paddle2_pos[0] = [599-8,399-80]
        paddle2_pos[1] = [599,399-80]
        paddle2_pos[2] = [599,399]
        paddle2_pos[3] = [599-8,399]
    paddle2_vel = [0,0]


    # draw paddles
    canvas.draw_polygon([paddle1_pos[0],paddle1_pos[1],paddle1_pos[2],paddle1_pos[3]], 2, 'White', 'White')
    canvas.draw_polygon([paddle2_pos[0],paddle2_pos[1],paddle2_pos[2],paddle2_pos[3]], 2, 'White', 'White' )

    # draw scores
    canvas.draw_text(str(score1), [(WIDTH / 2) - 70, HEIGHT / 2 ], 50, 'Yellow')
    canvas.draw_text(str(score2), [(WIDTH / 2) + 50, HEIGHT / 2 ], 50, 'Yellow')


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
       paddle1_vel = [sum(x) for x in zip(paddle1_vel, [0,40])]

    if key == simplegui.KEY_MAP["down"]:
       paddle2_vel = [sum(x) for x in zip(paddle2_vel, [0,40])]


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = [sum(x) for x in zip(paddle1_vel, [0,-40])]


    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = [sum(x) for x in zip(paddle2_vel, [0,-40])]

def button_handler():
    new_game()



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# create restart button
button1 = frame.add_button('Restart', button_handler, 200)

# start frame
new_game()
frame.start()
