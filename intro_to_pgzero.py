# pip install pgzero
# pgzrun intro_to_pgzero.py

hero = Actor('gameboy')
hero.topright = 0,10

HEIGHT = 500
WIDTH = 1500

def draw():
    screen.clear()
    hero.draw()

def update():
    hero.left += 2
    if hero.left > WIDTH:
        hero.right = 0    

def on_mouse_down(pos):
    if hero.collidepoint(pos):
        sounds.eep.play()
        hero.image = 'gameboy_hurt'
        clock.schedule_unique(set_hero_normal,.3)


def set_hero_normal():
    hero.image = 'gameboy'