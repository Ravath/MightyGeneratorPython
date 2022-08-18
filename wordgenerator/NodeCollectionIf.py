# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:39:26 2022

@author: Ehlion

| AbsCollectionNode is the parent of every collection Node in the generation structure.
| The collections are not managing the nodes directly,
| a RowNode class has to be implemented to encapsulate the children nodes.
"""

from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import CanConvToNode, ConvToNode
from macro.calc import ValueIf

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
        self._node=None
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
        self._node = ConvToNode(node)

    def get_node(self) -> AbsGeneratorNode :
        """Get the node of this Row"""
        return self._node

    node = property(get_node, set_node)

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
                            if (signature[it] == AbsGeneratorNode and
                                CanConvToNode(args[it])) :
                                pass
                            elif (signature[it] == int and
                                  issubclass(types[it], ValueIf)) :
                                  pass
                            else :
                                found = False
                                break

                # if type signature found, do conversion
                if found :
                    convertor(self, *args)
                    break
            if not found:
                raise TypeError(f"Can't convert given types {str(types)}")

        # Do the named arguments
        for (k,v) in kargs.items() :
            # use build-in functions to set the correct attribute
            self.__setattr__(k, v)

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

        self._node.print_node(tabs+1)

#___________________________________________________#
#                                                   #
#                 AbsCollectionNode                 #
#___________________________________________________#
class AbsCollectionNode(AbsGeneratorNode) :
    """ A generic collection node for the composite pattern. """

    @classmethod
    def __subclasshook__(cls, subclass) :
        """
        Check every instance implements an draw and a get_row function.
        """
        return (hasattr(subclass, 'draw') and
                callable(subclass.draw) and
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

    def __lshift__(self, other) :
        """Use '<<' as shortcut for the 'extend' operation."""
        return self.extend(other)

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
        """Implements spectific iteration access for the class."""
        return [n.node for n in self.children].__iter__()
    def __getitem__(self, key) :
        """Implements spectific '[]' access for the class."""
        return self.children[key].node
    def __setitem__(self, key, value) :
        """Implements spectific '[]' access for the class."""
        self.children[key].set_node(value)

    #####################################################
    #                  PRINT NODE LOGIC                 #
    #####################################################

    def __str_attributes__(self) -> str :
        """Get the attributes and values into a string"""
        return ""

    def print_node(self, tabs:int = 0) :
        """print the node and its children
        with an incremented indentation."""
        tab_sign="\t"*tabs
        print(f"{tab_sign}[{type(self).__name__} : {self.__str_attributes__()}]")
        
        for row in self.children :
            row.print_node(tabs+1)