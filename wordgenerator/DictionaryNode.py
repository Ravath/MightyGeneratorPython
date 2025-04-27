# -*- coding: utf-8 -*-
"""
@authors: Ehlion
"""

from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsLeafNode


class DictionaryNode(AbsLeafNode) :
    """Node managing a dictionary of nodes.
        In order to find which child to execute, looks forthe key in the generation result buffer.
        If don't find any, looks into the global variables."""

    def __init__(self, node_dictionary, *variables : str):
        AbsLeafNode.__init__(self)
        self.dict = node_dictionary
        """The children nodes, as a dictionary. Can be multi-dictionnaries deep."""
        self.variables = variables
        """Names of the variables to look for in orderto get the keys of the children to execute."""

    def node_action(self, generation_result:GenerationResult):
        """Execute the designated node."""
        to_execute = self.dict

        # progress through each dictionary
        for si in range(0, len(self.variables)) :
            # get name of the variable containing the key
            var_name = self.variables[si]
            # get the node associated with this key in the dictionary
            if generation_result.is_var_defined(var_name):
                # In the generation buffers if any
                to_execute = to_execute[generation_result.get_var(var_name)]
            else:
                # try the global variables if not
                to_execute = to_execute[globals()[var_name]]

        # Execute the found dictionary
        to_execute.node_action(generation_result)

    def print_node(self, tabs:int = 0) :
        """Print the node name and its dictionary keys and values."""
        # Node Name
        tab_sign="\t"
        print(f"{tab_sign*tabs}[{type(self).__name__} : {self.variables}]")
        # dictionary
        DictionaryNode.display_dico_node(self.dict, tabs + 1)

    def display_dico_node(dico_node, tabs : int) :
        tab_sign="\t"
        if isinstance(dico_node, dict) :
            for k in dico_node :
                print(f"{tab_sign*tabs}{k}")
                DictionaryNode.display_dico_node(dico_node[k], tabs + 1)
        else :
            dico_node.print_node(tabs)