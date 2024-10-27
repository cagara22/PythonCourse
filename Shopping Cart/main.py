foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (Q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter price of {food}: $"))
        prices.append(price)

print("-----CART-----")
for x, food in enumerate(foods):
    total += prices[x]
    print(f"{x + 1}. {food:>7} = ${prices[x]:<6.2f}")
print(f"Total = ${total}")
print("-----END-----")