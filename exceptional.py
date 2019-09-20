def convert1(s):
    try:
        x = int(s)
        print("Success")
    except ValueError as e:
        x = -1
        print("Failure", e)
    except TypeError as e:
        x = -1
        print("Failure", e)
    return x


def convert(s):
    x = -1
    try:
        x = int(s)
        print("Success")
    except (ValueError, TypeError) as e:
        print("Failure", e)
    return x

# programmer errors -
    ''' Indentation error
        Syntax error
        Name error  
        
        These errors should not be captured as they should be identified during development
        '''


def convert_pass(s):
    # Use Pass statement
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError) as e:
        pass
    return -1


def convert_1(s):
    # use simply return
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        return -1


# printing the error
def convert_print(s):
    # use simply return
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion Error: {0}".format(str(e)))
        return -1




