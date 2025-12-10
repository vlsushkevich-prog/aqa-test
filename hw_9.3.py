import math


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.height = length

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(5, 3)
print(rectangle.area())
circle = Circle(5)
print(circle.area())

