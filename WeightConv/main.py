weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ")

if unit == "K":
    weight = round(weight * 2.205, 3)
    unit = "Lb"
elif unit == "L":
    weight = round(weight / 2.205, 3)
    unit = "Kg"
else:
    print("Invalid Unit!")

print(f"Your weight is {weight}{unit}")
