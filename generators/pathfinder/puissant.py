# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import Title
from macro.dice import Pool, PoolSum

d100 = PoolSum(Pool(1,100))

def DoubleRelance(rel_node) :
    seq = Sequence()
    seq.extend([
        rel_node,
        rel_node,
    ])
    return seq

################ PROP SPE ARMES & ARMURES

spe_armure = Interval(d100).extend([
    [ 1,  3, "Mimétisme (+2 700 po)"],
    [ 4,  4, "Défense légère (bonus de +1)"],
    [ 5,  7, "Graisseuse supérieure (+15 000 po)"],
    [ 8, 13, "Ombre supérieure (+15 000 po)"],
    [14, 28, "Résistance aux énergies (+18 000 po)"],
    [29, 33, "Spectrale (bonus de +3)"],
    [34, 35, "Invulnérabilité (bonus de +3)"],
    [36, 40, "Défense intermédiaire (bonus de +3)"],
    [41, 42, "Résistance à la magie (15) (bonus de +3)"],
    [43, 43, "Forme animale (bonus de +3)"],
    [44, 48, "Graisseuse suprême (+3 750 po)"],
    [49, 58, "Ombre suprême (+3 750 po)"],
    [59, 83, "Résistance aux énergies supérieure (+42 000 po)"],
    [84, 88, "Résistance à la magie (17) (bonus de +4)"],
    [89, 89, "Éthérée (+49 000 po)"],
    [90, 90, "Contrôle des morts-vivants (+49 000 po)"],
    [91, 92, "Défense lourde (bonus de +5)"],
    [93, 94, "Résistance à la magie (19) (bonus de +5)"],
    [95, 99, "Résistance aux énergies suprême (+66 000 po)"],
])# 00 : relance 2 fois
spe_armure.append(100, 100, DoubleRelance(spe_armure))

spe_bouclier = Interval(d100).extend([
    [ 1,  5, "Interception de projectiles (bonus de +1)"],
    [ 6,  8, "Attaque (bonus de +1)"],
    [ 9, 10, "Aveuglant (bonus de +1)"],
    [11, 15, "Défense légère (bonus de +1)"],
    [16, 20, "Antiprojectiles (bonus de +2)"],
    [21, 25, "Animé (bonus de +2)"],
    [26, 41, "Résistance aux énergies (+18 000 po)"],
    [42, 46, "Spectral (bonus de +3)"],
    [47, 56, "Défense intermédiaire (bonus de +3)"],
    [57, 58, "Résistance à la magie (15) (bonus de +3)"],
    [59, 59, "Forme animale (bonus de +3)"],
    [60, 84, "Résistance aux énergies supérieure (+42 000 po)"],
    [85, 86, "Résistance à la magie (17) (bonus de +4)"],
    [87, 87, "Contrôle des morts-vivants (+49 000 po)"],
    [88, 91, "Défense lourde (bonus de +5)"],
    [92, 93, "Réfléchissant (bonus de +5)"],
    [94, 94, "Résistance à la magie (19) (bonus de +5)"],
    [95, 99, "Résistance aux énergies suprême (+66 000 po)"],
])# 00 : relance 2 fois
spe_bouclier.append(91, 100, DoubleRelance(spe_bouclier))

spe_cac = Interval(d100).extend([
    [ 1,  3, "Tueuse (bonus de +1)"],
    [ 4,  6, "Feu (bonus de +1)"],
    [ 7,  9, "Froid (bonus de +1)"],
    [10, 12, "Foudre (bonus de +1)"],
    [13, 15, "Spectrale (bonus de +1)"],
    [16, 19, "Focalisation ki (bonus de +1)"],
    [20, 21, "Enchaînement (bonus de +1)"],
    [22, 24, "Stockage de sort (bonus de +1)"],
    [25, 28, "Lancer (bonus de +1)"],
    [29, 32, "Tonnerre (bonus de +1)"],
    [33, 36, "Vicieuse (bonus de +1)"],
    [37, 41, "Anarchique (bonus de +2)"],
    [42, 46, "Axiomatique (bonus de +2)"],
    [47, 49, "Destruction (bonus de +2)"],
    [50, 54, "Feu intense (bonus de +2)"],
    [55, 59, "Froid intense (bonus de +2)"],
    [60, 64, "Sainte (bonus de +2)"],
    [65, 69, "Foudre intense (bonus de +2)"],
    [70, 74, "Impie (bonus de +2)"],
    [75, 78, "Sanglante (bonus de +2)"],
    [79, 83, "Rapidité (bonus de +3)"],
    [84, 86, "Lumière (bonus de +4)"],
    [87, 88, "Dansante (bonus de +4)"],
    [89, 90, "Vorpale (bonus de +5)"],
])# 00 : relance 2 fois
spe_cac.append(91, 100, DoubleRelance(spe_cac))

