# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:40:29 2022

@author: Ehlion
"""

from NodeCollectionIf import AbsCollectionNode
        
#___________________________________________________#
#                                                   #
#                     SequenceNode                  #
#___________________________________________________#
class SequenceNode(AbsCollectionNode):
    
    def __init__(self):
        AbsCollectionNode.__init__(self)
        
    def draw(self):
        """draw every children sequentially"""
        for row in self.children:
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