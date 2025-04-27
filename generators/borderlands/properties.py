# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import SetNode
from generators.borderlands.ponderation import type_flags, manufacturer_flags, element_flags, can_element
from generators.borderlands.ponderation import nbr_of_manufacturer_properties, special_flags
from generators.borderlands.ponderation import set_special_prop
from macro.math import SubOp, MulOp

"""Dictionnaries for item properties, including weapon element and bonus properties."""

#################################################
#                   ITEM ELEMENT                #
#################################################

def set_weapon_element(weapon_element) :
    """Allows to set and send back an element for firearm, shield or grenade generation.

    Named parameter:
    weapon_element is either FIRE, SHOCK, SLAG, COR, RAD or CRYO

    """
    # update the ponderations
    for v in element_flags.values() :
        v.value = 0
    element_flags[weapon_element].value = 1

# Picks an element for weapon generation, used by set_weapon_element
sel_element = Sequence() << [
    " - Effet élémentaire: ",
    Weight() << [
        Sequence() << ["incendiaire", SetNode(set_weapon_element, "FIRE")],
        Sequence() << ["électrique" , SetNode(set_weapon_element, "SHOCK")],
        Sequence() << ["slag"       , SetNode(set_weapon_element, "SLAG")],
        Sequence() << ["corrosif"   , SetNode(set_weapon_element, "COR")],
        Sequence() << ["radiation"  , SetNode(set_weapon_element, "RAD")],
        Sequence() << ["cryogénique", SetNode(set_weapon_element, "CRYO")],
    ],
    "\n"
]

#################################################
#                 ITEM PROPERTIES               #
#################################################

# Item_prop is a dictionnary with double key [ITEM_RARITY][ITEM_TYPE]
# The rarer the item, the more properties it gets
item_prop= {"" : {"" : Sequence() }}
item_prop.clear()

