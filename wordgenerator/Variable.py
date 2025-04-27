# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:55:00 2025

@author: Ehlion
"""

from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsLeafNode, AbsGeneratorNode
from wordgenerator.Print import ConvToNode

class CurrentVarNode(AbsLeafNode):
    """Node changing the buffer context.
        Every print onforth will be buffered to the variable with the given Id.

    Args:
        varid: Id of the variable to switch to.
    """

    def __init__(self, varid):
        AbsLeafNode.__init__(self)
        self.varid = varid

    def node_action(self, generation_result:GenerationResult):
        """Switch to the associated variable."""
        # use a new text buffer
        generation_result.switch_to_var(self.varid)
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}CURRENT_VAR[{self.varid}]")

class SetVarNode(AbsLeafNode):
    def __init__(self, varid, value):
        AbsLeafNode.__init__(self)
        self.varid = varid
        self.value = value

    def node_action(self, generation_result:GenerationResult):
        """Set value to the associated variable."""
        generation_result.set_var(self.varid, self.value)
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}SETVAR[{self.varid}:{self.value}]")

class DefineNode(AbsLeafNode):
    """Switch to a new buffer only if the variable doesn't already exist.
        Useful for managing generation input : If a input has been given, 
        the child is not executed, and the input valuue will be used instead.

    Args:
        varid : The name of the variable
        child : The child tree to execute and supposed to set the variable if not already done.
    """

    def __init__(self, varid, child:AbsGeneratorNode = None):
        AbsLeafNode.__init__(self)
        self.varid = varid
        self.child = child

    def node_action(self, generation_result:GenerationResult):
        """Switch to the associated variable if not already defined.
            In such case only, execute children nodes to have them define the desired variable."""
        if not generation_result.is_var_defined(self.varid):
            self.previous_varid = generation_result.current_var_id
            generation_result.switch_to_var(self.varid)
            self.child.node_action(generation_result)
            generation_result.switch_to_var(self.previous_varid)

    def set_child(self, new_child) :
        self._child = ConvToNode(new_child)

    def get_child(self) :
        return self._child

    child = property(get_child, set_child)

    def __lshift__(self, other) :
        """Use '<<' as shortcut for the 'set_child' operation."""
        self.set_child(other)
        return self
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}DEFINE[{self.varid}]")