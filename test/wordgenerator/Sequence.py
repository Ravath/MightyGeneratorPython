# -*- coding: utf-8 -*-
"""
Created on 12/08/2022

@author: Trense
"""
from wordgenerator.Sequence import SequenceNode
from utils.debug import test, print_log, test_result, test_action, trace

var = SequenceNode()
var.extend([
    "test",
    "problem",
    "manuel"])

var.print_node()

var.execute()