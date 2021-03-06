# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Print import PrintNode as Print
from wordgenerator.Print import PrintToBuffer, SetNode, Title, Label
from ponderation import pond_type, pond_fabriquant, pond_element, can_element
from ponderation import nbr_of_constructor_properties
from capacite import arme_spe, grenade_spe, bouclier_spe
from nom import nom_arme, nom_grenade, nom_bouclier

Print._printer = PrintToBuffer()

#################################################
#              INIT PROBABILITIES               #
#################################################

CHEST_TYPE = "COMMUN"

if CHEST_TYPE == "COMMUN" :
    ODD_COM = 50
    ODD_UNCOM = 30
    ODD_RAR = 10
    ODD_EPIC = 6
    ODD_ETECH = 3
    ODD_LEG = 1
elif CHEST_TYPE == "RARE" :
    ODD_COM = 26
    ODD_UNCOM = 40
    ODD_RAR = 18
    ODD_EPIC = 9
    ODD_ETECH = 5
    ODD_LEG = 2
elif CHEST_TYPE == "LEGENDAIRE" :
    ODD_COM = 0
    ODD_UNCOM = 0
    ODD_RAR = 0
    ODD_EPIC = 0
    ODD_ETECH = 10
    ODD_LEG = 10

ODD_PIS = 1
ODD_FAS = 1
ODD_MIT = 1
ODD_FPO = 1
ODD_FSN = 1
ODD_GRE = 1
ODD_BOU = 1

#################################################
#            SELECT TYPE AND RARITY             #
#################################################

WEAPON_TYPE = "PISTOLET"
WEAPON_RARITY = "COMMUN"

def SetWeaponType(weapon_type) :
    # update the flag
    global WEAPON_TYPE
    WEAPON_TYPE = weapon_type

    # update the ponderations
    for v in pond_type.values() :
        v.value = 0
    pond_type[weapon_type].value = 1

def SetWeaponRarity(weapon_rarity) :
    # update the flag
    global WEAPON_RARITY
    WEAPON_RARITY = weapon_rarity

def SetWeaponConstructor(weapon_constructor) :
    # update the ponderations
    global pond_fabriquant
    for v in pond_fabriquant.values() :
        v.value = 0
    pond_fabriquant[weapon_constructor].value = 1

def SetWeaponElement(weapon_element) :
    # update the ponderations
    for v in pond_element.values() :
        v.value = 0
    pond_element[weapon_element].value = 1


sel_type = Weight().extend([
    [ODD_PIS, SetNode(SetWeaponType, "PISTOLET")],
    [ODD_FAS, SetNode(SetWeaponType, "ASSAUT")],
    [ODD_MIT, SetNode(SetWeaponType, "MITRAILLETTE")],
    [ODD_FPO, SetNode(SetWeaponType, "POMPE")],
    [ODD_FSN, SetNode(SetWeaponType, "SNIPER")],
    [ODD_GRE, SetNode(SetWeaponType, "GRENADE")],
    [ODD_BOU, SetNode(SetWeaponType, "BOUCLIER")],
])

sel_rarity = Weight().extend([
    [ODD_COM,   SetNode(SetWeaponRarity, "COMMUN")],
    [ODD_UNCOM, SetNode(SetWeaponRarity, "INCOMMUN")],
    [ODD_RAR,   SetNode(SetWeaponRarity, "RARE")],
    [ODD_EPIC,  SetNode(SetWeaponRarity, "EPIQUE")],
    [ODD_ETECH, SetNode(SetWeaponRarity, "ETECH")],
    [ODD_LEG,   SetNode(SetWeaponRarity, "LEGENDAIRE")],
])

#################################################
#               SELECT CONSTRUCTOR              #
#################################################

sel_fabriquant = {"" : {"" : Sequence() }}
sel_fabriquant .clear()

sel_fabriquant["PISTOLET"] = {}
sel_fabriquant["PISTOLET"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Maliwan"),
    SetNode(SetWeaponConstructor, "Jakobs"),
    SetNode(SetWeaponConstructor, "Hyperion"),
    SetNode(SetWeaponConstructor, "Dahl"),
    SetNode(SetWeaponConstructor, "Vladof"),
    SetNode(SetWeaponConstructor, "Bandit"),
    SetNode(SetWeaponConstructor, "Tediore"),
    SetNode(SetWeaponConstructor, "Torgue"),
])
    
