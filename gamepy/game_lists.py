boxes =[]
for i in range(10):
    boxes.append(Actor('bluebox',topleft=(i*70,0)))

def draw():
    screen.clear()

    for box in boxes:
        box.draw()

def on_mouse_down(pos, button):
    boxes.append(Actor('bluebox',pos))
