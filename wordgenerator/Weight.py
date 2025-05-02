# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:53:57 2020

@authors: Ehlion, Trense
"""

from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.NodeIf import AbsGeneratorNode
from macro.math import ValueIf
from macro.dice import randint

#___________________________________________________#
#                                                   #
#                     WeightRow                     #
#___________________________________________________#
class WeightRow(RowNode):

    def _get_weight(self) -> int :
        if isinstance(self._weight, int) :
            return self._weight
        elif isinstance(self._weight, ValueIf) :
            return self._weight.value
        else :
            raise ValueError("Weight must be 'int' or 'ValueIf'")

    def _set_weight(self, new_weight) :
        self._weight = new_weight
        if (not isinstance(new_weight, int) and
            not isinstance(new_weight, ValueIf)) :
            raise ValueError("Weight must be 'int' or 'ValueIf'")

    weight = property(_get_weight, _set_weight)

    def _get_nbr_pick(self) -> int :
        if isinstance(self._nbr_pick, int) :
            return self._nbr_pick
        elif isinstance(self._nbr_pick, ValueIf) :
            return self._nbr_pick.value
        else :
            raise ValueError("Nbr_pick must be 'int' or 'ValueIf'")
    def _set_nbr_pick(self, new_nbr_pick) :
        self._nbr_pick = new_nbr_pick
        if (not isinstance(new_nbr_pick, int) and
            not isinstance(new_nbr_pick, ValueIf)) :
            raise ValueError("Nbr_pick must be 'int' or 'ValueIf'")

    nbr_pick = property(_get_nbr_pick, _set_nbr_pick)

    def __init__(self):
        RowNode.__init__(self)

        # Introduce new attributes
        self.weight= 1
        self.nbr_pick = -1 # nbr_pick indicates how many times a row
        # can be picked in a node, a value <0 for nbr_pick allows
        # an infinite pick in a node by default
        self.stopRow = False

        # Extend the signature conversion table
        def int1(self, i1):
            self.weight=i1
        def int2(self, i1, i2):
            self.weight=i1
            self.nbr_pick=i2
        def conv2(self, i1, s1) :
            self.weight=i1
            self.set_node(s1)
        def conv3(self, i1, i2, s1) :
            self.weight=i1
            self.nbr_pick=i2
            self.set_node(s1)
        self.argument_conversion.extend([
            ([int], int1),
            ([int,int], int2),
            ([int,AbsGeneratorNode], conv2),
            ([int,int,AbsGeneratorNode], conv3),
        ])

    def __str_attributes__(self) -> str :
        return f"Weight={self.weight} Pick={self.nbr_pick}"

#___________________________________________________#
#                                                   #
#                     WeightNode                    #
#___________________________________________________#
class WeightNode(AbsCollectionNode):

    def _set_nbr_draw(self, new_nbr_draw) :
        self._nbr_draw = new_nbr_draw
        if (not isinstance(new_nbr_draw, int) and
            not isinstance(new_nbr_draw, ValueIf)) :
            raise ValueError("nbr_draw must be 'int' or 'ValueIf'")

    def _get_nbr_draw(self) -> int :
        if isinstance(self._nbr_draw, int) :
            return self._nbr_draw
        elif isinstance(self._nbr_draw, ValueIf) :
            return self._nbr_draw.value
        else :
            raise ValueError("nbr_draw must be 'int' or 'ValueIf'")

    nbr_draw = property(_get_nbr_draw, _set_nbr_draw)

    def __init__(self, nbr_draw = 1, do_put_back:bool = True,
                 before_execute=None, after_execute=None, 
                 before_action=None, between_action=None, after_action=None):
        AbsCollectionNode.__init__(self, before_execute, after_execute,
                                   before_action, between_action, after_action)
        # flag raised if the total weight of the row
        # has changed and must be recomputed
        self.totalWeight = 0

        # introduce new attributes
        self.nbr_draw = nbr_draw # number of time we will draw a child
        self.do_put_back = do_put_back # (boolean) put back a picked child

    def get_row(self, *args, **kargs) -> WeightRow :
        new_row = WeightRow()
        new_row.put(*args, **kargs)
        return new_row

    def computeTotal(self):
        self.totalWeight = sum([ c.weight for c in self.children
                                if c.weight > 0 ])

    def draw(self):
        """Draw a random node from every node put into a Weightnode.
        Consider weight and number of pick for every node.
        """
        # Sum the total weight
        self.computeTotal()
        # Initialising stopRow value for picking
        for child in self.children :
            child.stopRow = False
            child.loop_nbr_pick = child.nbr_pick # loop_nbr_pick is made for not
            # changing nbr_pick value between several WeightNode calls

        if self.totalWeight == 0 : return

        for y in range(0, self.nbr_draw):
            # Stops if no one can be picked
            if self.totalWeight == 0 :
                return

            ### Roll ###
            # First, get a random number between 1 and totalWeight
            roll = randint(1,self.totalWeight)
            index = 0
            # Then, find associated entry
            # Particular case if first pick of the list has been row
            if self.children[index].stopRow == False :
                roll -= self.children[index].weight
            else : pass

            # roll decreases and index increases accordingly until roll = O...
            while roll > 0:
                index += 1
                if self.children[index].stopRow == False :
                    roll -= self.children[index].weight

            # ...and it picks children[index] associated.
            yield self.children[index].node
            self.children[index].loop_nbr_pick -= 1

            # Conditions for putting back row and how many times it will do it
            if (self.do_put_back == False or
                (self.do_put_back == True and self.children[index].loop_nbr_pick == 0)) :
                self.children[index].stopRow = True
                self.totalWeight -= self.children[index].weight
            else: pass

    def __str_attributes__(self) -> str :
        # Sum the total weight
        self.computeTotal()

        return f"TotalWeight={self.totalWeight} "\
               f"Draws={self.nbr_draw} " \
               f"PutBack={self.do_put_back}"
