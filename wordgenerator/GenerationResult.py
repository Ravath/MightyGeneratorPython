# -*- coding: utf-8 -*-
"""
The result of a generation
@author: Ehlion
"""
import re

replacement_pattern = re.compile(r'\{(.*?)\}')
"""The pattern to format the string and do replacements."""

class GenerationResult:
    
    def __init__(self):
        # The current indentation level.
        GenerationResult.tabs = 0
        self.current_var_id = "DEFAULT"
        self.var_list = { self.current_var_id }
        self._raw_text = {self.current_var_id : ""}
        self.text = ""
        
        self.checkpoints_stack = list()
        
    #### The raw_text property ####
    
    def get_text(self) -> str :
        return self._raw_text[self.current_var_id]
        
    def set_text(self, text:str):
        self._raw_text[self.current_var_id ] = text
    
    raw_text = property(get_text, set_text)
    
    #### The switch variable mechanism ####
    
    def switch_to_var(self, varid):
        self.current_var_id = varid
        if not varid in self.var_list:
            self.var_list.add(varid)
            self._raw_text[varid] = ""
    
    def set_var(self, varid, value):
        if not varid in self.var_list:
            self.var_list.add(varid)
        self._raw_text[varid] = value
    
    def get_var(self, varid):
        return self._raw_text[varid]
    
    def is_var_defined(self, varid):
        return varid in self.var_list and self._raw_text[varid] != ""
    
    #### The print accesses ####
    
    def do_print(self, to_print:str) :
        """Concatene the given text to the generated string."""
        tabs = ""
        if self.raw_text.endswith('\n') or self.raw_text == "":
            tabs = '\t' * GenerationResult.tabs
        self.raw_text += tabs + to_print

    def end_section(self) :
        self.raw_text += '\n'
    
    #### The stack mechanism ####
    
    def stack(self):
        self.checkpoints_stack.append(self.raw_text)
        self.raw_text = ""
    
    def unstack(self) -> str:
        ret = self.raw_text
        self.raw_text = self.checkpoints_stack.pop() + self.raw_text
        return ret
    
    #### output access ####
    
    def format(self, format_string:str) -> str:
        text = format_string
        for match in replacement_pattern.finditer(text):
            varid = match.group(1)
            if self.is_var_defined(varid):
                # find replacement text
                new_text = self._raw_text[varid]
                # replace any match
                text = re.sub(match.group(0), new_text, text)
        return text
        
    def print_to_console(self, format_string:str=None):
        toprint = self.raw_text
        if format_string:
            toprint = self.format(format_string)
        print(toprint)
        
    def display_vars(self):
        for var in self.var_list:
            print(var, self._raw_text[var])
        