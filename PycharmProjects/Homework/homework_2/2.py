from turtle import *
hideturtle()
speed(0)
colormode(255)
for i in range(10):
    fillcolor((i + 1) * 35 % 175, (i + 1) * 35 % 255, 75)
    begin_fill()
    for x in range(4):
        forward(200 - i * 15)
        left(90)
    left(30)
    end_fill()
mainloop()
