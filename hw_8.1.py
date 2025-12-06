import time


def retry(times):
    def retry_decorator(func):
        def wrapper():
            attempts = 0
            while attempts < times:
                result = func()
                if result == "PASSED":
                    return result
                attempts += 1
                if attempts <= times:
                    print(f"Не успешно! Попытка номер: {attempts}")
            print("Попыток больше нет")
            return result
        return wrapper
    return retry_decorator

@retry(times=3)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())