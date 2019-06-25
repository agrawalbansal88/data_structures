#!/anaconda2/bin/python
import random
N=10
data = range(1, N+1)
print data
rand_num = random.randint(1, N)
rand_loc = random.randint(1, N)
print "replaced number from", data[rand_loc], "to ", rand_num
data[rand_loc] = rand_num
print data

######### LIST IS CREATED ########

bitwise = 0
for dat in data:
    bitwise |= 1<< (dat)

for i in range(1, N+1):
    if not bitwise & 1<<i:
        print i
        break
