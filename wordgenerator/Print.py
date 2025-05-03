# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:37:14 2022

@author: Ehlion
"""

import typing
from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsLeafNode, AbsGeneratorNode

# pylint: disable-msg=R0903

def singleton(classe_definie):
    """Implements singleton classes.

    Parameters
    ----------
    classe_definie : Class
        The class to implement as singleton.

    Returns
    -------
    Class
        The instantiating method.
    """
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

class NodeChild :
    """
    At execution, prints a Title
    before printing the main text.
    The main text is indented, and starts at a new line.
    """

    def __init__(self, child = None) :
        self.child = child

    def set_child(self, new_child) :
        self._child = ConvToNode(new_child)

    def get_child(self) :
        return self._child

    child = property(get_child, set_child)

    def __lshift__(self, other) :
        """Use '<<' as shortcut for the 'set_child' operation."""
        self.set_child(other)
        return self

#___________________________________________________#
#                                                   #
#                      PrintNode                    #
#___________________________________________________#
class PrintNode(AbsLeafNode):
    """The most important generator node : prints the given text at execution."""

    def __init__(self, text:str = ""):
        AbsLeafNode.__init__(self)
        self.text = text

    def node_action(self, generation_result:GenerationResult):
        """Print the associated text."""
        generation_result.do_print(self.text)

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        tab_sign="\t"
        print(f"{tab_sign*tabs}{type(self).__name__} : '{self.text}'")

#___________________________________________________#
#                                                   #
#                   CheckpointNode                  #
#___________________________________________________#
class CheckpointNode(AbsLeafNode, NodeChild):
    """A Node wrapper used to manipulate subsections of the generation tree.
    Specific uses include catching output in variables
    and regenerating only a subtree of the whole."""
    
    # The current checkpoints
    checkpoints = dict()

    def __init__(self, label:str, child:AbsGeneratorNode = None):
        AbsLeafNode.__init__(self)
        NodeChild.__init__(self, child)
        self.label = label
        self.text = ""
        CheckpointNode.checkpoints[label] = self

    def node_action(self, generation_result:GenerationResult):
        """Print the associated text."""
        # stack the print
        generation_result.stack()
        
        self.child.node_action(generation_result)
        
        # unstack the print
        self.text = generation_result.unstack()
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}CHECKPOINT[{self.label}]")
        self.child.print_node(tabs+1)

#___________________________________________________#
#                                                   #
#                      ActionNode                   #
#___________________________________________________#
import inspect

def takes_no_arguments(func):
    sig = inspect.signature(func)
    return all(
        param.default != inspect.Parameter.empty or
        param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
        for param in sig.parameters.values()
    )
    
class ActionNode(AbsLeafNode):
    """Execute the given function at execution."""

    def __init__(self, func:typing.Callable[[], None]):
        AbsLeafNode.__init__(self)
        assert callable(func)
        self.func = func

    def node_action(self, generation_result:GenerationResult):
        """Execute the given function."""
        if takes_no_arguments(self.func):
            self.func()
        else:
            # if function argument, pass the generation result
            self.func(generation_result)

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        tab_sign="\t"
        print(f"{tab_sign*tabs}{type(self).__name__} : {self.func.__name__ }()")

class SetNode(ActionNode) :
    """Execute the given setter function at execution
    with the given argument"""

    def __init__(self, set_function, set_value) :
        """
        Initiate set SetNode class.

        Parameters
        ----------
        set_function : A setter function.
        set_value : The value to set at execution.
        """
        self.set_value = set_value
        ActionNode.__init__(self, set_function)

    def node_action(self, generation_result:GenerationResult):
        """Execute the given function."""
        self.func(self.set_value)

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        tab_sign="\t"
        print(f"{tab_sign*tabs}{type(self).__name__} : " \
              f"{self.func.__name__ }({self.set_value})")

#___________________________________________________#
#                                                   #
#                    CONV FACILITIES                #
#___________________________________________________#

def CanConvToNode(conv_from) -> AbsGeneratorNode :
    """Check if the given value is of a type the current implementation
    can mange/convert into a executable node.
    See 'ConvToNode' function.
    """
    return (isinstance(conv_from, str) or
            callable(conv_from) or
            isinstance(conv_from, AbsGeneratorNode))

def ConvToNode(conv_from) -> AbsGeneratorNode :
    """Convert a value to a managable node.
        str->PrintNode
        callable(function)->ActionNode
        Already a Node -> no need to convert it.
    """
    if conv_from is None :
        return None
    elif isinstance(conv_from, str) :
        return PrintNode(conv_from)
    elif callable(conv_from) :
        return ActionNode(conv_from)
    elif isinstance(conv_from, AbsGeneratorNode) :
        return conv_from
    else :
        raise TypeError(f"Must be a node, some text or a function, but is {type(conv_from)}")
#___________________________________________________#
#                                                   #
#                     STR FORMATING                 #
#___________________________________________________#

class Title(PrintNode, NodeChild) :
    """
    At execution, prints a Title
    before printing the main text.
    The main text is indented, and starts at a new line.
    """

    def __init__(self, title:str, child = None) :
        PrintNode.__init__(self, title)
        NodeChild.__init__(self, child)

    def node_action(self, generation_result:GenerationResult):
        """Print the title, and then
        execute the children with one tabulation more."""
        PrintNode.node_action(self, generation_result)
        GenerationResult.tabs += 1
        generation_result.end_section()
        self.child.node_action(generation_result)
        GenerationResult.tabs -= 1
        generation_result.end_section()

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        PrintNode.print_node(self, tabs)
        self.child.print_node(tabs+1)

class Label(PrintNode, NodeChild) :
    """
    At execution, prints a text label
    before printing the main text.
    The main text is concatened directly after the label and a ':'.
    """

    def __init__(self, label:str, child = None) :
        PrintNode.__init__(self, label + " : ")
        NodeChild.__init__(self, child)

    def node_action(self, generation_result:GenerationResult):
        """Print the label, and then
        execute the children with one tabulation more."""
        PrintNode.node_action(self, generation_result)
        self.child.node_action(generation_result)
        generation_result.end_section()

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        PrintNode.print_node(self, tabs)
        self.child.print_node(tabs+1)
