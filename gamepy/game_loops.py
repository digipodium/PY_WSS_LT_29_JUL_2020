import random
WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    # for x in range(0,500,100):
    #     screen.draw.filled_circle((x,20),50,'red')
    colors= ['red','green','blue']
    for x in range(0,WIDTH,10):
        for y in range(0,HEIGHT,10):
            # print(x,y)
            box = Rect((x,y),(5,5))
            screen.draw.filled_rect( box,random.choice(colors))
    