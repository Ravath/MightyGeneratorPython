# -*- coding: utf-8 -*-

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import Title
from wordgenerator.Generator import Generator

def DoubleRelance(rel_node) :
    seq = Sequence()
    seq << [
        rel_node,
        rel_node,
    ]
    return seq

################ PROP SPE ARMES & ARMURES

spe_armure = Weight() << [
    [ 5, "Mimétisme (+2 700 po)"],
    [ 3, "Défense légère (bonus de +1)"],
    [ 3, "Graisseuse (+3 750 po)"],
    [ 6, "Ombre (+3 750 po)"],
    [ 2, "Résistance à la magie (13) (bonus de +2)"],
    [10, "Graisseuse supérieure (+15 000 po)"],
    [20, "Ombre supérieure (+15 000 po)"],
    [25, "Résistance aux énergies (+18 000 po)"],
    [ 5, "Spectrale (bonus de +3)"],
    [ 5, "Invulnérabilité (bonus de +3)"],
    [ 5, "Défense intermédiaire (bonus de +3)"],
    [ 5, "Résistance à la magie (15) (bonus de +3)"],
    [ 5, "Forme animale (bonus de +3)"],
]# 00 : relance 2 fois
spe_armure.append(DoubleRelance(spe_armure))

spe_bouclier = Weight() << [
    [10, "Interception de projectiles (bonus de +1)"],
    [10, "Attaque (bonus de +1)"],
    [ 5, "Aveuglant (bonus de +1)"],
    [15, "Défense légère (bonus de +1)"],
    [10, "Antiprojectiles (bonus de +2)"],
    [ 7, "Animé (bonus de +2)"],
    [12, "Résistance à la magie (13) (bonus de +2)"],
    [10, "Résistance aux énergies (+18 000 po)"],
    [ 6, "Spectral (bonus de +3)"],
    [10, "Défense intermédiaire (bonus de +3)"],
    [ 3, "Résistance à la magie (15) (bonus de +3)"],
    [ 1, "Forme animale (bonus de +3)"],
]# 00 : relance 2 fois
spe_bouclier.append(DoubleRelance(spe_bouclier))

spe_cac = Weight() << [
    [ 6, "Tueuse (bonus de +1)"],
    [ 6, "Gardienne (bonus de +1)"],
    [ 7, "Feu (bonus de +1)"],
    [ 7, "Froid (bonus de +1)"],
    [ 7, "Foudre (bonus de +1)"],
    [ 5, "Spectrale (bonus de +1)"],
    [ 6, "Acérée (bonus de +1)"],
    [ 4, "Focalisation ki (bonus de +1)"],
    [ 2, "Miséricordieuse (bonus de +1)"],
    [ 4, "Enchaînement (bonus de +1)"],
    [ 5, "Stockage de sort (bonus de +1)"],
    [ 4, "Lancer (bonus de +1)"],
    [ 2, "Tonnerre (bonus de +1)"],
    [ 4, "Vicieuse (bonus de +1)"],
    [ 3, "Anarchique (bonus de +2)"],
    [ 3, "Axiomatique (bonus de +2)"],
    [ 3, "Destruction (bonus de +2)"],
    [ 3, "Feu intense (bonus de +2)"],
    [ 3, "Froid intense (bonus de +2)"],
    [ 3, "Sainte (bonus de +2)"],
    [ 3, "Foudre intense (bonus de +2)"],
    [ 3, "Impie (bonus de +2)"],
    [ 2, "Sanglante (bonus de +2)"],
]# 00 : relance 2 fois
spe_cac.append(5, DoubleRelance(spe_cac))

