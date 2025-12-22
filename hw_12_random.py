import random as rnd


"""Задания 1, 6, 8"""


def roll_dice():
    return f'На кубике выпало: {rnd.randint(1, 6)}'

def run_flaky_test():
    return 'FAILED' if rnd.random() < 0.3 else 'PASSED'

def generate_test_data(n):
    return rnd.choices(range(101), k=n)

print(roll_dice())
print(run_flaky_test())
print(generate_test_data(6))