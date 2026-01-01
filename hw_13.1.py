def even_numbers(iterable):
    for num in iterable:
        if num % 2 == 0:
            yield num

print(list(even_numbers([1, 2, 3, 4, 5, 6])))