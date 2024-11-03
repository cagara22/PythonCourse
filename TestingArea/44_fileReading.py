import json
import csv

file_path_txt = "output.txt"
file_path_json = "output.json"
file_path_csv = "output.csv"

try:
    with open(file_path_txt, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as ex:
    print(f"File Not Found: {ex}")
except PermissionError as ex:
    print(f"Permission Denied: {ex}")


try:
    with open(file_path_json, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError as ex:
    print(f"File Not Found: {ex}")
except PermissionError as ex:
    print(f"Permission Denied: {ex}")


try:
    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError as ex:
    print(f"File Not Found: {ex}")
except PermissionError as ex:
    print(f"Permission Denied: {ex}")
