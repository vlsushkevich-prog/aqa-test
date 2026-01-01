from hw_13_4 import counter


def take(n, iterable):
    for i in iterable:
        if n > 0:
            yield i
            n -= 1
        else:
            break

c = counter(100)
print(list(take(5, c)))