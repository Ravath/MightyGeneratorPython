# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 01:40:29 2022

@author: Ehlion
"""

from wordgenerator.NodeCollectionIf import AbsCollectionNode

#___________________________________________________#
#                                                   #
#                     SequenceNode                  #
#___________________________________________________#
class SequenceNode(AbsCollectionNode):
    """A basic collection node. Executes every child sequentially"""

    def __init__(self):
        AbsCollectionNode.__init__(self)
        self.inbetween_action = None

    def draw(self):
        """draw every children sequentially"""
        first_action = True

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

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#
if __name__ == "__main__" :
    var = SequenceNode()
    var.extend([
        "test",
        "problem",
        "manuel"])

    var.print_node()

    var.execute()
