# -*- coding: utf-8 -*-

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.GenerationResult import GenerationResult
from wordgenerator.Dictionary import DictionaryNode
from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Sequence import S
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import PrintNode as Print
from wordgenerator.Print import CheckpointNode as Checkpoint
from wordgenerator.Print import SetNode, Title, Label
from wordgenerator.Variable import SwitchVarNode as SwitchVar
from wordgenerator.Variable import SetVarNode as SetVar
from wordgenerator.Variable import ContextNode as Context
from wordgenerator.Variable import DefineNode as Define
from wordgenerator.Output import FormatNode as Format
from wordgenerator.Output import MacroNode as Macro
from wordgenerator.Generator import Generator
from generators.borderlands.ponderation import type_flags, manufacturer_flags, can_element, nbr_of_manufacturer_properties
from generators.borderlands.properties import item_prop , item_special, sel_element
from generators.borderlands.names import firearm_name, grenade_name, shield_name

"""The Mighty Item Generator for Borderlands RPG!

Mocks-up a loot generation from a chest in Borderlands, adapted for table roleplay
Generates an item with Type, Rarity, Manufacturer, Stats and Properties

Pendejo.
"""

#################################################
#             SELECT OF CHEST RARITY            #
#################################################

sel_chest = Weight() << [
    [1, "COMMON"],
    [1, "RARE"],
    [1, "LEGENDARY"],
]

#################################################
#               SELECT ITEM TYPE                #
#################################################

sel_type = Weight() << [
    [1, "HANDGUN"],
    [1, "RIFLE"],
    [1, "MACHINEGUN"],
    [1, "SHOTGUN"],
    [1, "SNIPER"],
    [1, "GRENADE"],
    [1, "SHIELD"],
]

def update_type_flags(res:GenerationResult) :
    for v in type_flags.values() :
        v.value = 0
    type_flags[res.get_var("ITEM_TYPE")].value = 1

#################################################
#              SELECT ITEM RARITY               #
#################################################

sel_rarity = {
    "COMMON" : Weight() << [
        [50,    "COMMON"],
        [30,    "UNCOMMON"],
        [10,    "RARE"],
        [6,     "EPIC"],
        [3,     "ETECH"],
        [1,     "LEGENDARY"],
    ],
    "RARE" : Weight() << [
        [26,    "COMMON"],
        [40,    "UNCOMMON"],
        [18,    "RARE"],
        [9,     "EPIC"],
        [5,     "ETECH"],
        [2,     "LEGENDARY"],
    ],
    "LEGENDARY" : Weight() << [
        [0,    "COMMON"],
        [0,    "UNCOMMON"],
        [0,    "RARE"],
        [0,    "EPIC"],
        [10,   "ETECH"],
        [10,   "LEGENDARY"],
    ],
}


#################################################
#               SELECT MANUFACTURER             #
#################################################

sel_manufacturer = {
    "HANDGUN" : Weight() << [
        "Maliwan",
        "Jakobs",
        "Hyperion",
        "Dahl",
        "Vladof",
        "Bandit",
        "Tediore",
        "Torgue",
    ],
    "MACHINEGUN" : Weight() << [
        "Maliwan",
        "Hyperion",
        "Dahl",
        "Bandit",
        "Tediore",
    ],
    "RIFLE" : Weight() << [
        "Jakobs",
        "Dahl",
        "Bandit",
        "Torgue",
    ],
    "SHOTGUN" : Weight() << [
        "Jakobs",
        "Hyperion",
        "Bandit",
        "Tediore",
        "Torgue",
    ],
    "SNIPER" : Weight() << [
        "Maliwan",
        "Jakobs",
        "Hyperion",
        "Vladof",
    ],
    "GRENADE" : Weight() << [
        "Classic",
        "Contact",
        "Proximity",
        "MIRV",
        "Singularity",
        "Tesla",
        "Transfusion",
        "Betty",
    ],
    "SHIELD" : Weight() << [
        "Absorb",
        "Adaptive",
        "Amplify",
        "Booster",
        "Lifeline",
        "Nova",
        "Raid",
        "Shield",
        "Spike",
        "Turtle",
    ],
}

def update_manufacturer_flags(res:GenerationResult) :
    for v in manufacturer_flags.values() :
        v.value = 0
    manufacturer_flags[res.get_var("ITEM_MANUFACTURER")].value = 1

#################################################
#           MANUFACTURER PROPERTIES             #
#################################################

