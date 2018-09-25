def testgen(gen, value):
    for target in gen(value):
        print(target)


def create_cubes(n):
    for x in range(n):
        yield x**3


for id in create_cubes(999):
    print(id)

print(list(create_cubes(999)))


def gen_fibon(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for fib in gen_fibon(30):
    print(fib)

for l in iter('hello'):
    print(l)


def squaregen(n):
    for value in range(n):
        yield (value + 1)**2


testgen(squaregen, 5)

from numpy import random


def randy(hi, low):
    for _ in range(30):
        yield random.random_integers(low, hi)


for randomy in randy(900, 3):
    print(randomy)