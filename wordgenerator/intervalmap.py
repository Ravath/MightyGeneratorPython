# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:35:42 2020

@author: Ehlion
"""

class intervalmap():
    
    def __init__(self):
        self.map = list()
        
    def extend(self, table):
        self.map.extend(table)
        
    def put(self, min, max, text):
        self.map.append(((min,max),text))
        
    def draw(self, roll):
        for x in self.map:
            if roll >= x[0][0] and roll <= x[0][1]:
                return x[1]