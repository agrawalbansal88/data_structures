def ank(num):
    for i in range(1, num+1):
        print "inside for  i= ", i
        if i%4==0:
            break
    else:
        print "inside else"

ank(2)
ank(5) 