item_prop["COMMON"]={}
item_prop["COMMON"]["HANDGUN"]      =\
item_prop["COMMON"]["RIFLE"]        =\
item_prop["COMMON"]["MACHINEGUN"]   =\
item_prop["COMMON"]["SHOTGUN"]      =\
item_prop["COMMON"]["SNIPER"]       =\
Weight(SubOp(1 , nbr_of_manufacturer_properties)) << [
    [10, 1, " - Baillonette\n"],
    [10, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [3, 1, " - Viseur X6\n"],
    [11, " - 1 augmentation de dé\n"],
    [15, " - -1 Difficulté de visée\n"],
    [15, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [10, " - +1 Dégâts\n"],
    [MulOp(10, can_element), 1, sel_element],
]

item_prop["UNCOMMON"]={}
item_prop["UNCOMMON"]["HANDGUN"]    =\
item_prop["UNCOMMON"]["RIFLE"]      =\
item_prop["UNCOMMON"]["MACHINEGUN"] =\
item_prop["UNCOMMON"]["SHOTGUN"]    =\
item_prop["UNCOMMON"]["SNIPER"]     =\
Weight(SubOp(2 , nbr_of_manufacturer_properties)) << [
    [8, 1, " - Baillonette\n"],
    [9, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [4, 1, " - Viseur X6\n"],
    [11, " - 1 augmentation de dé\n"],
    [15, " - -1 Difficulté de visée\n"],
    [15, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [10, " - +1 Dégâts\n"],
    [MulOp(12, can_element), 1, sel_element],
]

item_prop["RARE"]={}
item_prop["RARE"]["HANDGUN"]    =\
item_prop["RARE"]["RIFLE"]      =\
item_prop["RARE"]["MACHINEGUN"] =\
item_prop["RARE"]["SHOTGUN"]    =\
item_prop["RARE"]["SNIPER"]     =\
Weight(SubOp(3 , nbr_of_manufacturer_properties)) << [
    [7, 1, " - Baillonette\n"],
    [8, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [4, 1, " - Viseur X6\n"],
    [11, " - 1 augmentation de dé\n"],
    [10, " - -1 Difficulté de visée\n"],
    [10, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [10, " - +1 Dégâts\n"],
    [MulOp(14, can_element), 1, sel_element],
    [10, 1, SetNode(set_special_prop, "FIREARM")],
]

item_prop["EPIC"]={}
item_prop["EPIC"]["HANDGUN"]    =\
item_prop["EPIC"]["RIFLE"]      =\
item_prop["EPIC"]["MACHINEGUN"] =\
item_prop["EPIC"]["SHOTGUN"]    =\
item_prop["EPIC"]["SNIPER"]     =\
Weight(SubOp(4 , nbr_of_manufacturer_properties)) << [
    [7, 1, " - Baillonette\n"],
    [7, 1, " - Viseur X2\n"],
    [7, 1, " - Viseur X4\n"],
    [5, 1, " - Viseur X6\n"],
    [12, " - 1 augmentation de dé\n"],
    [7, " - -1 Difficulté de visée\n"],
    [7, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [7, " - +1 Dégâts\n"],
    [MulOp(16, can_element), 1, sel_element],
    [15, 1, SetNode(set_special_prop, "FIREARM")],
]

item_prop["ETECH"]={}
item_prop["ETECH"]["HANDGUN"]   =\
item_prop["ETECH"]["RIFLE"]     =\
item_prop["ETECH"]["MACHINEGUN"]=\
item_prop["ETECH"]["SHOTGUN"]   =\
item_prop["ETECH"]["SNIPER"]    =\
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [5, 1, " - Baillonette\n"],
    [6, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [6, 1, " - Viseur X6\n"],
    [13, " - 1 augmentation de dé\n"],
    [5, " - -1 Difficulté de visée\n"],
    [5, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [6, " - +1 Dégâts\n"],
    [MulOp(18, can_element), 1, sel_element],
    [20, 1, SetNode(set_special_prop, "FIREARM")],
]

item_prop["LEGENDARY"]={}
item_prop["LEGENDARY"]["HANDGUN"]   =\
item_prop["LEGENDARY"]["RIFLE"]     =\
item_prop["LEGENDARY"]["MACHINEGUN"]=\
item_prop["LEGENDARY"]["SHOTGUN"]   =\
item_prop["LEGENDARY"]["SNIPER"]    =\
Sequence() << [
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [5, 1, " - Baillonette\n"],
    [6, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [6, 1, " - Viseur X6\n"],
    [14, " - 1 augmentation de dé\n"],
    [5, " - -1 Difficulté de visée\n"],
    [5, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [5, " - +1 Dégâts\n"],
    [MulOp(20, can_element), 1, sel_element],
],
SetNode(set_special_prop, "FIREARM")
]

# GRENADES
item_prop["COMMON"]["GRENADE"] = \
Weight(SubOp(1 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [MulOp(2, can_element), sel_element],
]

item_prop["UNCOMMON"]["GRENADE"] = \
Weight(SubOp(2 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [MulOp(3, can_element), 1, sel_element],
]

item_prop["RARE"]["GRENADE"] = \
Weight(SubOp(3 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [2, 1, SetNode(set_special_prop, "GRENADE")],
    [MulOp(3, can_element), 1, sel_element],
]

item_prop["EPIC"]["GRENADE"] = \
Weight(SubOp(4 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [3, 1, SetNode(set_special_prop, "GRENADE")],
    [MulOp(4, can_element), 1, sel_element],
]

item_prop["ETECH"]["GRENADE"] = \
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [3, 1, SetNode(set_special_prop, "GRENADE")],
    [MulOp(4, can_element), 1, sel_element],
]

item_prop["LEGENDARY"]["GRENADE"] = Sequence() << [
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [MulOp(4, can_element), 1, sel_element],
],
SetNode(set_special_prop, "GRENADE")
]

# SHIELDS
item_prop["COMMON"]["SHIELD"] = \
Weight(SubOp(1 , nbr_of_manufacturer_properties)) << [
    [2, " - + [[1d3+3]] Capacité\n"],
    [2, " - + [[1d3+1]] Cadence/tour\n"],
    [1, " - 1 Amélioration compétence spéciale\n"],
]

item_prop["UNCOMMON"]["SHIELD"] = \
Weight(SubOp(2 , nbr_of_manufacturer_properties)) << [
    [2, " - + [[1d3+3]] Capacité\n"],
    [2, " - + [[1d3+1]] Cadence/tour\n"],
    [1, " - 1 Amélioration compétence spéciale\n"],
]

item_prop["RARE"]["SHIELD"] = \
Weight(SubOp(3 , nbr_of_manufacturer_properties)) << [
    [4, " - + [[1d3+3]] Capacité\n"],
    [4, " - + [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [1, 1, SetNode(set_special_prop, "SHIELD")],
]

item_prop["EPIC"]["SHIELD"] = \
Weight(SubOp(4 , nbr_of_manufacturer_properties)) << [
    [4, " - + [[1d3+3]] Capacité\n"],
    [4, " - + [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [2, 1, SetNode(set_special_prop, "SHIELD")],
]

item_prop["ETECH"]["SHIELD"] = \
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [3, " - + [[1d3+3]] Capacité\n"],
    [3, " - + [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [2, 1, SetNode(set_special_prop, "SHIELD")],
]

item_prop["LEGENDARY"]["SHIELD"] = Sequence() << [
Weight(SubOp(5 , nbr_of_manufacturer_properties)) << [
    [3, " - + [[1d3+3]] Capacité\n"],
    [3, " - + [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
],
SetNode(set_special_prop, "SHIELD")
]

#################################################
#             ITEM BONUS PROPERTIES             #
#################################################

# special_prop is obtained with Rare, Epic, E-Tech and Legendary (mandatory) items
# It gives the item special abilities in combat and destiny
# For more informations on every bonus properties, see Borderlands Rulebook

# FIREARMS
special_prop_firearm =\
Weight() << [
    ["Balise gN0w© intégrée!\n"],
    ["Celle-là, c'est cadeau\n"],
    ["Crie au génie\n"],
    ["TORGUE TE DIT DE RIEN\n"],
    ["Attends, il fait quoi ce gros bouton ROUGE?\n"],
    ["Elles pleuvront, ils pleureront\n"],
    ["Gladiator\n"],
    ["Anussassineur\n"],
    ["Tyrannosaure sexuel\n"],
    ["BOOM!\n"],
    ["1 canon? HAHAHAHA!\n"],
    ["Plus de cacahuètes!\n"],
    ["Je pratique l'échangisme énergétique\n"],
    ["Le passé du futur est imparfait\n"],
    ["100% naturel, pas de bio du tout\n"],
    ["Don't stop the music\n"],
    ["On avait dit pas les mamans!\n"],
    ["Le Tout-Puissant est avec vous\n"],
    ["Ce qui est à toi est pour moi\n"],
    ["FIRST!\n"],
    [type_flags["HANDGUN"], "Sagesse dans le chargeur\n"],
    [type_flags["HANDGUN"], "Le petit partenaire du manifestant\n"],
    [type_flags["HANDGUN"], "Le meilleur ami de l'homme\n"],
    [type_flags["HANDGUN"], "Gerbotron\n"],
    [type_flags["MACHINEGUN"], "Soutien aérien\n"],
    [type_flags["RIFLE"], "Tout est dans le poignet\n"],
    [type_flags["SHOTGUN"], "De l'amour en cône\n"],
    [type_flags["SHOTGUN"], "Génie des temps modernes\n"],
    [type_flags["SNIPER"], "Voir et être vu\n"],
    [type_flags["SNIPER"], "MultiomegatumulteBl4st3r8000000\n"],
    [type_flags["SNIPER"], "IMACHARGINMALAZAH\n"],
    [type_flags["SNIPER"], "Duel au soleil\n"],
    [type_flags["SNIPER"], "Fil du rasoir. Balle écarlate. Danse létale.\n"],
    [type_flags["SNIPER"], "Pour le meilleur tonton/la meilleure tatie\n"],
    [type_flags["SNIPER"], "J'avais écrit Arc à POULIE!\n"],
    [manufacturer_flags["Bandit"], "Absolument non écologique\n"],
    [manufacturer_flags["Dahl"], "C-C-C-C-COMBO\n"],
    [manufacturer_flags["Dahl"], "Vous n'avez rien vu...\n"],
    [manufacturer_flags["Dahl"], "Je ne reculerai pas\n"],
    [manufacturer_flags["Maliwan"], "Les fléaux se partagent\n"],
    [manufacturer_flags["Maliwan"], "Donner, c'est recevoir\n"],
    [manufacturer_flags["Maliwan"], "J'ai rien compris mais c'est sympa\n"],
    [manufacturer_flags["Maliwan"], "Deux tu l'auras\n"],
    [SubOp(1, manufacturer_flags["Maliwan"]), "Elite de la nation\n"],
    [manufacturer_flags["Tediore"], "N'y. Touchez. Pas.\n"],
    [manufacturer_flags["Tediore"], "Kiki a un fusil\n"],
    [manufacturer_flags["Tediore"], "Le meilleur cadeau est celui qu'on offre à soi-même\n"],
    [manufacturer_flags["Tediore"], "Tout est dans le poignet\n"],
    [manufacturer_flags["Tediore"], "Tape dans le fond\n"],
    [manufacturer_flags["Tediore"], "La taille compte\n"],
    [manufacturer_flags["Torgue"], "CE SERA NOTRE PETIT SECRET\n"],
    [manufacturer_flags["Torgue"], "Énorme et sec!\n"],
    [element_flags["CRYO"], "Patate/Agave/Aubépine/Cactus/Betterave/Miel inclus\n"],
    [element_flags["CRYO"], "Patins non-inclus\n"],
    [element_flags["CRYO"], "Votre meilleur ami en soirée\n"],
    [element_flags["SHOCK"], "Toute la pluie tombe sur eux\n"],
    [element_flags["SHOCK"], "Si je te touche, t'es mort hihi!\n"],
    [element_flags["FIRE"], "Hot like lava\n"],
    [element_flags["RAD"], "1984 is the new Borderlands\n"],
]

# GRENADES
special_prop_grenade =\
Weight() << [
    ["Une grenade peut cacher un autre nabot\n"],
    ["C'est mon anniversaire mais c'est moi qui vous fais un cadeau!\n"],
    ["Mets-y la petite soeur!\n"],
    ["Boum? Boum.\n"],
    ["Message dans une bouteille\n"],
    ["Stronks\n"],
    ["Homerun! Euh...Strike!\n"],
    ["Quand il pleut des dollars, les malchanceux n'ont pas de sac\n"],
    ["Les mystères de l'orient...\n"],
    ["Votre ami téléguidé\n"],
    ["Un jour je serai le meilleur tueur!\n"],
    ["Nobel était suicidaire\n"],
    ["Mon père était ninja, mais ma mère avait un amant\n"],
    [manufacturer_flags["Contact"], "Mon premier kit de terroriste\n"],
    [manufacturer_flags["MIRV"], "On saupoudre de sucre glace\n"],
    [manufacturer_flags["Proximity"], "Svradabaldjan!\n"],
    [manufacturer_flags["Proximity"], "Jeu de jambes\n"],
    [manufacturer_flags["Proximity"], "Technologie filaire sans fil\n"],
    [manufacturer_flags["Singularity"], "Savoure l'instant\n"],
    [manufacturer_flags["Singularity"], "Elle a su trouver les maux pour me faire revenir\n"],
    [manufacturer_flags["Singularity"], "Ebouriffant\n"],
    [manufacturer_flags["Singularity"], "Eblouissant\n"],
    [manufacturer_flags["Singularity"], "Hors de mon chemin\n"],
    [manufacturer_flags["Tesla"], "Mort par mignonnerie\n"],
    [manufacturer_flags["Tesla"], "Jean-Michel Jarre: hommage\n"],
    [manufacturer_flags["Tesla"], "Jeu de piste\n"],
    [manufacturer_flags["Transfusion"], "Fabriqué par Sapudukku, le célèbre aide-soignant-ninja\n"],
    [manufacturer_flags["Transfusion"], "Oui, c'est un ananas\n"],
    [manufacturer_flags["Transfusion"], "C'est n'importe quoi\n"],
    [element_flags["CRYO"], "Attention, sol glissant\n"],
    [element_flags["SHOCK"], "Plaisir d'offrir, douleur de recevoir\n"],
    [element_flags["SHOCK"], "C'est comme le hula-hoop\n"],
    [element_flags["FIRE"], "Ne pas utiliser en intérieur\n"],
    [element_flags["RAD"], "Les bonnes choses se partagent\n"],
    [element_flags["SLAG"], "Ça ne partira pas au lavage\n"],
]

# SHIELDS
special_prop_shield =\
Weight() << [
    ["Il est vivant!\n"],
    ["Jamais vous ne ploierez le genou\n"],
    ["Bouclier jeter poubelle\n"],
    ["Te mentirais-je?\n"],
    ["Comme un chevalier C.R.S.\n"],
    ["La bise sur tes fesses\n"],
    ["L'infini, c'est combien de zéros?\n"],
    ["Bien préparé, mal barré\n"],
    ["La science ne s'explique pas, elle se vit\n"],
    ["Faire chier, c'est une vocation à plein temps\n"],
    ["C'est comme le foot, sauf que c'est vous la balle\n"],
    ["Qui veut gagner du bouclier?\n"],
    ["Electrisant\n"],
    ["Les ennemis de mes ennemis sont mes ennemis\n"],
    ["Polymorphose\n"],
    ["Master Kill Steal\n"],
    ["Ma bonté te perdra\n"],
    ["Me mentionne pas, je te bloque\n"],
    ["Technologie Gravitox\n"],
    ["Que jaillisse l'eau!\n"],
    [manufacturer_flags["Absorb"], "Transfusions pour tout le monde!\n"],
    [manufacturer_flags["Adaptive"], "Il est cassé mon bouclier!\n"],
    [manufacturer_flags["Adaptive"], "Votre assistant de nettoyage\n"],
    [manufacturer_flags["Adaptive"], "Continue ça m'amuse\n"],
    [manufacturer_flags["Adaptive"], "Vous n'aurez jamais autant d'amis\n"],
    [manufacturer_flags["Booster"], "Tendre la joue\n"],
    [manufacturer_flags["Booster"], "Se faire avoiner n'a jamais été aussi sympa\n"],
    [manufacturer_flags["Booster"], "Bouclier sexuellement transmissible\n"],
    [manufacturer_flags["Lifeline"], "Juste une mise au point\n"],
    [manufacturer_flags["Lifeline"], "SUCC\n"],
    [manufacturer_flags["Lifeline"], "Un petit dernier pour la route?\n"],
    [manufacturer_flags["Nova"], "Phénix jubilatoire\n"],
    [manufacturer_flags["Nova"], "Très distingué\n"],
    [manufacturer_flags["Nova"], "Un va-et-vient désagréable\n"],
    [manufacturer_flags["Raid"], "N'oubliez pas de headbanguer\n"],
    [manufacturer_flags["Raid"], "Rocket-man!!!\n"],
    [manufacturer_flags["Raid"], "J'aime vivre dangereusement\n"],
    [manufacturer_flags["Raid"], "Tellement pratique pour retrouver ses clés de bagnole\n"],
    [manufacturer_flags["Raid"], "Ta gueule et fonce\n"],
    [manufacturer_flags["Shield"], "Attention, bouclier opiniâtre\n"],
    [manufacturer_flags["Shield"], "Mais papa, tu triches?\n"],
    [manufacturer_flags["Shield"], "Tout ou rien, pendejo\n"],
    [manufacturer_flags["Spike"], "Toute rose a ses épines\n"],
    [manufacturer_flags["Turtle"], "J'ai vraiment pas mal\n"],
    [manufacturer_flags["Turtle"], "Pr0p hunt l0lz\n"],
]

# If special has been row with item generation
# Will pick an associated special property
item_special = Interval (1) << [
    [0, special_flags["FIREARM"], special_prop_firearm],
    [0, special_flags["GRENADE"], special_prop_grenade],
    [0, special_flags["SHIELD"], special_prop_shield],
]