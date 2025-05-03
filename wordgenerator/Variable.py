# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 11:55:00 2025

@author: Ehlion
"""

from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsLeafNode, AbsGeneratorNode
from wordgenerator.Output import FormatNode, MacroNode
from wordgenerator.Print import NodeChild

class SwitchVarNode(AbsLeafNode):
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

class ContextNode(AbsLeafNode, NodeChild):
    """Use the target buffer as context, execute children, and then get back to previous context.\n
        Before leaving the context, can automatically 
    Args:
        varid : The name of the variable
        autoformat : true for applying the format on the current context at the end of the action.
        automacro : true for applying the macros on the current context at the end of the action.
        append : true to reset the target context when switching to it.
        child : The child tree to execute and supposed to set the variable if not already done.
    """

    def __init__(self, varid,
                 autoformat:bool=True, automacro:bool=True,
                 append=False,
                 child:AbsGeneratorNode = None):
        AbsLeafNode.__init__(self)
        NodeChild.__init__(self, child)
        self.varid = varid
        """The name of the context to switch to."""
        self.append = append
        """Reset the context at start."""
        self.autoformat = autoformat
        """At the end of context, automatically apply format."""
        self.automacro = automacro
        """At the end of context, automatically apply macros."""
        self.child = child
        """The generation that will happen in this context."""

    def node_action(self, generation_result:GenerationResult):
        """Change context,
            then execute children nodes to have them define the desired variable.\n
            Apply format and macro if needed,
            then switch back to previous context.
        """
        # Init new context
        self.previous_varid = generation_result.current_var_id
        generation_result.switch_to_var(self.varid)
        if not self.append:
            generation_result.set_text("")
            
        # Execute context
        self.child.node_action(generation_result)
        
        # Post-treatment
        if self.autoformat:
            FormatNode().node_action(generation_result)
        if self.automacro:
            MacroNode().node_action(generation_result)
        
        # Reset to previous context
        generation_result.switch_to_var(self.previous_varid)
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}CONTEXT[{self.varid} Autoformat:{self.autoformat}, Automacro:{self.automacro}]")
        self.child.print_node(tabs+1)

class DefineNode(ContextNode):
    """Switch to a new buffer only if the variable doesn't already exist.
        Useful for managing generation input : If a input has been given, 
        the child is not executed, and the input valuue will be used instead.

    Args:
        varid : The name of the variable
    """

    def __init__(self, varid, autoformat:bool=True, automacro:bool=True, child:AbsGeneratorNode = None):
        ContextNode.__init__(self, varid, autoformat, automacro, child=child)
    
    def node_action(self, generation_result:GenerationResult):
        """Switch to the contect only if not already defined."""
        if not generation_result.is_var_defined(self.varid):
            ContextNode.node_action(self, generation_result)
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}DEFINE[{self.varid} Autoformat:{self.autoformat}, Automacro:{self.automacro}]")
        self.child.print_node(tabs+1)