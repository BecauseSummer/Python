# –*–coding:utf-8 –*–
# 2021-07-09 10:10
__author__ = ''
# def my_abs(x):
#
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(my_abs(8))

# def fcat(n):
#     if n == 1:
#         return 1
#     return n * fcat(n - 1)
#
# print(fcat(5))

# s = set([1,3,  3, 2])
# print(s)


# def f(x):
#     return x * x
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

# def normalize(name):
#     return name.capitalize()
# L1 = ['adam', 'LIsa', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# a = 'PYTHON'
# a = a.capitalize()
# print(a)

# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#
#
# print (list(filter(lambda n: n % 2 ==1, range(1, 20))))

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @log('exeute')
# def now():
#     print('2021-7-9')
#
# now()

import math

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()