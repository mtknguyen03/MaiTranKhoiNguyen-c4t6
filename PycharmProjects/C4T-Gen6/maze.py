from turtle import *

colormode(255)
speed(0)
width(4)
for i in range(200):
    color((i * 4) % 255, (i * 5) % 255, 0)
    forward(i * 4)
    left(90)



mainloop()
