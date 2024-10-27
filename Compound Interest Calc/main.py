principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: "))
    if principle < 0:
        print("Principle can't be below $1!")
    else:
        break


while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate can't be below or equal to zero!")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("Time can't be below or equal to zero!")
    else:
        break

print(principle, rate, time)

total = principle * pow(1 + (rate / 100), time)
print(f"You're compound interest will be ${total:,.2f}")
