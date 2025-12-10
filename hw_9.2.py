class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 80000)

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name, 40000)

manager = Manager("Иван")
print(manager.salary)
developer = Developer("Петр")
print(developer.salary)
