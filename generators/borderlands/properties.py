# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import SetNode
from ponderation import pond_type, pond_manufacturer, pond_element, can_element
from ponderation import nbr_of_manufacturer_properties, pond_special
from ponderation import set_special_prop
from macro.calc import SubOp, MulOp

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
    for v in pond_element.values() :
        v.value = 0
    pond_element[weapon_element].value = 1

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
    [pond_type["HANDGUN"], "Sagesse dans le chargeur\n"],
    [pond_type["HANDGUN"], "Le petit partenaire du manifestant\n"],
    [pond_type["HANDGUN"], "Le meilleur ami de l'homme\n"],
    [pond_type["HANDGUN"], "Gerbotron\n"],
    [pond_type["MACHINEGUN"], "Soutien aérien\n"],
    [pond_type["RIFLE"], "Tout est dans le poignet\n"],
    [pond_type["SHOTGUN"], "De l'amour en cône\n"],
    [pond_type["SHOTGUN"], "Génie des temps modernes\n"],
    [pond_type["SNIPER"], "Voir et être vu\n"],
    [pond_type["SNIPER"], "MultiomegatumulteBl4st3r8000000\n"],
    [pond_type["SNIPER"], "IMACHARGINMALAZAH\n"],
    [pond_type["SNIPER"], "Duel au soleil\n"],
    [pond_type["SNIPER"], "Fil du rasoir. Balle écarlate. Danse létale.\n"],
    [pond_type["SNIPER"], "Pour le meilleur tonton/la meilleure tatie\n"],
    [pond_type["SNIPER"], "J'avais écrit Arc à POULIE!\n"],
    [pond_manufacturer["Bandit"], "Absolument non écologique\n"],
    [pond_manufacturer["Dahl"], "C-C-C-C-COMBO\n"],
    [pond_manufacturer["Dahl"], "Vous n'avez rien vu...\n"],
    [pond_manufacturer["Dahl"], "Je ne reculerai pas\n"],
    [pond_manufacturer["Maliwan"], "Les fléaux se partagent\n"],
    [pond_manufacturer["Maliwan"], "Donner, c'est recevoir\n"],
    [pond_manufacturer["Maliwan"], "J'ai rien compris mais c'est sympa\n"],
    [pond_manufacturer["Maliwan"], "Deux tu l'auras\n"],
    [SubOp(1, pond_manufacturer["Maliwan"]), "Elite de la nation\n"],
    [pond_manufacturer["Tediore"], "N'y. Touchez. Pas.\n"],
    [pond_manufacturer["Tediore"], "Kiki a un fusil\n"],
    [pond_manufacturer["Tediore"], "Le meilleur cadeau est celui qu'on offre à soi-même\n"],
    [pond_manufacturer["Tediore"], "Tout est dans le poignet\n"],
    [pond_manufacturer["Tediore"], "Tape dans le fond\n"],
    [pond_manufacturer["Tediore"], "La taille compte\n"],
    [pond_manufacturer["Torgue"], "CE SERA NOTRE PETIT SECRET\n"],
    [pond_manufacturer["Torgue"], "Énorme et sec!\n"],
    [pond_element["CRYO"], "Patate/Agave/Aubépine/Cactus/Betterave/Miel inclus\n"],
    [pond_element["CRYO"], "Patins non-inclus\n"],
    [pond_element["CRYO"], "Votre meilleur ami en soirée\n"],
    [pond_element["SHOCK"], "Toute la pluie tombe sur eux\n"],
    [pond_element["SHOCK"], "Si je te touche, t'es mort hihi!\n"],
    [pond_element["FIRE"], "Hot like lava\n"],
    [pond_element["RAD"], "1984 is the new Borderlands\n"],
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
    [pond_manufacturer["Contact"], "Mon premier kit de terroriste\n"],
    [pond_manufacturer["MIRV"], "On saupoudre de sucre glace\n"],
    [pond_manufacturer["Proximity"], "Svradabaldjan!\n"],
    [pond_manufacturer["Proximity"], "Jeu de jambes\n"],
    [pond_manufacturer["Proximity"], "Technologie filaire sans fil\n"],
    [pond_manufacturer["Singularity"], "Savoure l'instant\n"],
    [pond_manufacturer["Singularity"], "Elle a su trouver les maux pour me faire revenir\n"],
    [pond_manufacturer["Singularity"], "Ebouriffant\n"],
    [pond_manufacturer["Singularity"], "Eblouissant\n"],
    [pond_manufacturer["Singularity"], "Hors de mon chemin\n"],
    [pond_manufacturer["Tesla"], "Mort par mignonnerie\n"],
    [pond_manufacturer["Tesla"], "Jean-Michel Jarre: hommage\n"],
    [pond_manufacturer["Tesla"], "Jeu de piste\n"],
    [pond_manufacturer["Transfusion"], "Fabriqué par Sapudukku, le célèbre aide-soignant-ninja\n"],
    [pond_manufacturer["Transfusion"], "Oui, c'est un ananas\n"],
    [pond_manufacturer["Transfusion"], "C'est n'importe quoi\n"],
    [pond_element["CRYO"], "Attention, sol glissant\n"],
    [pond_element["SHOCK"], "Plaisir d'offrir, douleur de recevoir\n"],
    [pond_element["SHOCK"], "C'est comme le hula-hoop\n"],
    [pond_element["FIRE"], "Ne pas utiliser en intérieur\n"],
    [pond_element["RAD"], "Les bonnes choses se partagent\n"],
    [pond_element["SLAG"], "Ça ne partira pas au lavage\n"],
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
    [pond_manufacturer["Absorb"], "Transfusions pour tout le monde!\n"],
    [pond_manufacturer["Adaptive"], "Il est cassé mon bouclier!\n"],
    [pond_manufacturer["Adaptive"], "Votre assistant de nettoyage\n"],
    [pond_manufacturer["Adaptive"], "Continue ça m'amuse\n"],
    [pond_manufacturer["Adaptive"], "Vous n'aurez jamais autant d'amis\n"],
    [pond_manufacturer["Booster"], "Tendre la joue\n"],
    [pond_manufacturer["Booster"], "Se faire avoiner n'a jamais été aussi sympa\n"],
    [pond_manufacturer["Booster"], "Bouclier sexuellement transmissible\n"],
    [pond_manufacturer["Lifeline"], "Juste une mise au point\n"],
    [pond_manufacturer["Lifeline"], "SUCC\n"],
    [pond_manufacturer["Lifeline"], "Un petit dernier pour la route?\n"],
    [pond_manufacturer["Nova"], "Phénix jubilatoire\n"],
    [pond_manufacturer["Nova"], "Très distingué\n"],
    [pond_manufacturer["Nova"], "Un va-et-vient désagréable\n"],
    [pond_manufacturer["Raid"], "N'oubliez pas de headbanguer\n"],
    [pond_manufacturer["Raid"], "Rocket-man!!!\n"],
    [pond_manufacturer["Raid"], "J'aime vivre dangereusement\n"],
    [pond_manufacturer["Raid"], "Tellement pratique pour retrouver ses clés de bagnole\n"],
    [pond_manufacturer["Raid"], "Ta gueule et fonce\n"],
    [pond_manufacturer["Shield"], "Attention, bouclier opiniâtre\n"],
    [pond_manufacturer["Shield"], "Mais papa, tu triches?\n"],
    [pond_manufacturer["Shield"], "Tout ou rien, pendejo\n"],
    [pond_manufacturer["Spike"], "Toute rose a ses épines\n"],
    [pond_manufacturer["Turtle"], "J'ai vraiment pas mal\n"],
    [pond_manufacturer["Turtle"], "Pr0p hunt l0lz\n"],
]

# If special has been row with item generation
# Will pick an associated special property
item_special = Interval (1) << [
    [0, pond_special["FIREARM"], special_prop_firearm],
    [0, pond_special["GRENADE"], special_prop_grenade],
    [0, pond_special["SHIELD"], special_prop_shield],
]