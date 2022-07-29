# -*- coding: utf-8 -*-

from tkinter import *
from random import *


root = Tk()

# entrée
value = StringVar() 
value.set("texte par défaut")
entree = Entry(root, textvariable=value, width=30)
entree.pack()

root.mainloop()
