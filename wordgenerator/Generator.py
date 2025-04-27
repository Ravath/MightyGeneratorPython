# -*- coding: utf-8 -*-
from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsGeneratorNode
from macro.grammar import get_ValueIf
from macro.math import ListValue
import typing
import re


class Generator :
    """
    Generator nodes handler.
    Manages every step of the generation :
        - Text generation
        - Variable replacement in the text
        - Macro rolling and replacement in the text
    Then stores and provide access to the generated text.
    """

    replacement_pattern = re.compile(r'\{(.*?)\}')
    """The pattern to format the string and do replacements."""
    macro_pattern =re.compile(r'\[\[(.*?)\]\]')
    """The pattern to find the macros to execute."""

    def __init__(self, root : AbsGeneratorNode = None, variable_converter : typing.Callable[[str], str] = None) :
        self.root = root
        self.variable_converter = variable_converter


    def execute(self, input:dict=None) -> GenerationResult:
        assert self.root
        
        res = GenerationResult()
        
        # if any input, add them to the generation
        if input:
            for k in input:
                res.set_var(k, input[k])

        # Reset the things that needs to
        # Reset ListValues or they will be stuck or shifted across multiple generations.
        ListValue.reset_lists()

        # do generation
        self.root.node_action(res)

        # do Variable replacement
        for rtk in res.var_list:
            res._raw_text[rtk] = self.replace_variables(res._raw_text[rtk], res)
        # also do the checkpoints
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        # do macro rolls
        for rtk in res.var_list:
            res._raw_text[rtk] = self.roll_macros(res._raw_text[rtk])
        # also do the checkpoints
        # TODO With the current mechanism, the checkpoints rolls have different values than the original text. Idealy should not happen.
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        return res


    def replace_variables(self, text : str, res:GenerationResult) -> str :
        """
        Replaces the variables according to the defined pattern.
        ("{<Variable_Name>}" by default. See Generator.replacement_pattern).
        Uses the converter provided by user if any in self.variable_converter.

        Parameters
        ----------
        text : str The text to replace the variables from.

        Returns
        -------
        str Processed text.

        """
        # search for replacements in text
        for match in Generator.replacement_pattern.finditer(text) :
            key = match.group(1)
            # find replacement text in result variables
            if res.is_var_defined(key):
                new_text = res._raw_text[key]
            # or in the given var pool is any
            elif self.variable_converter:
                new_text = self.variable_converter(key)
            # replace any match
            text = re.sub(match.group(0), new_text, text)
        return text


    def roll_macros(self, text : str) -> str :
        """
        Replaces and rolls the internal macro according to the defined pattern.
        ("[[<Macro>]]" by default. See Generator.macro_pattern)

        Parameters
        ----------
        text : str The text to replace the macro from.

        Returns
        -------
        str Processed text.

        """
        res = Generator.macro_pattern.search(text)
        # for every found macro
        while(res) :
            # roll the macro
            newText = get_ValueIf(res.group(1)).value
            # replace it
            text = text.replace(res.group(0), str(newText), 1)
            # find next macro if any
            res = Generator.macro_pattern.search(text)
        return text