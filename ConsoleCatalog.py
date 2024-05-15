# -*- coding: utf-8 -*-
"""
Created on Sat May 05 14:30:13 2024

@author: Ehlion

Scan the generators and ask the user for the one to execute.
"""

import os
import pathlib
from importlib import import_module

# Parametrisation
WDIR="generators/"
extension=".py"
genprefix="gen_"

os.chdir(WDIR)

# Scan generator files
desktop = pathlib.Path(".")
files = list(p for p in desktop.rglob("*.py")
             if p.name.startswith("gen_"))
names = list(str(f)
            .replace("\\", " : ")
            .replace(genprefix, "")
            .replace(extension, "")
            .replace("_", " ")
            .capitalize() for f in files)

# Interface loop on the terminal
flag_continue = True
while flag_continue:
    # Display generator list
    index=0
    print("===========================")
    for fn in  names :
        index+=1
        print(index, ") ", fn)
    print("q) Quit")

    # Ask user
    index = input("\nSelect generator: ")
    if index.isnumeric() :
        # execute selected script
        index=int(index)
        genfile = files[index-1]

        print("\n === ", names[index-1], " ===\n")
        # convert path to module name
        clean = str(genfile).replace("\\", ".").replace("/", ".").replace(".py", "")
        # exec(open(genfile, encoding="utf-8").read(), globals())
        new_mod = import_module("generators."+clean)
        generation = new_mod.__dict__["generation"]
        generation.execute()
        generation.print_to_console()
        index = input(">")
    elif index == "q":
        # Quit the application
        flag_continue=False
    else:
        # Wrong input
        print("Wrong imput. Please try again.")