# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:37:14 2022

@author: Ehlion
"""

from wordgenerator.NodeIf import AbsLeafNode

#___________________________________________________#
#                                                   #
#                      PrintNode                    #
#___________________________________________________#
class PrintNode(AbsLeafNode):
    """
    The most important generator node : prints the given text at execution.
    """
    
    def __init__(self, text:str = ""):
        AbsLeafNode.__init__(self)
        self.text = text
        
    def execute(self):
        print(self.text)
    
    def printNode(self, tabs:int = 0) :
        print("{tabs}{name} : '{text}'".
              format(tabs="\t"*tabs,
                     name=type(self).__name__,
                     text=self.text))