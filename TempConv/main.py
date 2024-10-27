unit = input("Input Temp Unit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round(((temp * 9) / 5) + 32, 2)
    print(f"The Temp in Fahrenheit is {temp}°F.")
elif unit == "F":
    temp = round(((temp - 32) * 5) / 9, 2)
    print(f"The Temp in Celsius is {temp}°C.")
else:
    print("Invalid unit!")
