#NiceHexSpiral.py
import turtle   
colors=['red', 'purple', 'blue',
        'green', 'yellow', 'teal']
t=turtle.Pen()
t.speed(15)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/9999+1)
    t.forward(x)        
    t.left(59)