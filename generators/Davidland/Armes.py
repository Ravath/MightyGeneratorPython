# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import PrintNode as Print
from wordgenerator.Print import PrintToBuffer, ActionNode, Title, Label

Print._printer = PrintToBuffer()

#################################################
#              INIT PROBABILITIES               #
#################################################

CHEST_TYPE = "COMMUN"
print(globals()["CHEST_TYPE"])

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
class SetType(ActionNode) :
    def __init__(self, type_name:str) :
        self.type_name = type_name
        def SetWeaponType() :
            global WEAPON_TYPE
            WEAPON_TYPE = self.type_name
        ActionNode.__init__(self, SetWeaponType)
class SetRarity(ActionNode) :
    def __init__(self, rarity_name:str) :
        self.rarity_name = rarity_name
        def SetWeaponRarity() :
            global WEAPON_RARITY
            WEAPON_RARITY = self.rarity_name
        ActionNode.__init__(self, SetWeaponRarity)

sel_rarity = Weight().extend([
    [ODD_PIS, SetType("PISTOLET")],
    [ODD_FAS, SetType("ASSAUT")],
    [ODD_MIT, SetType("MITRAILLETTE")],
    [ODD_FPO, SetType("POMPE")],
    [ODD_FSN, SetType("SNIPER")],
    [ODD_GRE, SetType("GRENADE")],
    [ODD_BOU, SetType("BOUCLIER")],
])

sel_type = Weight().extend([
    [ODD_COM,   SetRarity("COMMUN")],
    [ODD_UNCOM, SetRarity("INCOMMUN")],
    [ODD_RAR,   SetRarity("RARE")],
    [ODD_EPIC,  SetRarity("EPIQUE")],
    [ODD_ETECH, SetRarity("ETECH")],
    [ODD_LEG,   SetRarity("LEGENDAIRE")],
])

#################################################
#                NAME GENERATION                #
#################################################

nom_arme = Sequence().extend([
    Weight().extend([
        ["Dévastateur"],
        ["Dézingueur"],
        ["Mitrailleur"],
        ["Ferrailleur"],
        ["Bousilleur"],
        ["Juge"],
        ["Regret"],
        ["Omelette"],
        ["Fléau"],
        ["Tonnerre"],
        ["Envahisseur"],
        ["Épineur"],
        ["Commercial"],
        ["Déception"],
        ["Levier"],
        ["Boucher"],
        ["Interfaceur"],
        ["Retrait automatique"],
        ["Briseur de coeurs"],
        ["Eparpilleur"],
        ["Tigre"],
        ["Pacifieur"],
        ["Empereur"],
        ["Psycho"],
        ["Clerc"],
        ["Mage"],
        ["Survivant"],
        ["Nettoyeur"],
        ["Tourment"],
        ["Renifleur"],
        ["Baiser"],
        ["Ninja"],
        ["Guerrier"],
        ["Lance"],
        ["Atomiseur"],
        ["Papy"],
        ["Appareil"],
        ["Employé"],
        ["Éclaireur"],
    ]),
    Weight().extend([
        ["de mamans"],
        [" impitoyable"],
        [" motorisé"],
        [" incroyable"],
        [" automatique"],
        [" acide"],
        [" ridicule"],
        [" soufflé"],
        [" sans effort"],
        [" dévastateur"],
        [" risqué"],
        [" tout rouge"],
        [" rabouin"],
        [" gicleur"],
        [" de pastèques"],
        [" camouflé"],
        [" du fromage"],
        [" vegan"],
        [" rebelle"],
        [" riche"],
        ["-robot"],
        ["-pangolin"],
        [" tueur de veuves"],
        [" sanguinaire"],
        [" dégueulasse"],
        [" des familles"],
        [" épineux"],
        [" obsolète"],
        ["-gobelin"],
        [" mou"],
        [" dur"],
        [" barbare"],
        [" du cul"],
        [" silencieux"],
        [" ronronnant"],
        [" qui tache"],
        [" sale"],
        [" de qualité"],
        [" chromé"],
        [" tactique"],
        [" canon"],
        [" glorieux"],
    ]),
    "\n"
])

