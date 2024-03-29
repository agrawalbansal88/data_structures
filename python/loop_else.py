# from weakref import WeakKeyDictionary, WeakValueDictionary
#
# import gc
# def func():
#     abc =  ABC
#     xx[abc] ="KALA"
#
# class ABC:
#     pass
# #xx= WeakValueDictionary()
# xx={}
# abc = ABC
# xx["KALA"] = abc
# del abc
# gc.collect()
# #print abc
# import time;time.sleep(3)
# print(xx.keys())
# print(xx["KALA"])

import gc
from pprint import pprint
import weakref

#gc.set_debug(gc.DEBUG_LEAK)


class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name

    def __del__(self):
        print '(Deleting ABC %s)' % self


def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # the cache using the factory we're given
    print 'CACHE TYPE:', cache_factory
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # decref

    print 'all_refs =',
    pprint(all_refs)
    print 'Before, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
        del value  # decref

    # Remove all references to our objects except the cache
    print 'Cleanup:'
    del all_refs
    gc.collect()

    print 'After, cache contains:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
    print 'demo returning'
    return


demo(dict)
print "---------"

demo(weakref.WeakValueDictionary)