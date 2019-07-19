#!/usr/bin/env python
def is_subsequence(a, b):
    b = iter(b)
    print(b)

    gen = (i for i in a)
    print(gen)

    for i in gen:
        print(i)

    print("===>")
    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print(i)

    print("####\n")
    return all(((i in b) for i in a))

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
