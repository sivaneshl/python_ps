# default argument
def defaultarg(name, gender="m"):
    print(name, gender)


defaultarg("Joe")
defaultarg("Kate", "f")
defaultarg(name="Mark", gender="m")


# variable arguments
def vararg(name, *args):
    print(name)
    print(args)


vararg("Jack", "hello", None, 93939, True)


def var_keyword_args(name, **kwargs):
    print(name)
    print(kwargs["last_name"], kwargs["feedback"])


var_keyword_args("Jack", last_name="Dawson", feedback=None, id=93939, subscriber=True)