# raise valueError exception instead of zero division error


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {0}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("End of tests")
    except ValueError as e:
        print("Value Error", str(e))
    print("Program execution complete")


if __name__ == "__main__":
    main()
