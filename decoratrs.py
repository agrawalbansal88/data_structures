def abc(arg1):
    def wrapper(f1):
        def func(*arg, **kwarg):
            print("abc", arg1)
            return f1(*arg, **kwarg)
        return func
    return wrapper

@abc("MAMA")
def Ankur(p,q):
    print "ANKUR", p, q


Ankur(10, 11)