sel_fabriquant["MITRAILLETTE"] = {}
sel_fabriquant["MITRAILLETTE"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Maliwan"),
    SetNode(SetWeaponConstructor, "Hyperion"),
    SetNode(SetWeaponConstructor, "Dahl"),
    SetNode(SetWeaponConstructor, "Bandit"),
    SetNode(SetWeaponConstructor, "Tediore"),
])
    
sel_fabriquant["ASSAUT"  ] = {}
sel_fabriquant["ASSAUT"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Jakobs"),
    SetNode(SetWeaponConstructor, "Dahl"),
    SetNode(SetWeaponConstructor, "Bandit"),
    SetNode(SetWeaponConstructor, "Torgue"),
])
    
sel_fabriquant["POMPE"] = {}
sel_fabriquant["POMPE"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Jakobs"),
    SetNode(SetWeaponConstructor, "Hyperion"),
    SetNode(SetWeaponConstructor, "Bandit"),
    SetNode(SetWeaponConstructor, "Tediore"),
    SetNode(SetWeaponConstructor, "Torgue"),
])
    
sel_fabriquant["SNIPER"  ] = {}
sel_fabriquant["SNIPER"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Maliwan"),
    SetNode(SetWeaponConstructor, "Jakobs"),
    SetNode(SetWeaponConstructor, "Hyperion"),
    SetNode(SetWeaponConstructor, "Vladof"),
])

sel_fabriquant["GRENADE"] = {}
sel_fabriquant["GRENADE"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Classic"),
    SetNode(SetWeaponConstructor, "Contact"),
    SetNode(SetWeaponConstructor, "Proximity"),
    SetNode(SetWeaponConstructor, "MIRV"),
    SetNode(SetWeaponConstructor, "Singularity"),
    SetNode(SetWeaponConstructor, "Tesla"),
    SetNode(SetWeaponConstructor, "Transfusion"),
    SetNode(SetWeaponConstructor, "Betty"),
])

sel_fabriquant["BOUCLIER"] = {}
sel_fabriquant["BOUCLIER"] = Weight().extend([
    SetNode(SetWeaponConstructor, "Absorb"),
    SetNode(SetWeaponConstructor, "Adaptive"),
    SetNode(SetWeaponConstructor, "Amplify"),
    SetNode(SetWeaponConstructor, "Booster"),
    SetNode(SetWeaponConstructor, "Lifeline"),
    SetNode(SetWeaponConstructor, "Nova"),
    SetNode(SetWeaponConstructor, "Raid"),
    SetNode(SetWeaponConstructor, "Shield"),
    SetNode(SetWeaponConstructor, "Spike"),
    SetNode(SetWeaponConstructor, "Turtle"),
])

#################################################
#              ELEMENT GENERATION               #
#################################################

sel_element = Sequence().extend([
    " - Effet ??l??mentaire: ",
    Weight().extend([
        Sequence().extend(["incendiaire", SetNode(SetWeaponElement, "FEU")]),
        Sequence().extend(["??lectrique" , SetNode(SetWeaponElement, "ELEC")]),
        Sequence().extend(["slag"       , SetNode(SetWeaponElement, "SLAG")]),
        Sequence().extend(["corrosif"   , SetNode(SetWeaponElement, "COR")]),
        Sequence().extend(["radiation"  , SetNode(SetWeaponElement, "RAD")]),
        Sequence().extend(["cryog??nique", SetNode(SetWeaponElement, "CRYO")]),
    ]),
    "\n"
])

def inhibit_element() :
    can_element.value = 0
def pretirage_one() :
    nbr_of_constructor_properties.value = 1

