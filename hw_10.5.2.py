class Duration:
    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        return f"{self.duration} sec"

    def __add__(self, other):
        return Duration(self.duration + other.duration)

d1 = Duration(1.5)
d2 = Duration(2.7)
d3 = d1 + d2
print(d1)
print(d2)
print(d3)