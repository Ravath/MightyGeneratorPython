# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:37:14 2022

@author: Ehlion
"""

import io
import typing
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

#___________________________________________________#
#                                                   #
#                  PrintDelegationIf                #
#___________________________________________________#
class PrintDelegationIf:
    """A delegation for managing a given string."""

    def __init__(self) :
        PrintDelegationIf.tabs = 0

    @classmethod
    def __subclasshook__(cls, subclass) :
        return (hasattr(subclass, 'do_print') and
                callable(subclass.do_print) or
                NotImplemented)

    def do_print(self, to_print:str) :
        """Print the given text."""
        raise NotImplementedError(f"In class {type(self).__name__}")

    def end_section(self) :
        """Print the end of a text section."""
        raise NotImplementedError(f"In class {type(self).__name__}")

@singleton
class PrintToConsole(PrintDelegationIf):
    """Print the given text to the console."""

    def do_print(self, to_print:str) :
        """Print the given text to the console."""
        tabs = '\t' * PrintDelegationIf.tabs
        print(tabs + to_print)

    def end_section(self) :
        pass

@singleton
class PrintToBuffer(PrintDelegationIf):
    """Concatene the text in a single string."""

    def __init__(self) :
        self.str_build = io.StringIO()

    def do_print(self, to_print:str) :
        """Concatene the given text to the generated string."""
        tabs = ""
        if self.str_build.getvalue().endswith('\n') :
            tabs = '\t' * PrintDelegationIf.tabs
        self.str_build.write(tabs + to_print)

    def end_section(self) :
        self.str_build.write('\n')

    def get_text(self) -> str :
        """Get the generated string."""
        return self.str_build.getvalue()

    def del_text(self) :
        """Reset the generated string."""
        self.str_build = ""

#___________________________________________________#
#                                                   #
#                      PrintNode                    #
#___________________________________________________#
class PrintNode(AbsLeafNode):
    """The most important generator node : prints the given text at execution."""

    # print delegate """
    _printer = PrintToConsole()

    def __init__(self, text:str = ""):
        AbsLeafNode.__init__(self)
        self.text = text

    def execute(self):
        """Print the associated text."""
        PrintNode._printer.do_print(self.text)

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        tab_sign="\t"
        print(f"{tab_sign*tabs}{type(self).__name__} : '{self.text}'")

class Title(PrintNode) :
    def __init__(self, title:str, child:AbsGeneratorNode) :
        PrintNode.__init__(self, title)
        self.child = child

    def execute(self) :
        """Print the title, and then
        execute the children with one tabulation more."""
        PrintNode.execute(self)
        PrintDelegationIf.tabs += 1
        self._printer.end_section()
        self.child.execute()
        PrintDelegationIf.tabs -= 1
        self._printer.end_section()

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        PrintNode.print_node(self, tabs)
        self.child.print_node(tabs+1)

class Label(PrintNode) :
    def __init__(self, label:str, child:AbsGeneratorNode) :
        PrintNode.__init__(self, label + " : ")
        self.child = child

    def execute(self) :
        """Print the label, and then
        execute the children with one tabulation more."""
        PrintNode.execute(self)
        self.child.execute()
        self._printer.end_section()

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        PrintNode.print_node(self, tabs)
        self.child.print_node(tabs+1)

#___________________________________________________#
#                                                   #
#                      ActionNode                   #
#___________________________________________________#
class ActionNode(AbsLeafNode):
    """Execute the given function at execution."""

    def __init__(self, func:typing.Callable[[], None]):
        AbsLeafNode.__init__(self)
        assert callable(func)
        self.func = func

    def execute(self):
        """Execute the given function."""
        self.func()
