
# global variables
xycoords = 400,300
radius = 100
WHITE = 255,255,255
BLACK = 0,0,0
GREEN = 0,255,0

bg = WHITE

def draw():
    screen.clear()
    screen.fill(bg)
    screen.draw.circle( xycoords, radius , GREEN )

def on_mouse_down():
    global bg               # telling us that bg is global variable
    bg = BLACK              # then on we can change the global one

def on_mouse_up():
    global bg
    bg = WHITE