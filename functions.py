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
    else:
        return 'Неподдерживаемый оператор'

numbers = tuple(map(int, input('Введите числа через пробел: ').split()))
operator = input('Введите оператор (+, -, *, /): ')
print(calculator(numbers, operator = operator))


"""2.1"""


test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]

passed_tests = list(filter(lambda x: x["status"] == "passed", test_results))
passed_tests_list = []
for tests in passed_tests:
    passed_tests_list.append(tests["name"])
print(passed_tests_list)


"""3.1"""


def apply_test_check(check_func, test_results):
    passed_count = 0
    for result in test_results:
        if check_func(result):
            passed_count += 1
    return passed_count

test_results = [
    {"staus": "passed"},
    {"staus": "failed"},
    {"staus": "passed"}
]

result = apply_test_check(lambda x: x["staus"] == "passed", test_results)
print(f"Прошло тестов: {result}")


"""4.1"""


def generate_report(title, *test_names, format="html", **options):
    print(f"Отчет: {title}")
    print(f"Формат: {format}")
    total_test_names = ""
    for i, test in enumerate(test_names):
        total_test_names += test
        if i == len(test_names) - 1:
            break
        else:
            total_test_names += ", "
    print(f"Тесты: {total_test_names}")
    for option, option_value in options.items():
        print(f"{option}: {option_value}")

generate_report("Daily Report", "test1", "test2", "test3",
                format = "pdf", author = "Tester")