spe_fabriquant = Interval(1).extend([
    # update ponderation to :
    # - inhibit elementary weapon if needed
    # - make the constructor capacity count as a regular one
    [0, pond_fabriquant["Maliwan"], inhibit_element],
    [0, pond_fabriquant["Maliwan"], pretirage_one],
    [0, pond_fabriquant["Torgue"],  inhibit_element],
    [0, pond_fabriquant["Nova"],    pretirage_one],
    [0, pond_fabriquant["Spike"],   pretirage_one],
    [0, pond_fabriquant["Tesla"],   inhibit_element],
    [0, pond_fabriquant["Tesla"],   pretirage_one],
    # resolve the constructor specific capacity
    # FUSILS
    [0, pond_fabriquant["Bandit"], "*Chargeur X2*\n"],
    [0, pond_fabriquant["Dahl"], "*Mode Rafale et Automatique: possibilit?? d'alterner 2 cartes successives d'un tir*\n"],
    [0, pond_fabriquant["Hyperion"], "*Bouclier d'??nergie avec [[1d20+10]]PV*\n"],
    [0, pond_fabriquant["Jakobs"], "*Tir ricochant si critique*\n"],
    [0, pond_fabriquant["Maliwan"], sel_element],
    [0, pond_fabriquant["Tediore"], "*Lancer l'arme pour recharger, d??g??ts similaire ?? une balle en zone*\n"],
    [0, pond_fabriquant["Torgue"], "*Arme Explosive*\n"],
    [0, pond_fabriquant["Vladof"], "*+1 Augmentation de d??, +1 D??g??ts, +1 Difficult?? de vis??e, +1 Magasin*\n"],
    # GRENADES
    [0, pond_fabriquant["Classic"], "*Grosse Explosion 5x5*\n"],
    [0, pond_fabriquant["Contact"], "*Explosion sur contact 3x3*\n"],
    [0, pond_fabriquant["Proximity"], "*Mine, explosion 3x3 si d??placement alentour*\n"],
    [0, pond_fabriquant["MIRV"], "*Explose 3x3, puis lance [[1d5+3]] mini grenades qui explosent 3x3 autour de l'explosion initiale le tour suivant*\n"],
    [0, pond_fabriquant["Singularity"], "*Attire les ennemis autour de la grenade 3x3 et explose 3x3*\n"],
    [0, pond_fabriquant["Tesla"], "*Explose 3x3 et laisse une tra??n??e ??l??mentaire pendant 2 tours*\n"],
    [0, pond_fabriquant["Transfusion"], "*Explosion 3x3, soigne le lanceur des d??g??ts inflig??s apr??s 1 tour*\n"],
    [0, pond_fabriquant["Betty"], "*Rebondit jusqu'?? toucher un ennemi, explosion 3x3*\n"],
    # BOUCLIERS
    [0, pond_fabriquant["Absorb"], "*Si l'arme utilis??e contre vous est la m??me que celle que vous utilisez, gagne (+1 Aug d??g??ts) ?? chaque tir re??u pour votre prochain tour*\n"],
    [0, pond_fabriquant["Adaptive"], "*D??g??ts/2 au 1er tir du dernier ??l??ment qui vous a touch??*\n"],
    [0, pond_fabriquant["Amplify"], "*Une fois totalement charg??, le bouclier ajoute [[1d10]] d??g??ts ?? la prochaine attaque et diminue les PVs du bouclier d'autant*\n"],
    [0, pond_fabriquant["Booster"], "*Une fois touch??, balance une unit?? de rechargement de bouclier ?? [[1d20]] PV*\n"],
    [0, pond_fabriquant["Lifeline"], "*Vie max +[[1d20+10]], Bouclier -[[1d20]]*\n"],
    [0, pond_fabriquant["Nova"], "*Une fois vid??, le bouclier g??n??re une nova ??l??mentaire faisant [[1d20]] d??g??ts autour de vous + effet ??l??mentaire*\n"],
    [0, pond_fabriquant["Raid"], "*Une fois vid??, ajoute un bonus de [[1d20]] d??g??ts ?? vos attaques de corps (une fois par tour)*\n"],
    [0, pond_fabriquant["Shield"], "*Cadence de rechargement +10, Capacit?? -15*\n"],
    [0, pond_fabriquant["Spike"], "*Si attaque subie ?? courte distance, inflige [[1d10]] d??g??ts ??l??mentaires ?? l'attaquant*\n"],
    [0, pond_fabriquant["Turtle"], "*Bouclier +[[1d20+10]] PV, Vie max -[[1d20]]*\n"],
])

#################################################
#               WEAPON GENERATION               #
#################################################

weapon_generation = {"" : {"" : Sequence() }}
weapon_generation .clear()

