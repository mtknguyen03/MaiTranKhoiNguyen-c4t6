from turtle import *
hideturtle()
speed(0)
colormode(255)
width(3)
for i in range(3):
    color("pink")
    forward(100)
    left(120)
for i in range(4):
    color(153, 153, 0)
    forward(100)
    left(90)
for i in range(5):
    color(51, 102, 0)
    forward(100)
    left(72)
for i in range(6):
    color(76, 153, 0)
    forward(100)
    left(60)
for i in range(7):
    color(51, 0, 102)
    forward(100)
    left(360 / 7)
for i in range(8):
    color(76, 0, 153)
    forward(100)
    left(45)


mainloop()