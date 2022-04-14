# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:53:57 2020

@author: Ehlion
"""

import random

class weightmap:
    
    
    def __init__(self):
       self.map = []
       self.knowntotal = False
       
    def extend(self, table):
        self.map.extend(table)
        self.knowntotal = False
       
    """ ceci est , ah ben non!"""
    def put(self, weight:int, text:str):
        """ ceci est de la doc bien pensée"""
        assert weight >= 0, "weight must be positive"
        self.map.append((weight, text))
        self.knowntotal = False
        
    def computeTotal(self):
        if not self.knowntotal:
            self.knowntotal = True
            self.totalWeight = 0
            for x in self.map:
                self.totalWeight += x[0]
        
    def draw(self):
        
        # Sum the total weight
        self.computeTotal()
            
        if self.totalWeight == 0 : return ""
    
        # Roll
        roll = random.randint(1,self.totalWeight)
        index = 0
        
        # Find associated entry
        roll -= self.map[index][0]
        while roll > 0:
            index += 1
            roll -= self.map[index][0]
            
        return self.map[index][1]

    