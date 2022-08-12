# -*- coding: utf-8 -*-
from wordgenerator.NodeIf import AbsGeneratorNode
from wordgenerator.Print import PrintNode
from macro.dice_macro import get_ValueIf
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
        self.text = self.raw_text = ""
        self.variable_converter = variable_converter

    def execute(self) :
        assert self.root

        # do generation
        self.generate_text()

        # do Variable replacement
        self.text = self.replace_variables(self.text)

        # do macro rolls
        self.text = self.roll_macros(self.text)

    def generate_text(self) :
        """
        Execute the root to get raw text.
        """
        # We have to use the buffer print mechanism in order to retreive the text.
        # (instead of directly printing to console)
        PrintNode.print_to_buffer()

        self.root.execute()
        self.text = self.raw_text= PrintNode._printer.get_text()

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


    def print_to_console(self) :
        print(self.text)

