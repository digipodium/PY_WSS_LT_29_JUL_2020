WIDTH = 500
HEIGHT = 500

gameboy = Actor('gameboy_happy')
gameboy.pos = (50,450)

bg = Actor('background')

def draw():
    screen.clear()
    bg.draw()
    gameboy.draw()

def update():
    gameboy.x +=2
    if gameboy.x>WIDTH:
        gameboy.x=0

