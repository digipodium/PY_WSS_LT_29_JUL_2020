WIDTH = 800
HEIGHT = 600

gb = Actor('gameboy')
gb.pos = (50,50)
box = Rect((20,400),(50,50)) # (x,y),(width,height)

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'red')
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

    box.x +=2
    if box.x > WIDTH:
        box.x=0
    
    if gb.x > WIDTH:
        gb.x=0

    if gb.colliderect(box):
        print("hit")
WIDTH = 800
HEIGHT = 600

gb = Actor('gameboy')
gb.pos = (50,50)
box = Rect((20,400),(50,50)) # (x,y),(width,height)

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'red')
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

    box.x +=2
    if box.x > WIDTH:
        box.x=0
        
    # character world limit
    if gb.x > WIDTH:
        gb.x=0
    if gb.y > HEIGHT:
        gb.y=0
    if gb.x < 0:
        gb.x= WIDTH
    if gb.y < 0:
        gb.y= HEIGHT
    
    if gb.colliderect(box):
        print("hit")