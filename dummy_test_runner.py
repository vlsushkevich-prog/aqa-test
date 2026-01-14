def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

results = {'total_tests': 0, 'passed': {'passed_amount': 0, 'passed_percentage': 0.0},
           'failed': {'failed_amount': 0, 'failed_percentage': 0.0, 'errors': []}}

for result, expected in tests:
    results['total_tests'] += 1

    try:
        assert result == expected
    except AssertionError as e:
        message = (f"Тест не пройден! Ожидается что пароль результат {expected}, " +
                   f"но фактический результат {result}")
        print(message)

        if message not in results['failed']['errors']:
            results['failed']['errors'].append(message)

        results['failed']['failed_amount'] += 1
        continue

    print("Тест прошёл!")
    results['passed']['passed_amount'] += 1

results['failed']['failed_percentage'] = round(results['failed']['failed_amount'] /
                                               results['total_tests'] * 100, 2)
results['passed']['passed_percentage'] = round(results['passed']['passed_amount'] /
                                               results['total_tests'] * 100, 2)
