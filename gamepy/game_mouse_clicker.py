import random

bomb = Actor('mine')
bomb.pos =(50,50)
score = 0

def draw():
    screen.clear()
    screen.draw.text(f"score : {score}",(10,10))
    bomb.draw()

def update():
    bomb.x += 2
    if bomb.x > 800:
        bomb.x = 0

def on_mouse_down(pos, button):
    global score
    if bomb.collidepoint(pos):
        bomb.image = 'bomb_defused'
        sounds.eep.play()
        score += 1
        clock.schedule_unique(pop_a_mine,1)

def pop_a_mine():
    bomb.pos = random.randint(0,800),random.randint(0,600)
    bomb.image = 'mine'