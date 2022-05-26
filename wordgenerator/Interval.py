# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:35:42 2020

@author: Ehlion
"""

from macro.dice import ValueIf, PoolSum, Pool
from macro.calc import Value
from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.NodeCollectionIf import AbsCollectionNode, RowNode
from wordgenerator.Print import PrintNode

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

    min = property(get_min, set_min)
    max = property(get_max, set_max)

    def __init__(self) :
        RowNode.__init__(self)

        # introduce new attributes
        self._min=1
        self._max=1

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
        self.argument_conversion.extend([
            ([int], int1),
            ([int,int], int2),
            ([int,AbsGeneratorNode], conv2),
            ([int,int,AbsGeneratorNode], conv3),
        ])
# pylint: enable-msg=C0103

    def __str_attributes__(self) -> str :
        return f"Min={self.min} Max={self.max}"

#___________________________________________________#
#                                                   #
#                    IntervalNode                   #
#___________________________________________________#
class IntervalNode(AbsCollectionNode) :
    """A random collection where the rows are drawn
    if the random is between the min and max interval
    of the given row."""

    def __init__(self, dice:ValueIf, number_of_draw = 1, put_back:bool = True) :
        AbsCollectionNode.__init__(self)

        # dice is a ValueIf, or an int
        self.dice = dice
        if isinstance(dice, int) :
            self.dice = Value(dice)
        # number_of_draw is a ValueIf, or an int
        self.number_of_draw = number_of_draw
        if isinstance(number_of_draw, int) :
            self.number_of_draw = Value(number_of_draw)
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

    def draw(self) :
        """Draw a random value from the given random generation
        and draw rows consequently."""
        res=self.dice.value
        return self.draw_from_result(res)

    def draw_from_result(self, roll:int) :
        """Get the result for the given value."""
        for row in self.children:
            if row.min <= roll <= row.max:
                yield row.node

    def __str_attributes__(self) -> str :
        return f"Draws={self.number_of_draw.value} PutBack={self.put_back}"

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :
    from utils.debug import test, print_log

    var = IntervalNode(PoolSum(Pool(1,4)))
    var.extend([
        [0, 4, "test"],
        [1, 2, PrintNode("yes")],
        [3, 2, "problem"],
        [5,10, PrintNode("manuel")]
    ])
    var.print_node()
    #can't do because have to implement roll
    #var.execute()
    for i in range(0,6) :
        print(f"== {i} ==")
        for resNode in var.draw_from_result(i) :
            resNode.execute()
    var.execute()