spe_dist = Weight() << [
    [ 8, "Tueuse (bonus de +1)"],
    [ 8, "Longue portée	(bonus de +1)"],
    [12, "Feu (bonus de +1)"],
    [12, "Froid (bonus de +1)"],
    [ 2, "Miséricordieuse (bonus de +1)"],
    [ 5, "Boomerang (bonus de +1)"],
    [12, "Foudre (bonus de +1)"],
    [ 5, "Traqueuse (bonus de +1)"],
    [ 4, "Tonnerre (bonus de +1)"],
    [ 3, "Anarchique (bonus de +2)"],
    [ 3, "Axiomatique (bonus de +2)"],
    [ 5, "Feu intense (bonus de +2)"],
    [ 3, "Sainte (bonus de +2)"],
    [ 5, "Froid intense (bonus de +2)"],
    [ 5, "Foudre intense (bonus de +2)"],
    [ 3, "Impie (bonus de +2)"],
]# 00 : relance 2 fois
spe_dist.append(5, DoubleRelance(spe_dist))

################ ARMURES & BOUCLIERS

obj_armure_spe = Weight() << [
    [25, "Chemise de mailles en mithral (1 100 po)"],
    [20, "Harnois en peau de dragon (3 300 po)"],
    [12, "Cotte de mailles elfique (5 150 po)"],
    [10, "Armure de peau de rhinocéros (5 165 po)"],
    [15, "Cuirasse en adamantium (10 200 po)"],
    [15, "Harnois nain (16 500 po)"],
    [ 3, "Crevice de la seconde chance (18 900 po)"],
]

obj_bouclier_spe = Weight() << [
	[20, "Rondache en ébénite (203 po)"],
    [25, "Écu en ébénite (257 po)"],
    [25, "Écu en mithral (1 020 po)"],
    [15, "Bouclier des arcanes (3 153 po)"],
    [ 5, "Bouclier de la manticore (5 580 po)"],
    [ 5, "Bouclier du lion (9 170 po)"],
    [ 5, "Bouclier ailé (17 257 po)"],
]

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

obj_bouclier_armure = Weight() << [
    [ 5, Sequence() << [
        "Bouclier +1 (+1 000po)",
        setShield]],
    [ 5, Sequence() << [
        "Armure +1 (+1 000po)",
        setArmor]],
    [10, Sequence() << [
        "Bouclier +2 (+4 000po)",
        setShield]],
    [10, Sequence() << [
        "Armure +2 (+4 000po)",
        setArmor]],
    [10, Sequence() << [
        "Bouclier +3 (+9 000po)",
        setShield]],
    [10, Sequence() << [
        "Armure +3 (+9 000po)",
        setArmor]],
    [ 5, Sequence() << [
        "Bouclier +4 (+16 000po)",
        setShield]],
    [ 2, Sequence() << [
        "Armure +4 (+16 000po)",
        setArmor]],
    [ 3, obj_armure_spe],
    [ 3, obj_bouclier_spe],
    # [37, reroll and add special property"],
]

obj_bouclier_armure_reroll = Weight()
obj_bouclier_armure_reroll.children = [c for c in obj_bouclier_armure.children[0:8]]

obj_bouclier_armure.append(37, Sequence() << [
    obj_bouclier_armure_reroll,
    Title("Propriété", RollArmorProperty)
])

################ ARMES CAC & DIST

obj_arme_spe = Weight() << [
    [ 9, "Javeline de foudre (1 500 po)"],
    [ 6, "Flèche mortelle (2 282 po)"],
    [ 9, "Dague en adamantium (3 002 po)"],
    [ 9, "Hache d’armes en adamantium (3 010 po)"],
    [ 4, "Flèche mortelle supérieure (4 057 po)"],
    [ 3, "Brise-arme (4 315 po)"],
    [ 6, "Dague venimeuse (8 302 po)"],
    [ 5, "Trident d’alerte (10 115 po)"],
    [ 6, "Dague de l’assassin (10 302 po)"],
    [ 5, "Regret du changeant (12 780 po)"],
    [ 4, "Trident de domination aquatique (18 650 po)"],
    [ 8, "Épée ardente (20 715 po)"],
    [ 5, "Épée de bonne fortune (0 souhait) (22 060 po)"],
    [ 7, "Épée de précision (22 310 po)"],
    [ 5, "Épée des plans (22 315 po)"],
    [ 4, "Épée des neuf vies (23 057 po)"],
    [ 3, "Arc du long serment (25 600 po)"],
    [ 2, "Épée voleuse de vie (25 715 po)"],
]

