n = input("Number (separate by ,) ? ")
b = n.split(",")
a = []
for i in b:
    x = int(i)
    a.append(x)
print(sum(a))