def reset_property_flags() :
    can_element.value = 1
    nbr_of_manufacturer_properties.value = 0
    
def inhibit_element() :
    """"Inhibits the capacity of drawing an element for an item.
    Used for Torgue manufacturer : no element, only EXPLOSIVE
    Used for Maliwan and Tesla manufacturer : mandatory, already picked before
    """
    can_element.value = 0
def predraw_one() :
    """"Reduce the number of picked properties by one for an item.
    Used for every element-mandatory item manufacturer (Maliwan, Nova, Spike, Tesla)
    """
    nbr_of_manufacturer_properties.value = 1

# resolves all specifications for every manufacturer
manufacturer_properties = Interval(1) << [
    # update ponderation to :
    [0, manufacturer_flags["Maliwan"], inhibit_element],
    [0, manufacturer_flags["Maliwan"], predraw_one],
    [0, manufacturer_flags["Torgue"],  inhibit_element],
    [0, manufacturer_flags["Nova"],    predraw_one],
    [0, manufacturer_flags["Spike"],   predraw_one],
    [0, manufacturer_flags["Tesla"],   inhibit_element],
    [0, manufacturer_flags["Tesla"],   predraw_one],
    # resolve the manufacturer specific capacity
    # FIREARMS
    [0, manufacturer_flags["Bandit"], "*Chargeur X2*\n"],
    [0, manufacturer_flags["Dahl"], "*Mode Rafale et Automatique: possibilité d'alterner 2 cartes successives d'un tir*\n"],
    [0, manufacturer_flags["Hyperion"], "*Bouclier d'énergie avec [[1d20+10]]PV*\n"],
    [0, manufacturer_flags["Jakobs"], "*Tir ricochant si critique*\n"],
    [0, manufacturer_flags["Maliwan"], "*Meilleures chances de déclencher l'effet élémentaire*\n"],
    [0, manufacturer_flags["Maliwan"], sel_element],
    [0, manufacturer_flags["Tediore"], "*Lancer l'arme pour recharger, dégâts similaire à une balle en zone*\n"],
    [0, manufacturer_flags["Torgue"], "*Arme Explosive*\n"],
    [0, manufacturer_flags["Vladof"], "*+1 Augmentation de dé, +1 Dégâts, +1 Difficulté de visée, +1 Magasin*\n"],
    # GRENADES
    [0, manufacturer_flags["Classic"], "*Grosse Explosion 5x5*\n"],
    [0, manufacturer_flags["Contact"], "*Explosion sur contact 3x3*\n"],
    [0, manufacturer_flags["Proximity"], "*Mine, explosion 3x3 si déplacement alentour*\n"],
    [0, manufacturer_flags["MIRV"], "*Explose 3x3, puis lance [[1d5+3]] mini grenades qui explosent 3x3 autour de l'explosion initiale le tour suivant*\n"],
    [0, manufacturer_flags["Singularity"], "*Attire les ennemis autour de la grenade 3x3 et explose 3x3*\n"],
    [0, manufacturer_flags["Tesla"], "*Explose 3x3 et laisse une traînée élémentaire pendant 2 tours*\n"],
    [0, manufacturer_flags["Tesla"], sel_element],
    [0, manufacturer_flags["Transfusion"], "*Explosion 3x3, soigne le lanceur des dégâts infligés après 1 tour*\n"],
    [0, manufacturer_flags["Betty"], "*Rebondit jusqu'à toucher un ennemi, explosion 3x3*\n"],
    # SHIELDS
    [0, manufacturer_flags["Absorb"], "*Si l'arme utilisée contre vous est la même que celle que vous utilisez, gagne (+1 Aug dégâts) à chaque tir reçu pour votre prochain tour*\n"],
    [0, manufacturer_flags["Adaptive"], "*Dégâts/2 au 1er tir du dernier élément qui vous a touché*\n"],
    [0, manufacturer_flags["Amplify"], "*Une fois totalement chargé, le bouclier ajoute [[1d10]] dégâts à la prochaine attaque et diminue les PVs du bouclier d'autant*\n"],
    [0, manufacturer_flags["Booster"], "*Une fois touché, balance une unité de rechargement de bouclier à [[1d20]] PV*\n"],
    [0, manufacturer_flags["Lifeline"], "*Vie max +[[1d20+10]], Bouclier -[[1d20]]*\n"],
    [0, manufacturer_flags["Nova"], "*Une fois vidé, le bouclier génère une nova élémentaire faisant [[1d20]] dégâts autour de vous + effet élémentaire*\n"],
    [0, manufacturer_flags["Nova"], sel_element],
    [0, manufacturer_flags["Raid"], "*Une fois vidé, ajoute un bonus de [[1d20]] dégâts à vos attaques de corps (une fois par tour)*\n"],
    [0, manufacturer_flags["Shield"], "*Cadence de rechargement +10, Capacité -15*\n"],
    [0, manufacturer_flags["Spike"], "*Si attaque subie à courte distance, inflige [[1d10]] dégâts élémentaires à l'attaquant*\n"],
    [0, manufacturer_flags["Spike"], sel_element],
    [0, manufacturer_flags["Turtle"], "*Bouclier +[[1d20+10]] PV, Vie max -[[1d20]]*\n"],
]

