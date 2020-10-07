
HEIGHT = 500
WIDTH = 500

box = Rect((20,20),(50,50))

def draw():
    screen.clear()
    screen.draw.filled_rect(box,'green')

def update():
    box.x += 2
    box.y += 3
    if box.x > WIDTH:
        box.x = 0 
    if box.y > HEIGHT:
        box.y = 0
  

# task
# make the box movie faster
# make the box move in top to bottom direction
# make two box of diffrent color and move then