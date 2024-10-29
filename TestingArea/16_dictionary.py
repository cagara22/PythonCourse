capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})
capitals.pop("China")
print(capitals)

keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)

items = capitals.items()
for country, capital in items:
    print(f"{country} = {capital}")