spe_dist = Interval(d100).extend([
    [ 1,  4, "Tueuse (bonus de +1)"],
    [ 5,  8, "Longue portée (bonus de +1)"],
    [ 9, 12, "Feu (bonus de +1)"],
    [13, 16, "Froid (bonus de +1)"],
    [17, 21, "Boomerang (bonus de +1)"],
    [22, 25, "Foudre (bonus de +1)"],
    [26, 27, "Traqueuse (bonus de +1)"],
    [28, 29, "Tonnerre (bonus de +1)"],
    [30, 34, "Anarchique (bonus de +2)"],
    [35, 39, "Axiomatique (bonus de +2)"],
    [40, 49, "Feu intense (bonus de +2)"],
    [50, 54, "Sainte (bonus de +2)"],
    [55, 64, "Froid intense (bonus de +2)"],
    [65, 74, "Foudre intense (bonus de +2)"],
    [75, 79, "Impie (bonus de +2)"],
    [80, 84, "Rapidité (bonus de +3)"],
    [85, 90, "Lumière (bonus de +4)"],
])# 00 : relance 2 fois
spe_dist.append(91, 100, DoubleRelance(spe_dist))

################ ARMURES & BOUCLIERS

obj_armure_spe = Interval(d100).extend([
    [ 1, 10, "Cuirasse en adamantium (10 200 po)"],
    [11, 20, "Harnois nain (16 500 po)"],
    [21, 32, "Crevice de la seconde chance (18 900 po)"],
    [33, 50, "Armure céleste (22 400 po)"],
    [51, 60, "Harnois des profondeurs (24 650po)"],
    [61, 75, "Cuirasse de commandement (25 400 po)"],
    [76, 90, "Harnois en mithral de vitesse (26 500 po)"],
    [91, 100, "Armure démoniaque (52 260 po)"],
])

obj_bouclier_spe = Interval(d100).extend([
    [ 1, 20, "Bouclier des arcanes (3 153 po)"],
    [21, 40, "Bouclier de la manticore (5 580 po)"],
    [41, 60, "Bouclier du lion (9 170 po)"],
    [61, 90, "Bouclier ailé (17 257 po)"],
    [91, 100, "Bouclier phagocyte (50 170 po)"],
])

armor_type = "NONE"
def setArmor() :
    global armor_type
    armor_type = "ARMOR"
def setShield() :
    global armor_type
    armor_type = "SHIELD"

def RollArmorProperty() :
    global armor_type
    if armor_type == "ARMOR" :
        spe_armure.execute()
    elif armor_type == "SHIELD" :
        spe_bouclier.execute()
    else :
        pass #raise ValueError(f"Not expected value {armor_type}")
    armor_type = "NONE"

obj_bouclier_armure = Weight().extend([
    [ 8, Sequence().extend([
        "Bouclier +3 (+9 000po)",
        setShield])],
    [ 8, Sequence().extend([
        "Armure +3 (+9 000po)",
        setArmor])],
    [11, Sequence().extend([
        "Bouclier +4 (+16 000po)",
        setShield])],
    [11, Sequence().extend([
        "Armure +4 (+16 000po)",
        setArmor])],
    [11, Sequence().extend([
        "Bouclier +5 (+25 000po)",
        setShield])],
    [ 8, Sequence().extend([
        "Armure +5 (+25 000po)",
        setArmor])],
])

