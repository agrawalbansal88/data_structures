import pickle

data={"Ankr":3}

with open('/Users/ankuragr/pickle.txt',  'wb') as f:
    pickle.dump(data, f)

with open('/Users/ankuragr/pickle.txt',  'rb') as f1:
    print pickle.load(f1)
