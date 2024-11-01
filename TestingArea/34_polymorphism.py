from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 + pow(self.radius, 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Circle(5), Square(10), Triangle(5, 4), Pizza("pineapple", 9)]

for shape in shapes:
    print(shape.area())
