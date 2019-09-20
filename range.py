# range is a collection
# arithmetic progression of integers

print(range(5))     # supply the stop value

for i in range(5):
    print(i)

range(5, 10)    # starting value 5; stop value 10
print(list(range(5, 10)))   # wrapping this call to the list

print(list(range(0, 10, 2))) # 2 is the step argument

# enumerate - to count
t = [6, 44, 532, 2232, 534536, 36443643]
for i in enumerate(t):      # enumerate returns a tuple
    print(i)

# tuple unpacking of enumerate
for i, v in enumerate(t):
    print("i={} v={}".format(i,v))
    



