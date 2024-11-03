import os
import json
import csv

txt_data = "I love you more that you'll ever know!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"'{file_path}' has been created!")

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"'{file_path}' has been created!")
except FileExistsError:
    print("That file already exist!")

append_txt = "I love you, Nicole!"
with open(file_path, "a") as file:
    file.write("\n" + append_txt)
    print(f"'{file_path}' has been appended!")

employee = {
    "name": "Vincent Felix",
    "age": 23,
    "position": "IT Teacher",
    "friends": ("Patrick", "Sandy", "Squidward")
}

file_path = "output.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"Json file '{file_path}' has been created!")

employees = [["Name", "Age", "Job"],
             ["Spongebob", 25, "Cook"],
             ["Patrick",  35, "Idiot"],
             ["Squidward", 40, "Cashier"]]

file_path = "output.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"Csv file '{file_path}' has been created!")
