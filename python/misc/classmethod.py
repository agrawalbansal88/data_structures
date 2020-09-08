
class Ankur:
    def __init__(self, value):
        self.a= value

    @classmethod
    def create_inst(cls, value):
        return Ankur(value/2)

    def create_inst1(cls, value):
        return Ankur(value/3)

    @staticmethod
    def static_method():
        print "Ankur"
        
    def static_method1():
        print "Ankur1"

    @property
    def prop(self):
        return 77

print Ankur.create_inst(11).a
#print Ankur.create_inst1(11).a

x=  Ankur(90)
x.static_method()
#x.static_method1()
print x.prop