nom_grenade = Sequence().extend([
    Weight().extend([
        ["Caillou"],
        ["Etoile du matin"],
        ["Samourai"],
        ["Barbecue"],
        ["Ogive"],
        ["Petit nuage"],
        ["Pulsar"],
        ["Missile"],
        ["Objet volant"],
        ["Corbeau"],
        ["Drone"],
        ["Petit boîtier"],
        ["Le petit Hansel"],
        ["Tartine"],
        ["Bouboule"],
        ["Coucou"],
        ["Psychologue"],
        ["Dahl"],
        ["Renégat"],
        ["Poutiflette"],
        ["Citron"],
        ["Attaché-case"],
        ["Tequila"],
        ["Rencard"],
        ["Cassoulet"],
        ["Beuglard"],
        ["Racaille"],
        ["Bagel"],
        ["Taco"],
        ["Patate"],
    ]),
    Weight().extend([
        [" dévastateur"],
        ["-bombe"],
        ["-tomate ketchup"],
        [" magique"],
        [" faiseur de paix durable"],
        [" totalement identifié"],
        [" grillé"],
        [" givré"],
        [" surprise"],
        [" téléguidé"],
        [" anu-ciblé"],
        [" instable"],
        [" cubiste"],
        [" moderne"],
        [" amical"],
        [" amer"],
        [" rouillé"],
        [" enrichi au Polonium"],
        [" à goupille"],
        [" sexy"],
        [" incandescent"],
        [" sans lactose"],
        [" OGM"],
        [" non désiré"],
        [" largué"],
        [" aux lentilles"],
        [" oppressif"],
        [" virulent"],
        [" couinant"],
        [" aux saucisses fumées"],
        [" explosif"],
        [" nihiliste"],
        [" à ressorts"],
        [" concentré"],
        [" salsa pimenté"],
        [" plasmatique"],
    ]),
    "\n"
])

nom_bouclier = Sequence().extend([
    Weight().extend([
        ["Gardien"],
        ["Policier"],
        ["Mur"],
        ["Miroir"],
        ["Éléphant"],
        ["Rhino"],
        ["Toubib"],
        ["Tank"],
        ["Bobine"],
        ["Grosse épine"],
        ["Whisky"],
        ["Bouteille"],
        ["Scarabée"],
        ["Baron"],
        ["Ornithorynque"],
        ["N3RD"],
        ["Concentrateur"],
        ["Casserole"],
        ["Cassolette"],
        ["Petit copain"],
        ["Soucoupe"],
        ["Lampadaire"],
        ["Placoplâtre"],
        ["Taco"],
        ["Grosse caisse"],
        ["Fagot"],
        ["Lentille"],
        ["Protecteur"],
        ["Gentil garçon"],
        ["Tuk-tuk"],
        ["Impôt"],
        ["Grand sorcier"],
    ]),
    Weight().extend([
        [" de la trève passagère"],
        ["-pangolin"],
        [" agent de la paix avant tout"],
        [" loyal"],
        [" anti-baffes"],
        [" affûté"],
        [" lumineux"],
        [" arriviste"],
        [" manichéen"],
        [" strict"],
        ["-pharyngite"],
        [" tissé"],
        [" protecteur"],
        [" electromagnétique"],
        [" riant"],
        [" stoïque"],
        [" professionnel"],
        [" coriace"],
        [" de fonction"],
        [" à ressorts assortis"],
        [" invisible"],
        [" gênant"],
        [" à vapeur"],
        [" vexatoire"],
        [" blindé"],
        [" troué"],
        [" de mamie"],
        [" à répulsif"],
        [" métallique"],
        [" en aluminium premium"],
        [" vitrifié"],
        [" religieux"],
        [" spirituel"],
        [" arcanique"],
        [" occultant"],
        [" de mauvaise facture"],
    ]),
    "\n"
])

