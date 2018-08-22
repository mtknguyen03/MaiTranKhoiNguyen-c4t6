item_list = ["T-Shirt", "Sweater"]
while True:
    a = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if a == "R":
        print("Our item:", item_list)
    elif a == "C":
        b = input("Enter New item: ")
        item_list.append(b)
        print("Our items:", item_list)
    elif a == "U":
        c = int(input("New position: "))
        d = input("New item: ")
        item_list.insert(c - 1, d)
        print("Our items:", item_list)
    elif a == "D":
        e = int(input("Remove position: "))
        item_list.pop(e - 1)
        print("Our items:", item_list)
    else:
        print("Who do you think you are, get out of my shop!")