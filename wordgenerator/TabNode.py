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

    def _set_nbr_draw(self, new_nbr_draw) :
        self._nbr_draw = get_ValueIf(new_nbr_draw)

    def _get_nbr_draw(self) -> ValueIf :
        return self._nbr_draw

    nbr_draw = property(_get_nbr_draw, _set_nbr_draw)

    def __init__(self, value, nbr_draw = 1) :
        AbsCollectionNode.__init__(self)
        self.value = value
        self.nbr_draw = nbr_draw

    def draw(self) :
        for _ in range(0, self.nbr_draw.value) :
            yield self.children[self.value.value].node

    def __str_attributes__(self) -> str :
        return f"Value={self.value} "\
               f"Draws={self.nbr_draw} "
