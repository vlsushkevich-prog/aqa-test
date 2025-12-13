def print_length(obj):
    print(len(obj))

class TestCollection:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)

print_length("Python")
print_length([1, 2, 3])
print_length({"a": 1, "b": 2})
print_length(TestCollection([10, 20, 30, 40]))
