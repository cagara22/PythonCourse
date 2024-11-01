class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a Circle with a area of {3.14 * pow(self.radius, 2)}cm^2.")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle = Circle("red", True, 5)
square = Square(color="blue", is_filled=False, width=10)
triangle = Triangle("yellow", False, 10, 10)

print(circle.color, circle.is_filled, circle.radius)
print(square.color, square.is_filled, square.width)
print(triangle.color, triangle.is_filled, triangle.width, triangle.height)

circle.describe()
square.describe()
triangle.describe()
