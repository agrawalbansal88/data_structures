from itertools import permutations, combinations
import math
N=2
x=set()
a=[1]*N + [2]*(N-1) + [3]*(N-2)
for i in range(N):
    p = set(list(combinations(a, i+1)))
    for p1 in p:
        if sum(p1) == N:
            for p2 in set(list(permutations(p1))):
                x.add(p2)

print "\n".join(map(str, x))
print len(x)
