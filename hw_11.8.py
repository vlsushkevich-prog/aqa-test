def calculator():
    expression = input('Введите выражение: ')
    try:
        result = eval(expression)
        print(result)
    except ZeroDivisionError:
        print('Невозможно выполнить операцию из-за деления на ноль')
    except SyntaxError:
        print('Неверный оператор, либо отсутствуют операнды')
    except NameError:
        print('Операнды должны быть числами')

calculator()