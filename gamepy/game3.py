WIDTH = 500
HEIGHT = 500

circleXY  = 250, 250 
line1XYstart = 150,20
line1XYend = 150, 480
line2XYstart = 150,20
line2XYend = 350,20 
line3XYstart = 350,20
line3XYend = 350, 480 
line4XYstart = 150,480
line4XYend = 350,480 

def draw():
    screen.clear()
    screen.draw.circle( circleXY, 50, "white" )
    screen.draw.filled_circle( circleXY, 30, "red" )
    # COMPLICATED RECTANGLE BELOW
    screen.draw.line(line1XYstart, line1XYend,'purple')
    screen.draw.line(line2XYstart,line2XYend,'purple')
    screen.draw.line(line3XYstart,line3XYend,'purple')
    screen.draw.line(line4XYstart,line4XYend,'purple')