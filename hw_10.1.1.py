class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            print("Отрицательную цену задать нельзя")

p = Product(100)
print(p.price)
p.price = 250
print(p.price)
p.price = -10
print(p.price)