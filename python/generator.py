def ank(num):
    for i in range(num):
        yield i


x= ank(3)

print x.next()  #0
print x.next()  #1
print x.next()  #2 
print x.next()  #StopIteraton exeption