obj_bouclier_armure_reroll = Weight()
obj_bouclier_armure_reroll.children = [c for c in obj_bouclier_armure.children]

obj_bouclier_armure.extend([
    [ 3, obj_armure_spe],
    [ 3, obj_bouclier_spe],
    # reroll and add a special property
    [37, Sequence().extend([
        obj_bouclier_armure_reroll,
        Title("Propriété", RollArmorProperty)])]
])

################ ARMES CAC & DIST

obj_arme_spe = Interval(d100).extend([
    [ 1,  4, "Dague de l’assassin (10 302 po)"],
    [ 5,  7, "Regret du changeant (12 780 po)"],
    [ 8,  9, "Trident de domination aquatique (18 650 po)"],
    [10, 13, "Épée ardente (20 715 po)"],
    [14, 17, "Épée de bonne fortune (0 souhait) (22 060 po)"],
    [18, 24, "Épée de précision (22 310 po)"],
    [25, 31, "Épée des plans (22 315 po)"],
    [32, 37, "Épée des neuf vies (23 057 po)"],
    [38, 42, "Arc du long serment (25 600 po)"],
    [43, 46, "Épée voleuse de vie (25 715 po)"],
    [47, 51, "Masse d’épouvante (38 552 po)"],
    [52, 57, "Hache dévitalisante (40 320 po)"],
    [58, 62, "Cimeterre des bois (47 315 po)"],
    [63, 67, "Rapière d’anémie (50 320 po)"],
    [68, 73, "Épée radieuse (50 335 po)"],
    [74, 79, "Épée de givre (54 475 po)"],
    [80, 84, "Marteau de lancer nain (60 312 po)"],
    [85, 91, "Épée de bonne fortune (1 souhait) (62 360 po)"],
    [92, 95, "Masse de démolition (75 312 po)"],
    [96, 97, "Épée de bonne fortune (2 souhaits) (102 660 po)"],
    [98, 99, "Épée de justice (120 630 po)"],
    [100, 100, "Épée de bonne fortune (3 souhaits) (142 960 po)"],
])

obj_cac_dist = Weight().extend([
    [20, "Arme +3	(+18 000 po)"],
    [18, "Arme +4	(+32 000 po)"],
    [11, "Arme +5	(+50 000 po)"],
])

obj_arme_reroll = Weight()
obj_arme_reroll.children = [c for c in obj_cac_dist.children]

obj_cac_dist.extend([
    [14, obj_arme_spe],
    # reroll and add a special property
    [37, Sequence().extend([
        obj_arme_reroll,
        Title("Propriété Cac", spe_cac),
        Title("Propriété Dist", spe_dist)])]
])

################ AUTRES

obj_potion = Weight().extend([
    [20, "Sort de niveau 2 (300 po)"],
    [80, "Sort de niveau 3 (750 po)"],
])

obj_anneaux = Interval(d100).extend([
    [ 3,  7, "Protection +3 (18 000 po)"],
    [ 8, 10, "Stockage de sorts mineurs (18 000 po)"],
    [11, 15, "Invisibilité (20 000 po)"],
    [16, 19, "Arcanes (premiers) (20 000 po)"],
    [20, 25, "Esquive totale (25 000 po)"],
    [26, 28, "Rayons X (25 000 po)"],
    [29, 32, "Clignotement (27 000 po)"],
    [33, 39, "Résistance aux énergies destructives, majeur (28 000 po)"],
    [40, 49, "Protection +4 (32 000 po)"],
    [50, 55, "Arcanes (deuxièmes) (40 000 po)"],
    [56, 60, "Liberté de mouvement (40 000 po)"],
    [61, 63, "Résistance aux énergies destructives, suprême (44 000 po)"],
    [64, 65, "Protection mutuelle (une paire) (50 000 po)"],
    [66, 70, "Protection +5 (50 000 po)"],
    [71, 74, "Feu d’étoiles (50 000 po)"],
    [75, 79, "Stockage de sorts (50 000 po)"],
    [80, 83, "Arcanes (troisièmes) (70 000 po)"],
    [84, 86, "Télékinésie (75 000 po)"],
    [87, 88, "Régénération (90 000 po)"],
    [89, 91, "Renvoi des sorts (100 000 po)"],
    [92, 93, "Arcanes (quatrièmes) (100 000 po)"],
    [94, 94, "Triple souhait (120 000 po)"],
    [95, 95, "Bon génie (125 000 po)"],
    [96, 96, "Contrôle des éléments (Air) (200 000 po)"],
    [97, 97, "Contrôle des éléments (Terre) (200 000 po)"],
    [98, 98, "Contrôle des éléments (Feu) (200 000 po)"],
    [99, 99, "Contrôle des éléments (Eau) (200 000 po)"],
    [100, 100, "Stockage de sorts supérieur (200 000 po)"],
])

