# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:02:57 2022

@author: Ehlion
"""

#___________________________________________________#
#                                                   #
#                  AbsGeneratorNode                 #
#___________________________________________________#
class AbsGeneratorNode :
    
    def __init__(self) : pass
        
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'execute') and 
                callable(subclass.execute) and
                hasattr(subclass, 'printNode') and 
                callable(subclass.printNode) or 
                NotImplemented)
    
    def execute(self):
        """Execute the node action"""
        raise NotImplementedError("In class {}".format(type(self).__name__))
    
    def printNode(self, tabs:int = 0) :
        """print the node """
        raise NotImplementedError("In class {}".format(type(self).__name__))
        
        

#___________________________________________________#
#                                                   #
#                    AbsLeafNode                    #
#___________________________________________________#
class AbsLeafNode(AbsGeneratorNode):
    """
    A generic leaf node for the composite pattern.
    """
    
    def __init__(self):
        AbsGeneratorNode.__init__(self)
        
    def printNode(self, tabs:int = 0) :
        print("{tabs}{name}".
              format(tabs="\t"*tabs,
                     name=type(self).__name__))