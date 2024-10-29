import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
is_guessed = False
guesses = 0

print(f"Guess the Number between {lowest_num} - {highest_num}!")

while True:
    number = input("Enter your guess (Q to Quit): ")
    if number.isdigit():
        number = int(number)
        if number < lowest_num or number > highest_num:
            print("You are out of the range!")
            guesses += 1
        elif number < answer:
            print("Too low! Guess again!")
            guesses += 1
        elif number > answer:
            print("Too High! Guess again!")
            guesses += 1
        else:
            is_guessed = True
            guesses += 1
            break
    else:
        if number.lower() == "q":
            break
        else:
            print("Invalid Guess! That is not a Number!")
            guesses += 1

if is_guessed:
    print(f"Correct! The number was {answer}!")
    print(f"It took you {guesses} guesses!")
else:
    print(f"You didn't guess the number. It was {answer}.")
    print(f"You guess {guesses} times.")
