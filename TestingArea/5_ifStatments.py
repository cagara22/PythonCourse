age = int(input("Enter your age: "))

if age >= 100:
    print("Just die already")
elif age >= 18:
    print("You are now an adult!")
elif age < 0:
    print("You are still a sperm.!")
else:
    print("Still a baby...")

response = input("Do you want to die? (Y/N)")

if response == "Y":
    print("DIE!")
else:
    print("IDC... DIE!")

is_dead = True

if is_dead:
    print("he dead...")
else:
    print("he not dead...")
