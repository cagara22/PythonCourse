doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

triples = [x * 3 for x in range(1, 11)]

print(triples)

even = [x for x in range(1, 21) if x % 2 == 0]

print(even)
