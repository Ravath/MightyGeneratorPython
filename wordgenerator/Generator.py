# -*- coding: utf-8 -*-
from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.NodeIf import AbsGeneratorNode
from macro.math import ListValue
import typing


class Generator :
    """
    Generator nodes handler.
    Manages every step of the generation :
        - Text generation
        - Variable replacement in the text
        - Macro rolling and replacement in the text
    Then stores and provide access to the generated text.
    """

    def __init__(self, root : AbsGeneratorNode = None, variable_converter : typing.Callable[[str], str] = None) :
        self.root = root
        self.variable_converter = variable_converter


    def execute(self, **input:dict) -> GenerationResult:
        assert self.root
        
        res = GenerationResult(variable_converter = self.variable_converter)
        
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
            res._raw_text[rtk] = res.format(res._raw_text[rtk])
        # also do the checkpoints
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        # do macro rolls
        for rtk in res.var_list:
            res._raw_text[rtk] = GenerationResult.roll_macros(res._raw_text[rtk])
        # also do the checkpoints
        # TODO With the current mechanism, the checkpoints rolls have different values than the original text. Idealy should not happen.
        # for ckpt in CheckpointNode.checkpoints.values():
        #     ckpt.text = self.replace_variables(ckpt.text)

        return res