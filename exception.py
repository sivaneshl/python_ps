from math import log


def convert(s):
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion Failure: {0}". format(str(e)))
        # return -1
        raise   # re-raise the exception to the caller

def string_log(s):
    v = convert(s)
    try:
        return log(v)
    except (ValueError) as e:
        print("Log Failure: ", format(str(e)))
    return -1


string_log('abcd')
