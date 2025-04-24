# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:02:57 2022

@author: Ehlion

| Upmost module of wordgenerator nodes.
| AbsGeneratorNode is the parent of every Node in the generation structure.
| AbsLeafNode is the parent of every leafNode in the generation structure.
|  - Leaf means the node shall not have any more chilren.
| The the collections nodes, see AbsCollectionNode in the NodeCollectionIf module.
"""
from wordgenerator.GenerationResult import GenerationResult

#___________________________________________________#
#                                                   #
#                  AbsGeneratorNode                 #
#___________________________________________________#
class AbsGeneratorNode :
    """Parent of every node of the word generator.
    Implements a composite pattern with AbsLeafNode and AbsCollectionNode."""

    def __init__(self) :
        pass

    @classmethod
    def __subclasshook__(cls, subclass) :
        """
        Check every instance implements an execute and a printNode function.
        """
        return (hasattr(subclass, 'execute') and
                callable(subclass.execute) and
                hasattr(subclass, 'node_action') and
                callable(subclass.node_action) and
                hasattr(subclass, 'print_node') and
                callable(subclass.printNode) or
                NotImplemented)

    def execute(self) -> GenerationResult:
        """Start the generation."""
        res = GenerationResult()
        self.node_action(res)
        res.text = res.raw_text
        return res
    
    def node_action(self, generation_result:GenerationResult) :
        """Execute the node action."""
        raise NotImplementedError(f"In class {type(self).__name__}")

    def print_node(self, tabs:int = 0) :
        """print the node fonctional data for analysis purposes."""
        raise NotImplementedError(f"In class {type(self).__name__}")

#___________________________________________________#
#                                                   #
#                    AbsLeafNode                    #
#___________________________________________________#
class AbsLeafNode(AbsGeneratorNode):
    """
    A generic terminal node for the composite pattern.
    """

    def __init__(self) :
        AbsGeneratorNode.__init__(self)

    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}{type(self).__name__}")