obj_sceptre = Interval(d100).extend([
    [ 1,  4, "Oblitération (11 000 po)"],
    [ 5,  6, "Métamagie modérée, Extension de portée (11 000 po)"],
    [ 7,  8, "Métamagie modérée, Extension de durée (11 000 po)"],
    [ 9, 10, "Métamagie modérée, Incantation silencieuse (11 000 po)"],
    [11, 14, "Merveilleux (12 000 po)"],
    [15, 19, "Python (13 000 po)"],
    [20, 21, "Extinction des feux (15 000 po)"],
    [22, 25, "Vipère (19 000 po)"],
    [26, 30, "Détection de l’hostilité (23 500 po)"],
    [31, 36, "Métamagie majeure, Extension de portée (24 500 po)"],
    [37, 42, "Métamagie majeure, Extension de durée (24 500 po)"],
    [43, 48, "Métamagie majeure, Incantation silencieuse (24 500 po)"],
    [49, 53, "Prestance (25 000 po)"],
    [54, 58, "Flétrissement (25 000 po)"],
    [59, 64, "Métamagie modérée, Extension d'effet (32 500 po)"],
    [65, 69, "Orage (33 000 po)"],
    [70, 73, "Métamagie mineure, Incantation rapide (35 000 po)"],
    [74, 77, "Annulation (37 000 po)"],
    [78, 80, "Absorption (50 000 po)"],
    [81, 84, "Grand fléau (50 000 po)"],
    [85, 86, "Métamagie modérée, Quintessence des sorts (54 000 po)"],
    [87, 88, "Suzeraineté (60 000 po)"],
    [89, 90, "Sécurité (61 000 po)"],
    [91, 92, "Seigneurs de la guerre (70 000 po)"],
    [93, 94, "Métamagie majeure, Extension d'effet (73 000 po)"],
    [95, 96, "Métamagie modérée, Incantation rapide (75 500 po)"],
    [97, 98, "Éternelle vigilance (85 000 po)"],
    [99, 99, "Métamagie majeure, Quintessence des sorts (121 500 po)"],
    [100, 100, "Métamagie majeure, Incantation rapide (170 000 po)"],
])

obj_parchemin = Interval(d100).extend([
    [ 1,  5, "Sort de niveau 4 (700 po)"],
    [ 6, 50, "Sort de niveau 5 (1125 po)"],
    [51, 70, "Sort de niveau 6 (1650 po)"],
    [71, 85, "Sort de niveau 7 (2275 po)"],
    [86, 95, "Sort de niveau 8 (3000 po)"],
    [96, 100, "Sort de niveau 9 (3825 po)"],
])

