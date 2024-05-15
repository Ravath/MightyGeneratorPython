# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:24:26 2 22

@author: Ehlion
"""

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Sequence import SequenceNode, S
from wordgenerator.Generator import Generator
from wordgenerator.Print import SetNode as Set
from wordgenerator.Print import Label, Title
from wordgenerator.TabNode import TabNode
from enum import Enum

# Renseigner ici le rang de l'objet entre 1 et 4,
# qui déterminera le nombre de ses améliorations
# NBR_AMELIORATION = RANG + QUALITY
RANG = 10
QUALITY = 0
WEAPON_TYPE = 0

def set_quality(value) :
    global QUALITY
    QUALITY = value

def set_weapon(value) :
    global WEAPON_TYPE
    WEAPON_TYPE = value.value

class WEAPON(Enum) :
    PISTOL = 0
    MACHINEGUN = 1
    ASSAULT = 2
    SNIPER = 3
    SHOTGUN = 4
    ROCKET = 5
    GRENADE = 6
    SHIELD = 7

# roll Weapon Type
sel_weapon = Interval("1d20") << [
    [ 1,  4, Set(set_weapon, WEAPON.PISTOL)],
    [ 5,  6, Set(set_weapon, WEAPON.MACHINEGUN)],
    [ 7,  8, Set(set_weapon, WEAPON.ASSAULT)],
    [ 9, 10, Set(set_weapon, WEAPON.SNIPER)],
    [11, 12, Set(set_weapon, WEAPON.SHOTGUN)],
    [13, 13, Set(set_weapon, WEAPON.ROCKET)],
    [14, 15, Set(set_weapon, WEAPON.GRENADE)],
    [16, 20, Set(set_weapon, WEAPON.SHIELD)],
]

# roll Quality
sel_quality = Interval("1d20") << [
    [ 1, 12, Set(set_quality, 1)],
    [13, 17, Set(set_quality, 2)],
    [18, 19, Set(set_quality, 3)],
    [20, 20, Set(set_quality, 4)],
]

# Weapon Specifics
weapon = {
    WEAPON.PISTOL : Interval("1d20") << [
        [ 1,  4, Label("Handgun", Interval("1d20") << [
                [ 1,  3, "Bandit Pistal"],
                [ 4,  6, "Dahl Repeater"],
                [ 7,  9, "Hyperion Apparatus"],
                [10, 11, "Jakobs Revolver"],
                [12, 13, "Maliwan Aegis"],
                [14, 16, "Tediore Handgun"],
                [17, 18, "Torgue Handcannon"],
                [19, 20, "Vladof TMP"],
            ])],
        [ 5,  8, Label("Aimshot", Interval("1d20") << [
                [ 1,  3, "Bandit Hed Shoter!"],
                [ 4,  6, "Dahl Anaconda"],
                [ 7,  9, "Hyperion Vision"],
                [10, 11, "Jakobs Longarm"],
                [12, 13, "Maliwan Phobia"],
                [14, 16, "Tediore Aimshot"],
                [17, 18, "Torgue Hole Puncher"],
                [19, 20, "Vladof Assassin"],
            ])],
        [ 9, 12, Label("Powershot", Interval("1d20") << [
                [ 1,  3, "Bandit Ass Beeter!"],
                [ 4,  6, "Dahl Peacemaker"],
                [ 7,  9, "Hyperion Leverage"],
                [10, 11, "Jakobs Iron"],
                [12, 13, "Maliwan Torment"],
                [14, 16, "Tediore Powershot"],
                [17, 18, "Torgue Rod"],
                [19, 20, "Vladof Fighter"],
            ])],
        [13, 16, Label("Big Gun", Interval("1d20") << [
                [ 1,  3, "Bandit Magamum!"],
                [ 4,  6, "Dahl Magnum"],
                [ 7,  9, "Hyperion Impact"],
                [10, 11, "Jakobs Widow Maker"],
                [12, 13, "Maliwan Animosity"],
                [14, 16, "Tediore Biggun"],
                [17, 18, "Torgue Slapper"],
                [19, 20, "Vladof Troublemaker"],
            ])],
        [17, 20, Label("Quickshot", Interval("1d20") << [
                [ 1,  3, "Bandit Ratatater!"],
                [ 4,  6, "Dahl Negotiator"],
                [ 7,  9, "Hyperion Synergy"],
                [10, 11, "Jakobs Wheelgun"],
                [12, 13, "Maliwan Umbrage"],
                [14, 16, "Tediore Quickshot"],
                [17, 18, "Torgue Injector"],
                [19, 20, "Vladof Anarchist"],
            ])],
    ],
    WEAPON.MACHINEGUN : Interval("1d20") << [
        [1, 6, Label("Subcompact MG", Interval("1d20") << [
                [ 1,  4, "Bandit smig"],
                [ 5,  8, "Dahl SMG"],
                [ 9, 12, "Hyperion Projectile Convergence"],
                [13, 16, "Maliwan SubMalevolent Grace"],
                [17, 20, "Tediore Subcompact MG"],
            ])],
        [7, 13, Label("Special", Interval("1d20") << [
                [ 1,  4, "Bandit rokgun"],
                [ 5,  8, "Dahl Fox"],
                [ 9, 12, "Hyperion Presence"],
                [13, 16, "Maliwan Trance"],
                [17, 20, "Tediore Special"],
            ])],
        [14, 20, Label("Ace", Interval("1d20") << [
                [ 1,  4, "Bandit smgg"],
                [ 5,  8, "Dahl Falcon"],
                [ 9, 12, "Hyperion Transmurdera"],
                [13, 16, "Maliwan Gospel"],
                [17, 20, "Tediore Ace"],
            ])],
    ],
    WEAPON.ASSAULT : Interval("1d20") << [
        [1, 4, Label("Fusil d’assaut", Interval("1d20") << [
                [ 1,  4, "Bandit Mashine gun"],
                [ 5,  8, "Dahl Rifle"],
                [ 9, 12, "Jakobs Rifle"],
                [13, 16, "Torgue Rifle"],
                [17, 20, "Vladof Rifle"],
            ])],
        [5, 8, Label("Fusil à lunette", Interval("1d20") << [
                [ 1,  4, "Bandit Carbene"],
                [ 5,  8, "Dahl Carbine"],
                [ 9, 12, "Jakobs Scarab"],
                [13, 16, "Torgue Root"],
                [17, 20, "Vladof Renegade"],
            ])],
        [9, 12, Label("Fusil d’assaut lourd", Interval("1d20") << [
                [ 1,  4, "Bandit Ass Beeter!"],
                [ 5,  8, "Dahl Defender"],
                [ 9, 12, "Jakobs Rifle"],
                [13, 16, "Torgue Lance"],
                [17, 20, "Vladof Guerilla"],
            ])],
        [13, 16, Label("Mitrailleuse", Interval("1d20") << [
                [ 1,  4, "Bandit Spinigun"],
                [ 5,  8, "Dahl Minigun"],
                [ 9, 12, "Jakobs Gatling gun"],
                [13, 16, "Torgue Spitter"],
                [17, 20, "Vladof Spinigun"],
            ])],
        [17, 20, Label("Lance-grenades", Interval("1d20") << [
                [ 1,  4, "Bandit Rokets!"],
                [ 5,  8, "Dahl Grenadier"],
                [ 9, 12, "Jakobs"],
                [13, 16, "Torgue Torpedo"],
                [17, 20, "Vlad Rocketeer"],
            ])],
    ],
    WEAPON.SNIPER : Interval("1d20") << [
        [1, 5, Label("Basique", Interval("1d20") << [
                [ 1,  4, "Dahl Sniper"],
                [ 5,  8, "Hyperion Sniper Rifle"],
                [ 9, 12, "Jakobs Callipeen"],
                [13, 16, "Maliwan Snider"],
                [17, 20, "Vladof Pooshka"],
            ])],
        [6, 10, Label("Longue portée", Interval("1d20") << [
                [ 1,  4, "Dahl Strike"],
                [ 5,  8, "Hyperion Transaction"],
                [ 9, 12, "Jakobs Chinook"],
                [13, 16, "Maliwan Jericho"],
                [17, 20, "Vladof Bratchny"],
            ])],
        [11, 15, Label("Perce-armure", Interval("1d20") << [
                [ 1,  4, "Dahl Terror"],
                [ 5,  8, "Hyperion Policy"],
                [ 9, 12, "Jakobs Muckamuck"],
                [13, 16, "Maliwan Corinthian"],
                [17, 20, "Vladof Horrorshow"],
            ])],
        [16, 20, Label("Semi-automatique", Interval("1d20") << [
                [ 1,  4, "Dahl Scoop"],
                [ 5,  8, "Hyperion Competition"],
                [ 9, 12, "Jakobs Diaub"],
                [13, 16, "Maliwan Rakehell"],
                [17, 20, "Vladof Droog"],
            ])],
    ],
    WEAPON.SHOTGUN :Interval("1d20") << [
        [1, 5, Label("Basique", Interval("1d20") << [
                [ 1,  4, "Bandit Skatergun"],
                [ 5,  8, "Hyperion Projectile Diversification"],
                [ 9, 12, "Jakobs Scattergun"],
                [13, 16, "Tediore Home Security"],
                [17, 20, "Torgue Bangstick"],
            ])],
        [6, 10, Label("Précis", Interval("1d20") << [
                [ 1,  4, "Bandit longer ragne kilier"],
                [ 5,  8, "Hyperion Thinking"],
                [ 9, 12, "Jakobs Longrider"],
                [13, 16, "Tediore Sportsman"],
                [17, 20, "Torgue Stalker"],
            ])],
        [11, 15, Label("Double canon", Interval("1d20") << [
                [ 1,  4, "Bandit Stret Sweper"],
                [ 5,  8, "Hyperion Face Time"],
                [ 9, 12, "Jakobs Coach Gun"],
                [13, 16, "Tediore Double Barrels!"],
                [17, 20, "Torgue Double Lovin’ Pounder"],
            ])],
        [16, 20, Label("Triple canon", Interval("1d20") << [
                [ 1,  4, "Bandit Room Clener"],
                [ 5,  8, "Hyperion Crowdsourcing"],
                [ 9, 12, "Jakobs Bushwack"],
                [13, 16, "Tediore Triple Barrels!"],
                [17, 20, "Torgue Three Way Hulk"],
            ])],
    ],
    WEAPON.ROCKET : Interval("1d20") << [
        [1, 5, Label("Basique", Interval("1d20") << [
                [ 1,  4, "Bandit Launcher"],
                [ 5,  8, "Maliwan Projectile"],
                [ 9, 12, "Tediore Launcher"],
                [13, 16, "Torgue boom"],
                [17, 20, "Vladof RPG"],
            ])],
        [6, 10, Label("Basique 2", Interval("1d20") << [
                [ 1,  4, "Bandit bombabarbardeer"],
                [ 5,  8, "Maliwan Prowler"],
                [ 9, 12, "Tediore Dispatch"],
                [13, 16, "Torgue Dee"],
                [17, 20, "Vladof Vanquisher"],
            ])],
        [11, 15, Label("Destructeur", Interval("1d20") << [
                [ 1,  4, "Bandit Zooka!"],
                [ 5,  8, "Maliwan Punishment"],
                [ 9, 12, "Tediore Bazooka"],
                [13, 16, "Torgue Duuurp!"],
                [17, 20, "Vladof Hero"],
            ])],
        [16, 20, Label("Précis", Interval("1d20") << [
                [ 1,  4, "Bandit area effect"],
                [ 5,  8, "Maliwan Panorama"],
                [ 9, 12, "Tediore Spread"],
                [13, 16, "Torgue Blaaa"],
                [17, 20, "Vladof Glory"],
            ])],
    ],
    WEAPON.GRENADE : Interval("1d20") << [
        [ 1,  5, "Standard"],
        [ 6,  8, S("MIRV ", Weight() << [ "Bandit", "Torgue", ])],
        [ 9, 11, "Dahl Bouncing Betty"],
        [12, 14, "Vladof à aire d’effet"],
        [15, 17, "Hyperion Singularity"],
        [18, 20, "Maliwan Transfusion"],
    ],
    WEAPON.SHIELD : Weight() << [
        [2, "Anshin Adaptive"],
        [2, "Bandit Roid"],
        [2, "Dahl Booster"],
        [2, "Hyperion Amplify "],
        [2, "Maliwan Nova "],
        [2, "Maliwan Spike "],
        [2, "Pangolin Turtle "],
        [2, "Tediore Shield "],
        [1, "Torgue Niva "],
        [1, "Torgue Spike "],
        [2, "Vladof Absorption "],
    ],
}
#TODO WeightNode value, with a ComputeTotalWeight as default
#TODO implement nbr_draw in CollectionNode
#TODO Maybe implement Roll in CollectionNode (remove then from SequenceNode)
#TODO Sequence as a Specific case of IntervalNode with roll=0, every interval=0
#TODO Similarly, TabNode maybe a IntervalNode with a custom behavior for default row values
#TODO Implémenter WeighNode.fusion(WeighNode)
#TODO implémenter contre-mesures contre les récursions dans print_node

from macro.grammar import get_ValueIf
def Automaton(nbr_draw, val1:str, val2:str) -> Interval :
    return Interval([(0, get_ValueIf(nbr_draw)), (1, -1)]) << [
        [0, 0, val1],
        [1, 1, val2],
    ]

# Weapon Improvements
improvement = {
    WEAPON.PISTOL : Weight() << [
        [2, Automaton(2,  "Dégâts", "->AP")],
        [2, Automaton(2,  "Portée", "->Visée")],
        [2, Automaton(1, "Capacité du chargeur", "->Mode de Tir")],
        [2, Automaton(2,  "AP", "->Dégâts")],
        [2, S("Dégâts spéciaux : ",
                Weight() << [
                    [4, Automaton(3,     "Corrosifs +1", "->AP")],
                    [4, Automaton(3,     "Electriques +1", "->Dégâts")],
                    [4, Automaton("1d6", "Incendiaires +1", "->AP")],
                    [4, Automaton(1,    "Slaguaires", "->Dégâts")],
                    [3, Automaton(1,    "Explosifs", "->Dégâts")],
                    [1, Automaton(1,    "Arme Lourde", "->Dégâts")],
                ]
            )
        ],
        [2, Automaton(1,  "Stabilité",           "->Portée")],
        [2, Automaton(1,  "Visée",               "->Portée")],
        [2, Automaton(1,  "Mode de tir",         "->Capacité du chargeur")],
        [2, Automaton(1,  "Baïonette",           "->Reroll")],
        [2, Automaton(1,  "Rechargement rapide", "->Mode de tir")],
    ],
    WEAPON.MACHINEGUN : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.ASSAULT : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.SNIPER : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.SHOTGUN : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.ROCKET : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.GRENADE : Weight() << [
        [2, "Dégâts"],
    ],
    WEAPON.SHIELD : Weight() << [
        [2, "Dégâts"],
    ],
}

# <Selector Number="{RANG}+{QUAL}, S(<Row>
#     # TODO : Other weapons
#     # PISTOLS
#     Interval("1d20") << [
#         [ 1,  2, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="2, "Dégats"]</State>
#                 <State Repeat="1, "Relancer Dégats"]</State>
#             </Automaton>

#         [ 3,  4, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="2, "Portée"]</State>
#                 <State Repeat="1, "Relancer Portée"]</State>
#             </Automaton>

#         [ 5,  6, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Capacité du Chargeur"]</State>
#                 <State Repeat="1, "Relancer Capacité"]</State>
#             </Automaton>

#         [ 7,  8, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="2, "AP"]</State>
#                 <State Repeat="1, "Relancer AP"]</State>
#             </Automaton>

#         [ 9, 10, S(
#             "Dégats Spéciaux : ",
#             Interval("1d20") << [
#                 [ 1,  4, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="3, "Corrosifs +1"]</State>
#                         <State Repeat="1, "Relancer Corod"]</State>
#                     </Automaton>

#                 [ 5,  8, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="3, "Electriques +1"]</State>
#                         <State Repeat="1, "Relancer Elec"]</State>
#                     </Automaton>

#                 [ 9, 12, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="1d6, "Incendiaires +1"]</State>
#                         <State Repeat="1, "Relancer Feu"]</State>
#                     </Automaton>

#                 [13, 16, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="1, "Slaguaires"]</State>
#                         <State Repeat="1, "Relancer Slag"]</State>
#                     </Automaton>

#                 [17, 19, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="1, "Explosifs"]</State>
#                         <State Repeat="1, "Relancer Exlpos"]</State>
#                     </Automaton>

#                 [20, 20, S(
#                     <Automaton Behaviour="Stop, S(
#                         <State Repeat="1, "Arme Lourde"]</State>
#                         <State Repeat="1, "Relancer Lourd"]</State>
#                     </Automaton>

#         [11, 12, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Stabilité"]</State>
#                 <State Repeat="1, "Relancer Stab"]</State>
#             </Automaton>

#         [13, 14, S(
#             "",
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Visée"]</State>
#                 <State Repeat="1, "Relancer Visée"]</State>
#             </Automaton>

#         [15, 16, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Mode de Tir"]</State>
#                 <State Repeat="1, "Relancer Mode"]</State>
#             </Automaton>

#         [17, 18, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Baïonette"]</State>
#                 <State Repeat="1, "Relancer Baïonette"]</State>
#             </Automaton>

#         [19, 20, S(
#             <Automaton Behaviour="Stop, S(
#                 <State Repeat="1, "Rechargement Rapide"]</State>
#                 <State Repeat="1, "Relancer Rechargement"]</State>
#             </Automaton>

# test = TabNode(lambda : WEAPON_TYPE) << list(weapon.values())
# print(test.value.value)

generation = Generator(S(
    sel_weapon,
    sel_quality,
    Title("Arme",
          TabNode(lambda : WEAPON_TYPE) << list(weapon.values())
    ),
    Title("Ameliorations",
        SequenceNode(lambda : RANG + QUALITY, "\n") << [
            TabNode(lambda : WEAPON_TYPE) << list(improvement.values())
        ]
    ),
    # Title("Améliorations", None),
))

if __name__ == "__main__" :
    generation.execute()
    generation.print_to_console()