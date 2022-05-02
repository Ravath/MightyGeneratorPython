# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:39:26 2022

@author: Ehlion
"""

from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import CanConvToNode, ConvToNode

#___________________________________________________#
#                                                   #
#                      RowNode                      #
#___________________________________________________#
class RowNode :
    """ A generic row node for the bridge pattern between
    the CollectionNode and the children nodes. """

    def __init__(self) :
        """ The node child of this row
                TYPE : AbsGeneratorNode
        """
        self.node=None
        """ Conversion table (signature -> convertor function).
                A list of signature types associated with the conversion method
                parsing the arguments given to the row.
                TYPE : *(*types, function(self, *args))
        """
        self.argument_conversion={}

        """ We introduce default behavor:
            String or nodes or stored in self.node.
        """
        # Be Carreful : messing with attribute names will create new ones
        def conv1(self, s1) :
            self.set_node(s1)
        self.argument_conversion = [
            ([AbsGeneratorNode], conv1),
        ]

    def set_node(self, node) :
        """
            Set the child node of the row

            Parameters
            ----------
            node
                AbsGeneratorNode

            Raises
            ------
            TypeError
                The argument must be a string or a node.
        """
        self.node = ConvToNode(node)

    def put(self, *args, **kargs) :
        """
            Parse the given arguments according to type and name

            Parameters
            ----------
            *args : List of arguments for the row
                The type and order of the arguments
                are relevant and must match a signature in
                the 'self.argument_conversion' table.
            **kargs : dictionnary of arguments for the row
                The given argument names must match
                attributes names of the row.

            Raises
            ------
            TypeError
                The argument type must match or be a subclass
                of the attribute type.
            NameError
                The argument name must correspond to an attribute name.
        """

        # Do the unnamed arguments
        if len(args) > 0:
            types = [type(v) for v in args]
            found = False

            # compare every signature
            for signature, convertor in self.argument_conversion:
                if len(signature) != len(args) : continue

                # check same signature
                if signature == types:
                    found=True
                else : # compare signature types one by one
                    found=True
                    for it in range(0,len(args)) :
                        # check if it is a subtype
                        if (signature[it] != types[it] and
                            not issubclass(types[it], signature[it])) :
                            # or a specific : str and functions are converted
                            # and must therefore be treated as equivalent as a node
                            if (signature[it] != AbsGeneratorNode or
                                not CanConvToNode(args[it])) :
                                found=False
                                break

                # if type signature found, do conversion
                if found :
                    convertor(self, *args)
                    break
            if not found:
                raise TypeError(f"Can't convert given types {str(types)}")

        # Do the named arguments
        for (k,v) in kargs.items() :
            # get ride of trivial case
            if k == "node":
                self.set_node(v)
            # Check if the attribute exists
            elif k in self.__dict__:
                # Check if the type is compatible
                if isinstance(v, type(self.__dict__[k])) :
                    self.__dict__[k]=v
                else : raise  TypeError(f"argument '{k}' of type {type(v)} "\
                                        f"is incompatible with type '{type(self.__dict__[k])}'")
            else : raise NameError(f"Row has no attribute '{k}'")

    #####################################################
    #                  PRINT NODE LOGIC                 #
    #####################################################

    def __str_attributes__(self) -> str :
        """Get the attributes and values into a string"""
        return ""

    def print_node(self, tabs:int = 0) :
        """print the row node and its child."""
        tab_signs = "\t"*tabs
        print(f"{tab_signs}[ROW : {self.__str_attributes__()}]")

        self.node.print_node(tabs+1)

#___________________________________________________#
#                                                   #
#                 AbsCollectionNode                 #
#___________________________________________________#
class AbsCollectionNode(AbsGeneratorNode) :
    """ A generic collection node for the composite pattern. """

    @classmethod
    def __subclasshook__(cls, subclass) :
        return (hasattr(subclass, 'draw') and
                callable(subclass.draw)and
                hasattr(subclass, 'get_row') and
                callable(subclass.get_row) or
                NotImplemented)

    def __init__(self) :
        AbsGeneratorNode.__init__(self)
        self.children = []

    #####################################################
    #                   EXECUTE LOGIC                   #
    #####################################################

    def draw(self) :
        """draw some children"""
        raise NotImplementedError(f"In class {type(self).__name__}")

    def execute(self) :
        """Execute every node drawn from the collection."""
        for node in self.draw() :
            if node :
                node.execute()

    #####################################################
    #                ROW COLLECTION LOGIC               #
    #####################################################

    def get_row(self, *args, **kargs) -> RowNode:
        """Convert given arguments into a suitable row
            for the collection.
            No specific arguments by default.
        """
        new_row = RowNode()
        new_row.put(*args, **kargs)
        return new_row

    def extend(self, table) :
        """Append new RowNodes.
        Arguments are managed by the argument_conversion table
        of the appropriate row class."""
        assert isinstance(table, list)
        for row_args in table :
            if (isinstance(row_args, str) or
                not isinstance(row_args, list)) :
                new_row = self.get_row(row_args)
            else :
                new_row = self.get_row(*row_args)
            self.children.append(new_row)
        return self

    def append(self, *args, **kargs) :
        """Append a new RowNode.
        Arguments are managed by the argument_conversion table
        of the appropriate row class."""
        new_row = self.get_row(*args, **kargs)
        self.children.append(new_row)
        return self

    def insert(self, index:int, *args, **kargs) :
        """Insert a new RowNode at the given index.
        Arguments are managed by the argument_conversion table
        of the appropriate row class."""
        new_row = self.get_row(*args, **kargs)
        self.children.insert(index, new_row)
        return self

    def __iter__(self) :
        return [n.node for n in self.children].__iter__()
    def __getitem__(self, key) :
        return self.children[key].node
    def __setitem__(self, key, value) :
        self.children[key].set_node(value)

    #####################################################
    #                  PRINT NODE LOGIC                 #
    #####################################################

    def __str_attributes__(self) -> str :
        """Get the attributes and values into a string"""
        return ""

    def print_node(self, tabs:int = 0) :
        """print the node and its children."""
        tab_sign="\t"*tabs
        print(f"{tab_sign}[{type(self).__name__} : {self.__str_attributes__()}]")

        for row in self.children :
            row.print_node(tabs+1)
