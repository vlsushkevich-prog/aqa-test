class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Двигаюсь со скоростью {self.speed}")

class Car(Vehicle):
    def honk(self):
        print("Бип-бип!")

car = Car(100)
car.move()
car.honk()