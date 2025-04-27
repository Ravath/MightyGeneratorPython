# -*- coding: utf-8 -*-

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Variable import DefineNode as Define
from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import S
from wordgenerator.Print import Title, Label
from wordgenerator.Generator import Generator

################ Population

population_type = Weight() << [
    ["Aucune"],
    ["Campement"],
    ["Tribale"],
    ["Clanique"],
    ["Village"],
    ["Cité"],
    ["Bastide"],
    ["Forteresse"],
    ["Urbaine"],
]

population_race = Weight() << [
    ["Humanoide"],
    ["Humanoide Monstrueuse"],
    ["Monstrueuse"],
    ["Magique"],
]

population_organisation_sociale = Weight() << [
    ["Libérale"],
    ["Méritocratie/Aristocratie"],
    ["Monarchie"],
    ["Théocratie"],
    ["Magocratie"],
    ["Oligarchie"],
    ["Gérontocratie"],
    ["Démocratie"],
    ["Caste"],
    ["Dictature"],
]

################ Minéraux

minéraux = Weight() << [
    ["Sable"],
    ["Terre"],
    ["Boue"],
    ["Pierre"],
    ["Métaux"],
    ["Gemmes"],
]

################ Magie

magie = Weight() << [
    ["Morte"],
    ["Faible"],
    ["Normale"],
    ["Intense"],
    ["Erratique"],
    ["Chaotique"],
    ["Tempête"],
    ["Altérée (Element, ...)"],
]

################ Point d'interet

point_interet = Weight() << [
    ["Volcan"],
    ["Geysers"],
    ["Volcan"],
    ["Crépuscule éternel"],
    ["Cimetière"],
    ["Champ de Bataille"],
    ["Ruines"],
    ["Zone de Reproduction"],
    ["Zone de Chasse"],
    ["Zone de Migration"],
    ["Zone de Cimetière"],
    ["Zone"],
]

################ ROOT

root = S(
    # Population
    Define("POPULATION_TYPE")       << population_type,
    Define("POPULATION_RACE")       << population_race,
    Define("POPULATION_SOCIETY")    << population_organisation_sociale,
    # Environment
    Define("MINERALS")  << minéraux,
    Define("MAGIC")     << magie,
    Define("INTEREST")  << point_interet,
)

################ Generation

generation = Generator(root)
if __name__ == "__main__" :
    
    input = {"" : ""}
    #input = {"MAGIC" : "Tournade"}

    result = generation.execute(**input)
    
    #result.display_vars()

    result.print_to_console(
"""Une colonie!
Population :
\t{POPULATION_TYPE}
\t{POPULATION_RACE}
\t{POPULATION_SOCIETY}
Ressources : {MINERALS}
Magie : {MAGIC}
Point d'interet : {INTEREST}
"""
)