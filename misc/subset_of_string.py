def minion_game(string):
    # your code goes here
    
    ank = string
    ln = len(ank)
    subsets = set()

    def get_score(subset):
        count = 0
        idx = 0
        while ank[idx:].find(subset) != -1:
            count += 1
            idx += ank[idx:].find(subset) + 1
            if idx >= ln: break
        return count

    for i in range(ln):
        for j in range(i+1, ln+1):
            subsets.add(ank[i:j])

    Stuart_set = filter(lambda x: x[0] not in ['A', 'E', 'I', 'O', 'U'], subsets)
    Kevin_set = filter(lambda x: x[0] in ['A', 'E', 'I', 'O', 'U'], subsets)

    Stuart_score = reduce(lambda x,y : x+y, map(get_score, Stuart_set))
    Kevin_score = reduce(lambda x,y : x+y, map(get_score, Kevin_set))

    if Stuart_score>Kevin_score:
        print "Stuart", Stuart_score
    elif Stuart_score<Kevin_score:
        print "Kevin", Kevin_score
    else:
        print "Draw"

minion_game('BANANA')
