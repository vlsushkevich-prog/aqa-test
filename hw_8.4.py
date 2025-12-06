import time


def wait_with_retry_until(timeout, interval):
    def decorator(func):
        def wrapper():
            start_time = time.time()
            attempt = 1
            while time.time() - start_time < timeout:
                result = func()
                if result:
                    return "Элемент найден"
                print(f"Попытка {attempt}: неуспешно")
                time.sleep(interval)
                attempt += 1
            return "Превышено максимальное время выполнения"
        return wrapper
    return decorator

@wait_with_retry_until(timeout = 3, interval = 0.5)
def element_visible():
    return time.time() % 3 < 2

print(element_visible())