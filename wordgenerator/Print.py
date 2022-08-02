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
        # The current indentation level.
        PrintDelegationIf.tabs = 0

    @classmethod
    def __subclasshook__(cls, subclass) :
        """
        The instance must instanciate a do_print function.
        """
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
    """Concatene the text in a single string.
    Have to manage endOfLine and indentation by hand
    in order to be consistent with the PrintToConsole class behavior.
    """

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
        self.str_build = io.StringIO()

#___________________________________________________#
#                                                   #
#                      PrintNode                    #
#___________________________________________________#
class PrintNode(AbsLeafNode):
    """The most important generator node : prints the given text at execution."""

    # print delegate """
    _printer = PrintToConsole()

    def print_to_buffer() :
        PrintNode._printer = PrintToBuffer()

    def print_buffer() :
        print(PrintNode._printer.get_text())

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
        set_value : The value to set à execution.
        """
        self.set_value = set_value
        ActionNode.__init__(self, set_function)

    def execute(self):
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
        callable(function)->ActoinNode
        Already a Node -> no need to convert it.
    """
    if isinstance(conv_from, str) :
        return PrintNode(conv_from)
    elif callable(conv_from) :
        return ActionNode(conv_from)
    elif isinstance(conv_from, AbsGeneratorNode) :
        return conv_from
    else :
        raise TypeError("Must be a node, some text or a function")
#___________________________________________________#
#                                                   #
#                     STR FORMATING                 #
#___________________________________________________#

class Title(PrintNode) :
    """
    At execution, prints a Title
    before printing the main text.
    The main text is indented, and starts at a new line.
    """

    def __init__(self, title:str, child) :
        PrintNode.__init__(self, title)
        self.child = ConvToNode(child)

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
    """
    At execution, prints a text label
    before printing the main text.
    The main text is concatened directly after the label and a ':'.
    """

    def __init__(self, label:str, child) :
        PrintNode.__init__(self, label + " : ")
        self.child = ConvToNode(child)

    def execute(self) :
        """Print the label, and then
        execute the children with one tabulation more."""

        # We need to use the PrintToBuffer delegate in order to
        # handle the concatenation. because The PrintToConsole
        # delegate will otherwise insert unwanted newLine at each print.
        last, new = self._printer, PrintToBuffer()

        if last == new :
            # The current Print delegation is already a PrintToBuffer.
            PrintNode.execute(self)
            self.child.execute()
            self._printer.end_section()
        else :
            # Use the PrintToBuffer
            PrintNode._printer = new
            prev_buffer_text = new.get_text()
            new.del_text()

            # Do the Printing
            PrintNode.execute(self)
            self.child.execute()

             # flush to the actual Print delegate.
            last.do_print(new.get_text())
            new.del_text()

            # Tidy
            new.do_print(prev_buffer_text)
            PrintNode._printer = last
            self._printer.end_section()

    def print_node(self, tabs:int = 0) :
        """Print the node name and printed text."""
        PrintNode.print_node(self, tabs)
        self.child.print_node(tabs+1)