def GetWeaponBuilder(weapon_name:str,
                     weapon_damage,
                     weapon_aim:str,
                     weapon_magazin:str,
                     weapon_modes) :
    return Title(weapon_name, Sequence().extend([
        nom_arme,
        Label("D??gats",              weapon_damage),
        Label("Difficult?? de vis??e", weapon_aim),
        Label("Magasin",             weapon_magazin),
        weapon_modes,
    ]))

############# PISTOL

pistol_damage = Weight().extend([
    [25, "1D4 + [[1d5+5]]"],
    [50, "1D6 + [[1d5+4]]"],
    [25, "1D8 + [[1d5+3]]"],
])
pistol_modes = Weight(2, False).extend([
    [" - Tir Simple\n"],
    [" - Tir Rafale\n"],
    [" - Tir Automatique\n"],
])
# TODO check it works (execution and printing) after weighNode fully implemented

weapon_generation["PISTOLET"] = {}
weapon_generation["PISTOLET"]["COMMUN"] = GetWeaponBuilder(
    "Pistolet Commun", pistol_damage,
    "[[3-1d5]]", "[[1d5+3]]",
    pistol_modes,
)
weapon_generation["PISTOLET"]["INCOMMUN"] = GetWeaponBuilder(
    "Pistolet Peu Commun", pistol_damage,
    "[[3-1d5]]", "[[1d5+4]]",
    pistol_modes,
)
weapon_generation["PISTOLET"]["RARE"] = GetWeaponBuilder(
    "Pistolet Rare", pistol_damage,
    "[[2-1d4]]", "[[1d5+4]]",
    pistol_modes,
)
weapon_generation["PISTOLET"]["EPIQUE"] = GetWeaponBuilder(
    "Pistolet Epique", pistol_damage,
    "[[2-1d4]]", "[[1d5+5]]",
    pistol_modes,
)
weapon_generation["PISTOLET"]["ETECH"] = GetWeaponBuilder(
    "Pistolet E-Tech", pistol_damage,
    "[[1-1d4]]", "[[1d5+5]]",
    pistol_modes,
)
weapon_generation["PISTOLET"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Pistolet L??gendaire", pistol_damage,
    "[[1-1d4]]", "[[1d5+6]]",
    pistol_modes,
)

############# RIFLE

rifle_damage = Weight().extend([
    [15, "1D4 + [[1d7+9]]"],
    [30, "1D6 + [[1d7+8]]"],
    [40, "1D8 + [[1d7+6]]"],
    [15, "1D10 + [[1d7+5]]"],
])
rifle_modes = pistol_modes

weapon_generation["ASSAUT"] = {}
weapon_generation["ASSAUT"]["COMMUN"] = GetWeaponBuilder(
    "Fusil d'assaut Commun", rifle_damage,
    "[[4-1d7]]", "[[1d5+6]]",
    rifle_modes,
)
weapon_generation["ASSAUT"]["INCOMMUN"] = GetWeaponBuilder(
    "Fusil d'assaut Peu Commun", rifle_damage,
    "[[4-1d7]]", "[[1d5+8]]",
    rifle_modes,
)
weapon_generation["ASSAUT"]["RARE"] = GetWeaponBuilder(
    "Fusil d'assaut Rare", rifle_damage,
    "[[3-1d6]]", "[[1d5+8]]",
    rifle_modes,
)
weapon_generation["ASSAUT"]["EPIQUE"] = GetWeaponBuilder(
    "Fusil d'assaut Epique", rifle_damage,
    "[[3-1d6]]", "[[1d5+10]]",
    rifle_modes,
)
weapon_generation["ASSAUT"]["ETECH"] = GetWeaponBuilder(
    "Fusil d'assaut E-Tech", rifle_damage,
    "[[3-1d5]]", "[[1d5+10]]",
    rifle_modes,
)
weapon_generation["ASSAUT"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Fusil d'assaut L??gendaire", rifle_damage,
    "[[3-1d5]]", "[[1d5+12]]",
    rifle_modes,
)

############# SUB-MACHINEGUN

machinegun_damage = Weight().extend([
    [20, "1D8 + [[1d7]]"],
    [40, "1D10 + [[1d7-1]]"],
    [40, "1D12 + [[1d7-2]]"],
])
machinegun_modes = Sequence().extend([
    " - Tir Simple\n",
    " - Tir Rafale\n",
    " - Tir Automatique\n"
])

