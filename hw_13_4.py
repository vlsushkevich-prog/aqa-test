def counter(start):
    while True:
        yield start
        start += 1

if __name__ == '__main__':
    c = counter(10)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))