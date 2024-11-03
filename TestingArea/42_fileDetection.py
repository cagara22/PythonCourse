import os

file_path_rel = "stuff/test.txt"
file_path_abs = "C:\\Users\\Vincent Felix Cagara\\Desktop\\test_folder\\Documents"

if os.path.exists(file_path_abs):
    print(f"The location of '{file_path_abs}' exist")
    if os.path.isfile(file_path_abs):
        print("Its a file!")
    else:
        print("Its not a file!")
else:
    print("That location does not exist!")
