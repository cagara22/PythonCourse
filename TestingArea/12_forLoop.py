for i in range(1, 11):
    print(i)

for i in reversed(range(1, 11)):
    print(i)

for i in range(1, 11, 2):
    print(i)

name = "Vincent"
for i in name:
    print(i)

for i in range(1, 21):
    if i == 13:
        print("Hell naw!")
        continue
    print(i)

for i in range(1, 21):
    if i == 13:
        print("Hell naw!")
        break
    print(i)