obj_baton = Interval(d100).extend([
    [ 1,  3, "Envoûtement (17 600 po)"],
    [ 4,  9, "Feu (18 950 po)"],
    [10, 11, "Grand essaim (22 800 po)"],
    [12, 13, "Altération de taille (26 150 po)"],
    [14, 19, "Guérison (29 600 po)"],
    [20, 24, "Givre (41 400 po)"],
    [25, 31, "Clarté (51 500 po)"],
    [32, 38, "Défense (62 000 po)"],
    [39, 45, "Abjuration (82 000 po)"],
    [46, 50, "Invocation (82 000 po)"],
    [51, 55, "Divination (82 000 po)"],
    [56, 60, "Enchantement (82 000 po)"],
    [61, 65, "Évocation (82 000 po)"],
    [66, 70, "Illusion (82 000 po)"],
    [71, 75, "Nécromancie (82 000 po)"],
    [76, 80, "Transmutation (82 000 po)"],
    [81, 85, "Pierre et terre (85 800 po)"],
    [86, 90, "Forêt profonde (100 400 po)"],
    [91, 95, "Vie (109 400 po)"],
    [96, 98, "Transport (206 900 po)"],
    [99, 100, "Surpuissance (235 000 po)"],
])

obj_baguette = Weight().extend([
    [60, "Sort de niveau 2 (4 500 po)"],
    [40, "Sort de niveau 3 (11 250 po)"]
])

