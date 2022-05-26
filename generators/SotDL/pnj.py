# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:03:13 2020

@author: Ehlion
"""

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import Title, Label
from macro.dice import Pool, PoolSum

d100 = PoolSum(Pool(1,100))
_3d6 = PoolSum(Pool(3,6))

physique = Weight().extend([
    ["Curieuse odeur"],
    ["Air crasseux"],
    ["Bouche en forme étrange"],
    ["Etrange pigmentation"],
    ["Très chevelu"],
    ["Cheveux clairsemés"],
    ["Vilaine cicatrice"],
    ["Séduisant"],
    ["Laid"],
    ["Beaux Habits"],
    ["Pieds nus"],
    ["Parfumé"],
    ["Malade"],
    ["Mauvaise haleine"],
    ["Kyste disgracieux"],
    ["Taches de rousseur"],
    ["Tatouage"],
    ["Estropié"],
])

motivation = Weight().extend([
    ["Aventure"],
    ["Expiation"],
    ["Chaos"],
    ["Gloire"],
    ["Bien"],
    ["Immortalité"],
    ["Amélioration"],
    ["Justice"],
    ["Liberté"],
    ["Amour"],
    ["Magie"],
    ["Ordre"],
    ["Paix"],
    ["Puissance"],
    ["Salut"],
    ["Sécurité"],
    ["Reconnaissance"],
    ["Vengeance"],
    ["Richesse"],
])

charactere = Weight().extend([
    ["Fou"],
    ["Méchant"],
    ["Cruel"],
    ["Bruyant"],
    ["Vulgaire"],
    ["Ignoble"],
    ["Comploteur"],
    ["Cupide"],
    ["Imprévisible"],
    ["Nerveux"],
    ["Calme"],
    ["Raisonnable"],
    ["Généreux"],
    ["Sincère"],
    ["Noble"],
    ["Distingué"],
    ["Discret"],
    ["Bienveillant"],
    ["Vertueux"],
    ["Concentré"],
])


################ ROOT

def S(*args) :
    return Sequence().extend([*args])

sel_main = S(
    Title("Trait Physique", S(physique)),
    Title("Motivation", S(motivation)),
    Title("Trait de Charactère", S(charactere)),
)

sel_main.execute()
