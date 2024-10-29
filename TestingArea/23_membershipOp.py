fruit = "Banana"
numbers = [1, 2, 3, 4, 5]
ages = (1, 2, 4, 5, 6)
body_count = {1, 2, 3, 4, 5}
letters = {"A": 1, "B": 3, "C": 4}

letter = "B"
if letter in fruit:
    print(f"{letter} is in {fruit}")
else:
    print(f"{letter} is not in {fruit}")

letter = "C"
if letter not in fruit:
    print(f"{letter} is not in {fruit}")
else:
    print(f"{letter} is in {fruit}")