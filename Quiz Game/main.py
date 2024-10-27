questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the Human body?: ",
            "Which planet in the solar system is the hottest?: ")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0

for x, question in enumerate(questions):
    print("--------------------------------------------------------")
    print(question)
    for option in options[x]:
        print(option)
    while True:
        answer = input("Enter Letter (A-D): ")
        if answer.upper() in ("A", "B", "C", "D"):
            if answer.upper() == answers[x]:
                print("CORRECT!")
                score += 1
            else:
                print(f"INCORRECT! Correct answer is {answers[x]}.")
            guesses.append(answer.upper())
            break
        print("Invalid option! Try again...")

print("-------RESULT------")
print("Answers", end=": ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses", end=": ")
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Score is {int((score / len(questions)) * 100)}%")
print("-------------------")
