class BaseTest:
    def run(self, *args):
        pass

class APITest(BaseTest):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def run(self):
        print(f"{self.__class__.__name__}: проверяем эндпоинт {self.endpoint}")

class UITest(BaseTest):
    def __init__(self, page):
        self.page = page

    def run(self):
        print(f"{self.__class__.__name__}: проверяем страницу {self.page}")

def run_all(tests):
    for test in tests:
        test.run()

tests = [APITest("/login"),
         UITest("LoginPage"),
         APITest("/users")]
run_all(tests)
