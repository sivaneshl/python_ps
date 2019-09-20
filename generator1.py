def gen246():
    print('about to yield 2')
    yield 2
    print('about to yield 4')
    yield 4
    print('about to yield 6')
    yield 6
    print('about to return')


print('assign g')
g = gen246()

print('next g')
print(next(g))

print('next g')
print(next(g))

print('next g')
print(next(g))

print('next g')
print(next(g))



