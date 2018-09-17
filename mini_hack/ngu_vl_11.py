n = input("Month (number not name)? ")
m = int(n)
if m == 1 and 3 and 5 and 7 and 8 and 10 and 12:
    print("There are 31 days in this month")
elif m == 4 and 6 and 9 and 11:
    print("There are 30 days in this month")
elif m == 2:
    print("There are 28 or 29 days in this month(it depends)")
else:
    print("Are you drunk?")
