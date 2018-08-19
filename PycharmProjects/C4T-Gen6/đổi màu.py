from turtle import *
hideturtle()
speed(0)
width(3)
for i in range(12):
    n = i % 3
    for y in range(3):
        if n == 1 or n == 2:
            color("blue")
        else:
            color("red")
        forward(20)
        penup()
        forward(10)
        pendown()

mainloop()
