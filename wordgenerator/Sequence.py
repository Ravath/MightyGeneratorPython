# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:40:29 2022

@author: Ehlion
"""

from wordgenerator.NodeCollectionIf import AbsCollectionNode
        
#___________________________________________________#
#                                                   #
#                     SequenceNode                  #
#___________________________________________________#
class SequenceNode(AbsCollectionNode):
    
    def __init__(self):
        AbsCollectionNode.__init__(self)
        self.inbetweenAction = None
        
    def draw(self):
        """draw every children sequentially"""
        firstAction=True
        
        for row in self.children:
            if firstAction : firstAction = False
            else : yield self.inbetweenAction
            yield row.node

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :
    var = SequenceNode();
    var.extend([
        "test",
        "problem",
        "manuel"])
    var.execute()