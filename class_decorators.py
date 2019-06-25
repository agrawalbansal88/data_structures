def time_all_class_methods(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            print "INIT CALLED", args, kwargs
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            print "__getattribute__ CALLED", s
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
                return x               # this is equivalent of just decorating the method with time_this
            else:
                return x
    return NewCls

#now lets make a dummy class to test it out on:

@time_all_class_methods
class Foo(object):
    def __init__(self, *args, **kwargs):
        print "FOO INIT", args, kwargs
    def a(self, args):
        print "entering a", args
        import time
        time.sleep(1)
        print "exiting a", args

oF = Foo(111, 222)
print "-------"
oF.a(10)
oF.a(11)