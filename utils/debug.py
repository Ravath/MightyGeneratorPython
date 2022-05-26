# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:28:43 2022

@author: Ehlion

| Module with debug and testing tools.
"""

def print_log(log_name:str, message:str) :
    """Format and print a log message"""
    print(f"{log_name.upper():<8}| {message}")

def trace(print_arg = True, print_ret = True) :
    """
    Decorator the print the trace in and out of a function

    Parameters
    ----------
    print_arg : Bool, optional
        For printing the entry and arguments to the function.
        The default is True.
    print_ret : Bool, optional
        For printing the return value from the function.
        The default is True.
    """

    # case with given arguments
    def trace_decoration(func):
        def wrapper(*arg, **karg):
            if print_arg:
                print(f"{func.__name__}({arg} | {karg}) ...")
            res = func(*arg, *karg)
            if print_ret:
                print(f"{func.__name__}({arg} | {karg}) = {res}")
            return res
        return wrapper

    # case without given arguments
    if callable(print_arg) :
        func = print_arg
        def wrapper(*arg, **karg):
            print(f"{func.__name__}({arg} | {karg}) ...")
            res = func(*arg, *karg)
            print(f"{func.__name__}({arg} | {karg}) = {res}")
            return res
        return wrapper
    return trace_decoration

def test(expected, received) :
    """
    Test the result by comparing exoected and received values.
    Good for unitary testing.

    Parameters
    ----------
    expected :
        The expected result.
    received :
        The value actually received.
    """
    if expected == received :
        print_log("SUCCESS", f"Expected : {expected} = Received : {received}")
    else :
        print_log("ERROR", f"Expected : {expected}, Received : {received}")
