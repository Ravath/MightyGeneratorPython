# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:53:57 2020

@author: Ehlion
"""

import random
from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import PrintNode

#___________________________________________________#
#                                                   #
#                     WeightRow                     #
#___________________________________________________#
class WeightRow(RowNode):
    def __init__(self):
        RowNode.__init__(self)
        
        """ introduce new attributes """
        self.weight=1
        self.putBack=1
        
        """ extend the signature conversion table """
        def int1(self, i1):
            self.weight=i1
        def int2(self, i1, i2):
            self.weight=i1
            self.putBack=i2
        def conv2(self, i1, s1) :
            self.weight=i1
            self.setNode(s1)
        def conv3(self, i1, i2, s1) :
            self.weight=i1
            self.putBack=i2
            self.setNode(s1)
        self.argumentConversion.extend([
            ([int], int1),
            ([int,int], int2),
            ([int,str], conv2),
            ([int,int,str], conv3),
            ([int,AbsGeneratorNode], conv2),
            ([int,int,AbsGeneratorNode], conv3),
        ])
        
    def __str_attributes__(self) -> str :
        return "Weight={} Back={}".format(
            self.weight, self.putBack)
            
#___________________________________________________#
#                                                   #
#                     WeightNode                    #
#___________________________________________________#
class WeightNode(AbsCollectionNode):
    
    def __init__(self, numberOfDraw:int=1, putBack:bool=True):
        AbsCollectionNode.__init__(self)
        """ flag raised if the total weight of the row
            has changed and must be recomputed
        """
        self.totalWeight = 0
        self.knowntotal = True
        
        """ introduce new attributes """
        self.numberOfDraw = numberOfDraw
        self.putBack = putBack
        
    def getRow(self, *args, **kargs) -> WeightRow:
        newRow=WeightRow()
        newRow.put(*args, **kargs)
        return newRow
        
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
            self.totalWeight = 0
            for x in self.children:
                self.totalWeight += x.weight
        
    def draw(self):
        
        # Sum the total weight
        self.computeTotal()
            
        if self.totalWeight == 0 : return ""
    
        for y in range(0, self.numberOfDraw):
            # Roll
            roll = random.randint(1, self.totalWeight) #We ask to get a random number 
            index = 0
        
            # Find associated entry
            roll -= self.children[index].weight
            while roll > 0:
                index += 1
                roll -= self.children[index].weight
            
            yield  self.children[index].node
        
    def __str_attributes__(self) -> str :
        # Sum the total weight
        self.computeTotal()
        
        return "Weight={} Draws={} PutBack={}".format(
            self.totalWeight, self.numberOfDraw, self.putBack)

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :
    var = WeightNode(5);
    var.extend([
        "test",
        [2, PrintNode("yes")],
        [3, 2, "problem"],
        PrintNode("manuel")])
    var.append("append")
    var.insert(1, 2, node="insert")
    var.insert(index=1, weight=3, node="insert2")
    var.printNode()
    var.execute()
    