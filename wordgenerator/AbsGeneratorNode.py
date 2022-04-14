# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:02:57 2022

@author: Ehlion
"""

class AbsGeneratorNode :
        
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'execute') and 
                callable(subclass.execute) or 
                NotImplemented)
    
    def execute(self):
        """Execute the node action"""
        raise NotImplementedError

class AbsLeafNode(AbsGeneratorNode):
    """
    A generic leaf node for the composite pattern.
    """
    
    def __init__(self):
        AbsGeneratorNode.__init__(self)

class PrintNode(AbsLeafNode):
    """
    The most important generator node : prints the given text at execution.
    """
    
    def __init__(self, text:str = ""):
        AbsLeafNode.__init__(self)
        self.text = text
        
    def execute(self):
        print(self.text)


class AbsCollectionNode(AbsGeneratorNode):
    """
    A generic collection node for the composite pattern.
    """
    
    def __init__(self):
        AbsGeneratorNode.__init__(self)
        self.children = list()
        
    def extend(self, table):
        """
        Append a node collection to the node children.
        
        Parameters
            table : collection of strings or nodes.

        Returns none
        """
        for t in table:
            self.append(t)
        
    def append(self, node):
        """
        Append a node to the node children.
        
        Parameters
            node : a string or node.

        Returns none
        """
        if type(node) is str :
            self.children.append(PrintNode(node))
        elif isinstance(node, AbsGeneratorNode) :
            self.children.append(node)
        else:
            raise TypeError("Must be a node or some text")
        
class SequenceNode(AbsCollectionNode):
    
    def __init__(self):
        AbsCollectionNode.__init__(self)
    
    def execute(self):
        for node in self.children:
            node.execute()
            
class SelectionNode(AbsCollectionNode):
    
    def __init__(self):
        AbsCollectionNode.__init__(self)
    
    def execute(self):
        for node in self.children:
            node.execute()

var = SequenceNode();
var.extend([
    "test",
    "problem",
    "manuel"])
var.execute()