def chain(iter1, iter2):
    for i in iter1:
        yield i
    for i in iter2:
        yield i

print(list(chain([1, 2], [3, 4])))