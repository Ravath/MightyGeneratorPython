# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:53:57 2020

@author: Ehlion
"""

import random
from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import PrintNode
from utils.debug import trace

#___________________________________________________#
#                                                   #
#                     WeightRow                     #
#___________________________________________________#
class WeightRow(RowNode):
    def __init__(self):
        RowNode.__init__(self)
        
        # Introduce new attributes
        self.weight= 1
        # putBack indicates how many times a row can be put back in a node
        # A value <0 for putBack allows an infinite put back in a node by default
        self.putBack= 0 
        # putBack indicates how many times a row 
        # can be put back in a node. A value <0 for putBack allows
        # an infinite put back in a node
        self.stopRow = False
        
        # Extend the signature conversion table
        def int1(self, i1):
            self.weight=i1
        def int2(self, i1, i2):
            self.weight=i1
            self.putBack=i2
        def conv2(self, i1, s1) :
            self.weight=i1
            self.set_node(s1)
        def conv3(self, i1, i2, s1) :
            self.weight=i1
            self.putBack=i2
            self.set_node(s1)
        self.argument_conversion.extend([
            ([int], int1),
            ([int,int], int2),
            ([int,str], conv2),
            ([int,int,str], conv3),
            ([int,AbsGeneratorNode], conv2),
            ([int,int,AbsGeneratorNode], conv3),
        ])
        
    def __str_attributes__(self) -> str :
        return f"Weight={self.weight}  "\
            f"Back={self.putBack}"

def randint(vmin:int, vmax:int) :
    return random.randint(vmin, vmax)

#___________________________________________________#
#                                                   #
#                     WeightNode                    #
#___________________________________________________#
class WeightNode(AbsCollectionNode):
    
    def __init__(self, numberOfDraw:int = 1, putBack:bool = True) :
        AbsCollectionNode.__init__(self)
        # flag raised if the total weight of the row
        # has changed and must be recomputed
        self.totalWeight = 0
        self.knowntotal = True
        
        # introduce new attributes
        self.numberOfDraw = numberOfDraw
        self.putBack = putBack
        
    def get_row(self, *args, **kargs) -> WeightRow :
        new_row = WeightRow()
        new_row.put(*args, **kargs)
        return new_row
        
    def extend(self, table) :
        AbsCollectionNode.extend(self, table)
        self.knowntotal = False
        
    def append(self, *args, **kargs) :
        AbsCollectionNode.append(self, *args, **kargs)
        self.knowntotal = False
        
    def insert(self, index:int, *args, **kargs) :
        AbsCollectionNode.insert(self, index, *args, **kargs)
        self.knowntotal = False
        
        
    def computeTotal(self):
        if not self.knowntotal:
            self.knowntotal = True
            self.totalWeight = sum([ c.weight for c in self.children
                                    if c.weight > 0])
        
    def draw(self):
        # Sum the total weight
        self.computeTotal()
        for child in self.children :
            child.stopRow = False
        for child in self.children :
            child.putBack = child.putBack
            
        if self.totalWeight == 0 : return
    
        for y in range(0, self.numberOfDraw):
            # Stops if no one can be picked
            if self.totalWeight == 0 :
                return
        
            # Roll
            roll = randint(1,self.totalWeight) #We ask to get a random number
            index = 0
            # Find associated entry
            # Particular case if first pick of the list has been row 
            if self.children[index].stopRow == False :
                roll -= self.children[index].weight
            else : pass

            while roll > 0:
                index += 1
                if self.children[index].stopRow == False :
                    roll -= self.children[index].weight
                
            yield self.children[index].node
            
            # Conditions for putting back row and how many times it will do it
            if (self.putBack == False or
                (self.putBack == True and self.children[index].putBack == 0)):
                self.children[index].stopRow = True
                self.totalWeight -= self.children[index].weight
            elif self.putBack == True and self.children[index].putBack != 0 :
                 self.children[index].putBack -= 1
            else: pass
        
    def __str_attributes__(self) -> str :
        # Sum the total weight
        self.computeTotal()
        
        return f"TotalWeight={self.totalWeight} "\
               f"Draws={self.numberOfDraw} " \
               f"PutBack={self.putBack}"

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :

    # var = WeightNode(7, True);
    # var.extend([
    #     "test",
    #     [2, PrintNode("yes")],
    #     [3, 2, "problem"],
    #     PrintNode("manuel")])
    # var.append("append")
    # var.insert(1, 2, node="insert")
    # var.insert(index=1, weight=2, node="insert2")
    # var.print_node()
    # var.execute()
    # raise "toto"
    
    from utils.debug import test, print_log
    from Print import ActionNode

    print_log("START", "WEIGHTNODE UNITARY TESTING")
    p1, p2, p3 = PrintNode("1"), PrintNode("2"), PrintNode("3")

    print_log("TEST", "Initialisation : Initial Values")
# initial values
    wmap = WeightNode()
    test(0, len(wmap.children))
    test(1, wmap.numberOfDraw)
    test(True, wmap.putBack)
    wmap.print_node()

    print_log("TEST", "Initialisation : Constructors")
# Different number of draws
    wmap = WeightNode(7)
    test(0, len(wmap.children))
    test(7, wmap.numberOfDraw)
    test(True, wmap.putBack)
# Different number of draws and putback
    wmap = WeightNode(7, False)
    test(0, len(wmap.children))
    test(7, wmap.numberOfDraw)
    test(False, wmap.putBack)
# Different putback
    wmap = WeightNode(putBack = False)
    test(0, len(wmap.children))
    test(1, wmap.numberOfDraw)
    test(False, wmap.putBack)
    wmap.print_node()

    print_log("TEST", "Initialisation : Adding rows")
# Extend 3 rows
    wmap.extend([p2,p1,p3])
    test(3, len(wmap.children))
    test(p2, wmap.children[0].node)
    test(p1, wmap.children[1].node)
    test(p3, wmap.children[2].node)
# Append
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

    def test_print_node(index:int, node, weight:int = 1, nbrPutback:int = 1) :
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
        nbrPutback : int, optional, The default is 1.
            expected putback of the row to check.
        """

        print_log("CHECK", f"node at index {index}")
        trow = wmap.children[index]
        test(True, isinstance(trow, type(WeightRow)))
        test(weight, trow.weight)
        test(nbrPutback, trow.putBack)
        if isinstance(node, str) :
            test(True, isinstance(trow.node, type(PrintNode)))
            test(node, trow.node.text)
        else :
            test(node, trow.node)

    print_log("TEST", "Initialisation : append")
    wmap = WeightNode()
