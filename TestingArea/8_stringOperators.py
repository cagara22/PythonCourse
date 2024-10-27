name = input("Enter name: ")
phone_number = input("Enter Phone Number: ")
print(len(name))
print(name.find("cent"))
print(name.rfind("t"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(phone_number.count("-"))
print(phone_number.replace("-", " "))

username = input("Enter a Username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters!")
elif username.find(" ") >= 0:
    print("Must have no spaces!")
elif not username.isalpha():
    print("Must not contain any number!")
else:
    print(f"Welcome {username}!")
