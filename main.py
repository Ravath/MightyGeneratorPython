# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:55:17 2020

@author: Ehlion
"""

from macro.dice import PoolSum, Pool
from wordgenerator.Weight import WeightNode
from wordgenerator.Interval import IntervalNode
from wordgenerator.Sequence import SequenceNode
from wordgenerator.Generator import Generator

#___________________________________________________#
#                                                   #
#                     WeightNode                    #
#___________________________________________________#

""" Declarations """

w_empty = WeightNode()
w_single = WeightNode()
w_easy = WeightNode()
w_ponder = WeightNode()
w_back = WeightNode(8)

w_single.extend([
    [1, "The best one in the world"],
])
w_easy.extend([
    [1, "banana"],
    [1, "Chocolat"],
])
w_ponder.extend([
    [0, "NEVER"],
    [5, "YES"],
    [1, "NO"],
    [1, lambda : print("papa")],
])
w_back.extend([
    [0,-1, "I won't be there"],
    [5,2, "I will be seen max 3 times"],
    [3,0, "I'm the only one"],
    [1, "You can see me often"],
    ])

""" Executions """

print("== Weigh maps ==")

print("- Empty map :")
w_empty.execute()

print("- 1 row map :")
w_single.execute()

print("- 2 row map, weight=1 (5times) :")
for i in range(0,5):
    w_easy.execute()

print("- 3 row map, different weight, including 0 (10times) :")
for i in range(0,10):
    w_ponder.execute()

w_ponder.print_node()

print("- 4 row map, 1 time but 8 draw in the same execution, with different put back :")
w_back.execute()
w_back.print_node()

#___________________________________________________#
#                                                   #
#                    IntervalNode                   #
#___________________________________________________#

""" Declarations """

rand_pool = PoolSum(Pool(1,4))

i_empty = IntervalNode(rand_pool)
i_single = IntervalNode(rand_pool)
i_test = IntervalNode(rand_pool)

i_single.extend([
    [1,1,"your majesty"]
])
i_test.extend([
    [1,1, "AAA"],
    [2,4, "BBB"],
    [0,3, "CCC"],
    [4,1, "DDD"],
])

""" Executions """

print("== Interval maps ==")

print("- Empty map :")
for resNode in i_empty.draw_from_result(1):
    resNode.execute()

print("- 1 row map (0->2) :")
for i in range(0,3):
    print("single {}".format(i))
    for resNode in i_single.draw_from_result(i):
        resNode.execute()

print("- 4 row map, with overlaps (0->5) :")
for i in range(0,6):
    print("test {}".format(i))
    for resNode in i_test.draw_from_result(i):
        resNode.execute()

print("== Interval maps ==")
i_empty.execute()
i_single.execute()
i_test.execute()

#___________________________________________________#
#                                                   #
#                    SequenceNode                   #
#___________________________________________________#

""" Declarations """

test = SequenceNode().extend([
    "ZARA",
    "ZOMEU",
    "{TOUTATIS}",
    "{BELENOS}"
])

""" Executions """

print("== Sequence Node ==")

test.print_node()

for n in test :
    n.print_node()

test.execute()

#___________________________________________________#
#                                                   #
#                     GENERATOR                     #
#___________________________________________________#

""" Declarations """

# The root of the generator is the SequenceNode from the SequenceNode step
gen = Generator(test)

global TOUTATIS
TOUTATIS = "-GABUZOMEU"

# use a variable converter from the global variables
def var_converter(name) -> str :
    if name in globals().keys() :
        return globals()[name]
    else :
        return "{" + name + "}"
gen.variable_converter = var_converter

""" Executions """

print("== Generator ==")

gen.execute()
gen.print_to_console()
