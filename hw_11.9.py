from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)
print(p2)
print(p2.x)
