# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import PrintNode as Print
from wordgenerator.Print import SetNode, Title, Label
from wordgenerator.Generator import Generator
from generators.borderlands.ponderation import pond_type, pond_manufacturer, can_element, nbr_of_manufacturer_properties
from generators.borderlands.properties import item_prop , item_special, sel_element
from generators.borderlands.names import firearm_name, grenade_name, shield_name

"""The Mighty Item Generator for Borderlands RPG!

Mocks-up a loot generation from a chest in Borderlands, adapted for table roleplay
Generates an item with Type, Rarity, Manufacturer, Stats and Properties

Pendejo.
"""

#################################################
#              INIT PROBABILITIES               #
#################################################

# CHEST_TYPE changes odds of getting some rarities
CHEST_TYPE = "LEGENDARY"

if CHEST_TYPE == "COMMON" :
    ODD_COM = 50   # Odds for getting a common item
    ODD_UNCOM = 30 # Odds for getting an uncommon item
    ODD_RAR = 10   # Odds for getting a rare item
    ODD_EPIC = 6   # Odds for getting an epic item
    ODD_ETECH = 3  # Odds for getting an e-tech item
    ODD_LEG = 1    # Odds for getting a legendary item
elif CHEST_TYPE == "RARE" :
    ODD_COM = 26
    ODD_UNCOM = 40
    ODD_RAR = 18
    ODD_EPIC = 9
    ODD_ETECH = 5
    ODD_LEG = 2
elif CHEST_TYPE == "LEGENDARY" : # Currently used for test, real values later
    ODD_COM = 0
    ODD_UNCOM = 0
    ODD_RAR = 0
    ODD_EPIC = 0
    ODD_ETECH = 10
    ODD_LEG = 10

ODD_HAN = 1 # Odds for getting a handgun
ODD_RIF = 1 # Odds for getting a rifle
ODD_MAC = 1 # Odds for getting a sub-machinegun
ODD_SHO = 1 # Odds for getting a shotgun
ODD_SNI = 1 # Odds for getting a sniper rifle
ODD_GRE = 1 # Odds for getting a grenade
ODD_SHI = 1 # Odds for getting a shield

#################################################
#            SELECT TYPE AND RARITY             #
#################################################

# Initialisations for every new item generation
ITEM_TYPE = "INIT"
ITEM_RARITY = "INIT"
ITEM_MANUFACTURER = "INIT"

def set_item_type(item_type) :
    # update the flag
    global ITEM_TYPE
    ITEM_TYPE = item_type

    # update the ponderations
    for v in pond_type.values() :
        v.value = 0
    pond_type[item_type].value = 1

def set_item_rarity(item_rarity) :
    # update the flag
    global ITEM_RARITY
    ITEM_RARITY = item_rarity

def set_item_manufacturer(item_manufacturer) :
    # update the ponderations
    global pond_manufacturer
    for v in pond_manufacturer.values() :
        v.value = 0
    pond_manufacturer[item_manufacturer].value = 1
    global ITEM_MANUFACTURER
    ITEM_MANUFACTURER = item_manufacturer

sel_type = Weight() << [
    [ODD_HAN, SetNode(set_item_type, "HANDGUN")],
    [ODD_RIF, SetNode(set_item_type, "RIFLE")],
    [ODD_MAC, SetNode(set_item_type, "MACHINEGUN")],
    [ODD_SHO, SetNode(set_item_type, "SHOTGUN")],
    [ODD_SNI, SetNode(set_item_type, "SNIPER")],
    [ODD_GRE, SetNode(set_item_type, "GRENADE")],
    [ODD_SHI, SetNode(set_item_type, "SHIELD")],
]

sel_rarity = Weight() << [
    [ODD_COM,   SetNode(set_item_rarity, "COMMON")],
    [ODD_UNCOM, SetNode(set_item_rarity, "UNCOMMON")],
    [ODD_RAR,   SetNode(set_item_rarity, "RARE")],
    [ODD_EPIC,  SetNode(set_item_rarity, "EPIC")],
    [ODD_ETECH, SetNode(set_item_rarity, "ETECH")],
    [ODD_LEG,   SetNode(set_item_rarity, "LEGENDARY")],
]

#################################################
#               SELECT MANUFACTURER             #
#################################################

