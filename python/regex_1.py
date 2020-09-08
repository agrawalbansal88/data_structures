import re
NON_METAL_REGEX=re.compile('hyd\w+ic')
POLYATOMIC_REGEX=re.compile('\w+ic')
def acidNaming(acid_name):
    if NON_METAL_REGEX.search(acid_name):
        return "non-metal acid"
    elif POLYATOMIC_REGEX.search(acid_name):
        return "polyatomic acid"
    else:
        return "not an acid"


"""

hydrochloric
rainbowic
idontevenknow

non-metal acid
polyatomic acid
not an acid

"""