#################################################
#              ELEMENT GENERATION               #
#################################################

sel_element = Sequence().extend([
    " - Effet élémentaire: ",
    Weight().extend([
        "incendiaire",
        "électrique",
        "slag",
        "corrosif",
        "radiation",
        "cryogénique",
    ]),
    "\n"
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
    global nom_arme
    return Title(weapon_name, Sequence().extend([
        nom_arme,
        Label("Dégats",              weapon_damage),
        Label("Difficulté de visée", weapon_aim),
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
    "Pistolet Légendaire", pistol_damage,
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
    "Fusil d'assaut Légendaire", rifle_damage,
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
    "Mitraillette Légendaire", machinegun_damage,
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
    "Fusil à pompe Commun", pompe_damage,
    "[[6-1d7]]", "[[1d3]]",
    pompe_modes,
)
weapon_generation["POMPE"]["INCOMMUN"] = GetWeaponBuilder(
    "Fusil à pompe Peu Commun", pompe_damage,
    "[[6-1d7]]", "[[1d3+1]]",
    pompe_modes,
)
weapon_generation["POMPE"]["RARE"] = GetWeaponBuilder(
    "Fusil à pompe Rare", pompe_damage,
    "[[5-1d7]]", "[[1d3+1]]",
    pompe_modes,
)
weapon_generation["POMPE"]["EPIQUE"] = GetWeaponBuilder(
    "Fusil à pompe Epique", pompe_damage,
    "[[5-1d7]]", "[[1d3+2]]",
    pompe_modes,
)
weapon_generation["POMPE"]["ETECH"] = GetWeaponBuilder(
    "Fusil à pompe E-Tech", pompe_damage,
    "[[4-1d7]]", "[[1d3+2]]",
    pompe_modes,
)
weapon_generation["POMPE"]["LEGENDAIRE"] = GetWeaponBuilder(
    "Fusil à pompe Légendaire", pompe_damage,
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
    "Sniper Légendaire", sniper_damage,
    "[[1-1d4]]", "[[1d4+3]]",
    sniper_modes,
)

############# GRENADE

def GetGrenadeBuilder(weapon_name:str,
                     weapon_damage,
                     weapon_aim:str,
                     weapon_modes) :
    global nom_arme
    return Title(weapon_name, Sequence().extend([
        nom_grenade,
        Label("Dégats",              weapon_damage),
        Label("Difficulté de visée", weapon_aim),
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
    "Grenade Légendaire", grenade_damage,
    "[[3-1d5]]",
    grenade_modes,
)

############# SHIELD

# TODO resolve this roll at runtime ?
shield_intensity = "[[1d11+6]]"

def GetShieldBuilder(shield_name:str) :
    return Title(shield_name, Sequence().extend([
        nom_bouclier,
        Label("Capacité", f"[[0-3*{shield_intensity}+84]]+[[1d7]]"),
        Label("Cadence",  f"[[1d5+{shield_intensity}]]"),
    ]))

weapon_generation["SHIELD"] = {}
weapon_generation["SHIELD"]["COMMUN"] = GetShieldBuilder(
    "Bouclier Commun",
)
weapon_generation["SHIELD"]["INCOMMUN"] = GetShieldBuilder(
    "Bouclier Peu Commun",
)
weapon_generation["SHIELD"]["RARE"] = GetShieldBuilder(
    "Bouclier Rare",
)
weapon_generation["SHIELD"]["EPIQUE"] = GetShieldBuilder(
    "Bouclier Epique",
)
weapon_generation["SHIELD"]["ETECH"] = GetShieldBuilder(
    "Bouclier E-Tech",
)
weapon_generation["SHIELD"]["LEGENDAIRE"] = GetShieldBuilder(
    "Bouclier Légendaire",
)

print(Print._printer.get_text())
