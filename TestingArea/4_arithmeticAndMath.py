import math

friends = 0
friends = friends + 5
friends += 5
print(friends)
friends = friends - 1
friends -= 1
print(friends)
friends = friends * 5
friends *= 5
print(friends)
friends = friends / 2
friends /= 2
print(friends)
friends = friends ** 2
friends **= 2
print(friends)
friends = friends % 2
print(friends)

x = 3.14
y = -4
z = 5

result = round(x)
print(result)
result = abs(y)
print(result)
result = pow(z, 2)
print(result)
result = max(x, y, z)
print(result)
result = min(x, y, z)
print(result)

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.ceil(10.5))
print(math.floor(10.5))

# Circumference
radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius
print(round(circumference, 2))

# Area of Circle
radius = float(input("Enter the radius: "))
area = math.pi * pow(radius, 2)
print(round(area, 2))

# Hypotenuse
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
hyp = math.sqrt(pow(a, 2) + pow(b, 2))
print(round(hyp, 3))