sel_manufacturer = {
    "HANDGUN" : Weight() << [
        SetNode(set_item_manufacturer, "Maliwan"),
        SetNode(set_item_manufacturer, "Jakobs"),
        SetNode(set_item_manufacturer, "Hyperion"),
        SetNode(set_item_manufacturer, "Dahl"),
        SetNode(set_item_manufacturer, "Vladof"),
        SetNode(set_item_manufacturer, "Bandit"),
        SetNode(set_item_manufacturer, "Tediore"),
        SetNode(set_item_manufacturer, "Torgue"),
    ],
    "MACHINEGUN" : Weight() << [
        SetNode(set_item_manufacturer, "Maliwan"),
        SetNode(set_item_manufacturer, "Hyperion"),
        SetNode(set_item_manufacturer, "Dahl"),
        SetNode(set_item_manufacturer, "Bandit"),
        SetNode(set_item_manufacturer, "Tediore"),
    ],
    "RIFLE" : Weight() << [
        SetNode(set_item_manufacturer, "Jakobs"),
        SetNode(set_item_manufacturer, "Dahl"),
        SetNode(set_item_manufacturer, "Bandit"),
        SetNode(set_item_manufacturer, "Torgue"),
    ],
    "SHOTGUN" : Weight() << [
        SetNode(set_item_manufacturer, "Jakobs"),
        SetNode(set_item_manufacturer, "Hyperion"),
        SetNode(set_item_manufacturer, "Bandit"),
        SetNode(set_item_manufacturer, "Tediore"),
        SetNode(set_item_manufacturer, "Torgue"),
    ],
    "SNIPER" : Weight() << [
        SetNode(set_item_manufacturer, "Maliwan"),
        SetNode(set_item_manufacturer, "Jakobs"),
        SetNode(set_item_manufacturer, "Hyperion"),
        SetNode(set_item_manufacturer, "Vladof"),
    ],
    "GRENADE" : Weight() << [
        SetNode(set_item_manufacturer, "Classic"),
        SetNode(set_item_manufacturer, "Contact"),
        SetNode(set_item_manufacturer, "Proximity"),
        SetNode(set_item_manufacturer, "MIRV"),
        SetNode(set_item_manufacturer, "Singularity"),
        SetNode(set_item_manufacturer, "Tesla"),
        SetNode(set_item_manufacturer, "Transfusion"),
        SetNode(set_item_manufacturer, "Betty"),
    ],
    "SHIELD" : Weight() << [
        SetNode(set_item_manufacturer, "Absorb"),
        SetNode(set_item_manufacturer, "Adaptive"),
        SetNode(set_item_manufacturer, "Amplify"),
        SetNode(set_item_manufacturer, "Booster"),
        SetNode(set_item_manufacturer, "Lifeline"),
        SetNode(set_item_manufacturer, "Nova"),
        SetNode(set_item_manufacturer, "Raid"),
        SetNode(set_item_manufacturer, "Shield"),
        SetNode(set_item_manufacturer, "Spike"),
        SetNode(set_item_manufacturer, "Turtle"),
    ],
}

#################################################
#              ELEMENT GENERATION               #
#################################################

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

