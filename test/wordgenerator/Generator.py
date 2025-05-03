# -*- coding: utf-8 -*-
from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.Dictionary import DictionaryNode
from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import S
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import PrintNode as Print
from wordgenerator.Print import CheckpointNode as Checkpoint
from wordgenerator.Print import SetNode, Title, Label
from wordgenerator.Variable import SwitchVarNode as SwitchVar
from wordgenerator.Variable import SetVarNode as SetVar
from wordgenerator.Variable import ContextNode as Context
from wordgenerator.Variable import DefineNode as Define
from wordgenerator.Output import FormatNode as Format
from wordgenerator.Output import MacroNode as Macro
from wordgenerator.Generator import Generator

random_result = Weight() << [
    "A",
    "B",
    "C",
]

# When structuring a complex generation, it is recommended to use "contexts"
generation = Generator(S(
    # 'Define' will use a context only if the target context has not been already defined
    Define("TASK1") << random_result,
    Define("TASK2") << random_result,
    # 'Context', on the contrary, will always redefine the target.
    Context("MEAN1", append = False) << random_result,
    Context("MEAN2", append = True) << random_result,
    # When not specified, "DEFAULT" is the default context
    "THIS WILL BE PRINTED IN DEFAULT",
    # It is possible to switch. Every generation further on will be applyed on the switched buffer.
    SwitchVar("SIDE_STORY1"),
    random_result,
    random_result,
    random_result,
    # Usefull for adding multiple actions, or coming back and forth.
    SwitchVar("SIDE_STORY2"),
    random_result,
    random_result,
    # But don't forget to switch back to "DEFAULT"
    SwitchVar("VAR_NAME"),
    random_result,
    # SetVar is for setting a ponctual value to a context. Previous values will be replaced.
    SetVar("VAR_NAME", "RESET VALUE"),
))


# Do generation
# You can initialise contexts as input of the generation
result = generation.execute(TASK1="Fetch the buk",
                            MEAN1="This will be replaced",
                            MEAN2="This will not:")

# Print only de current context (The last active one) by default.
result.print_to_console()
# print generation result with a formating
result.print_to_console(
"""
________________________
Taches  : {TASK1} / {TASK2}
Moyens  : {MEAN1} / {MEAN2}
Alters  : {SIDE_STORY1} / {SIDE_STORY2}
Objectif: {Objective}
________________________
{DEFAULT}
________________________
""")
print("_EVERY BUFFER GENERATED_")
# For analyse, display every generated context.
result.display_vars()