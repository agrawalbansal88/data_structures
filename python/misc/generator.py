
class Ankur:
    def __init__(self, count):
        self.count = count
    def __iter__(self):
        return self
    def next(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return self.count


ank = Ankur(11)
print type(ank)
for i in ank:
    print i

for i in range(11):
    if i ==5:
        print i
        break
else:
    print "A"
