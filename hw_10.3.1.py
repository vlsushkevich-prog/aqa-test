from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Прямоугольник. Площадь {self.width * self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Круг. Площадь {self.radius ** 2}"

shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    print(s.area())
