import re
string = "reeks for reeks contribute practice"
w1="reeks"
w2="practice"
#string="the quick the brown quick brown the frog"
#w1="quick"
#w2="frog"
w1_locs =[]
w2_locs =[]
words = string.strip().split()
min_dis = len(words)
for i, word in enumerate(words):
    if word == w1: w1_locs.append(i)
    if word == w2: w2_locs.append(i)

print w1_locs, w2_locs
for wl1 in w1_locs:
    for wl2 in w2_locs:
        if abs(wl1-wl2) < min_dis:
            min_dis = abs(wl1-wl2)-1

print min_dis
