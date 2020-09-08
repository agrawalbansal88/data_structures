#can't change the body of this function
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        print ".........", x
        if x is not None:
            n = x
        else:
            n += 1

# can only change this function            
def change_generator(generator, n):
    print "===========GENE", n
    while n%2 !=0:
        n = next(generator)
    yield n



# can't change this code either
# should print 1, 2, 4, 6, 8
g = positive_integers_generator() 
for _ in range(5):
    n = next(g)
    print "main...", n
    print(n)
    import pdb;pdb.set_trace()
    change_generator(g, n)
