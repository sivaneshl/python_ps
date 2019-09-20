words = "Are you a programming beginner? Maybe you've just started, or maybe you've taken a couple of entry-level programming classes and want to learn more. The beginner courses here will show you the basics of object-oriented programming (OOP) while teaching you the simple and functional Python programming language. When you've completed this section, you'll be ready to move on to improving your code quality.".split()

lengths = []
for word in words:
    lengths.append(len(word))
print(lengths)

# the comprehension for the above
print([len(word) for word in words])

from math import factorial
f = [factorial(x) for x in range(20)]
print(f)
print(type(f))
