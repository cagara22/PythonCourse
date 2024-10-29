def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello", last="Felix", title="Mr.", first="Vincent")

print("hello", end=" - ")
print("hi", end="\n")
print(1, 2, 3, 4, 5, sep=" - ")


def create_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = create_phone(country=1, area=123, first=456, last=7890)

print(phone_num)
