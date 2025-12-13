class TestRunner:
    def __init__(self, tests):
        self.tests = tests

    def __call__(self):
        print("Запускаем тесты")
        for test in self.tests:
            print(f"- {test}")
        print(f"Всего тестов {len(self.tests)}")

runner = TestRunner(["test_login", "test_signup", "test_payment"])
runner()