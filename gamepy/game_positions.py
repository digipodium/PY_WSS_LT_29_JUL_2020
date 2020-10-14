WIDTH = 500
HEIGHT = 500

hero = Actor('gameboy')

def draw():
    screen.clear()
    hero.topleft = (250,250)
    hero.draw()
    hero.topright = (250,250)
    hero.draw()
    hero.midtop = (250,250)
    hero.draw()
    hero.midleft = (250,250)
    hero.draw()
    hero.midright = (250,250)
    hero.draw()
    hero.center = (250,250)
    hero.draw()
    hero.bottomleft = (250,250)
    hero.draw()
    hero.bottomright = (250,250)
    hero.draw()
    hero.midbottom = (250,250)
    hero.draw()