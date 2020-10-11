gb = Actor('gameboy')
gb.pos = (50,50)
box = Rect((20,400),(100,100)) # (x,y),(width,height)

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'blue')
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

    # box will chase
    if box.x < gb.x:
        box.x += 1
    if box.x > gb.x:
        box.x -= 1
    if box.y < gb.y:
        box.y += 1
    if box.y > gb.y:
        box.y -= 1

    if gb.colliderect(box):
        sounds.eep.play()
        gb.image = 'gameboy_hurt'
    else:
        gb.image = 'gameboy'


# task 
# - make 2 zombie an enemy
# and handle collision with a another image of character
