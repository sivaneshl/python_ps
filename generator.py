def gen123():
    yield 1
    yield 2
    yield 3
    # implicit return statement here

g = gen123()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # this will result in a StopIteration exception

for v in gen123():
    print(v)

h = gen123()
i = gen123()
print(h, i)     # h and i are different and can be advanced independent of each other
print(h is i)
print(next(h))
print(next(h))
print(next(i))





