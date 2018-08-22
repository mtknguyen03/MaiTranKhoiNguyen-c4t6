from turtle import *
shape("turtle")
speed(0)
color_list = ["red", "blue", "brown", "yellow", "gray"]
for colors in color_list:
    color(colors)
    fillcolor(colors)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()


hideturtle()
mainloop()