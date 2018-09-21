# def spy(*args):
#     strl = [x for x in args if x == 0 or x == 7]
#     has = '007' in ''.join(str(x) for x in strl)
#     return has

# print(spy(1, 2, 3, 4, 0, 1, 0, 2, 7, 10))

# l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

# def func(n):
#     return n % 3 == 0

# nl = list(filter(func, l))

# print(nl)

# l = [
#     23,
#     4235,
#     26,
#     2436,
#     54,
#     6543,
#     6,
#     546,
#     34,
#     6345,
#     6,
#     354,
#     6345,
#     56,
#     254,
#     63546,
# ]

# print(list(filter(lambda num: num > 100, l)))

# from math import pi

# def vol(rad):
#     return round((4 / 3) * (pi) * (rad ** 3), 2)

# print(vol(10))

# def surfacearea(rad):
#     return round(4 * (pi) * (rad ** 2), 2)

# print(surfacearea(10))

# def ran_check(num, low, high):
#     return num <= high and num >= low

# from collections import Counter

# def up_low(s):
#     t = tuple(Counter(s).elements())
#     u = list(filter(lambda v: v.isupper(), t))
#     l = list(filter(lambda v: v.islower(), t))
#     print(f'Uppercase: {len(u)}')
#     print(f'Lowercase: {len(l)}')

# up_low('Hello World')


def _calculate(x, y, z):
    return (x / y) / (y / z)


print(_calculate(10, 20, 30))
