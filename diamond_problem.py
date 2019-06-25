


class A:
    def pri(self):
        print("A")

class B(A):
    def pri(self):
        print("B")
class C(A):
    def pri(self):
        print("C")

class D(B, C):
    pass
    #def pri(self):
    #    print("D")


obj=D()
obj.pri()
