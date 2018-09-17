from turtle import *
shape("turtle")
speed(0)
n = input("Radius? ")
m = int(n)
for i in range(1):
    forward(m)
    circle(m)

mainloop()