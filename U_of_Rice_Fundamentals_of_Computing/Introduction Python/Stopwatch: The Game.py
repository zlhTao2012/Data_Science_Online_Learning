__author__ = 'Linghuan'

import simplegui

#global integer
n = 0

#global game trial counter integer
y = 0 # Total counts
x = 0 # Success counts

# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = int(t/600)
    X = t%600
    B = int(X/100)
    C = int((X-B*100)/10)
    D = X-B*100-C*10
    text =  str(A)+':'+str(B)+str(C)+'.'+str(D)
    return text

#create a timer handler
def timer_handler():
    global n
    global x
    n = n + 1
    return n

timer = simplegui.create_timer(100, timer_handler)


#create a event handler

frame = simplegui.create_frame("Canvas",200,300)

def draw(canvas):
    sf = str(x)+'/'+str(y)
    canvas.draw_text(format(n), (99, 149), 20, "Green")
    canvas.draw_text(sf, (169, 20), 20, "Green")




frame.set_draw_handler(draw)

frame.start()

#Create start, stop and rest button

def start_handler():
    timer.start()

def stop_handler():
    global n
    global y
    global x
    timer.stop()
    y = y + 1
    if n%10 == 0:
        x = 1 + x

def reset_handler():
    global n
    global y
    global x
    timer.stop()
    n = 0
    y = 0
    x = 0
    frame.set_draw_handler(draw)



button1 = frame.add_button('Start', start_handler, 50)
button2 = frame.add_button('Stop', stop_handler, 50)
button3 = frame.add_button('Reset', reset_handler, 50)
