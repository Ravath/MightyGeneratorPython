# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:37:14 2022

@author: Ehlion
"""

import io
from wordgenerator.NodeIf import AbsLeafNode

def singleton(classe_definie):
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
    
    @classmethod
    def __subclasshook__(cls, subclass) :
        return (hasattr(subclass, 'doPrint') and 
                callable(subclass.doPrint) or 
                NotImplemented)
    
    def doPrint(self, toPrint:str) :
        raise NotImplementedError("In class {}".format(type(self).__name__))

@singleton
class PrintToConsole(PrintDelegationIf):
    
    def doPrint(self, toPrint:str) :
        print(toPrint)

@singleton
class PrintToBuffer(PrintDelegationIf):
    
    def __init__(self) :
        self.sb = io.StringIO()
    
    def doPrint(self, toPrint:str) :
        self.sb.write(toPrint)
    
    def getText(self) -> str :
        return self.sb.getvalue()

#___________________________________________________#
#                                                   #
#                      PrintNode                    #
#___________________________________________________#
class PrintNode(AbsLeafNode):
    """
    The most important generator node : prints the given text at execution.
    """
    
    """ print delegate """
    _printer = PrintToConsole()
    
    def __init__(self, text:str = ""):
        AbsLeafNode.__init__(self)
        self.text = text
        
    def execute(self):
        PrintNode._printer.doPrint(self.text)
    
    def printNode(self, tabs:int = 0) :
        print("{tabs}{name} : '{text}'".
              format(tabs="\t"*tabs,
                     name=type(self).__name__,
                     text=self.text))
    
    # """ Printer Delegate Attribute """
    # def _get_printer(self):
    #     return PrintNode._printer
    # def _set_printer(self, newPrinter):
    #     if isinstance(newPrinter, PrintDelegationIf) :
    #         PrintNode._printer = newPrinter
    #     else : raise TypeError("{} is not an implementation of {}"
    #                            .format(type(newPrinter), "PrintDelegationIf"))
    # printer = property(_get_printer, _set_printer)


