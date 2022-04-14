# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:55:17 2020

@author: Ehlion
"""
from wordgenerator.weightmap import weightmap as weightmap

w_empty = weightmap()
w_single = weightmap()
w_easy = weightmap()
w_ponder = weightmap()

w_empty.map
w_single.map
w_easy.map

w_single.put(1, "The best one in the world")
w_easy.put(1, "banana")
w_easy.put(1, "Chocolat")
w_ponder.put(0, "NEVER")
w_ponder.put(5, "YES")
w_ponder.put(1, "NO")


print(w_empty.draw())
print(w_single.draw())
for i in range(0,5):
    print(w_easy.draw())
for i in range(0,10):
    print(w_ponder.draw())
    
w_range = weightmap()
w_range.extend([
    (3,"test3"),
    (5,"test5"),
    ])
print(w_range.draw())

from wordgenerator.intervalmap import intervalmap as intervalmap

i_empty = intervalmap()
i_single = intervalmap()
i_test = intervalmap()

i_single.put(1,1,"your majesty")
i_test.put(1,1, "AAA")
i_test.put(2,4, "BBB")
i_test.put(0,3, "CCC")
i_test.put(4,1, "DDD")

print(i_empty.draw(1))

for i in range(0,3):
    print("single {}".format(i))
    print(i_single.draw(i))

for i in range(0,6):
    print("test {}".format(i))
    print(i_test.draw(i))
