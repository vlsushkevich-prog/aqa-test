from enum import Enum


class TestType(Enum):
    UI = 'UI'
    API = 'API'
    UNIT = 'UNIT'

tests = [
    ('test_login_api', TestType.API),
    ('test_login_ui', TestType.UI),
    ('test_sum', TestType.UNIT),
    ('test_profile_api', TestType.API),
    ]

def filter_tests_by_type(tests, test_type: TestType):
    return [test[0] for test in tests if test[1] == test_type]

print(filter_tests_by_type(tests, TestType.API))
print(filter_tests_by_type(tests, TestType.UI))
print(filter_tests_by_type(tests, TestType.UNIT))
