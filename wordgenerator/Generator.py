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
    macro_pattern =re.compile(r'\[\[(.*?)\]\]')

    def __init__(self, root : AbsGeneratorNode = None, variable_converter : typing.Callable[[str], str] = None) :
        self.root = root
        self.variable_converter = variable_converter


    def execute(self) -> GenerationResult:
        assert self.root
        
        res = GenerationResult()

        # Reset the things that needs to
        # Reset ListValues or they will be stuck or shifted across multiple generations.
        ListValue.reset_lists()

        # do generation
        self.root.node_action(res)

        # do Variable replacement
        res.text = self.replace_variables(res.raw_text)
        # also do the checkpoints
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        # do macro rolls
        res.text = self.roll_macros(res.text)
        # also do the checkpoints
        # TODO With the current mechanism, the checkpoints rolls have different values than the original text. Idealy should not happen.
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        return res


    def replace_variables(self, text : str) -> str :
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
        # only if a converter is provided by user
        if self.variable_converter :
            for match in Generator.replacement_pattern.finditer(text) :
                # find replacement text
                new_text = self.variable_converter(match.group(1))
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