weapon_generation["MITRAILLETTE"] = {}
weapon_generation["MITRAILLETTE"]["COMMUN"] = GetWeaponBuilder(
    "Mitraillette Commune", machinegun_damage,
    "[[4-1d7]]", "[[1d7+9]]",
    machinegun_modes,
)
weapon_generation["MITRAILLETTE"]["INCOMMUN"] = GetWeaponBuilder(
    "Mitraillette Peu Commune", machinegun_damage,
    "[[4-1d7]]", "[[1d7+11]]",
    machinegun_modes,
)
weapon_generation["MITRAILLETTE"]["RARE"] = GetWeaponBuilder(
    "Mitraillette Rare", machinegun_damage,
    "[[3-1d6]]", "[[1d7+11]]",
    machinegun_modes,
)
weapon_generation["MITRAILLETTE"]["EPIQUE"] = GetWeaponBuilder(
    "Mitraillette Epique", machinegun_damage,
    "[[3-1d6]]", "[[1d7+13]]",
    machinegun_modes,
)
weapon_generation["MITRAILLETTE"]["ETECH"] = GetWeaponBuilder(
    "Mitraillette E-Tech", machinegun_damage,
    "[[3-1d5]]", "[[1d7+13]]",
    machinegun_modes,
)
weapon_generation["MITRAILLETTE"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Mitraillette L??gendaire", machinegun_damage,
    "[[3-1d5]]", "[[1d7+15]]",
    machinegun_modes,
)

############# SHOTGUN

pompe_damage = Weight().extend([
    [10, "2D8 + [[1d9+14]]"],
    [40, "2D10 + [[1d9+12]]"],
    [40, "2D12 + [[1d9+10]]"],
    [10, "2D20 + [[1d9+2]]"],
])
pompe_modes = " - Tir Simple\n"

weapon_generation["POMPE"] = {}
weapon_generation["POMPE"]["COMMUN"] = GetWeaponBuilder(
    "Fusil ?? pompe Commun", pompe_damage,
    "[[6-1d7]]", "[[1d3]]",
    pompe_modes,
)
weapon_generation["POMPE"]["INCOMMUN"] = GetWeaponBuilder(
    "Fusil ?? pompe Peu Commun", pompe_damage,
    "[[6-1d7]]", "[[1d3+1]]",
    pompe_modes,
)
weapon_generation["POMPE"]["RARE"] = GetWeaponBuilder(
    "Fusil ?? pompe Rare", pompe_damage,
    "[[5-1d7]]", "[[1d3+1]]",
    pompe_modes,
)
weapon_generation["POMPE"]["EPIQUE"] = GetWeaponBuilder(
    "Fusil ?? pompe Epique", pompe_damage,
    "[[5-1d7]]", "[[1d3+2]]",
    pompe_modes,
)
weapon_generation["POMPE"]["ETECH"] = GetWeaponBuilder(
    "Fusil ?? pompe E-Tech", pompe_damage,
    "[[4-1d7]]", "[[1d3+2]]",
    pompe_modes,
)
weapon_generation["POMPE"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Fusil ?? pompe L??gendaire", pompe_damage,
    "[[4-1d7]]", "[[1d3+3]]",
    pompe_modes,
)

############# SNIPER

sniper_damage = Weight().extend([
    [60, "1D4 + [[1d7+35]]"],
    [25, "1D6 + [[1d7+34]]"],
    [15, "1D8 + [[1d7+33]]"],
])
sniper_modes = " - Tir Simple\n"

weapon_generation["SNIPER"] = {}
weapon_generation["SNIPER"]["COMMUN"] = GetWeaponBuilder(
    "Sniper Commun", sniper_damage,
    "[[3-1d5]]", "[[1d4]]",
    sniper_modes,
)
weapon_generation["SNIPER"]["INCOMMUN"] = GetWeaponBuilder(
    "Sniper Peu Commun", sniper_damage,
    "[[3-1d5]]", "[[1d4+1]]",
    sniper_modes,
)
weapon_generation["SNIPER"]["RARE"] = GetWeaponBuilder(
    "Sniper Rare", sniper_damage,
    "[[2-1d4]]", "[[1d4+1]]",
    sniper_modes,
)
weapon_generation["SNIPER"]["EPIQUE"] = GetWeaponBuilder(
    "Sniper Epique", sniper_damage,
    "[[2-1d4]]", "[[1d4+2]]",
    sniper_modes,
)
weapon_generation["SNIPER"]["ETECH"] = GetWeaponBuilder(
    "Sniper E-Tech", sniper_damage,
    "[[1-1d4]]", "[[1d4+2]]",
    sniper_modes,
)
weapon_generation["SNIPER"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Sniper L??gendaire", sniper_damage,
    "[[1-1d4]]", "[[1d4+3]]",
    sniper_modes,
)

