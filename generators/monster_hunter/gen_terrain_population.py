# -*- coding: utf-8 -*-

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import S
from wordgenerator.Print import Title, Label
from wordgenerator.Generator import Generator


################ FLORE

flore = Weight() << [
    ["Stérile/Désolé"],
    ["Sable"],
    ["Boue"],
    ["Rocailleux"],
    ["Foret"],
    ["Jungle"],
    ["Toundra"],
    ["Savane"],
    ["Buissons"],
    ["Champs/prairies"],
    ["Brousailles"],
]

flore_type = Weight() << [
    ["Herbe"],
    ["Buisson"],
    ["Liane"],
    ["Arbre Moyen"],
    ["Arbre Grand"],
    ["Fougères"],
    ["Mousse"],
    ["Algues"],
    ["Champignons"],
]

feuillage = Weight() << [
    ["Inexistant"],
    ["Epars"],
    ["Dru"],
    ["Sec et Mort"],
]

feuille = Weight() << [
    ["Simples"],
    ["Composées"],
    ["Aiguille"],
    ["Ecaille"],
]

fruit = Weight() << [
    ["Pollen"],
    ["Fruits"],
    ["Grappes"],
    ["Graines"],
]

flore_autre = Weight() << [
    ["Epineux"],
    ["Carnivore"],
    ["Mobile"],
    ["Organes inhabituels"],
    ["Sentient"],
    ["Lumineux"],
    ["Odeur forte (Agréable ou pas)"],
    ["Sêve étrange (sang, lumière, ...)"],
    ["Parasite/Symbiote Animal/Végétal/Minéral"],
    ["Sort"],
    ["Gaz"],
]

################ Faune

faune = Weight() << [
    ["Déserte/Rare"],
    ["Normale"],
    ["Abondante"],
]

faune_taille = Weight() << [
    ["Petit"],
    ["Moyen"],
    ["Grand"],
]

faune_type = Weight() << [
    ["Animal"],
    ["Insecte"],
    ["Créature Magique"],
    ["Monstre/Aberration"],
    ["Saurien/Dragon"],
]

faune_regime = Weight() << [
    ["Herbivore"],
    ["Prédateur"],
    ["Charognard"],
    ["Granivore"],
    ["Mange-Magie"],
    ["Fouille-Terre"],
    ["Insectivore"],
]

faune_reproduction = Weight() << [
    ["Mammifère"],
    ["Ovipare"],
    ["Clonage"],
    ["Parasitisme"],
]

faune_locomotion = Weight() << [
    ["Bipère"],
    ["Quadripède"],
    ["Beaucoup de pattes"],
    ["Reptation"],
    ["Ailes"],
]

faune_autre = Weight() << [
    ["C'est tout"],
    ["Ailes"],
    ["Amphibien"],
    ["Creusement"],
]

################ Faune - Suite

faune_milieu_naturel = Weight() << [
    ["Surface"],
    ["Aquatique"],
    ["Amphibie"],
    ["Arboricole"],
    ["Souterrain"],
]

faune_organisation_sociale = Weight() << [
    ["Solitaire"],
    ["Couple"],
    ["Groupe (4-6)"],
    ["Meute (10-20)"],
    ["Troupeau (10-100)"],
    ["Horde (100-500+)"],
]

faune_comportement = Weight() << [
    ["Territorial"],
    ["Nomade"],
    ["Colonie"],
    ["Parasite"],
]

faune_attitude = Weight() << [
    ["Peureux"],
    ["Curieux"],
    ["Aggressif"],
    ["Placide"],
]

faune_aspect = Weight() << [
    ["Carapace"],
    ["Venin"],
    ["Souffle"],
    ["Magie"],
    ["Tentacules"],
    ["Cornes"],
    ["Pince/Dard"],
]

################ ROOT

root = S(
    # Flore
    Title("Flore") << S(
        flore,
        Title("Specimen") << S(
            Label("Type      ", flore_type),
            Label("Feuillage ", feuillage),
            Label("Feuilles  ", feuille),
            Label("Fruit     ", fruit),
            Label("Autre     ", flore_autre),
        ),
    ),
    # Faune
    Title("Faune") << S(
        faune,
        Title("Specimen") << S(
            Label("Taille    ", faune_taille),
            Label("Type      ", faune_type),
            Label("Regime    ", faune_regime),
            Label("Reproduction", faune_reproduction),
            Label("Locomotion", faune_locomotion),
            Label("Autre     ", faune_autre),
            Label("Milieu naturel", faune_milieu_naturel),
            Label("Organisation Sociale", faune_organisation_sociale),
            Label("Comportement", faune_comportement),
            Label("Attitude    ", faune_attitude),
            Label("Aspect     ", faune_aspect),
        ),
    )
)

################ Generation

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute().print_to_console()