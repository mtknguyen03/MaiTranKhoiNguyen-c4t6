H = float(input("Height:"))
print(H, "m")
M = float(input("Mass:"))
print(M, "kg")
BMI = M / (H * H)
print("BMI = ",BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")