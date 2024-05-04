# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:40:29 2022

@author: Ehlion
"""

from wordgenerator.NodeCollectionIf import AbsCollectionNode
from wordgenerator.Print import ConvToNode
from macro.grammar import get_ValueIf

#___________________________________________________#
#                                                   #
#                     SequenceNode                  #
#___________________________________________________#
class SequenceNode(AbsCollectionNode):
    """A basic collection node. Executes every child sequentially"""

    def __init__(self, nbr_draw = 1, inbetween_action = None):
        AbsCollectionNode.__init__(self)
        self.nbr_draw = nbr_draw
        self.inbetween_action = inbetween_action

    def draw(self):
        """draw every children sequentially"""
        first_action = True

        for _ in range(0, self.nbr_draw.value) :

            for row in self.children :
                if first_action :
                    first_action = False
                else :
                    yield self.inbetween_action
                yield row.node

    def print_node(self, tabs:int = 0) :
        """print the node and its children.
        Hide the rows"""
        tab_sign="\t"*tabs
        print(f"{tab_sign}[{type(self).__name__} : {self.__str_attributes__()}]")

        for row in self.children :
            row.node.print_node(tabs+1)

    def get_nbr_draw(self) :
        return self._nbr_draw
    def set_nbr_draw(self, dice) :
        self._nbr_draw = get_ValueIf(dice)
    nbr_draw = property(get_nbr_draw, set_nbr_draw)

    def set_inbetween_action(self, new_inbetween) :
        self._inbetween_action = ConvToNode(new_inbetween)
    def get_inbetween_action(self) :
        return self._inbetween_action
    inbetween_action = property(get_inbetween_action, set_inbetween_action)

    def __str_attributes__(self) -> str :
        return f"Draws={self.nbr_draw} " \


def S(*args) :
    """Simplification use of Sequence Node."""
    return SequenceNode() << [*args]