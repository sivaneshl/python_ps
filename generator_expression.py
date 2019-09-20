million_squares = (x*x for x in range(1000))
print(million_squares)  # at this point the generator object is just contained in the list
print(list(million_squares))    # just an iterator
print(list(million_squares))    # no more items because the iterator is exhausted



# generator to compute the sum of first 1000 numbers
# no memeory used
# it list is used, it should hold the value and store in memory
print(sum(x for x in range(1000)))