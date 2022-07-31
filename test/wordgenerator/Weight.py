# -*- coding: utf-8 -*-
"""
Created on 12/08/2022

@author: Trense
"""
from wordgenerator.Weight import WeightNode, WeightRow
import wordgenerator.Weight as w
from wordgenerator.Print import PrintNode
from utils.debug import test, print_log, test_result, test_action, trace
from wordgenerator.Print import ActionNode

print_log("START", "WEIGHTNODE UNITARY TESTING")
p1, p2, p3 = PrintNode("1"), PrintNode("2"), PrintNode("3")

print_log("TEST", "Initialisation : Initial Values")
# initial values
wmap = WeightNode()
test(0, len(wmap.children))
test(1, wmap.nbr_draw)
test(True, wmap.do_put_back)
wmap.print_node()

print_log("TEST", "Initialisation : Constructors")
# Different number of draws
wmap = WeightNode(7)
test(0, len(wmap.children))
test(7, wmap.nbr_draw)
test(True, wmap.do_put_back)
# Different number of draws and do put back
wmap = WeightNode(7, False)
test(0, len(wmap.children))
test(7, wmap.nbr_draw)
test(False, wmap.do_put_back)
# Different do putback
wmap = WeightNode(do_put_back = False)
test(0, len(wmap.children))
test(1, wmap.nbr_draw)
test(False, wmap.do_put_back)
# Different number of putback
wmap = WeightNode(nbr_draw=4, nbr_put_back=8)
test(0, len(wmap.children))
test(8, wmap.nbr_put_back)
test(True, wmap.do_put_back)
wmap.print_node()

print_log("TEST", "Initialisation : Adding rows")
# Extend 3 rows
wmap.extend([p2,p1,p3])
test(3, len(wmap.children))
test(p2, wmap.children[0].node)
test(p1, wmap.children[1].node)
test(p3, wmap.children[2].node)
# AppendDebug
wmap.append(p1)
test(4, len(wmap.children))
test(p1, wmap.children[3].node)
# Insert at 0
wmap.insert(0, p1)
test(5, len(wmap.children))
test(p1, wmap.children[0].node)
# Clear children
wmap.children.clear()
test(0, len(wmap.children))
wmap.print_node()

def test_print_node(index:int, node, weight:int = 1, nbr_put_back:int = -1) :
    """Test function of a weightrow.

    Parameters
    ----------
    index : int
        expected index of the row to check.
    node : str or AbsGeneratorNode
        expected node to check
        or expected string of a printnode to check.
    weight : int, optional, The default is 1.
        expected weight of the row to check.
    nbr_put_back : int, optional, The default is -1 (infinite put back).
        expected putback of the row to check.
    """

    print_log("CHECK", f"====== row at index {index} ======")
    trow = wmap.children[index]
    if not test(True, isinstance(trow, WeightRow), f"test row_{index} is a WeightRow") :
        print_log("DISPLAY", type(trow))
    test(weight, trow.weight, f"test row_{index}.weight")
    test(nbr_put_back, trow.nbr_put_back, f"test row_{index}.nbr_put_back")
    if isinstance(node, str) :
        if not test(True, isinstance(trow.node, PrintNode), f"test row_{index}.node is a PrintNode") :
            print_log("DISPLAY", type(trow))
        test(node, trow.node.text, f"test row_{index}.text")
    else :
        test(node, trow.node, f"test row_{index}'s reference")

print_log("TEST", "Initialisation : append")
wmap = WeightNode()
wmap.print_node()
# append a string
test_action("Append a String")
wmap.append("aba")
test(1, len(wmap.children), "Length increased")
test_print_node(0,"aba")
wmap.print_node()
# append a string with a weight
test_action("Append a string with a weight")
wmap.append(3, "babo")
test(2, len(wmap.children), "Length increased")
test_print_node(1,"babo", 3)
# append a string with a weight and putback
test_action("Append a string with a weight and a putback value")
wmap.append(4, 6, "babo")
test(3, len(wmap.children), "Length increased")
test_print_node(2,"babo", 4, 6)
# append a node
test_action("Clear Children")
test_action("Append a node")
wmap.children.clear()
wmap.append(p1)
test(1, len(wmap.children))
test_print_node(0,p1)
# append a node with a weight
test_action("append a node with a weight")
wmap.append(15, p2)
test(2, len(wmap.children))
test_print_node(1,p2, 15)
# append a node with a weight and putback
test_action("append a node with a weight and putback")
wmap.append(-1, -2, p3)
test(3, len(wmap.children))
test_print_node(2, p3, -1, -2)
wmap.print_node()

