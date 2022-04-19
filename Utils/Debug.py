# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:28:43 2022

@author: Ehlion
"""

def getReturn(func) :
    """Decorator which prints the return values of a function."""
    def wrapper(*arg, **karg):
        res = func(*arg, *karg)
        print("Result({}) = {}".format(func.__name__, str(res)))
        return res
    return wrapper

def getArgs(func) :
    """Decorator which prints the arguments values of a function."""
    def wrapper(*arg, **karg):
        print("{}({} | {})".format(func.__name__, arg, karg))
        res = func(*arg, *karg)
        return res
    return wrapper

def trace(printArg = True, printRet = True) :
    """
    Decorator the print the trace in and out of a function

    Parameters
    ----------
    printArg : Bool, optional
        For printing the entry and arguments to the function.
        The default is True.
    printRet : Bool, optional
        For printing the return value from the function.
        The default is True.
    """
    
    def traceDecoration(func):
        def wrapper(*arg, **karg):
            if printArg:
                print("{}({} | {}) ...".format(func.__name__, arg, karg))
            res = func(*arg, *karg)
            if printRet:
                print("{}({} | {}) = {}".format(func.__name__, arg, karg, res))
            return res
        return wrapper
        
    if type(printArg) == type((trace)) :
        func = printArg
        def wrapper(*arg, **karg):
            print("{}({} | {}) ...".format(func.__name__, arg, karg))
            res = func(*arg, *karg)
            print("{}({} | {}) = {}".format(func.__name__, arg, karg, res))
            return res
        return wrapper
    return traceDecoration
