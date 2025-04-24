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
    [25, "Mimétisme (+2 700 po)"],
    [ 7, "Défense légère (+1 altération)"],
    [20, "Graisseuse (+3 750 po)"],
    [40, "Ombre (+3 750 po)"],
    [ 4, "Résistance à la magie (13) (+2 altération)"],
    [ 1, "Graisseuse supérieure (+15 000 po)"],
    [ 2, "Ombre supérieure (+15 000 po)"],
]# 00 : relance 2 fois
spe_armure.append(DoubleRelance(spe_armure))

spe_bouclier = Weight() << [
    [20, "Interception de projectiles (+1 altération)"],
    [20, "Attaque (+1 altération)"],
    [10, "Aveuglant (+1 altération)"],
    [25, "Défense légère (+1 altération)"],
    [17, "Antiprojectiles (+2 altération)"],
    [ 5, "Animé (+2 altération)"],
    [ 2, "Résistance à la magie (13) (+2 altération)"],
]# 00 : relance 2 fois
spe_bouclier.append(DoubleRelance(spe_bouclier))

spe_cac = Weight() << [
    [10, "Tueuse (+1 altération)"],
    [ 7, "Gardienne (+1 altération)"],
    [10, "Feu (+1 altération)"],
    [10, "Froid (+1 altération)"],
    [10, "Foudre (+1 altération)"],
    [ 9, "Spectrale (+1 altération)"],
    [11, "Acérée (+1 altération)"],
    [ 4, "Focalisation Ki (+1 altération)"],
    [ 4, "Miséricordieuse (+1 altération)"],
    [ 7, "Enchaînement (+1 altération)"],
    [ 5, "Stockage de Sorts (+1 altération)"],
    [ 4, "Lancer (+1 altération)"],
    [ 4, "Tonnerre (+1 altération)"],
    [ 4, "Vicieuse (+1 altération)"],
]# 00 : relance 2 fois
spe_cac.append(DoubleRelance(spe_cac))

spe_dist = Weight() << [
    [12, "Tueuse (+1 altération)"],
    [13, "Longue portée (+1 altération)"],
    [15, "Flamme (+1 altération)"],
    [15, "Froid (+1 altération)"],
    [ 5, "Miséricordieuse (+1 altération)"],
    [ 8, "Boomerang (+1 altération)"],
    [15, "Foudre (+1 altération)"],
    [10, "Traqueuse (+1 altération)"],
    [ 6, "Tonnerre (+1 altération)"],
]# 00 : relance 2 fois
spe_dist.append(DoubleRelance(spe_dist))

################ ARMURES & BOUCLIERS

obj_armure_spe = Weight() << [
    [50, "Chemise de mailles en mithral (1 100 po)"],
    [30, "Harnois en peau de dragon (3 300 po)"],
    [20, "Cotte de maille elfique (5 150 po)"],
]

