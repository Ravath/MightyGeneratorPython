# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:28:43 2022

@author: Ehlion

| Module with debug and testing tools.
"""
from datetime import datetime

nbr_success = 0
nbr_error = 0
log = open("debug.txt", "w")
log.write("DEBUG LOG ("+datetime.now().strftime("%Y/%m/%d %H:%M:%S")+")\n")

def print_log(log_name:str, message:str) :
    """Format and print a log message in console and debug log."""
    global log
    print(f"{log_name.upper():<8}| {message}")
    log.write(f"{log_name.upper():<8}| {message}\n")

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
                print_log("TRACE", f"{func.__name__}({arg} | {karg}) ...")
            res = func(*arg, *karg)
            if print_ret:
                print_log("TRACE", f"{func.__name__}({arg} | {karg}) = {res}")
            return res
        return wrapper

    # case without given arguments
    if callable(print_arg) :
        func = print_arg
        def wrapper(*arg, **karg):
            print_log("TRACE", f"{func.__name__}({arg} | {karg}) ...")
            res = func(*arg, *karg)
            print_log("TRACE", f"{func.__name__}({arg} | {karg}) = {res}")
            return res
        return wrapper
    return trace_decoration

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

def test_action(message) :
    print_log("ACTION", f"=============>>> {message}")

def test_result() :
    global log

    if nbr_error > 0 :
        print_log("ERROR", f"TEST FINISHED WITH {nbr_success} OK AND {nbr_error} KO")
    else :
        print_log("SUCCESS", f"TEST FINISHED WITH {nbr_success} OK")

    log.close()
