# -*- coding: utf-8 -*-
"""
@author: Ehlion
"""
from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsLeafNode

class FormatNode(AbsLeafNode):
    """Applies the current format and saves in the target buffer."""

    def __init__(self, varid = None, format:str = None):
        AbsLeafNode.__init__(self)
        self.varid = varid
        """If null, uses current buffer"""
        self.format = format
        """If null, uses buffer content"""

    def node_action(self, generation_result:GenerationResult):
        """Set value to the target variable using the given format."""
        # get format
        to_process = self.format
        if not self.format:
            to_process = generation_result.get_var_or_text(self.varid)
        
        # process
        text = generation_result.format(to_process)
        
        # return to the buffer
        generation_result.set_var_or_text(self.varid, text)
    
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}FORMAT[{self.varid}:{self.format}]")


class MacroNode(AbsLeafNode):
    """Applies the random macros on the target buffer."""

    def __init__(self, varid = None, macro:str = None):
        AbsLeafNode.__init__(self)
        self.varid = varid
        """If null, uses current buffer"""
        self.macro = macro
        """If null, uses buffer content"""

    def node_action(self, generation_result:GenerationResult):
        """Applies the random macros."""
        # get macro
        to_process = self.macro
        if not self.macro:
            to_process = generation_result.get_var_or_text(self.varid)
        
        # process
        text = GenerationResult.roll_macros(to_process)
        
        # return to the buffer
        generation_result.set_var_or_text(self.varid, text)
        
    def print_node(self, tabs:int = 0) :
        tab_signs="\t"*tabs
        print(f"{tab_signs}MACRO[{self.varid}:{self.macro}]")