obj_bouclier_spe = Weight() << [
    [30, "Bouclier en ébénite (205 po)"],
    [50, "Ecu en ébénite (257 po)"],
    [15, "Ecu en mithral (1 020 po)"],
    [ 5, "Bouclier des arcanes (3 153 po)"],
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
        raise ValueError(f"Not expected value {armor_type}")

obj_bouclier_armure = Weight() << [
    [60, Sequence() << [
        "Bouclier +1 (+1 000po)",
        setShield]],
    [20, Sequence() << [
        "Armure +1 (+1 000po)",
        setArmor]],
    [ 5, Sequence() << [
        "Bouclier +2 (+4 000po)",
        setShield]],
    [ 3, Sequence() << [
        "Armure +2 (+4 000po)",
        setArmor]],
    [ 2, obj_armure_spe],
    [ 2, obj_bouclier_spe],
    # [ 8, reroll and add special property"],
]

obj_bouclier_armure_reroll = Weight()
obj_bouclier_armure_reroll.children = [c for c in obj_bouclier_armure.children[0:4]]

obj_bouclier_armure.append(8, Sequence() << [
    obj_bouclier_armure_reroll,
    Title("Propriété", RollArmorProperty)
])

################ ARMES CAC & DIST

obj_arme_spe = Weight() << [
    [15, "Flèche endormante (132 po)"],
    [10, "Carreau hurleur (267 po)"],
    [20, "Dague de maître en argent (322 po)"],
    [20, "Epée longue de maître en fer froid (330 po)"],
    [10, "Javeline de foudre (1 500 po)"],
    [ 5, "Flèche mortelle (2 282 po)"],
    [10, "Dague en adamantium (3 002 po)"],
    [10, "Hache d'armes en adamantium (3 010 po)"],
]

obj_cac_dist = Weight() << [
    [70, "Arme +1 (+1 000po)"],
    [15, "Arme +2 (+8 000po)"],
    [ 5, obj_arme_spe],
    # [10, reroll and add special property"],
]

obj_arme_reroll = Weight()
obj_arme_reroll.children = [c for c in obj_cac_dist.children[0:2]]

obj_cac_dist.append(10, Sequence() << [
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
   [18, "Protection +1 (2 000 po)"],
   [10, "Feuille morte (2 200 po)"],
   [ 8, "Subsistance (2 500 po)"],
   [ 8, "Escalade (2 500 po)"],
   [ 8, "Saut (2 500 po)"],
   [ 8, "Nage (2 500 po)"],
   [10, "Contresort (4 000 po)"],
   [ 5, "Barrière mentale (8 000 po)"],
   [ 5, "Protection +2 (8 000 po)"],
   [ 5, "Bouclier de force (8 500 po)"],
   [ 5, "Bélier (8 600 po)"],
   [ 3, "Amitié avec les animaux (10 800 po)"],
   [ 3, "Résistance aux énergies destructives, mineur (12 000 po)"],
   [ 2, "Caméléon (12 700 po)"],
   [ 2, "Marche sur l’onde (15 000 po)"],
]

obj_parchemin = Weight() << [
    [ 5, "Sort de niveau 0 (12,5 po)"],
    [45, "Sort de niveau 1 (25 po)"],
    [46, "Sort de niveau 2 (150 po)"],
    [ 4, "Sort de niveau 3 (375 po)"],
]

obj_baguette = Weight() << [
    [ 5, "Sort de niveau 0 (375 po)"],
    [55, "Sort de niveau 1 (750 po)"],
    [40, "Sort de niveau 2 (4 500 po)"],
]

obj_merveilleux = Weight() << [
    ["Plume magique (ancre) (50 po)"],
    ["Solvant universel (50 po)"],
    ["Philtre d’amour (mineur) (150 po)"],
    ["Onguent d’intemporalité (150 po)"],
    ["Plume magique (éventail) (200 po)"],
    ["Poudre de dissimulation des traces (250 po)"],
    ["Élixir de discrétion instinctive (250 po)"],
    ["Élixir d’acrobatie (250 po)"],
    ["Élixir de nage (250 po)"],
    ["Élixir d’acuité visuelle (250 po)"],
    ["Lustrargent (250 po)"],
    ["Plume magique (oiseau) (300 po)"],
    ["Plume magique (arbre) (400 po)"],
    ["Plume magique (bateau cygne) (450 po)"],
    ["Sérum de vérité (500 po)"],
    ["Plume magique (fouet) (500 po)"],
    ["Poudre dessiccative (850 po)"],
    ["Main du mage (900 po)"],
    ["Bracelets d’armure (+1) (1 000 po)"],
    ["Cape de résistance (+1) (1 000 po)"],
    ["Perle de thaumaturge (sort du 1er niveau) (1 000 po)"],
    ["Phylactère du croyant (1 000 po)"],
    ["Onguent d’insaisissabilité (1 000 po)"],
    ["Élixir de souffle enflammé (1 100 po)"],
    ["Flûte d’Hamelin (1 150 po)"],
    ["Poudre d’illusion (1 150 po)"],
    ["Broche de défense (1 500 po)"],
    ["Collier à boules de feu (1er modèle) (1 650 po)"],
    ["Poudre d’apparition (1 800 po)"],
    ["Couvre-chef de déguisement (1 800 po)"],
    ["Flûte à bruitages (1 800 po)"],
    ["Carquois efficace (1 800 po)"],
    ["Amulette d’armure naturelle (+1) (2 000 po)"],
    ["Havresac (2 000 po)"],
    ["Corne de brume (2 000 po)"],
    ["Gemme à élémentaire (2 250 po)"],
    ["Robe d’ossements (2 400 po)"],
    ["Colle universelle (2 400 po)"],
    ["Sac sans fond (1er modèle) (2 500 po)"],
    ["Bottes elfiques (2 500 po)"],
    ["Bottes des terres gelées (2 500 po)"],
    ["Cierge de vérité (2 500 po)"],
    ["Cape elfique (2 500 po)"],
    ["Yeux de lynx (2 500 po)"],
    ["Lunettes grossissantes (2 500 po)"],
    ["Broche antigolems (2 500 po)"],
    ["Collier à boules de feu (2e modèle) (2 700 po)"],
    ["Pierre d’alerte (2 700 po)"],
    ["Bille de force (3 000 po)"],
    ["Carillon d’ouverture (3 000 po)"],
    ["Fers à cheval de rapidité (3 000 po)"],
    ["Corde d’escalade (3 000 po)"],
    ["Sac à malice (gris) (3 400 po)"],
    ["Poudre de disparition (3 500 po)"],
    ["Loupe de détection (3 500 po)"],
    ["Chasuble de druide (3 750 po)"],
    ["Statuette merveilleuse (corbeau d’argent) (3 800 po)"],
    ["Ceinturon de force de géant (+2) (4 000 po)"],
    ["Ceinturon de dextérité du chat (+2) (4 000 po)"],
    ["Ceinturon de constitution de l’ours (+2) (4 000 po)"],
    ["Bracelets d’armure (+2) (4 000 po)"],
    ["Cape de résistance (+2) (4 000 po)"],
    ["Gants antiprojectiles (4 000 po)"],
    ["Bandeau de belle allure (+2) (4 000 po)"],
    ["Bandeau d’inspiration (+2) (4 000 po)"],
    ["Bandeau d'intelligence (+2) (4 000 po)"],
    ["Pierre ioun (fuseau translucide) (4 000 po)"],
    ["Onguent de restauration (4 000 po)"],
    ["Pigments merveilleux (4 000 po)"],
    ["Perle de thaumaturge (sort du 2e niveau) (4 000 po)"],
    ["Onguent des roches (4 000 po)"],
    ["Collier à boules de feu (3e modèle) (4 350 po)"],
    ["Serre-tête de persuasion (4 500 po)"],
    ["Chaussons d’araignée (4 800 po)"],
    ["Encens de méditation (4 900 po)"],
    ["Amulette des poings invincibles (+1) (4 000 po)"],
    ["Sac sans fond (2e modèle) (5 000 po)"],
    ["Bracelets d’archer (5 000 po)"],
    ["Pierre ioun (prisme rose laiteux) (5 000 po)"],
    ["Casque de compréhension (5 200 po)"],
    ["Gilet d’évasion (5 200 po)"],
    ["Urne fumigène (5 400 po)"],
    ["Cuillère nourrissante (5 400 po)"],
    ["Collier à boules de feu (4e modèle) (5 400 po)"],
    ["Bottes de sept lieues (5 500 po)"],
    ["Éventail enchanté (5 500 po)"],
    ["Collier à boules de feu (5e modèle) (6 000 po)"],
    ["Fers à cheval du zéphyr (6 000 po)"],
    ["Flûte de hantise (6 000 po)"],
    ["Gants de nage et d’escalade (6 250 po)"],
    ["Serre-tête de lumière destructrice (6 480 po)"],
    ["Cor du Bien/du Mal (6 500 po)"],
    ["Robe de camelot (7 000 po)"],
    ["Bateau pliant (7 200 po)"],
    ["Cape de la raie manta (7 200 po)"],
    ["Flacon d’air pur (7 250 po)"],
    ["Sac sans fond (3e modèle) (7 400 po)"],
    ["Charme de bonne santé (7 400 po)"],
    ["Bottes de lévitation (7 500 po)"],
    ["Harpe de suggestion (7 500 po)"],
]

################ ROOT

root = Weight() << [
    [ 4, Title("Armure", obj_bouclier_armure)],
    [ 5, Title("Arme", obj_cac_dist)],
    [35, Title("Potion", obj_potion)],
    [ 2, Title("Anneau", obj_anneaux)],
    [35, Title("Parchemin", obj_parchemin)],
    [10, Title("Baguette", obj_baguette)],
    [ 9, Title("Objet Merveilleux", obj_merveilleux)],
]

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute().print_to_console()
