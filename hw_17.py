import argparse


parser = argparse.ArgumentParser(description='Performs simple calculations', prog='Calculator')
parser.add_argument('num1', help='First number')
parser.add_argument('num2', help='Second number')
parser.add_argument('operator', choices=['+', '-', '*', '/'],
                    help='Operation to perform')
args = parser.parse_args()

def calculator(first_number, second_number, operator):
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        return 'Операнды должны быть числами'

    print('Результат:')
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

print(calculator(args.num1, args.num2, args.operator))