# spe_manufacturer resolves all specifications for every manufacturer
spe_manufacturer = Interval(1) << [
    # update ponderation to :
    [0, pond_manufacturer["Maliwan"], inhibit_element],
    [0, pond_manufacturer["Maliwan"], predraw_one],
    [0, pond_manufacturer["Torgue"],  inhibit_element],
    [0, pond_manufacturer["Nova"],    predraw_one],
    [0, pond_manufacturer["Spike"],   predraw_one],
    [0, pond_manufacturer["Tesla"],   inhibit_element],
    [0, pond_manufacturer["Tesla"],   predraw_one],
    # resolve the manufacturer specific capacity
    # FIREARMS
    [0, pond_manufacturer["Bandit"], "*Chargeur X2*\n"],
    [0, pond_manufacturer["Dahl"], "*Mode Rafale et Automatique: possibilité d'alterner 2 cartes successives d'un tir*\n"],
    [0, pond_manufacturer["Hyperion"], "*Bouclier d'énergie avec [[1d20+10]]PV*\n"],
    [0, pond_manufacturer["Jakobs"], "*Tir ricochant si critique*\n"],
    [0, pond_manufacturer["Maliwan"], "*Meilleures chances de déclencher l'effet élémentaire*\n"],
    [0, pond_manufacturer["Maliwan"], sel_element],
    [0, pond_manufacturer["Tediore"], "*Lancer l'arme pour recharger, dégâts similaire à une balle en zone*\n"],
    [0, pond_manufacturer["Torgue"], "*Arme Explosive*\n"],
    [0, pond_manufacturer["Vladof"], "*+1 Augmentation de dé, +1 Dégâts, +1 Difficulté de visée, +1 Magasin*\n"],
    # GRENADES
    [0, pond_manufacturer["Classic"], "*Grosse Explosion 5x5*\n"],
    [0, pond_manufacturer["Contact"], "*Explosion sur contact 3x3*\n"],
    [0, pond_manufacturer["Proximity"], "*Mine, explosion 3x3 si déplacement alentour*\n"],
    [0, pond_manufacturer["MIRV"], "*Explose 3x3, puis lance [[1d5+3]] mini grenades qui explosent 3x3 autour de l'explosion initiale le tour suivant*\n"],
    [0, pond_manufacturer["Singularity"], "*Attire les ennemis autour de la grenade 3x3 et explose 3x3*\n"],
    [0, pond_manufacturer["Tesla"], "*Explose 3x3 et laisse une traînée élémentaire pendant 2 tours*\n"],
    [0, pond_manufacturer["Tesla"], sel_element],
    [0, pond_manufacturer["Transfusion"], "*Explosion 3x3, soigne le lanceur des dégâts infligés après 1 tour*\n"],
    [0, pond_manufacturer["Betty"], "*Rebondit jusqu'à toucher un ennemi, explosion 3x3*\n"],
    # SHIELDS
    [0, pond_manufacturer["Absorb"], "*Si l'arme utilisée contre vous est la même que celle que vous utilisez, gagne (+1 Aug dégâts) à chaque tir reçu pour votre prochain tour*\n"],
    [0, pond_manufacturer["Adaptive"], "*Dégâts/2 au 1er tir du dernier élément qui vous a touché*\n"],
    [0, pond_manufacturer["Amplify"], "*Une fois totalement chargé, le bouclier ajoute [[1d10]] dégâts à la prochaine attaque et diminue les PVs du bouclier d'autant*\n"],
    [0, pond_manufacturer["Booster"], "*Une fois touché, balance une unité de rechargement de bouclier à [[1d20]] PV*\n"],
    [0, pond_manufacturer["Lifeline"], "*Vie max +[[1d20+10]], Bouclier -[[1d20]]*\n"],
    [0, pond_manufacturer["Nova"], "*Une fois vidé, le bouclier génère une nova élémentaire faisant [[1d20]] dégâts autour de vous + effet élémentaire*\n"],
    [0, pond_manufacturer["Nova"], sel_element],
    [0, pond_manufacturer["Raid"], "*Une fois vidé, ajoute un bonus de [[1d20]] dégâts à vos attaques de corps (une fois par tour)*\n"],
    [0, pond_manufacturer["Shield"], "*Cadence de rechargement +10, Capacité -15*\n"],
    [0, pond_manufacturer["Spike"], "*Si attaque subie à courte distance, inflige [[1d10]] dégâts élémentaires à l'attaquant*\n"],
    [0, pond_manufacturer["Spike"], sel_element],
    [0, pond_manufacturer["Turtle"], "*Bouclier +[[1d20+10]] PV, Vie max -[[1d20]]*\n"],
]

#################################################
#                 ITEM GENERATION               #
#################################################

item_generation = {"" : {"" : Sequence() }}
item_generation .clear()

def get_firearm_builder(firearm_type:str,
                     firearm_damage,
                     firearm_aim:str,
                     firearm_magazine:str,
                     firearm_modes) :
    return Title(firearm_type+" {ITEM_MANUFACTURER}",
                 Sequence() << [
                    firearm_name,
                    Label("Dégats",              firearm_damage),
                    Label("Difficulté de visée", firearm_aim),
                    Label("Magasin",             firearm_magazine),
                    firearm_modes,
    ])

############# HANDGUN BUILDING

