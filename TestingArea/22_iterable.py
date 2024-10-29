numbers = [1, 2, 3, 4, 5]
ages = (1, 2, 4, 5, 6)
body_count = {1, 2, 3, 4, 5}
letters = {"A": 1, "B": 3, "C": 4}

for number in numbers:
    print(number)

for age in ages:
    print(age, end=" - ")

for body in body_count:
    print(body)

for key, value in letters.items():
    print(f"{key}: {value}")
