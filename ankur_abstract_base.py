from abc import abstractmethod, ABCMeta



class BaseClass(metaclass = ABCMeta):
    @abstractmethod
    def Method1(self):
        pass

    @abstractmethod
    def Method2(self):
        pass

class DerivedClass(BaseClass):
    def Method1(self):
        print("Method 1 DerivedClass")

    def Method2(self):
        print("Method 2 DerivedClass")

@BaseClass.register
class VirtualDerivedClass:
    pass

#x = BaseClass()
y = DerivedClass()
y.Method1()

print ("issubclass(DerivedClass, BaseClass)", issubclass(DerivedClass, BaseClass))
print ("issubclass(VirtualDerivedClass, BaseClass)", issubclass(VirtualDerivedClass, BaseClass))

