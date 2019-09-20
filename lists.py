# list - mutable

l =  "show how to index a list".split()
print(l)
print(l[3])

# negative index
print(l[-4])    # starts at -1

# slicing
print(l[1:3])
print(l[1:-1])
print(l[3:])
print(l[:3])
print(l[:])

# copying lists - 3 ways
i = l[:]    # full slice
print(i)

j = l.copy()    # copy method
print(j)

k = list(l)     # list consturctor
print(k)

k[2] = "jack"
print(l)
print(k)


# list repetition
c = [12, 45]
d = c * 4
print(d)

c = [0] * 9
print(c)

# search using index
w = "how how to search a word in a list".split()
i = w.index("search")
print(i)
print(w[i])

# count matching elements
i = w.count('a')
print(i)

# in and not in
print(37 in [23, 45, 37, 95, 33])
print(37 not in [23, 45, 37, 95, 33])

# del using index
s = [23, 45, 37, 95, 33]
del s[3]
print(s)

# remove using value
s.remove(37)
print(s)

# insert
s.insert(2, 88)
print(s)

# concate lists using +
s1 = [3, 4, 6]
s2 = [9, 5, 2]
s3 = s1 + s2
print(s3)

s3 += [8, 2, 3]
print(s3)

s3.extend([4, 2, 5])
print(s3)

# reverse list
s3.reverse()
print(s3)

# sort
s3.sort()
print(s3)
s3.sort(reverse=True)   # reverse sort
print(s3)

# sort by key eg: len
text = "This path will take you from the basics of the Python language all the way up to working with web frameworks and" \
       " programming a Raspberry Pi".split()
text.sort(key=len)
print(text)
print(' '.join(text))


# sorted()
x = [4, 9, 2, 1]
y = sorted(x)
print(x)
print(y)

# reversed
z = reversed(x)
print(z)
print(list(z))

