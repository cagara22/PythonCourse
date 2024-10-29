import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

print("Beat the Computer in Rock, Paper, Scissors!")
while True:
    choice = input("Enter your choice: ").lower()
    if choice in options:
        player = choice
        break
    else:
        print("Invalid Choice!")

print(f"Player: {player.capitalize()}")
print(f"Computer: {computer.capitalize()}")

if player == computer:
    print("Its a Draw!")
else:
    if player == options[0]:
        if computer == options[1]:
            print("Computer WON!")
        else:
            print("You WON!")
    elif player == options[1]:
        if computer == options[2]:
            print("Computer WON!")
        else:
            print("You WON!")
    elif player == options[2]:
        if computer == options[0]:
            print("Computer WON!")
        else:
            print("You WON!")
