import time


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        result = round(end - start, 2)
        print(func.__name__ , f"выполнился за {result} сек")
        print(func())
    return wrapper

@timer
def slow_test():
    time.sleep(3)
    return "OK"

slow_test()