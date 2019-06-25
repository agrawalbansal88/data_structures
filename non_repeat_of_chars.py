from collections import defaultdict
string = "geeksforgeeksandgeeksquizfor"
dic = defaultdict(int)
for char in string:
    dic[char] +=1

print [char for char, count in dic.iteritems() if count ==1]

print [a for a in string if string.count(a) == 1]