# append a string
    wmap.append("aba")
    test(1, len(wmap.children))
    test_print_node(0,"aba")
# append a string with a weight
    wmap.append(3, "babo")
    test(2, len(wmap.children))
    test_print_node(1,"babo", 3)
# append a string with a weight and putback
    wmap.append(4, 2, "babo")
    test(3, len(wmap.children))
    test_print_node(2,"babo", 4, 2)
# append a node
    wmap.children.clear()
    wmap.append(p1)
    test(1, len(wmap.children))
    test_print_node(0,p1)
# append a node with a weight
    wmap.append(15, p2)
    test(2, len(wmap.children))
    test_print_node(1,p2, 15)
# append a node with a weight and putback
    wmap.append(-1, -2, p3)
    test(3, len(wmap.children))
    test_print_node(2,p3, -1, -2)
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
    wmap.insert(index=2, putBack=-9, weight=3, node="insert2")
    test_print_node(2, "insert2", 3, -9)
    wmap.print_node()


    default_dice = [2,1,3]
    dice_results = []
    received_results = []
    def res1() : received_results.append(1)
    def res2() : received_results.append(2)
    def res3() : received_results.append(3)
# pylint: disable-msg=E0102
    @trace
    def randint(vmin:int, vmax:int) :
        """Stub of the random function for unit testing"""
        return ((dice_results.pop(0)-vmin) % vmax)+vmin
# pylint: enable-msg=E0102

    def test_map(tmap:WeightNode, expected:list, determined_rand:list = default_dice) :
        dice_results.clear()
        dice_results.extend(determined_rand)
        received_results.clear()
        tmap.execute()
        test(expected, received_results)

    print_log("TEST", "Drawing with default values")
# Empty
    wmap = WeightNode()
    test_map(wmap, [])
# One row
    wmap.append(ActionNode(res1))
    test_map(wmap, [1])
# Multiple rows
    wmap.extend([
        ActionNode(res2),
        ActionNode(res3),
    ])
    test_map(wmap, [2])
    print_log("TEST", "Multiple draws")
# Multiple draw
    wmap.numberOfDraw = 3
    test_map(wmap, [2,1,3])
# Null weight
    wmap.children[1].Weight = 0
    test_map(wmap, [3,1,1])
# Superior weight
    wmap.children[1].Weight = 2
    test_map(wmap, [2,1,2])
    wmap.children[1].Weight = 1
    print_log("TEST", "Putback behaviors")
# No putback
    wmap.putBack = False
    default_dice = [1,1,1]
    test_map(wmap, [1,2,3])
# Behavior is the same the second time (rows are reset)
    test_map(wmap, [1,2,3])
# Too much draws
    wmap.numberOfDraw = 4
    test_map(wmap, [1,2,3])
    wmap.numberOfDraw = 3
# With a different individual putback
    wmap.numberOfDraw = 4
    wmap.children[1].putBack = 2
    test_map(wmap, [1,2,2,3])
# With a different weight
    wmap.children[0].Weight = 3
    test_map(wmap, [1,2,2,3])
    test_map(wmap, [3,2,1,1], [5,4,3,1])
    wmap.children[0].Weight = 1
# Infinite putback
    wmap.numberOfDraw = 6
    wmap.children[1].putBack = -1
    test_map(wmap, [2,2,1,3,2,2], [2,2,1,2,3,1])
    