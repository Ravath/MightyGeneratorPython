# -*- coding: utf-8 -*-

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

population_organisatoin_sociale = Weight() << [
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
    Title("Population") << S(
        Label("Type      ", population_type),
        Label("Race      ", population_race),
        Label("Organisation Sociale", population_organisatoin_sociale),
    ),
    # Minéraux
    Title("Minéraux") << S(
        Label("Minéraux      ", minéraux),
    ),
    # Magie
    Title("Magie") << S(
        Label("Magie ", magie),
    ),
    # Point d'interet
    Title("Point d'interet") << S(
        point_interet,
    ),
)

################ Generation

generation = Generator(root)
generation.execute()
generation.print_to_console()