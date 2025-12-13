class LoggingMixin:
    def log(self):
        print("[Log] Выполняем задачу")

class RetryMixin():
    def retry(self, tries = 3):
        for i in range(1, tries + 1):
            print(f"Попытка {i}")
            self.run()

class Job(RetryMixin, LoggingMixin):
    def run(self):
        self.log()
        print("Job что-то делает...")

j = Job()
j.retry(2)
