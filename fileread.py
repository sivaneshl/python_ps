f = open('wasteland.txt', mode='rt', encoding='utf-8')

# read method to read chars
# pointer moves
print(f.read(32))
print(f.read())
print(f.read())
f.seek(0)   # move the pointer back to start
print(f.read())
f.seek(0)

# readline()
# reads each line
# pointer moves
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)

# readlines
# reads lines into a list
print(f.readlines())

# close
f.close()