#################################################
#                 ITEM GENERATION               #
#################################################

item_generation = {"ITEM_TYPE" : {"ITEM_RARITY" : Sequence() }}
item_generation .clear()

def get_firearm_builder(firearm_type:str,
                     firearm_damage,
                     firearm_aim:str,
                     firearm_magazine:str,
                     firearm_modes) :
    return S(
            Define("W_TYPE") << firearm_type,
            Define("W_NAME") << firearm_name,
            
            Context("W_DGTS") << firearm_damage,
            Context("W_AIM") << firearm_aim,
            Context("W_MAG") << firearm_magazine,
            Context("W_SHOOT") << firearm_modes,
            
            Format(format="""{W_TYPE} {ITEM_MANUFACTURER}
    {W_NAME}
    Dégats : {W_DGTS}
    Difficulté de visée  : {W_AIM}
    Magasin  : {W_MAG}
    Modes :
{W_SHOOT}""")
        )

############# HANDGUN BUILDING

handgun_damage = Weight() << [
    [25, "1D4 + [[1d5+5]]"],
    [50, "1D6 + [[1d5+4]]"],
    [25, "1D8 + [[1d5+3]]"],
]
handgun_modes = Weight(2, False, between_action="\n") << [
    [" - Tir Simple"],
    [" - Tir Rafale"],
    [" - Tir Automatique"],
]

item_generation["HANDGUN"] = {
    "COMMON":   get_firearm_builder("Pistolet Commun",     handgun_damage, "[[3-1d5]]", "[[1d5+3]]", handgun_modes),
    "UNCOMMON": get_firearm_builder("Pistolet Peu Commun", handgun_damage, "[[3-1d5]]", "[[1d5+4]]", handgun_modes),
    "RARE":     get_firearm_builder("Pistolet Rare",       handgun_damage, "[[2-1d4]]", "[[1d5+4]]", handgun_modes),
    "EPIC":     get_firearm_builder("Pistolet Epique",     handgun_damage, "[[2-1d4]]", "[[1d5+5]]", handgun_modes),
    "ETECH":    get_firearm_builder("Pistolet E-Tech",     handgun_damage, "[[1-1d4]]", "[[1d5+5]]", handgun_modes),
    "LEGENDARY":get_firearm_builder("Pistolet Légendaire", handgun_damage, "[[1-1d4]]", "[[1d5+6]]", handgun_modes),
}

############# RIFLE BUILDING

rifle_damage = Weight() << [
    [15, "1D4 + [[1d7+9]]"],
    [30, "1D6 + [[1d7+8]]"],
    [40, "1D8 + [[1d7+6]]"],
    [15, "1D10 + [[1d7+5]]"],
]
rifle_modes = handgun_modes

item_generation["RIFLE"] = {
    "COMMON":   get_firearm_builder("Fusil d'assaut Commun",     rifle_damage, "[[4-1d7]]", "[[1d5+6]]",  rifle_modes),
    "UNCOMMON": get_firearm_builder("Fusil d'assaut Peu Commun", rifle_damage, "[[4-1d7]]", "[[1d5+8]]",  rifle_modes),
    "RARE":     get_firearm_builder("Fusil d'assaut Rare",       rifle_damage, "[[3-1d6]]", "[[1d5+8]]",  rifle_modes),
    "EPIC":     get_firearm_builder("Fusil d'assaut Epique",     rifle_damage, "[[3-1d6]]", "[[1d5+10]]", rifle_modes),
    "ETECH":    get_firearm_builder("Fusil d'assaut E-Tech",     rifle_damage, "[[3-1d5]]", "[[1d5+10]]", rifle_modes),
    "LEGENDARY":get_firearm_builder("Fusil d'assaut Légendaire", rifle_damage, "[[3-1d5]]", "[[1d5+12]]", rifle_modes),
}

