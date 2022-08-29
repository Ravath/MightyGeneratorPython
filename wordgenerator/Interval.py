# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:35:42 2020

@author: Ehlion
"""

from macro.dice import ValueIf
from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.Print import PrintNode
from macro.dice_macro import get_ValueIf

#___________________________________________________#
#                                                   #
#                    IntervalRow                    #
#___________________________________________________#
class IntervalRow(RowNode) :
    """The row of an IntervalNode. Encapsulates a node,
    and uses a min-max interval to determine the odds of getting drawn."""

    def set_min(self, new_min) :
        self._min = new_min
        if (not isinstance(new_min, int) and
            not isinstance(new_min, ValueIf)) :
            raise ValueError("Min must be 'int' or 'ValueIf'")

    def get_min(self) -> int :
        if isinstance(self._min, int) :
            return self._min
        elif isinstance(self._min, ValueIf) :
            return self._min.value
        else :
            raise ValueError("Min must be 'int' or 'ValueIf'")

    def set_max(self, new_max) :
        self._max = new_max
        if (not isinstance(new_max, int) and
            not isinstance(new_max, ValueIf)) :
            raise ValueError("Max must be 'int' or 'ValueIf'")

    def get_max(self) -> int :
        if isinstance(self._max, int) :
            return self._max
        elif isinstance(self._max, ValueIf) :
            return self._max.value
        else :
            raise ValueError("Max must be 'int' or 'ValueIf'")
            
    def set_nbr_pick(self, new_nbr_pick) :
            self._nbr_pick = new_nbr_pick
            if (not isinstance(new_nbr_pick, int) and
                not isinstance(new_nbr_pick, ValueIf)) :
                raise ValueError("Nbr_pick must be 'int' or 'ValueIf'")

    def get_nbr_pick(self) -> int :
            if isinstance(self._nbr_pick, int) :
                return self._nbr_pick
            elif isinstance(self._nbr_pick, ValueIf) :
                return self._nbr_pick.value
            else :
                raise ValueError("Nbr_pick must be 'int' or 'ValueIf'")

    min = property(get_min, set_min)
    max = property(get_max, set_max)
    nbr_pick = property(get_nbr_pick, set_nbr_pick)

    def __init__(self) :
        RowNode.__init__(self)

        # introduce new attributes
        self._min=1
        self._max=1
        self._nbr_pick=-1
        
        # extend the signature conversion table
# pylint: disable-msg=C0103
        def int1(self, i1) :
            self.min=i1
        def int2(self, i1, i2) :
            self.min=i1
            self.max=i2
        def conv2(self, i1, s1) :
            self.min=i1
            self.set_node(s1)
        def conv3(self, i1, i2, s1) :
            self.min=i1
            self.max=i2
            self.set_node(s1)
        def conv4(self, i1, i2, i3, s1) :
            self.min=i1
            self.max=i2
            self.nbr_pick=i3
            self.set_node(s1)
        self.argument_conversion.extend([
            ([int], int1),
            ([int,int], int2),
            ([int,AbsGeneratorNode], conv2),
            ([int,int,AbsGeneratorNode], conv3),
            ([int,int,int,AbsGeneratorNode], conv4)
        ])
# pylint: enable-msg=C0103

    def __str_attributes__(self) -> str :
        return f"Min={self.min} Max={self.max}; Pick={self.nbr_pick}"

#___________________________________________________#
#                                                   #
#                    IntervalNode                   #
#___________________________________________________#
class IntervalNode(AbsCollectionNode) :
    """A random collection where the rows are drawn
    if the random is between the min and max interval
    of the given row."""

    def get_dice(self) :
        return self._dice
    def set_dice(self, dice) :
        self._dice = get_ValueIf(dice)
    dice = property(get_dice, set_dice)

    def get_nbr_draw(self) :
        return self._nbr_draw
    def set_nbr_draw(self, dice) :
        self._nbr_draw = get_ValueIf(dice)
    nbr_draw = property(get_nbr_draw, set_nbr_draw)

    def __init__(self, dice, nbr_draw = 1, put_back:bool = True) :
        AbsCollectionNode.__init__(self)

        # dice is a ValueIf, or an int
        self.dice = dice
        self.nbr_draw = nbr_draw
        # put_back is a boolean flag
        self.put_back = put_back
        
    def get_row(self, *args, **kargs) -> IntervalRow :
        """Instanciate the proper row with the given arguments"""
        new_row=IntervalRow()
        new_row.put(*args, **kargs)
        return new_row

    def put(self, vmin, vmax, text) :
        """Add a row with the given interval."""
        self.children.append(((vmin,vmax),text))

    def filter_rows(self, value:int) :
        """Get the rows for the given value."""
        for row in self.children :
            if row.min <= value <= row.max :
                yield row
        
    def draw(self) :
        """Draw a random value from the given random generation
        and draw rows consequently."""
        for child in self.children :
            child.loop_nbr_pick = child.nbr_pick
        for _ in range(0, self.nbr_draw.value) :
            res = self.dice.value
            for row in self.filter_rows(res) :
                if row.loop_nbr_pick != 0 :
                    yield row.node
                    row.loop_nbr_pick -= 1

    def draw_from_result(self, value:int) :
        """Get the result for the given value."""
        for row in self.filter_rows(value) :
                yield row.node

    def __str_attributes__(self) -> str :
        return f"Roll={self.dice} " \
               f"Draws={self.nbr_draw} " \
               f"PutBack={self.put_back}"
