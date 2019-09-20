import sys


def read_series(filename):
    # f = open(filename, mode="rt", encoding='utf-8')
    # series = []
    # for line in f:
    #     a = int(line.strip())
    #     series.append(a)
    # f.close()
    # return series

    try:
        f = open(filename, mode="rt", encoding='utf-8')
        return [int(line.strip()) for line in f]

    except Exception    :
        print("Exception")

    finally:
        f.close()


def main(filename):
    series = read_series(filename)
    print(series)


if __name__=="__main__":
    main(sys.argv[1])