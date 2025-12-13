class TestResults:
    def __init__(self):
        self.results = {}

    def __setitem__(self, test_name, test_result):
        self.results[test_name] = test_result

    def __getitem__(self, test_name):
        return self.results[test_name]

    def __len__(self):
        return len(self.results)

results = TestResults()
results["test_login"] = "passed"
results["test_payment"] = "failed"
print(results["test_login"])
print(len(results))