############# SUB-MACHINEGUN BUILDING

machinegun_damage = Weight() << [
    [20, "1D8 + [[1d7]]"],
    [40, "1D10 + [[1d7-1]]"],
    [40, "1D12 + [[1d7-2]]"],
]
machinegun_modes = Sequence(between_action="\n") << [
    " - Tir Simple",
    " - Tir Rafale",
    " - Tir Automatique"
]

item_generation["MACHINEGUN"] = {
    "COMMON":   get_firearm_builder("Mitraillette Commune",     machinegun_damage, "[[4-1d7]]", "[[1d7+9]]",  machinegun_modes),
    "UNCOMMON": get_firearm_builder("Mitraillette Peu Commune", machinegun_damage, "[[4-1d7]]", "[[1d7+11]]", machinegun_modes),
    "RARE":     get_firearm_builder("Mitraillette Rare",        machinegun_damage, "[[3-1d6]]", "[[1d7+11]]", machinegun_modes),
    "EPIC":     get_firearm_builder("Mitraillette Epique",      machinegun_damage, "[[3-1d6]]", "[[1d7+13]]", machinegun_modes),
    "ETECH":    get_firearm_builder("Mitraillette E-Tech",      machinegun_damage, "[[3-1d5]]", "[[1d7+13]]", machinegun_modes),
    "LEGENDARY":get_firearm_builder("Mitraillette Légendaire",  machinegun_damage, "[[3-1d5]]", "[[1d7+15]]", machinegun_modes),
}

############# SHOTGUN BUILDING

shotgun_damage = Weight() << [
    [10, "2D8 + [[1d9+14]]"],
    [40, "2D10 + [[1d9+12]]"],
    [40, "2D12 + [[1d9+10]]"],
    [10, "2D20 + [[1d9+2]]"],
]
shotgun_modes = " - Tir Simple"

item_generation["SHOTGUN"] = {
    "COMMON":   get_firearm_builder("Fusil à pompe Commun",     shotgun_damage, "[[6-1d7]]", "[[1d3]]",   shotgun_modes),
    "UNCOMMON": get_firearm_builder("Fusil à pompe Peu Commun", shotgun_damage, "[[6-1d7]]", "[[1d3+1]]", shotgun_modes),
    "RARE":     get_firearm_builder("Fusil à pompe Rare",       shotgun_damage, "[[5-1d7]]", "[[1d3+1]]", shotgun_modes),
    "EPIC":     get_firearm_builder("Fusil à pompe Epique",     shotgun_damage, "[[5-1d7]]", "[[1d3+2]]", shotgun_modes),
    "ETECH":    get_firearm_builder("Fusil à pompe E-Tech",     shotgun_damage, "[[4-1d7]]", "[[1d3+2]]", shotgun_modes),
    "LEGENDARY":get_firearm_builder("Fusil à pompe Légendaire", shotgun_damage, "[[4-1d7]]", "[[1d3+3]]", shotgun_modes),
}

############# SNIPER BUILDING

sniper_damage = Weight() << [
    [60, "1D4 + [[1d7+35]]"],
    [25, "1D6 + [[1d7+34]]"],
    [15, "1D8 + [[1d7+33]]"],
]
sniper_modes = " - Tir Simple"

item_generation["SNIPER"] = {
    "COMMON":   get_firearm_builder("Sniper Commun",     sniper_damage, "[[3-1d5]]", "[[1d4]]",   sniper_modes),
    "UNCOMMON": get_firearm_builder("Sniper Peu Commun", sniper_damage, "[[3-1d5]]", "[[1d4+1]]", sniper_modes),
    "RARE":     get_firearm_builder("Sniper Rare",       sniper_damage, "[[2-1d4]]", "[[1d4+1]]", sniper_modes),
    "EPIC":     get_firearm_builder("Sniper Epique",     sniper_damage, "[[2-1d4]]", "[[1d4+2]]", sniper_modes),
    "ETECH":    get_firearm_builder("Sniper E-Tech",     sniper_damage, "[[1-1d4]]", "[[1d4+2]]", sniper_modes),
    "LEGENDARY":get_firearm_builder("Sniper Légendaire", sniper_damage, "[[1-1d4]]", "[[1d4+3]]", sniper_modes),
}