obj_cac_dist = Weight() << [
    [10, "Arme +1	(+2 000 po)"],
    [19, "Arme +2	(+8 000 po)"],
    [29, "Arme +3	(+18 000 po)"],
    [ 4, "Arme +4	(+32 000 po)"],
    [ 6, obj_arme_spe],
    # [32, reroll and add special property"],
]

obj_arme_reroll = Weight()
obj_arme_reroll.children = [c for c in obj_cac_dist.children[0:4]]

obj_cac_dist.append(32, Sequence() << [
    obj_arme_reroll,
    Title("Propriété Cac", spe_cac),
    Title("Propriété Dist", spe_dist)
])

################ AUTRES

obj_potion = Weight() << [
   [20, "Sort de niveau 0 (25 po)"],
   [40, "Sort de niveau 1 (50 po)"],
   [40, "Sort de niveau 2 (300 po)"],
]

obj_anneaux = Weight() << [
    [ 5, "Contresort (4 000 po)"],
    [ 3, "Barrière mentale (8 000 po)"],
    [10, "Protection +2 (8 000 po)"],
    [ 5, "Bouclier de force (8 500 po)"],
    [ 5, "Bélier (8 600 po)"],
    [ 6, "Escalade supérieure (10 000 po)"],
    [ 6, "Saut supérieur (10 000 po)"],
    [ 6, "Nage supérieure (10 000 po)"],
    [ 4, "Amitié avec les animaux (10 800 po)"],
    [ 6, "Résistance aux énergies destructives, mineur (12 000 po)"],
    [ 5, "Caméléon (12 700 po)"],
    [ 5, "Marche sur l’onde (15 000 po)"],
    [ 5, "Protection +3 (18 000 po)"],
    [ 5, "Stockage de sorts mineurs (18 000 po)"],
    [ 5, "Invisibilité (20 000 po)"],
    [ 4, "Arcanes (premiers) (20 000 po)"],
    [ 5, "Esquive totale (25 000 po)"],
    [ 3, "Rayons X (25 000 po)"],
    [ 4, "Clignotement (27 000 po)"],
    [ 3, "Résistance aux énergies destructives, majeur (28 000 po)"],
]

obj_sceptre = Weight() << [
    [ 7, "Métamagie mineure, Extension de portée (3 000 po)"],
    [ 7, "Métamagie mineure, Extension de durée (3 000 po)"],
    [ 7, "Métamagie mineure, Incantation silencieuse (3 000 po)"],
    [ 7, "Inamovible (5 000 po)"],
    [ 7, "Métamagie mineure, Extension d’effet (9 000 po)"],
    [ 7, "Détection des métaux et des minéraux (10 500 po)"],
    [11, "Oblitération (11 000 po)"],
    [ 4, "Métamagie modérée, Extension de portée (11 000 po)"],
    [ 4, "Métamagie modérée, Extension de durée (11 000 po)"],
    [ 4, "Métamagie modérée, Incantation silencieuse (11 000 po)"],
    [ 6, "Merveilleux (12 000 po)"],
    [ 8, "Python (13 000 po)"],
    [ 4, "Métamagie mineure, Quintessence des sorts (14 000 po)"],
    [ 6, "Extinction des feux (15 000 po)"],
    [ 8, "Vipère (19 000 po)"],
    [ 2, "Métamagie modérée, Extension d'effet (32 500 po)"],
    [ 1, "Métamagie mineure, Incantation rapide (35 000 po)"],
]

obj_parchemin = Weight() << [
    [ 5, "Sort de niveau 2 (150 po)"],
    [60, "Sort de niveau 3 (375 po)"],
    [30, "Sort de niveau 4 (700 po)"],
    [ 5, "Sort de niveau 5 (1 125 po)"],
]

