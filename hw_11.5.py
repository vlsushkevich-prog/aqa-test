from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

tasks = [
    ('Починить тест логина', Priority.HIGH),
    ('Обновить документацию', Priority.LOW),
    ('Настроить CI', Priority.MEDIUM),
    ]

tasks_sorted = sorted(tasks, key=lambda task: task[1].value)

for name, prio in tasks_sorted:
    print(prio.name, '-', name)

