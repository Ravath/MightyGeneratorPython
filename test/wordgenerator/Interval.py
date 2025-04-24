# -*- coding: utf-8 -*-
"""
Created on 12/08/2022

@author: Trense
"""
from wordgenerator.Interval import IntervalNode
from wordgenerator.Print import PrintNode
from utils.debugtools import test, print_log
from macro.dice import PoolSum, Pool

var = IntervalNode(PoolSum(Pool(1,4)))
var.extend([
    [0, 4, 3, "test"], #we can see "test" only 3 times
    [1, 2, PrintNode("yes")],
    [3, 2, "problem"],
    [5,10, PrintNode("manuel")]
    ])
var.print_node()

for i in range(0,6) :
    print(f"== {i} ==")
    for resNode in var.draw_from_result(i) :
        resNode.execute().print_to_console()

print("===== One pick in row 1d4 =====")
var2 = IntervalNode(1)
var2.extend([
    [0, 4, 3, "test"], #we can see "test" only 3 times
    [1, 2, PrintNode("yes")],
    [3, 2, "problem"],
    [5,10, PrintNode("manuel")]
    ])
var2.execute().print_to_console()

print("===== Eight picks in row 1d4 =====")
var3 = IntervalNode("1d4",8)
var3.extend([
    [0, 4, 3, "test"], #we can see "test" only 3 times
    [1, 2, PrintNode("yes")],
    [3, 2, "problem"],
    [5,10, PrintNode("manuel")]
    ])
var3.print_node()

print("=================================")
var3.execute().print_to_console()

print("==========Do it again?===========")
var3.execute().print_to_console()