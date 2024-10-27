fruits = ["apples", "oranges", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][0])
print(groceries[1][1])
print(groceries[2][2])

for foods in groceries:
    for food in foods:
        print(food, end=" ")
    print()

keypad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ('*', 0, '#'))

for row in keypad:
    for key in row:
        print(key, end=" ")
    print()


