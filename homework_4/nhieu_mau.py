from turtle import *
shape("turtle")
speed(0)
color_list = ["red", "blue", "brown", "yellow", "gray"]
angle = 0
times = 3
for c in color_list:
    color(c)
    angle = angle + 180
    for i in range(times):
        forward(100)
        left(180 - (angle / times))
    times = times + 1
hideturtle()
mainloop()