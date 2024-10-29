import random

number1 = random.randint(1, 6)
number2 = random.random()
options = ("rock", "paper", "scissors")
option1 = random.choice(options)
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)

print(number1)
print(round(number2, 2))
print(option1)
print(cards)
