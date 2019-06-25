



def is_prime(num):
    if num <= 1:
        return False
    if num ==2:
        return True

    for i in range(3,(num/2)+1):
        if num%i == 0:
            return False

    return True


def prime_recursive(num, start=2):
    if num <= 1:
        return False
    if num ==2:
        return True
    if num%start == 0:
        return False
    else:
        if start<num/2 +1:
            return prime_recursive(num, start+1)
        else:
            return True

def get_prime_product(num):
    primes = []
    for i in range(2, num/2+1):
        if is_prime(i):
            primes.append(i)
            if num%i == 0 and (num/i) in primes:
                return True, (i, num/i)

    return False, None


import math
prime_factor  =  []
num = 31534334
while num % 2 == 0:
    prime_factor.append(2) 
    num = num / 2

for i in xrange(3, num+1, 2):
    while(num%i==0):
        prime_factor.append(i)
        num = num/i
    if i>num:
        break

print prime_factor
"""
#print Find the highest occurring digit in prime numbers in a range
from collections import Counter
xx= []
for i in range(1, 20+1):
    if prime_recursive(i):
        xx.extend(map(int, str(i)))

print Counter(xx).most_common(1)[0][1]

for i in range(100):
    if prime_recursive(i):
        print i

for i in range(100):
    ret_val, vals = get_prime_product(i)
    if ret_val:
        print i, vals
"""
