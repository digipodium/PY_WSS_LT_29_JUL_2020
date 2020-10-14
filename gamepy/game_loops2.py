gb = Actor('gameboy')
fence = Actor('fence')

def draw():
    screen.clear()
    for x in range(0,800,70):
        fence.bottomleft= (x,600)
        fence.draw()
    gb.draw()