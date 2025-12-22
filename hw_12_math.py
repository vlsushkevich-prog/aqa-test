import math


"""Задания 1, 3, 6, 10"""


def circle_area(radius):
    print(f'Площадь круга радиусом {radius} равна {math.pi * (radius ** 2)}')

def sin_angle(angle):
    print(f'Синус угла {angle} равен {math.sin(math.radians(angle))}')

def tan_angle(angle):
    print(f'Тангенс угла {angle} равен {math.tan(math.radians(angle))}')

circle_area(5)
sin_angle(45)
tan_angle(60)
print(math.exp(3))