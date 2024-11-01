import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" 0 ",
                   " | ",
                   "   "),
               3: (" 0 ",
                   "/| ",
                   "   "),
               4: (" 0 ",
                   "/|\\",
                   "   "),
               5: (" 0 ",
                   "/|\\",
                   "/  "),
               6: (" 0 ",
                   "/|\\",
                   "/ \\")}


def display_man(num_of_guesses: int):
    art = hangman_art[num_of_guesses]
    print("___")
    for line in art:
        print(line)
    print("___")


def display_hint(hint: list, word: str, char: str):
    for index, letter in enumerate(word):
        if letter == char:
            hint[index] = char
    return "".join(hint)


def display_answer(guess_word: str, answer_word: str):
    if guess_word == answer_word:
        return True


def main():
    word_to_guess = random.choice(words)
    hint = ["_"] * len(word_to_guess)
    guesses = 0
    answer = ""
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(guesses)
        word_hint = display_hint(hint, word_to_guess, answer)
        is_guessed = display_answer(word_to_guess, word_hint)
        print(f"Guess the word: {word_hint}")

        if guesses < 6:
            if is_guessed:
                is_running = False
                print(f"Congratulation! You guessed the word '{word_to_guess}'")
            else:
                while True:
                    answer = input("Enter a letter: ").lower()

                    if len(answer) != 1 or not answer.isalpha():
                        print("Invalid Input! Try again...")
                        continue

                    if answer in guessed_letters:
                        print(f"You've already guess the letter '{answer}'! Try again...")
                        continue

                    guessed_letters.add(answer)
                    if answer not in word_to_guess:
                        guesses += 1
                    break

        else:
            print(f"The Correct Word was {word_to_guess}")
            is_running = False


if __name__ == "__main__":
    main()
