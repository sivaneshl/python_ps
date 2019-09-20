import sys


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:      # file obj can be used as an iterator
        # print(line.strip())     # same as sys.stdout.write
        sys.stdout.write(line)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
