class Tag:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, cls):
        cls.tag = self.tag
        return cls


@Tag("Smoke")
class SmokeTests:
    pass

@Tag("Regression")
class RegressionTests:
    pass

print(SmokeTests.tag)
print(RegressionTests.tag)
