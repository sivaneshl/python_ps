def minmax(items):
    return min(items), max(items)

items = [23, 68, 93, 73, 71, 90, 2]
print(minmax(items))

# tuple unpacking - unpack data structures into named references
min, max = minmax(items)
print(min, max)


# tuple unpacking with nested tuples
(a, (b, (c, d))) = (1, (2, (3, 4)))
print(a, b, c, d)


# construct a tuple from list
a = tuple([83, 74, 83, 22, 84])
print(a, type(a))

# in operator
print(5 in (3,5,7,9))
print(5 not in (3,5,7,9))


