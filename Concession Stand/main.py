menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("---------MENU---------")
for food, price in menu.items():
    print(f"{food:<10} = ${price:.2f}")
print("-----------------------")

while True:
    choice = input("Enter chosen food (Q to Quit): ").lower()

    if choice == "q":
        break

    if choice in menu.keys():
        cart.append(choice)
        total += menu.get(choice)
        print(f"{choice.capitalize()} added to cart!")
    else:
        print(f"{choice.capitalize()} is not in the Menu!")

print("---------CART---------")
for item in cart:
    print(f"{item:^10}")
print(f"TOTAL: ${total:.2f}")
print("----------------------")