############# GRENADE

def GetGrenadeBuilder(weapon_name:str,
                     weapon_damage,
                     weapon_aim:str,
                     weapon_modes) :
    return Title(weapon_name, Sequence().extend([
        nom_grenade,
        Label("D??gats",              weapon_damage),
        Label("Difficult?? de vis??e", weapon_aim),
        weapon_modes,
    ]))

grenade_damage = Print("2D20 + [[1d11+23]]")
grenade_modes = " - Tir Simple\n"

weapon_generation["GRENADE"] = {}
weapon_generation["GRENADE"]["COMMUN"] = GetGrenadeBuilder(
    "Grenade Commune", grenade_damage,
    "[[4-1d7]]",
    grenade_modes,
)
weapon_generation["GRENADE"]["INCOMMUN"] = GetGrenadeBuilder(
    "Grenade Peu Commune", grenade_damage,
    "[[4-1d7]]",
    grenade_modes,
)
weapon_generation["GRENADE"]["RARE"] = GetGrenadeBuilder(
    "Grenade Rare", grenade_damage,
    "[[3-1d6]]",
    grenade_modes,
)
weapon_generation["GRENADE"]["EPIQUE"] = GetGrenadeBuilder(
    "Grenade Epique", grenade_damage,
    "[[3-1d6]]",
    grenade_modes,
)
weapon_generation["GRENADE"]["ETECH"] = GetGrenadeBuilder(
    "Grenade E-Tech", grenade_damage,
    "[[3-1d5]]",
    grenade_modes,
)
weapon_generation["GRENADE"]["LEGENDAIRE"] = GetGrenadeBuilder(
    "Grenade L??gendaire", grenade_damage,
    "[[3-1d5]]",
    grenade_modes,
)

############# SHIELD

# TODO resolve this roll at runtime ?
shield_intensity = "[[1d11+6]]"

def GetShieldBuilder(shield_name:str) :
    return Title(shield_name, Sequence().extend([
        nom_bouclier,
        Label("Capacit??", f"[[0-3*{shield_intensity}+84]]+[[1d7]]"),
        Label("Cadence",  f"[[1d5+{shield_intensity}]]"),
    ]))

weapon_generation["BOUCLIER"] = {}
weapon_generation["BOUCLIER"]["COMMUN"] = GetShieldBuilder(
    "Bouclier Commun",
)
weapon_generation["BOUCLIER"]["INCOMMUN"] = GetShieldBuilder(
    "Bouclier Peu Commun",
)
weapon_generation["BOUCLIER"]["RARE"] = GetShieldBuilder(
    "Bouclier Rare",
)
weapon_generation["BOUCLIER"]["EPIQUE"] = GetShieldBuilder(
    "Bouclier Epique",
)
weapon_generation["BOUCLIER"]["ETECH"] = GetShieldBuilder(
    "Bouclier E-Tech",
)
weapon_generation["BOUCLIER"]["LEGENDAIRE"] = GetShieldBuilder(
    "Bouclier L??gendaire",
)

#################################################
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

generation = Sequence().extend([
    sel_type,
    sel_rarity,
    DictionaryNode(weapon_generation, "WEAPON_TYPE", "WEAPON_RARITY"),
    DictionaryNode(sel_fabriquant, "WEAPON_TYPE"), # nothing to display for constructor yet
    Title("Propri??t??s", Sequence().extend([
        spe_fabriquant,
        DictionaryNode(arme_spe, "WEAPON_RARITY"),
        DictionaryNode(grenade_spe, "WEAPON_RARITY"),
        DictionaryNode(bouclier_spe, "WEAPON_RARITY"),
    ])),
])

generation.execute()
print("Coffre :", globals()["CHEST_TYPE"])
print("Arme   :", WEAPON_TYPE)
print("Raret?? :", WEAPON_RARITY)

print()
print(Print._printer.get_text())