############# GRENADE BUILDING

def get_grenade_builder(grenade_type:str,
                     grenade_damage,
                     grenade_aim:str,
                     grenade_modes) :
    return S(
            Define("W_TYPE") << grenade_type,
            Define("W_NAME") << grenade_name,
            
            Context("W_DGTS") << grenade_damage,
            Context("W_AIM") << grenade_aim,
            Context("W_SHOOT") << grenade_modes,
            
            Format(format="""{W_TYPE} {ITEM_MANUFACTURER}
    {W_NAME}
    Dégats : {W_DGTS}
    Difficulté de visée  : {W_AIM}
    {W_SHOOT}""")
        )

grenade_damage = Print("2D20 + [[1d11+23]]")
grenade_modes = " - Tir Simple"

item_generation["GRENADE"] = {
    "COMMON":   get_grenade_builder("Grenade Commune",     grenade_damage, "[[4-1d7]]", grenade_modes),
    "UNCOMMON": get_grenade_builder("Grenade Peu Commune", grenade_damage, "[[4-1d7]]", grenade_modes),
    "RARE":     get_grenade_builder("Grenade Rare",        grenade_damage, "[[3-1d6]]", grenade_modes),
    "EPIC":     get_grenade_builder("Grenade Epique",      grenade_damage, "[[3-1d6]]", grenade_modes),
    "ETECH":    get_grenade_builder("Grenade E-Tech",      grenade_damage, "[[3-1d5]]", grenade_modes),
    "LEGENDARY":get_grenade_builder("Grenade Légendaire",  grenade_damage, "[[3-1d5]]", grenade_modes),
}

############# SHIELD BUILDING

def get_shield_builder(shield_type:str) :
    return S(
            Define("W_TYPE") << shield_type,
            Define("W_NAME") << shield_name,
            Macro("S_INTENSITY", "[[1d11+6]]"),
            
            Context("W_CAPA") << "[[84 - 3*{S_INTENSITY} + 1d7]]",
            Context("W_CADE") << "[[1d5 + {S_INTENSITY}]]",
            
            Format("DEFAULT", """{W_TYPE} {ITEM_MANUFACTURER}
    {W_NAME} [{S_INTENSITY}]
    Capacité : {W_CAPA}
    Cadence  : {W_CADE}""")
        )

item_generation["SHIELD"] = {
    "COMMON":   get_shield_builder("Bouclier Commun"),
    "UNCOMMON": get_shield_builder("Bouclier Peu Commun"),
    "RARE":     get_shield_builder("Bouclier Rare"),
    "EPIC":     get_shield_builder("Bouclier Epique"),
    "ETECH":    get_shield_builder("Bouclier E-Tech"),
    "LEGENDARY":get_shield_builder("Bouclier Légendaire"),
}

#####################################P#E#N#D#E#J#
#                   GENERATION                  O
#################################################
                       
generation = Generator(
    Sequence() << [
        reset_property_flags,
        Define("CHEST_TYPE") << sel_chest,
        Define("ITEM_TYPE")  << sel_type,
        update_type_flags,
        Define("ITEM_RARITY")       << DictionaryNode(sel_rarity, "CHEST_TYPE"),
        Define("ITEM_MANUFACTURER") << DictionaryNode(sel_manufacturer, "ITEM_TYPE"),
        update_manufacturer_flags,
        DictionaryNode(item_generation, "ITEM_TYPE", "ITEM_RARITY"),
        SwitchVar("PROPERTIES"),
        manufacturer_properties,
        DictionaryNode(item_prop, "ITEM_RARITY", "ITEM_TYPE"),
        item_special,
])


if __name__ == "__main__" :
    for i in range(0,1):
        # Do generation
        # Tesla / Proximity
        result = generation.execute(CHEST_TYPE="LEGENDARY",
                                    ITEM_TYPE="GRENADE",
                                    ITEM_RARITY="ETECH",
                                    ITEM_MANUFACTURER="Tesla")
        
        # print generation result
        result.print_to_console(
"""
________________________
Coffre : {CHEST_TYPE}
Arme   : {ITEM_TYPE}
Rareté : {ITEM_RARITY}
Fabriquant : {ITEM_MANUFACTURER}
________________________
{DEFAULT}
________________________
{PROPERTIES}
________________________
""")
    
    #result.display_vars()