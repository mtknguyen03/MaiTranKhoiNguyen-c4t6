from turtle import *

n = input("Colors (separate by ,) ? ")
a = n.split(",")

for i in a:
    color(i)
    forward(100)
    penup()
    pendown()

mainloop()