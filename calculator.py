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