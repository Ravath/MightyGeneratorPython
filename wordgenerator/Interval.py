# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:35:42 2020

@author: Ehlion
"""

from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.Print import PrintNode

#___________________________________________________#
#                                                   #
#                    IntervalRow                    #
#___________________________________________________#
class IntervalRow(RowNode):
    def __init__(self):
        RowNode.__init__(self)
        
        """ introduce new attributes """
        self.min=1
        self.max=1
        
        """ extend the signature conversion table """
        def int1(self, i1):
            self.min=i1
        def int2(self, i1, i2):
            self.min=i1
            self.max=i2
        def conv2(self, i1, s1) :
            self.min=i1
            self.setNode(s1)
        def conv3(self, i1, i2, s1) :
            self.min=i1
            self.max=i2
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
        return "Min={} Max={}".format(
            self.min, self.max)

#___________________________________________________#
#                                                   #
#                    IntervalNode                   #
#___________________________________________________#
class IntervalNode(AbsCollectionNode):
    
    def __init__(self):
        AbsCollectionNode.__init__(self)
        
        """ introduce new attributes """
        self.numberOfDraw=1
        self.putBack=True
        
    def getRow(self, *args, **kargs) -> IntervalRow:
        newRow=IntervalRow()
        newRow.put(*args, **kargs)
        return newRow
        
    def put(self, min, max, text):
        self.map.append(((min,max),text))
        
    def draw(self) :
        #TODO
        res=1
        return self.drawFromResult(res)
        
    def drawFromResult(self, roll:int):
        for row in self.children:
            if roll >= row.min and roll <= row.max:
                yield row.node
                
    def __str_attributes__(self) -> str :
        return "Draws={} PutBack={}".format(
            self.numberOfDraw, self.putBack)
            
#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :
    var = IntervalNode();
    var.extend([
        "test",
        [1, 2, PrintNode("yes")],
        [3, 2, "problem"],
        PrintNode("manuel")])
    var.printNode()
    #can't do because have to implement roll
    #var.execute()
    for i in range(0,6):
        print("== {} ==".format(i))
        for resNode in var.drawFromResult(i):
            resNode.execute()