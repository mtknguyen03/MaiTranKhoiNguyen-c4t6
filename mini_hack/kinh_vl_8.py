from turtle import *
shape("turtle")
speed(0)
n = input("Number of edges? ")
m = int(n)
for i in range(m):
    forward(100)
    left(360 / m)


mainloop()