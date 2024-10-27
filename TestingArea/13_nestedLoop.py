for i in range(3):
    for j in range(1, 10):
        print(j, end="")
    print()

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
symbols = input("Enter symbol: ")

for i in range(rows):
    for j in range(cols):
        print(symbols, end="")
    print()