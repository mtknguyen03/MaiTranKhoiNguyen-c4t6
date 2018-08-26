from turtle import *

turtle_list = []
for _ in range(5):
    turtle_list.append(Turtle())

n = len(turtle_list)
print("I have", n, "turtles")

position = int(input("Which one do you want to control? "))
color_str = input("What color? ")
shape_str = input("What shape? ")
cmd = input("What command? ")

cmd_list = cmd.split(" ")
t = turtle_list[position - 1]
t.color(color_str)
t.shape(shape_str)
for cmd in cmd_list:
    if cmd == "fd":
        t.forward(100)
    elif cmd == "bd":
        t.backward(100)
    elif cmd == "lt":
        t.left(90)
    elif cmd == "rt":
        t.right(90)

mainloop()