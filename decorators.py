def say_hello(func):
    print("Начинается тест")
    return func

@say_hello
def test():
    print("Тест запущен")

test()

def check_positive_args(func):
    def wrapper(*args):
        func(*args)
        if args[0] > 0:
            print("Аргумент положительный")
        else:
            print("Ошибка: Аргумент должен быть положительным")
    return wrapper

@check_positive_args
def process_number(num):
    print(f"Обрбатываем число {num}")

process_number(-6)

def decorator_wrapper(tag_name):
    def tag(func):
        def wrapper():
            print(f"[{tag_name}] Начало функции display")
            func()
        return wrapper
    return tag


@decorator_wrapper("DEBUG")
def display():
    print("Выполняется display")

display()