


def create_data(num):
    for i in  range(num):
        print "\n\ncreating ", i
        yield i


def use_data():
    while True:
        x = yield
        print "sqaring ", x
        data = yield x*x
        print "--------------data ", data

def print_data():
    while True:
        x = yield
        print "printing ", x


prod = create_data(3)
cons =  use_data()
next(cons)
print_Data= print_data()
next(print_Data)
for num in prod:
    #print "NUMBER", num
    num = cons.send(num)
    #next(cons)
    #print "NUMBER", num
    print_Data.send(num)
cons.close()
print_Data.close()
