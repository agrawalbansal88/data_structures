
#################################
def dec1(f):
    print("DEC 1 depth 1")
    def wrapper():
        print("DEC 1 depth 2")
        retval  = f()
        return retval
    return wrapper

@dec1
def ActualFunc1():
    print("Actual 1 function called")

#################################

def dec2(f):
    print("DEC 2 depth 1")
    def wrapper(*args, **kwargs):
        print("DEC 2 depth 2 args={}, kwargs=[{}]".format(args, kwargs))
        retVal = f(*args, **kwargs)
        return retVal
    return wrapper

@dec2
def ActualFunc2(*args, **kwargs):
    print("Actual 2 function called args={}, kwargs=[{}]".format(args, kwargs))

#################################

def dec3(deckey):
    print("DEC 3 depth 1")
    def dec_wrapper(f):
        print("DEC 3 depth 2", deckey)
        def wrapper(*args, **kwargs):
            if deckey=="UPPER":
                print("DEC 3 depth 3 args={}, kwargs=[{}]".format(args, kwargs))
                for k, v in kwargs.items():
                    kwargs[k]=v.upper()
            print("DEC 3 depth 3 args={}, kwargs=[{}]".format(args, kwargs))
            retVal = f(*args, **kwargs)
            return retVal
        return wrapper
    return dec_wrapper

@dec3(deckey="UPPER")
def ActualFunc3(*args, **kwargs):
    print("Actual 3 function called args={}, kwargs=[{}]".format(args, kwargs))

#################################

class ClassDeco:
    def __init__(self, function):
        print("INIT_CALLED with function={}".format(function))
        self.function = function

    def __call__(self, *args, **kwargs):
        print("CALL INNER args={}, kwargs=[{}]".format(args, kwargs))
        retval= self.function(*args, **kwargs)
        return retval

@ClassDeco
def ClassDecoFunc(*args, **kwargs):
    print("ClassDecoFunc function called args={}, kwargs=[{}]".format(args, kwargs))


#################################
class ClassDeco1:
    def __init__(self, arg1, arg2, arg3):
        print(" 1 INIT_CALLED with function={} {} {}".format(arg1, arg2, arg3))
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        print("__call__ with function={}".format(f))
        def wrapper(*args, **kwargs):
            print("1 CALL INNER args={}, kwargs=[{}]".format(args, kwargs))
            retval= f(*args, **kwargs)
            return retval
        return wrapper

@ClassDeco1("hello", "world", 42)
def ClassDecoFunc2(*args, **kwargs):
    print("ClassDecoFunc2 function called args={}, kwargs=[{}]".format(args, kwargs))


#################################


def outer(f):
    def wrapper():
        print("outer entry", f)
        retval = f()
        print("outer exit")
        return retval
    return wrapper

def inner(f):
    def wrapper():
        print("inner entry", f)
        retval = f()
        print("inner exit")
        return retval
    return wrapper

@outer
@inner
def ClassMultiDecos():
    print("ClassMultiDecos")

if __name__=="__main__":
    print("-----------MIAN________")
    print()
    ActualFunc1()
    print()
    ActualFunc2(1,"Amk")
    print()
    ActualFunc3(1,"Amk", KEY1="value1")
    print()
    ClassDecoFunc(1, "Ank", key="key1")
    print()
    ClassDecoFunc2(1, "Ank", key="key1")

    print()
    ClassMultiDecos()