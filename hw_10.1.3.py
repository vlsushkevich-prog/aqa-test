class TestStats:
    def __init__(self, total, passed):
        self.total = total
        self.passed = passed

    @property
    def success_rate(self):
        return str((self.passed / self.total) * 100) + "%"

stats = TestStats(10, 8)
print(stats.success_rate)