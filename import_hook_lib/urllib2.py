def urlopen(*args, **kwargs):
    print("dummy urlopen: {}".format(str(args)))
    print("** do something cool **")
    return args[0]
