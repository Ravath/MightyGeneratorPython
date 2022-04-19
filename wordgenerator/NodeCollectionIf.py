# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:39:26 2022

@author: Ehlion
"""

from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import PrintNode

#___________________________________________________#
#                                                   #
#                      RowNode                      #
#___________________________________________________#
class RowNode:
    
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
        self.argumentConversion={}
        
        """ We introduce default behavor:
            String or nodes or stored in self.node.
        """
        # Be Carreful : messing with attribute names will create new ones
        def conv1(self, s1) :
                self.setNode(s1)
        self.argumentConversion = [
            ([str], conv1),
            ([AbsGeneratorNode], conv1),
        ]
    
    def setNode(self, node) :
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
        if type(node) is str :
            self.node=PrintNode(node)
        elif isinstance(node, AbsGeneratorNode) :
            self.node=node
        else :
            raise TypeError("Must be a node or some text")
            
    def put(self, *args, **kargs) :
        """
            Parse the given arguments according to type and name
    
            Parameters
            ----------
            *args : List of arguments for the row
                The type and order of the arguments
                are relevant and must match a signature in
                the 'self.argumentConversion' table.
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
        
        """Do the unnamed arguments"""
        if len(args) > 0:
            types = [type(v) for v in args]
            found = False
            
            # compare every signature
            for signature, convertor in self.argumentConversion:
                if len(signature) != len(args) : continue
            
                # check same signature
                if signature == types:
                    found=True
                else : # compare signature types one by one
                    found=True
                    for it in range(0,len(args)) :
                        if (signature[it] != types[it] and
                           not issubclass(types[it], signature[it]) ) :
                            found=False
                            break
                        
                # if type signature found, do conversion
                if found :
                    convertor(self, *args)
                    break
            if not found:
                raise TypeError("Can't convert given types " + str(types))
        
        """Do the named arguments"""
        for (k,v) in kargs.items() :
            # get ride of trivial case
            if k == "node":
                self.setNode(v)
            # Check if the attribute exists
            elif k in self.__dict__:
                # Check if the type is compatible
                if type(v) == type(self.__dict__[k]) :
                    self.__dict__[k]=v
                else : raise  TypeError("argument '{}' of type {} is incompatible with type '{}'".
                                        format(k, type(v), type(self.__dict__[k])))
            else : raise NameError("Row has no attribute '" + k + "'")
        
    #####################################################
    #                  PRINT NODE LOGIC                 #
    #####################################################
    
    def __str_attributes__(self) -> str :
        """Get the attributes and values into a string"""
        return ""
    
    def printNode(self, tabs:int = 0) :
        
        print("{tabs}[{name} : {attributes}]".
              format(tabs="\t"*tabs,
                     name="ROW",
                     attributes=self.__str_attributes__()))
        
        self.node.printNode(tabs+1)

#___________________________________________________#
#                                                   #
#                 AbsCollectionNode                 #
#___________________________________________________#
class AbsCollectionNode(AbsGeneratorNode) :
    """
    A generic collection node for the composite pattern.
    """
        
    @classmethod
    def __subclasshook__(cls, subclass) :
        return (hasattr(subclass, 'draw') and 
                callable(subclass.draw)and
                hasattr(subclass, 'getRow') and 
                callable(subclass.getRow) or 
                NotImplemented)
    
    def __init__(self) :
        AbsGeneratorNode.__init__(self)
        self.children = list()
        
    #####################################################
    #                   EXECUTE LOGIC                   #
    #####################################################
    
    def draw(self) :
        """draw some children"""
        raise NotImplementedError("In class {}".format(type(self).__name__))
    
    def execute(self) :
        for node in self.draw() :
            if node :
                node.execute()
        
    #####################################################
    #                ROW COLLECTION LOGIC               #
    #####################################################
        
    def getRow(self, *args, **kargs) -> RowNode:
        """Convert given arguments into a suitable row
            for the collection.
            No specific arguments by default.
        """
        newRow=RowNode()
        newRow.put(*args, **kargs)
        return newRow
        
    def extend(self, table) :
        assert type(table) is list
        for t in table :
            if (type(t) is str or
                type(t) is not list) :
                newRow = self.getRow(t)
            else :
                newRow = self.getRow(*t)
            self.children.append(newRow)
        
    def append(self, *args, **kargs) :
        newRow = self.getRow(*args, **kargs)
        self.children.append(newRow)
        
    def insert(self, index:int, *args, **kargs) :
        newRow = self.getRow(*args, **kargs)
        self.children.insert(index, newRow)
        
    #####################################################
    #                  PRINT NODE LOGIC                 #
    #####################################################
    
    def __str_attributes__(self) -> str :
        """Get the attributes and values into a string"""
        return ""
    
    def printNode(self, tabs:int = 0) :
        
        print("{tabs}[{name} : {attributes}]".
              format(tabs="\t"*tabs,
                     name=type(self).__name__,
                     attributes=self.__str_attributes__()))
        
        for row in self.children :
            row.printNode(tabs+1)
        