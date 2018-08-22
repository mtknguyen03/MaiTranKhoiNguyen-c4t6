sheep_list = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Nguyen and this is my sheep sizes")
print(sheep_list)
m = max(sheep_list)
print("Now my biggest sheep has size", m, "let's shear it")
max_index = sheep_list.index(max(sheep_list))
sheep_list[max_index] = 8
print("After shearing this is my flock")
print(sheep_list)
for i in range(1, 3):
    print("Month", i, ":")
    print("One month has passed, here is my flock:")
    sheep_list = [sheep + 50 for sheep in sheep_list]
    print(sheep_list)
    m = max(sheep_list)
    print("Now my biggest sheep has size", m, "let's shear it")
    max_index = sheep_list.index(max(sheep_list))
    sheep_list[max_index] = 8
    print("After shearing this is my flock")
    print(sheep_list)
print("Month", 3, ":")
print("One month has passed, here is my flock:")
sheep_list = [sheep + 50 for sheep in sheep_list]
print(sheep_list)
s = sum(sheep_list)
print("My flock has size in total:", s)
money = s * 2
print("I would get", s, "* 2$ =", money, "$")
