
from math import sqrt
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, vector):
        return Vector(self.a + vector.a , self.b + vector.b)

    def __str__(self):
        return "Vector({},{})".format(self.a, self.b)

ab= Vector(1,2)
ac= Vector(5,8)

print ab+ac

x=1
print eval('sqrt(x+3)')

import random

print random.seed(3)
print random.random()
print random.seed(3)
print random.random()
print random.seed(3)
print random.random()
print random.random()
print random.seed(3)
print random.random()
print random.random()
print random.seed(3)
print random.random()
