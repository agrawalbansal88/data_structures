class Test:
    def __init__(self, count):
        self.count = count
    def __iter__(self):
        return self

    def next(self):
        self.count -= 1
        if self.count ==0:
            raise StopIteration
        return self.count

a=Test(10)

for i in a:
    print i


import itertools
import operator
li1 = [1, 4, 5, 7]
li2 = [1, 6, 5, 9]
li3 = [8, 10, 5, 4]

# using accumulate()
# prints the successive summation of elements
print "The sum after each iteration is : ", list(itertools.accumulate(li1))
 
# using accumulate()
# prints the successive multiplication of elements
#print ("The product after each iteration is : ",end="")
#print (list(itertools.accumulate(li1,operator.mul)))
 
# using chain() to print all elements of lists
#print ("All values in mentioned chain are : ",end="")
#print (list(itertools.chain(li1,li2,li3)))
