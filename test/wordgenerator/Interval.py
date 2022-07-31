# -*- coding: utf-8 -*-
"""
Created on 12/08/2022

@author: Trense
"""
from wordgenerator.Interval import IntervalNode
from wordgenerator.Print import PrintNode
from utils.debug import test, print_log
from macro.dice import PoolSum, Pool

var = IntervalNode(PoolSum(Pool(1,4)))
var.extend([
    [0, 4, 3, "test"], #we can see "test" only 3 times
    [1, 2, PrintNode("yes")],
    [3, 2, "problem"],
    [5,10, PrintNode("manuel")]
    ])
var.print_node()
#can't do because have to implement roll
#var.execute()
for i in range(0,6) :
    print(f"== {i} ==")
    for resNode in var.draw_from_result(i) :
        resNode.execute()
print("============")
var.execute()
print("============")
var2 = IntervalNode("1d4",8)
var2.extend([
    [0, 4, 3, "test"], #we can see "test" only 3 times
    [1, 2, PrintNode("yes")],
    [3, 2, "problem"],
    [5,10, PrintNode("manuel")]
    ])
var2.print_node()
print("============")
var2.execute()