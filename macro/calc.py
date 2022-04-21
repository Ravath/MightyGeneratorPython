# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:40:36 2022

@author: Ehlion

| Module for integer management in macros and generator.
| Includes mathematical operators and IntReferences.
"""


#___________________________________________________#
#                                                   #
#                  Rand Interface                   #
#___________________________________________________#
class ValueIf :
    """Default interface with basic implementation
    of an encapsulated integer value"""

    def __init__(self) :
        pass

    def get_value(self) -> int :
        """Get the value."""
        raise NotImplementedError(f"In class {type(self).__name__}")

    value = property(get_value)

#TODO mathematical operations
