from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1

    def total(self):
        return self.price * self.quantity

p1 = Product('Keyboard', 50.0, 2)
p2 = Product('Mouse', 25.0)
print(p1.name, 'total:', p1.total())
print(p2.name, 'total:', p2.total())