obj_baton = Weight() << [
    [15, "Envoûtement (17 600 po)"],
    [15, "Feu (18 950 po)"],
    [10, "Grand essaim (22 800 po)"],
    [15, "Altération de taille (26 150 po)"],
    [20, "Guérison (29 600 po)"],
    [15, "Givre (41 400 po)"],
    [ 5, "Clarté (51 500 po)"],
    [ 5, "Défense (62 000 po)"],
]

obj_baguette = Weight() << [
    [60, "Sort de niveau 2 (4 500 po)"],
    [40, "Sort de niveau 3 (11 250 po)"]
]

obj_merveilleux = Weight() << [
    ["Amulette d’armure naturelle (+2) (8 000 po)"],
    ["Traité de création des golems de chair (8 000 po)"],
    ["Main miraculeuse (8 000 po)"],
    ["Pierre ioun (sphère rouge sang) (8 000 po)"],
    ["Pierre ioun (sphère bleu incandescent) (8 000 po)"],
    ["Pierre ioun (rhombe bleu pâle) (8 000 po)"],
    ["Pierre ioun (sphère rose et verte) (8 000 po)"],
    ["Pierre ioun (rhombe rose vif) (8 000 po)"],
    ["Pierre ioun (sphère rouge et bleue) (8 000 po)"],
    ["Cartes fantasmagoriques (8 100 po)"],
    ["Collier à boules de feu (6e modèle) (8 100 po)"],
    ["Cierge d’invocation (8 400 po)"],
    ["Robe de mimétisme (8 400 po)"],
    ["Sac à malice (rouille) (8 500 po)"],
    ["Collier à boules de feu (7e modèle) (8 700 po)"],
    ["Bracelets d’armure (+3) (9 000 po)"],
    ["Cape de résistance (+3) (9 000 po)"],
    ["Carafe intarissable (9 000 po)"],
    ["Collier d’adaptation (9 000 po)"],
    ["Perle de thaumaturge (sort du 3e niveau) (9 000 po)"],
    ["Statuette merveilleuse (hibou de chrysolite) (9 100 po)"],
    ["Chapelet de prières (mineur) (9 600 po)"],
    ["Sac sans fond (4e modèle) (10 000 po)"],
    ["Ceinturon de puissance de géant (+2) (10 000 po)"],
    ["Statuette merveilleuse (griffon de bronze) (10 000 po)"],
    ["Statuette merveilleuse (mouche d’ébène) (10 000 po)"],
    ["Gant de rangement (10 000 po)"],
    ["Bandeau de prouesse mentale (+2) (10 000 po)"],
    ["Pierre ioun (rhombe bleu nuit) (10 000 po)"],
    ["Cape de prestidigitateur (10 800 po)"],
    ["Phylactère de canalisation négative (11 000 po)"],
    ["Phylactère de canalisation positive (11 000 po)"],
    ["Gantelet de rouille (11 500 po)"],
    ["Bottes de rapidité (12 000 po)"],
    ["Lunettes de nyctalope (12 000 po)"],
    ["Traité de création des golems d’argile (12 000 po)"],
    ["Médaillon des pensées (12 000 po)"],
    ["Livre magique (12 500 po)"],
    ["Gemme d’illumination (13 000 po)"],
    ["Lyre de bâtisseur (13 000 po)"],
    ["Robe de moine (13 000 po)"],
    ["Cape de l’araignée (14 000 po)"],
    ["Ceinture des nains (14 900 po)"],
    ["Charme de coagulation (15 000 po)"],
    ["Perle des sirènes (15 300 po)"],
    ["Statuette merveilleuse (chien d’onyx) (16 000 po)"],
    ["Sac à malice (ocre) (16 000 po)"],
    ["Ceinturon de force de géant (+4) (16 000 po)"],
    ["Ceinturon de dextérité du chat (+4) (16 000 po)"],
    ["Ceinturon de constitution de l’ours (+4) (16 000 po)"],
    ["Ceinturon de la perfection physique (+2) (16 000 po)"],
    ["Bottes ailées (16 000 po)"],
    ["Bracelets d’armure (+4) (16 000 po)"],
    ["Cape de résistance (+4) (16 000 po)"],
    ["Bandeau de belle allure (+4) (16 000 po)"],
    ["Bandeau d’inspiration (+4) (16 000 po)"],
    ["Bandeau de supériorité mentale (+2) (16 000 po)"],
    ["Bandeau d’intelligence (+4) (16 000 po)"],
    ["Perle de thaumaturge (sort du 4e niveau) (16 000 po)"],
    ["Fourreau d’affûtage (16 000 po)"],
    ["Statuette merveilleuse (lions d’or) (16 500 po)"],
    ["Carillon d’interruption (16 800 po)"],
    ["Balai volant (17 000 po)"],
    ["Statuette merveilleuse (éléphant de marbre) (17 000 po)"],
    ["Amulette d’armure naturelle (+3) (18 000 po)"],
    ["Pierre ioun (fuseau irisé) (18 000 po)"],
    ["Bracelet d’assistance (19 000 po)"],
    ["Amulette des poings invincibles (+2) (16 000 po)"],
    ["Tapis volant (1 50 m x 1 50 m) (20 000 po)"],
    ["Cor de dévastation (20 000 po)"],
    ["Pierre ioun (ellipsoïde lavande) (20 000 po)"],
    ["Pierre ioun (fuseau blanc laiteux) (20 000 po)"],
    ["Trou portable (20 000 po)"],
    ["Pierre porte-bonheur (20 000 po)"],
    ["Statuette merveilleuse (chèvres d’ivoire) (21 000 po)"],
    ["Corde d’enchevêtrement (21 000 po)"],
    ["Traité de création des golems de pierre (22 000 po)"],
    ["Masque de la camarde (22 000 po)"],
    ["Pioche des titans (23 350 po)"],
    ["Serre-tête de lumière dévastatrice (23 760 po)"],
    ["Cape de déplacement (mineure) (24 000 po)"],
    ["Casque de l’homme-poisson (24 000 po)"],
    ["Bracelets d’archer hors pair (25 000 po)"],
    ["Bracelets d'armure (+5) (25 000 po)"],
    ["Cape de résistance (+5) (25 000 po)"],
    ["Yeux d’anathème (25 000 po)"],
    ["Perle de thaumaturge (sort du 5e niveau) (25 000 po)"],
    ["Maillet des titans (25 300 po)"],
    ["Cape de la chauve-souris (26 000 po)"],
    ["Liens d'acier mystiques (26 000 po)"],
    ["Cube de résistance au froid (27 000 po)"],
    ["Casque de télépathie (27 000 po)"],
    ["Charme antipoison (27 000 po)"],
    ["Robe prismatique (27 000 po)"],
    ["Manuel de coordination physique (+1) (27 500 po)"],
    ["Manuel de remise en forme (+1) (27 500 po)"],
    ["Manuel de vitalité (+1) (27 500 po)"],
    ["Traité de perspicacité (+1) (27 500 po)"],
    ["Traité d’autorité et d’influence (+1) (27 500 po)"],
    ["Traité de compréhension (+1) (27 500 po)"],
]

################ ROOT

root = Weight() << [
    [10, Title("Armure", obj_bouclier_armure)],
    [10, Title("Arme", obj_cac_dist)],
    [10, Title("Potion", obj_potion)],
    [10, Title("Anneau", obj_anneaux)],
    [10, Title("Sceptre", obj_sceptre)],
    [15, Title("Parchemin", obj_parchemin)],
    [ 3, Title("Baton", obj_baton)],
    [15, Title("Baguette", obj_baguette)],
    [17, Title("Objet Merveilleux", obj_merveilleux)],
]

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute()
    generation.print_to_console()