obj_merveilleux = Weight().extend([
    ["Chaînes dimensionnelles (28 000 po)"],
    ["Statuette merveilleuse (destrier d’obsidienne) (28 500 po)"],
    ["Timbales de panique (30 000 po)"],
    ["Pierre ioun (prisme orange) (30 000 po)"],
    ["Pierre ioun (prisme vert pâle) (30 000 po)"],
    ["Lanterne révélatrice (30 000 po)"],
    ["Amulette d’armure naturelle (+4) (32 000 po)"],
    ["Amulette d’antidétection (35 000 po)"],
    ["Tapis volant (1 50 m x 3 m) (35 000 po)"],
    ["Traité de création des golems de fer (35 000 po)"],
    ["Ceinturon de force de géant (+6) (36 000 po)"],
    ["Ceinturon de dextérité du chat (+6) (36 000 po)"],
    ["Ceinturon de constitution de l’ours (+6) (36 000 po)"],
    ["Bracelets d’armure (+6) (36 000 po)"],
    ["Bandeau de belle allure (+6) (36 000 po)"],
    ["Bandeau d’inspiration (+6) (36 000 po)"],
    ["Bandeau d’intelligence (+6) (36 000 po)"],
    ["Pierre ioun (prisme violet vif) (36 000 po)"],
    ["Perle de thaumaturge (sort du 6e niveau) (36 000 po)"],
    ["Scarabée de protection (38 000 po)"],
    ["Ceinturon de puissance de géant (+4) (40 000 po)"],
    ["Bandeau de prouesse mentale (+4) (40 000 po)"],
    ["Pierre ioun (ellipsoïde vert et lavande) (40 000 po)"],
    ["Anneaux de transport (40 000 po)"],
    ["Boule de cristal (42 000 po)"],
    ["Traité de création des golems de pierre monumentaux (44 000 po)"],
    ["Amulette des poings invincibles (+3) (36 000 po)"],
    ["Chapelet de prières (courant) (45 800 po)"],
    ["Orbe des tempêtes (48 000 po)"],
    ["Bottes de téléportation (49 000 po)"],
    ["Bracelets d’armure (+7) (49 000 po)"],
    ["Perle de thaumaturge (sort du 7e niveau) (49 000 po)"],
    ["Amulette d’armure naturelle (+5) (50 000 po)"],
    ["Cape de déplacement (supérieure) (50 000 po)"],
    ["Boule de cristal (détection de l’invisibilité) (50 000 po)"],
    ["Cor du Valhalla (50 000 po)"],
    ["Boule de cristal (détection des pensées) (51 000 po)"],
    ["Ailes de vol (54 000 po)"],
    ["Cape éthérée (55 000 po)"],
    ["Forteresse instantanée (55 000 po)"],
    ["Manuel de vitalité (+2) (55 000 po)"],
    ["Manuel de remise en forme (+2) (55 000 po)"],
    ["Manuel de coordination physique (+2) (55 000 po)"],
    ["Traité de perspicacité (+2) (55 000 po)"],
    ["Traité d’autorité et d’influence (+2) (55 000 po)"],
    ["Traité de compréhension (+2) (55 000 po)"],
    ["Yeux de charme (56 000 po)"],
    ["Robe étoilée (58 000 po)"],
    ["Tapis volant (3 m x 3 m) (60 000 po)"],
    ["Crâne des ténèbres (60 000 po)"],
    ["Cube de force (62 000 po)"],
    ["Ceinturon de la perfection physique (+4) (64 000 po)"],
    ["Bracelets d’armure (+8) (64 000 po)"],
    ["Bandeau de supériorité mentale (+4) (64 000 po)"],
    ["Perle de thaumaturge (sort du 8e niveau) (64 000 po)"],
    ["Boule de cristal (télépathie) (70 000 po)"],
    ["Cor de dévastation supérieur (70 000 po)"],
    ["Perle de thaumaturge (2 sorts) (70 000 po)"],
    ["Casque de téléportation (73 500 po)"],
    ["Gemme de vision (75 000 po)"],
    ["Robe d’archimage (75 000 po)"],
    ["Chasuble de la foi (76 000 po)"],
    ["Amulette des poings invincibles (+4) (64 000 po)"],
    ["Boule de cristal (vision lucide) (80 000 po)"],
    ["Perle de thaumaturge (sort du 9e niveau) (81 000 po)"],
    ["Puits des mondes (82 000 po)"],
    ["Manuel de coordination physique (+3 ) (82 500 po)"],
    ["Manuel de remise en forme (+3) (82 500 po)"],
    ["Manuel de vitalité (+3) (82 500 po)"],
    ["Traité d’autorité et d’influence (+3) (82 500 po)"],
    ["Traité de compréhension (+3) (82 500 po)"],
    ["Traité de perspicacité (+3) (82 500 po)"],
    ["Submersible du crabe (90 000 po)"],
    ["Ceinturon de puissance de géant (+6) (90 000 po)"],
    ["Bandeau de prouesse mentale (+6) (90 000 po)"],
    ["Écharpe de résistance à la magie (90 000 po)"],
    ["Miroir d’opposition (92 000 po)"],
    ["Chapelet de prières (majeur) (92 500 po)"],
    ["Manuel de coordination physique (+4) (110 000 po)"],
    ["Manuel de remise en forme (+4) (110 000 po)"],
    ["Manuel de vitalité (+4) (110 000 po)"],
    ["Traité d’autorité et d’influence (+4) (110 000 po)"],
    ["Traité de compréhension (+4) (110 000 po)"],
    ["Traité de perspicacité (+4) (110 000 po)"],
    ["Amulette des plans (120 000 po)"],
    ["Robe de vision totale (120 000 po)"],
    ["Amulette des poings invincibles (100 000 po)"],
    ["Casque de mille feux (125 000 po)"],
    ["Manuel de coordination physique (+5) (137 500 po)"],
    ["Manuel de remise en forme (+5) (137 500 po)"],
    ["Manuel de vitalité (+5) (137 500 po)"],
    ["Traité d’autorité et d’influence (+5) (137 500 po)"],
    ["Traité de compréhension (+5) (137 500 po)"],
    ["Traité de perspicacité (+5) (137 500 po)"],
    ["Ceinturon de la perfection physique (+6) (144 000 po)"],
    ["Bandeau de supériorité mentale (+6) (144 000 po)"],
    ["Urne du mauvais génie (145 000 po)"],
    ["Cube des plans (164 000 po)"],
    ["Flasque de fer (170 000 po)"],
    ["Miroir d’emprisonnement (200 000 po)"],
])

################ ROOT

sel_main = Weight()
sel_main.extend([
    [10, Title("Armure", obj_bouclier_armure)],
    [10, Title("Arme", obj_cac_dist)],
    [ 5, Title("Potion", obj_potion)],
    [10, Title("Anneau", obj_anneaux)],
    [10, Title("Sceptre", obj_sceptre)],
    [10, Title("Parchemin", obj_parchemin)],
    [20, Title("Baton", obj_baton)],
    [ 5, Title("Baguette", obj_baguette)],
    [20, Title("Objet Merveilleux", obj_merveilleux)],
])

sel_main.execute()
