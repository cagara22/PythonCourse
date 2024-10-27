name = input("Enter name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}!")