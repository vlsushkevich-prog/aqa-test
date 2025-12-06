import time


def cache_results(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def count_exec_time(func):
    def wrapper(n):
        print(f"Выполняю expensive_calculation c аргументом: {n}")
        start = time.time()
        result = func(n)
        end = time.time()
        exec_time = round(end - start, 2)
        print(f"Время выполнения: {exec_time}")
        return result
    return wrapper

@count_exec_time
@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(3)
    return n * n

print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(6))
print(expensive_calculation(5))