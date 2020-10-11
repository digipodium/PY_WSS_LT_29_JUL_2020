gb = Actor('gameboy_happy')
gb.pos = (50,50)


def draw():
    screen.clear()
    gb.draw()

def update():
    if keyboard.right :
        gb.x += 2
    elif keyboard.left:
        gb.x -= 2
    elif keyboard.up:
        gb.y -= 2
    elif keyboard.down:
        gb.y += 2

