#https://www.codementor.io/sheena/advanced-use-python-decorators-class-function-du107nxsv
def time_this(original_function):
    print "decorating"
    def new_function(*args,**kwargs):
        print "starting timer"
        import datetime
        before = datetime.datetime.now()
        x = original_function(*args,**kwargs)
        after = datetime.datetime.now()
        print "Elapsed Time = {0}".format(after-before)
        return x
    return new_function

def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to 
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and 
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__): # it is an instance method
                return time_this(x)                 # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls

#now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):
    def a(self):
        print "entering a"
        import time
        time.sleep(3)
        print "exiting a"

###############################################
def deco2(val):
    print "deco2 start"
    def deco(f):
        print "deco start"
        def inner2(*args, **kwargs):
            print "inner2 start"
            ret_val = f(*args, **kwargs)
            print "inner2 end"
            return ret_val
        print "deco end"
        return inner2
    print "deco2 end"
    return deco

@deco2(val=10)
def f2(x):
    print"F2"
    print x
    return x+3

###############################################
def deco1(f):
    print "deco1 start"
    def inner1(*args, **kwargs):
        print "inner1 start"
        ret_val = f(*args, **kwargs)
        print "inner1 end"
        return ret_val
    print "deco1 end"
    return inner1


@deco1
def f1(x):
    print"F1"
    print x
    return x+2


###############################################
class decor():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        retval= self.func(*args, **kwargs)
        return retval

@decor
def f3(x):
    print"F3"
    print x
    return x+4

###############################################
if __name__ == "__main__":
    print "main start"
    ret=f1(10)
    print ret, '\n\n'
    ret=f2(20)
    print ret
    ret = f3(30)
    print ret
    print "main end"
    oF = Foo()
    oF.a()

