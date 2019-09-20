# break and continue

for index in range(10):
    if index == 5:
        print("Hello")
        break
    print(index)

for index in range(10):
    if index == 5:
        continue
        print("Hello")
    print(index)
