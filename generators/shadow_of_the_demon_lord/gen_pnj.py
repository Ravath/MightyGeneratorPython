# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:03:13 2020

@author: Ehlion
"""

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import S
from wordgenerator.Print import Title
from wordgenerator.Generator import Generator

physique = Weight() << [
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
]

motivation = Weight() << [
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
]

charactere = Weight() << [
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
]


################ ROOT

root = S(
    Title("Trait Physique") << physique,
    Title("Motivation") << motivation,
    Title("Trait de Charactère") << charactere,
)

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute().print_to_console()