handgun_damage = Weight() << [
    [25, "1D4 << [[1d5+5]]"],
    [50, "1D6 << [[1d5+4]]"],
    [25, "1D8 << [[1d5+3]]"],
]
handgun_modes = Weight(2, False) << [
    [" - Tir Simple\n"],
    [" - Tir Rafale\n"],
    [" - Tir Automatique\n"],
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
machinegun_modes = Sequence() << [
    " - Tir Simple\n",
    " - Tir Rafale\n",
    " - Tir Automatique\n"
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
shotgun_modes = " - Tir Simple\n"

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
sniper_modes = " - Tir Simple\n"

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
    return Title(grenade_type+" {ITEM_MANUFACTURER}",
                 Sequence() << [
                     grenade_name,
                     Label("Dégats",              grenade_damage),
                     Label("Difficulté de visée", grenade_aim),
                     grenade_modes,
    ])

grenade_damage = Print("2D20 + [[1d11+23]]")
grenade_modes = " - Tir Simple\n"

item_generation["GRENADE"] = {
    "COMMON":   get_grenade_builder("Grenade Commune",     grenade_damage, "[[4-1d7]]", grenade_modes),
    "UNCOMMON": get_grenade_builder("Grenade Peu Commune", grenade_damage, "[[4-1d7]]", grenade_modes),
    "RARE":     get_grenade_builder("Grenade Rare",        grenade_damage, "[[3-1d6]]", grenade_modes),
    "EPIC":     get_grenade_builder("Grenade Epique",      grenade_damage, "[[3-1d6]]", grenade_modes),
    "ETECH":    get_grenade_builder("Grenade E-Tech",      grenade_damage, "[[3-1d5]]", grenade_modes),
    "LEGENDARY":get_grenade_builder("Grenade Légendaire",  grenade_damage, "[[3-1d5]]", grenade_modes),
}

############# SHIELD BUILDING

shield_intensity = "(1d11+6)"

def get_shield_builder(shield_type:str) :
    return Title(shield_type+" {ITEM_MANUFACTURER}",
                 Sequence() << [
                     shield_name,
                     Label("Capacité", f"[[84 - 3*{shield_intensity} + 1d7]]"),
                     Label("Cadence",  f"[[1d5 + {shield_intensity}]]"),
    ])

item_generation["SHIELD"] = {
    "COMMON":   get_shield_builder("Bouclier Commun"),
    "UNCOMMON": get_shield_builder("Bouclier Peu Commun"),
    "RARE":     get_shield_builder("Bouclier Rare"),
    "EPIC":     get_shield_builder("Bouclier Epique"),
    "ETECH":    get_shield_builder("Bouclier E-Tech"),
    "LEGENDARY":get_shield_builder("Bouclier Légendaire"),
}

###################################P#E#N#D#E#J#O#
#                   GENERATION                  #
#################################################

from wordgenerator.NodeIf import AbsLeafNode
class DictionaryNode(AbsLeafNode) :
    """Node managing a dictionary of nodes"""

    def __init__(self, node_dictionary, *variables : str):
        AbsLeafNode.__init__(self)
        self.dict = node_dictionary
        # name of variables
        self.variables = variables

    def execute(self):
        """Execute the designated node."""
        # Get the first dictionary
        var_name = self.variables[0]
        to_execute = self.dict[globals()[var_name]]

        # progress through each dictionary
        for si in range(1, len(self.variables)) :
            # get name of the variable containing the key
            var_name = self.variables[si]
            # get the node associated with this key in the dictionary
            to_execute = to_execute[globals()[var_name]]

        # Execute the found dictionary
        to_execute.execute()

    def print_node(self, tabs:int = 0) :
        """Print the node name and its dictionary keys and values."""
        # Node Name
        tab_sign="\t"
        print(f"{tab_sign*tabs}[{type(self).__name__} : {self.variables}]")
        # dictionary
        DictionaryNode.display_dico_node(self.dict, tabs + 1)

    def display_dico_node(dico_node, tabs : int) :
        tab_sign="\t"
        if isinstance(dico_node, dict) :
            for k in dico_node :
                print(f"{tab_sign*tabs}{k}")
                DictionaryNode.display_dico_node(dico_node[k], tabs + 1)
        else :
            dico_node.print_node(tabs)

### GENERATION TEMPLATE ###
generation = Generator(
    Sequence() << [
        sel_type,
        sel_rarity,
        DictionaryNode(sel_manufacturer, "ITEM_TYPE"),
        DictionaryNode(item_generation, "ITEM_TYPE", "ITEM_RARITY"),
        Title("Propriétés",
            Sequence() << [
                spe_manufacturer,
                DictionaryNode(item_prop, "ITEM_RARITY", "ITEM_TYPE"),
                item_special,
])])

# text var converter
def var_converter(name) -> str :
    if name in globals().keys() :
        return globals()[name]
    else :
        return "{" + name + "}"
generation.variable_converter = var_converter

if __name__ == "__main__" :
    # Do generation
    generation.execute()
    
    print("Coffre :", globals()["CHEST_TYPE"])
    print("Arme   :", ITEM_TYPE)
    print("Rareté :", ITEM_RARITY)
    print("Fabriquant :", ITEM_MANUFACTURER)
    print()
    
    # print generation result
    generation.print_to_console()