print_log("TEST", "Initialisation : extend")
wmap.children.clear()
wmap.extend([
    "test",
    [2, PrintNode("yes")],
    [3, 2, "problem"],
    p1,
    [7, p2],
    [9, 3, p3]
])
test_print_node(0, "test")
test_print_node(1, "yes", 2)
test_print_node(2, "problem", 3, 2)
test_print_node(3, p1)
test_print_node(4, p2, 7)
test_print_node(5, p3, 9, 3)
wmap.print_node()

print_log("TEST", "Initialisation : insert")
wmap.insert(0, "baba")
test_print_node(0, "baba")
wmap.insert(4, 2, "bobo")
test_print_node(4, "bobo", 2)
wmap.insert(1, 2, 5, "bibi")
test_print_node(1, "bibi", 2, 5)
wmap.insert(index=2, nbr_put_back=-9, weight=3, node="insert2")
test_print_node(2, "insert2", 3, -9)
wmap.print_node()


default_dice = [2,1,3]
dice_results = []
received_results = []
def res1() : received_results.append(1)
def res2() : received_results.append(2)
def res3() : received_results.append(3)
# pylint: disable-msg=E0102

@trace(False, True)
def randint(vmin:int, vmax:int) :
    """Stub of the random function for unit testing"""
    return ((dice_results.pop(0)-vmin) % vmax)+vmin

w.randint = randint
# pylint: enable-msg=E0102

def test_map(tmap:WeightNode, expected:list, determined_rand:list = default_dice) :
    dice_results.clear()
    dice_results.extend(determined_rand)
    received_results.clear()
    tmap.execute()
    test(expected, received_results, "test roll outcome")

print_log("TEST", "Drawing with default values")
# Empty
print_log("TEST", "Empty")
wmap = WeightNode()
test_map(wmap, [])
# One row
print_log("TEST", "One row")
wmap.append(ActionNode(res1))
test_map(wmap, [1])
# Multiple rows
print_log("TEST", "Multiple rows")
wmap.extend([
    ActionNode(res2),
    ActionNode(res3),
])
test_map(wmap, [2])
# Multiple draw
print_log("TEST", "Multiple draws")
wmap.nbr_draw = 3
test_map(wmap, [2,1,3])
# Null weight
print_log("TEST", "Null weight")
wmap.children[1].weight = 0
test_map(wmap, [3,1,1])
# Superior weight
print_log("TEST", "Superior Weight")
wmap.children[1].weight = 2
test_map(wmap, [2,1,2])
wmap.children[1].weight = 1

print_log("TEST", "Putback behaviors")
# No put back
print_log("TEST", "No put back")
wmap.do_put_back = False
#default_dice = [1,1,1]
test_map(wmap, [1,2,3], [1,1,1])
# Behavior is the same the second time (rows are reset)
print_log("TEST", "No put back, second time")
test_map(wmap, [1,2,3], [1,1,1])
# Too much draws
print_log("TEST", "Too much draws")
wmap.nbr_draw = 4
test_map(wmap, [1,2,3], [1,1,1])
# With a different individual putback
print_log("TEST", "4 Authorised draws, individual put back")
wmap.do_put_back = True
wmap.children[0].nbr_put_back = 0
wmap.children[1].nbr_put_back = 1
wmap.children[2].nbr_put_back = 0
test_map(wmap, [1,2,2,3], [1,1,1,1])
# With a different weight
print_log("TEST", "4 Draws, individual put back, and different weight")
wmap.children[0].weight = 3
test_map(wmap, [1,2,2,3], [1,1,1,1])
test_map(wmap, [3,2,1,2], [5,4,3,1])
wmap.children[0].weight = 1
# Infinite putback
print_log("TEST", "6 Authorised draws, infinite put back")
wmap.nbr_draw = 6
wmap.children[1].nbr_put_back = -1
test_map(wmap, [2,2,1,3,2,2], [2,2,1,2,3,1])

test_result()

