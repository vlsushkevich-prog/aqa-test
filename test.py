"""Складывает, вычитает, умножает или делит два числа"""


def calculator(first_number, second_number, operator):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            return 'Деление на ноль'
        else:
            return first_number / second_number
    else:
        return 'Неподдерживаемый оператор'

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
operator = input('Введите оператор (+, -, *, /): ')
result = calculator(first_number, second_number, operator)
print(result)

"""Складывает, вычитает, умножает или делит неограниченное количество чисел (только один оператор)"""


def calculator(*numbers, operator):
    numbers = numbers[0]
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        return result
    elif operator == '*':
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
        return result
    elif operator == '/':
        result = numbers[0]
        for number in numbers[1:]:
            if number == 0:
                return 'Деление на ноль'
            else:
                result /= number
        return result

numbers = tuple(map(int, input('Введите числа через пробел: ').split()))
operator = input('Введите оператор (+, -, *, /): ')
print(calculator(numbers, operator = operator))





