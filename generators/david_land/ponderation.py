# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import SetNode
from macro.calc import Value

""" Init values.
Odds are updated during the generation,
when the different weapon type and constructor
are chosen.
"""

# Ponderations for each weapon type
pond_type = {
    "PISTOLET"  : Value(0),
    "MITRAILLETTE" : Value(0),
    "ASSAUT"    : Value(0),
    "POMPE"     : Value(0),
    "SNIPER"    : Value(0),
    "GRENADE"    : Value(0),
    "BOUCLIER"    : Value(0),
}

# Ponderations for each weapon constructor
pond_fabriquant = {
    # FUSILS
    "Bandit"    : Value(0),
    "Dahl"      : Value(0),
    "Hyperion"  : Value(0),
    "Jakobs"    : Value(0),
    "Maliwan"   : Value(0),
    "Tediore"   : Value(0),
    "Torgue"    : Value(0),
    "Vladof"    : Value(0),
    # GRENADES
    "Classic"   : Value(0),
    "Contact"   : Value(0),
    "Proximity" : Value(0),
    "MIRV"      : Value(0),
    "Singularity" : Value(0),
    "Tesla"     : Value(0),
    "Transfusion" : Value(0),
    "Betty"     : Value(0),
    # BOUCLIERS
    "Absorb"    : Value(0),
    "Adaptive"  : Value(0),
    "Amplify"   : Value(0),
    "Booster"   : Value(0),
    "Lifeline"  : Value(0),
    "Nova"      : Value(0),
    "Raid"      : Value(0),
    "Shield"    : Value(0),
    "Spike"     : Value(0),
    "Turtle"    : Value(0),
}

# Ponderations for each element
pond_element = {
    "FEU"  : Value(0),
    "COR"  : Value(0),
    "ELEC" : Value(0),
    "SLAG" : Value(0),
    "RAD"  : Value(0),
    "CRYO" : Value(0),
}

def SetWeaponElement(weapon_element) :
    # update the ponderations
    for v in pond_element.values() :
        v.value = 0
    pond_element[weapon_element].value = 1
    
sel_element = Sequence().extend([
    " - Effet élémentaire: ",
    Weight().extend([
        Sequence().extend(["incendiaire", SetNode(SetWeaponElement, "FEU")]),
        Sequence().extend(["électrique" , SetNode(SetWeaponElement, "ELEC")]),
        Sequence().extend(["slag"       , SetNode(SetWeaponElement, "SLAG")]),
        Sequence().extend(["corrosif"   , SetNode(SetWeaponElement, "COR")]),
        Sequence().extend(["radiation"  , SetNode(SetWeaponElement, "RAD")]),
        Sequence().extend(["cryogénique", SetNode(SetWeaponElement, "CRYO")]),
    ]),
    "\n"
])

# flag : multiply with weight for actual chances to have an elementary property
#   0 : no chance to have a elementary property
#   1 : Can have an elementary property
can_element = Value(1)

# Counter of the number of properties preset by the weapon constructor.
nbr_of_constructor_properties = Value(0)