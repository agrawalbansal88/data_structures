from functools import singledispatch


class Base:
    def __init__(self, solid=None):
        self.solid = solid

class Circular(Base):
    def __init__(self, center, radius, *args, **kwargs):
        super(Circular, self).__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

class Sqaure(Base):
    def __init__(self, side, *args, **kwargs):
        super(Sqaure, self).__init__(*args, **kwargs)
        self.side = side

class Triangle(Base):
    def __init__(self, dummy, *args, **kwargs):
        super(Triangle, self).__init__(*args, **kwargs)
        self.dummy = dummy

@singledispatch
def draw(shape):
    raise TypeError("Unkonw Shape")

@draw.register(Circular)
def _(shape):
    print("Is is Circle")

@draw.register(Sqaure)
def _(shape):
    print("Is is Sqaure")


@draw.register(Triangle)
def _(shape):
    print("Is is Triangle")



def main():
    shapes = [Circular(12,12), Sqaure(12), Triangle("23")]
    for shape in shapes:
        draw(shape)
if __name__=="__main__":
    print("dispatch testing")
    main()

