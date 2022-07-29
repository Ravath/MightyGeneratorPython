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

nbr_success = 0
nbr_error = 0

def test(expected, received, message = "") -> bool :
    """
    Test the result by comparing exoected and received values.
    Good for unitary testing.

    Parameters
    ----------
    expected :
        The expected result.
    received :
        The value actually received.
    message :
        The message describing the check.
    """
    global nbr_success, nbr_error
    if expected == received :
        print_log("SUCCESS", f"{message:30} (Expected : {expected} = Received : {received})")
        nbr_success+=1
        return True
    else :
        print_log("ERROR", f"{message:30} (Expected : {expected}, Received : {received})")
        nbr_error+=1
        return False

def test_result() :
    if nbr_error > 0 :
        print_log("ERROR", f"TEST FINISHED WITH {nbr_success} OK AND {nbr_error} KO")
    else :
        print_log("SUCCESS", f"TEST FINISHED WITH {nbr_success} OK")
