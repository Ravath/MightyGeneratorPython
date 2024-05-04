# -*- coding: utf-8 -*-

from macro.math import Value

""" Dictionnaries for each weighting values used in items.py.

Init values.
Odds are updated during the generation,
when the different item type and manufacturer
are chosen.

"""
# Ponderations for each chest type

pond_chest = {
    "COMMON"    : Value(0),
    "RARE"      : Value(0),
    "LEGENDARY" : Value(0),
}

# Ponderations for each weapon type
pond_type = {
    "HANDGUN"   : Value(0),
    "MACHINEGUN": Value(0),
    "RIFLE"     : Value(0),
    "SHOTGUN"   : Value(0),
    "SNIPER"    : Value(0),
    "GRENADE"   : Value(0),
    "SHIELD"    : Value(0),
}

# Ponderations for each item manufacturer
pond_manufacturer = {
    # FIREARMS
    "Bandit"    : Value(0),
    "Dahl"      : Value(0),
    "Hyperion"  : Value(0),
    "Jakobs"    : Value(0),
    "Maliwan"   : Value(0),
    "Tediore"   : Value(0),
    "Torgue"    : Value(0),
    "Vladof"    : Value(0),
    # GRENADES
    "Classic"       : Value(0),
    "Contact"       : Value(0),
    "Proximity"     : Value(0),
    "MIRV"          : Value(0),
    "Singularity"   : Value(0),
    "Tesla"         : Value(0),
    "Transfusion"   : Value(0),
    "Betty"         : Value(0),
    # SHIELDS
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
    "FIRE"  : Value(0),
    "COR"   : Value(0),
    "SHOCK" : Value(0),
    "SLAG"  : Value(0),
    "RAD"   : Value(0),
    "CRYO"  : Value(0),
}

# flag : multiply with weight for actual chances to have an elementary property
#   0 : no chance to have a elementary property
#   1 : Can have an elementary property
can_element = Value(1)

# Counter of the number of properties preset by the weapon manufacturer.
nbr_of_manufacturer_properties = Value(0)

### Ponderations for Special properties ###

# Initialisation for every item, resets every time
ITEM_SPECIAL = "INIT"

# Ponderation special properties for each item type
pond_special = {
    "FIREARM"   : Value(0),
    "GRENADE"   : Value(0),
    "SHIELD"    : Value(0),
}

def set_special_prop(item_special) :
    """Allows to set and send back a special property for item generation.

    Named parameter:
    item_special is either firearm_special, grenade_special or shield_special

    """
    global pond_special
    # update the ponderations
    for v in pond_special.values() :
        v.value = 0
    pond_special[item_special].value = 1
    global ITEM_SPECIAL
    ITEM_SPECIAL = item_special
