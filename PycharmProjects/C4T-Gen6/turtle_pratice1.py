from turtle import *
import math
speed(0)
shape("turtle")
hideturtle()

left(90)

lv = 11
l = 100
s = 17

penup()
backward(l)
pendown()
forward(l)

def draw_tree(l, level):
    l = 3/4 * l
    left(s)
    forward(l)
    level += 1
    if level < lv:
        draw_tree(l, level)

    backward(l)
    right(2*s)
    forward(l)
    if level <= lv:
        draw_tree(l, level)
    backward(l)
    left(s)
    level -= 1

draw_tree(l, 1)



mainloop()