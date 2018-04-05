# Nicholas A. Zwan
# P4T1
# Draw a triangle and a square using turtle and loops.
# 03/19/18

import turtle
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Tess & Alex')

tess = turtle.Turtle()
tess.color ('hotpink')
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)



