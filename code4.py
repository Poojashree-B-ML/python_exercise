class arg:
    def print_func(a1, b1, *args, **kwargs):
        print(a1, b1)
        print(args)
        print(kwargs)
obj=arg()
obj.print_func(1, 2, "a", "c",45, a=4, b=5,m="d", l=5)
