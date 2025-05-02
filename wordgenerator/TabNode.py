# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 23:13:25 2022

@author: Ehlion
"""

from wordgenerator.NodeCollectionIf import AbsCollectionNode
from macro.math import ValueIf
from macro.grammar import get_ValueIf

class TabNode(AbsCollectionNode) :

    def _set_value(self, new_value) :
        self._value = get_ValueIf(new_value)

    def _get_value(self) -> ValueIf :
        return self._value

    value = property(_get_value, _set_value)
    """Index of the value to draw at execution."""

    def _set_nbr_draw(self, new_nbr_draw) :
        self._nbr_draw = get_ValueIf(new_nbr_draw)

    def _get_nbr_draw(self) -> ValueIf :
        return self._nbr_draw

    nbr_draw = property(_get_nbr_draw, _set_nbr_draw)
    """The number of items to draw at execution."""

    def __init__(self, value, nbr_draw = 1, before_execute=None, after_execute=None, 
                 before_action=None, between_action=None, after_action=None) :
        AbsCollectionNode.__init__(self, before_execute, after_execute,
                                   before_action, between_action, after_action)
        self.value = value
        self.nbr_draw = nbr_draw
    
    def Automaton(pick_nbr:list[int], nbr_draw:int = 1):
        tp = []
        it = 0
        for p in pick_nbr:
            tp.append((it,p))
            it += 1
        
        return TabNode(tp, nbr_draw)

    def draw(self) :
        for _ in range(0, self.nbr_draw.value) :
            yield self.children[self.value.value].node

    def __str_attributes__(self) -> str :
        return f"Value={self.value} "\
               f"Draws={self.nbr_draw} "
