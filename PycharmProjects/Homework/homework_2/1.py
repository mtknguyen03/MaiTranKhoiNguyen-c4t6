from turtle import *
hideturtle()
speed(0)
colormode(255)
for i in range(5):
    fillcolor(0,(i + 1) * 35 % 255, 0)
    begin_fill()
    for x in range(4):
        forward(200 - i * 25)
        left(90)
    end_fill()
mainloop()