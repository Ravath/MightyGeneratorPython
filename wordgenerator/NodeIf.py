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
    """Parent of every node of the word generator."""

    def __init__(self) :
        pass

    @classmethod
    def __subclasshook__(cls, subclass) :
        return (hasattr(subclass, 'execute') and
                callable(subclass.execute) and
                hasattr(subclass, 'print_node') and
                callable(subclass.printNode) or
                NotImplemented)

    def execute(self) :
        """Execute the node action"""
        raise NotImplementedError(f"In class {type(self).__name__}")

    def print_node(self, tabs:int = 0) :
        """print the node."""
        raise NotImplementedError(f"In class {type(self).__name__}")

#___________________________________________________#
#                                                   #
#                    AbsLeafNode                    #
#___________________________________________________#
class AbsLeafNode(AbsGeneratorNode):
    """
    A generic leaf node for the composite pattern.
    """

    def __init__(self) :
        AbsGeneratorNode.__init__(self)

    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}{type(self).__name__}")