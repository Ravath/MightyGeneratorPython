# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from ponderation import pond_type, pond_fabriquant, pond_element, can_element
from ponderation import nbr_of_constructor_properties , sel_element
from macro.calc import SubOp, MulOp
from macro.calc import ValueIf

#################################################
#                WEAPON BONUSES                 #
#################################################

capa_arme = Weight() << [
    ["Balise gN0w© intégrée!\n"],
    ["Celle-là, c'est cadeau\n"],
    ["Crie au génie\n"],
    ["TORGUE TE DIT DE RIEN\n"],
    ["Attends, il fait quoi ce gros bouton ROUGE?\n"],
    ["Elles pleuvront, ils pleureront\n"],
    ["Gladiator\n"],
    ["Anussassineur\n"],
    ["Tyrannosaure sexuel\n"],
    ["BOOM!\n"],
    ["1 canon? HAHAHAHA!\n"],
    ["Plus de cacahuètes!\n"],
    ["Je pratique l'échangisme énergétique\n"],
    ["Le passé du futur est imparfait\n"],
    ["100% naturel, pas de bio du tout\n"],
    ["Don't stop the music\n"],
    ["On avait dit pas les mamans!\n"],
    ["Le Tout-Puissant est avec vous\n"],
    ["Ce qui est à toi est pour moi\n"],
    ["FIRST!\n"],
    [pond_type["PISTOLET"], "Sagesse dans le chargeur\n"],
    [pond_type["PISTOLET"], "Le petit partenaire du manifestant\n"],
    [pond_type["PISTOLET"], "Le meilleur ami de l'homme\n"],
    [pond_type["PISTOLET"], "Gerbotron\n"],
    [pond_type["MITRAILLETTE"], "Soutien aérien\n"],
    [pond_type["ASSAUT"], "Tout est dans le poignet\n"],
    [pond_type["POMPE"], "De l'amour en cône\n"],
    [pond_type["POMPE"], "Génie des temps modernes\n"],
    [pond_type["SNIPER"], "Voir et être vu\n"],
    [pond_type["SNIPER"], "MultiomegatumulteBl4st3r8000000\n"],
    [pond_type["SNIPER"], "IMACHARGINMALAZAH\n"],
    [pond_type["SNIPER"], "Duel au soleil\n"],
    [pond_type["SNIPER"], "Fil du rasoir. Balle écarlate. Danse létale.\n"],
    [pond_type["SNIPER"], "Pour le meilleur tonton/la meilleure tatie\n"],
    [pond_type["SNIPER"], "J'avais écrit Arc à POULIE!\n"],
    [pond_fabriquant["Bandit"], "Absolument non écologique\n"],
    [pond_fabriquant["Dahl"], "C-C-C-C-COMBO\n"],
    [pond_fabriquant["Dahl"], "Vous n'avez rien vu...\n"],
    [pond_fabriquant["Dahl"], "Je ne reculerai pas\n"],
    [pond_fabriquant["Maliwan"], "Les fléaux se partagent\n"],
    [pond_fabriquant["Maliwan"], "Donner, c'est recevoir\n"],
    [pond_fabriquant["Maliwan"], "J'ai rien compris mais c'est sympa\n"],
    [pond_fabriquant["Maliwan"], "Deux tu l'auras\n"],
    [SubOp(1, pond_fabriquant["Maliwan"]), "Elite de la nation\n"],
    [pond_fabriquant["Tediore"], "N'y. Touchez. Pas.\n"],
    [pond_fabriquant["Tediore"], "Kiki a un fusil\n"],
    [pond_fabriquant["Tediore"], "Le meilleur cadeau est celui qu'on offre à soi-même\n"],
    [pond_fabriquant["Tediore"], "Tout est dans le poignet\n"],
    [pond_fabriquant["Tediore"], "Tape dans le fond\n"],
    [pond_fabriquant["Tediore"], "La taille compte\n"],
    [pond_fabriquant["Torgue"], "CE SERA NOTRE PETIT SECRET\n"],
    [pond_fabriquant["Torgue"], "Énorme et sec!\n"],
    [pond_element["CRYO"], "Patate/Agave/Aubépine/Cactus/Betterave/Miel inclus\n"],
    [pond_element["CRYO"], "Patins non-inclus\n"],
    [pond_element["CRYO"], "Votre meilleur ami en soirée\n"],
    [pond_element["ELEC"], "Toute la pluie tombe sur eux\n"],
    [pond_element["ELEC"], "Si je te touche, t'es mort hihi!\n"],
    [pond_element["FEU"], "Hot like lava\n"],
    [pond_element["RAD"], "1984 is the new Borderlands\n"],
]

capa_grenade = Weight() << [
    ["Une grenade peut cacher un autre nabot\n"],
    ["C'est mon anniversaire mais c'est moi qui vous fais un cadeau!\n"],
    ["Mets-y la petite soeur!\n"],
    ["Boum? Boum.\n"],
    ["Message dans une bouteille\n"],
    ["Stronks\n"],
    ["Homerun! Euh...Strike!\n"],
    ["Quand il pleut des dollars, les malchanceux n'ont pas de sac\n"],
    ["Les mystères de l'orient...\n"],
    ["Votre ami téléguidé\n"],
    ["Un jour je serai le meilleur tueur!\n"],
    ["Nobel était suicidaire\n"],
    ["Mon père était ninja, mais ma mère avait un amant\n"],
    [pond_fabriquant["Contact"], "Mon premier kit de terroriste\n"],
    [pond_fabriquant["MIRV"], "On saupoudre de sucre glace\n"],
    [pond_fabriquant["Proximity"], "Svradabaldjan!\n"],
    [pond_fabriquant["Proximity"], "Jeu de jambes\n"],
    [pond_fabriquant["Proximity"], "Technologie filaire sans fil\n"],
    [pond_fabriquant["Singularity"], "Savoure l'instant\n"],
    [pond_fabriquant["Singularity"], "Elle a su trouver les maux pour me faire revenir\n"],
    [pond_fabriquant["Singularity"], "Ebouriffant\n"],
    [pond_fabriquant["Singularity"], "Eblouissant\n"],
    [pond_fabriquant["Singularity"], "Hors de mon chemin\n"],
    [pond_fabriquant["Tesla"], "Mort par mignonnerie\n"],
    [pond_fabriquant["Tesla"], "Jean-Michel Jarre: hommage\n"],
    [pond_fabriquant["Tesla"], "Jeu de piste\n"],
    [pond_fabriquant["Transfusion"], "Fabriqué par Sapudukku, le célèbre aide-soignant-ninja\n"],
    [pond_fabriquant["Transfusion"], "Oui, c'est un ananas\n"],
    [pond_fabriquant["Transfusion"], "C'est n'importe quoi\n"],
    [pond_element["CRYO"], "Attention, sol glissant\n"],
    [pond_element["ELEC"], "Plaisir d'offrir, douleur de recevoir\n"],
    [pond_element["ELEC"], "C'est comme le hula-hoop\n"],
    [pond_element["FEU"], "Ne pas utiliser en intérieur\n"],
    [pond_element["RAD"], "Les bonnes choses se partagent\n"],
    [pond_element["SLAG"], "Ça ne partira pas au lavage\n"],
]

capa_bouclier = Weight() << [
    ["Il est vivant!\n"],
    ["Jamais vous ne ploierez le genou\n"],
    ["Bouclier jeter poubelle\n"],
    ["Te mentirais-je?\n"],
    ["Comme un chevalier C.R.S.\n"],
    ["La bise sur tes fesses\n"],
    ["L'infini, c'est combien de zéros?\n"],
    ["Bien préparé, mal barré\n"],
    ["La science ne s'explique pas, elle se vit\n"],
    ["Faire chier, c'est une vocation à plein temps\n"],
    ["C'est comme le foot, sauf que c'est vous la balle\n"],
    ["Qui veut gagner du bouclier?\n"],
    ["Electrisant\n"],
    ["Les ennemis de mes ennemis sont mes ennemis\n"],
    ["Polymorphose\n"],
    ["Master Kill Steal\n"],
    ["Ma bonté te perdra\n"],
    ["Me mentionne pas, je te bloque\n"],
    ["Technologie Gravitox\n"],
    ["Que jaillisse l'eau!\n"],
    [pond_fabriquant["Absorb"], "Transfusions pour tout le monde!\n"],
    [pond_fabriquant["Adaptive"], "Il est cassé mon bouclier!\n"],
    [pond_fabriquant["Adaptive"], "Votre assistant de nettoyage\n"],
    [pond_fabriquant["Adaptive"], "Continue ça m'amuse\n"],
    [pond_fabriquant["Adaptive"], "Vous n'aurez jamais autant d'amis\n"],
    [pond_fabriquant["Booster"], "Tendre la joue\n"],
    [pond_fabriquant["Booster"], "Se faire avoiner n'a jamais été aussi sympa\n"],
    [pond_fabriquant["Booster"], "Bouclier sexuellement transmissible\n"],
    [pond_fabriquant["Lifeline"], "Juste une mise au point\n"],
    [pond_fabriquant["Lifeline"], "SUCC\n"],
    [pond_fabriquant["Lifeline"], "Un petit dernier pour la route?\n"],
    [pond_fabriquant["Nova"], "Phénix jubilatoire\n"],
    [pond_fabriquant["Nova"], "Très distingué\n"],
    [pond_fabriquant["Nova"], "Un va-et-vient désagréable\n"],
    [pond_fabriquant["Raid"], "N'oubliez pas de headbanguer\n"],
    [pond_fabriquant["Raid"], "Rocket-man!!!\n"],
    [pond_fabriquant["Raid"], "J'aime vivre dangereusement\n"],
    [pond_fabriquant["Raid"], "Tellement pratique pour retrouver ses clés de bagnole\n"],
    [pond_fabriquant["Raid"], "Ta gueule et fonce\n"],
    [pond_fabriquant["Shield"], "Attention, bouclier opiniâtre\n"],
    [pond_fabriquant["Shield"], "Mais papa, tu triches?\n"],
    [pond_fabriquant["Shield"], "Tout ou rien, pendejo\n"],
    [pond_fabriquant["Spike"], "Toute rose a ses épines\n"],
    [pond_fabriquant["Turtle"], "J'ai vraiment pas mal\n"],
    [pond_fabriquant["Turtle"], "Pr0p hunt l0lz\n"],
]

# arme_spe = dict()
arme_spe= {"" : {"" : Sequence() }}
arme_spe.clear()
#grenade_spe = dict()
#bouclier_spe = dict()

#TODO When weight.nbrTirage as ValueIf implemented : nbr_tirage = x-pretirage
# use nbr_of_constructor_properties

# TODO : the unique capacities must be drawn after every other capacity
#   Because : if a elementary prop is drawn along the way, will inbalance chances of elem unic capas
#   How : raise a flag and resolve at end of generation

arme_spe["COMMUN"]={}
arme_spe["COMMUN"]["PISTOLET"] =\
arme_spe["COMMUN"]["ASSAUT"] =\
arme_spe["COMMUN"]["MITRAILLETTE"] =\
arme_spe["COMMUN"]["POMPE"] =\
arme_spe["COMMUN"]["SNIPER"] =\
    Weight(1 - int(nbr_of_constructor_properties)) << [
        [10, 1, " - Baillonette\n"],
        [10, 1, " - Viseur X2\n"],
        [6, 1, " - Viseur X4\n"],
        [3, 1, " - Viseur X6\n"],
        [11, " - 1 augmentation de dé\n"],
        [15, " - -1 Difficulté de visée\n"],
        [15, " - +2 Magasin\n"],
        [10, " - Dégâts critiques +25%\n"],
        [10, " - +1 Dégâts\n"],
        [MulOp(10, can_element), 1, sel_element],
    ]
    
arme_spe["INCOMMUN"]={}
arme_spe["INCOMMUN"]["PISTOLET"] =\
arme_spe["INCOMMUN"]["ASSAUT"] =\
arme_spe["INCOMMUN"]["MITRAILLETTE"] =\
arme_spe["INCOMMUN"]["POMPE"] =\
arme_spe["INCOMMUN"]["SNIPER"] =\
    Weight(2 - int(nbr_of_constructor_properties)) << [
        [8, 1, " - Baillonette\n"],
        [9, 1, " - Viseur X2\n"],
        [6, 1, " - Viseur X4\n"],
        [4, 1, " - Viseur X6\n"],
        [11, " - 1 augmentation de dé\n"],
        [15, " - -1 Difficulté de visée\n"],
        [15, " - +2 Magasin\n"],
        [10, " - Dégâts critiques +25%\n"],
        [10, " - +1 Dégâts\n"],
        [MulOp(12, can_element), 1, sel_element],
    ]

arme_spe["RARE"]={}
arme_spe["RARE"]["PISTOLET"] =\
arme_spe["RARE"]["ASSAUT"] =\
arme_spe["RARE"]["MITRAILLETTE"] =\
arme_spe["RARE"]["POMPE"] =\
arme_spe["RARE"]["SNIPER"] =\
    Weight(3 - int(nbr_of_constructor_properties)) << [
        [7, 1, " - Baillonette\n"],
        [8, 1, " - Viseur X2\n"],
        [6, 1, " - Viseur X4\n"],
        [4, 1, " - Viseur X6\n"],
        [11, " - 1 augmentation de dé\n"],
        [10, " - -1 Difficulté de visée\n"],
        [10, " - +2 Magasin\n"],
        [10, " - Dégâts critiques +25%\n"],
        [10, " - +1 Dégâts\n"],
        [MulOp(14, can_element), 1, sel_element],
        [10, 1, capa_arme],
    ]

arme_spe["EPIQUE"]={}
arme_spe["EPIQUE"]["PISTOLET"] =\
arme_spe["EPIQUE"]["ASSAUT"] =\
arme_spe["EPIQUE"]["MITRAILLETTE"] =\
arme_spe["EPIQUE"]["POMPE"] =\
arme_spe["EPIQUE"]["SNIPER"] =\
    Weight(4 - int(nbr_of_constructor_properties)) << [
        [7, 1, " - Baillonette\n"],
        [7, 1, " - Viseur X2\n"],
        [7, 1, " - Viseur X4\n"],
        [5, 1, " - Viseur X6\n"],
        [12, " - 1 augmentation de dé\n"],
        [7, " - -1 Difficulté de visée\n"],
        [7, " - +2 Magasin\n"],
        [10, " - Dégâts critiques +25%\n"],
        [7, " - +1 Dégâts\n"],
        [MulOp(16, can_element), 1, sel_element],
        [15, 1, capa_arme],
    ]

arme_spe["ETECH"]={}
arme_spe["ETECH"]["PISTOLET"] =\
arme_spe["ETECH"]["ASSAUT"] =\
arme_spe["ETECH"]["MITRAILLETTE"] =\
arme_spe["ETECH"]["POMPE"] =\
arme_spe["ETECH"]["SNIPER"] =\
Weight(5 - int(nbr_of_constructor_properties)) << [
    [5, 1, " - Baillonette\n"],
    [6, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [6, 1, " - Viseur X6\n"],
    [13, " - 1 augmentation de dé\n"],
    [5, " - -1 Difficulté de visée\n"],
    [5, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [6, " - +1 Dégâts\n"],
    [MulOp(18, can_element), 1, sel_element],
    [20, 1, capa_arme],
]

arme_spe["LEGENDAIRE"]={}
arme_spe["LEGENDAIRE"]["PISTOLET"] =\
arme_spe["LEGENDAIRE"]["ASSAUT"] =\
arme_spe["LEGENDAIRE"]["MITRAILLETTE"] =\
arme_spe["LEGENDAIRE"]["POMPE"] =\
arme_spe["LEGENDAIRE"]["SNIPER"] =\
Sequence() << [
Weight(5) << [
    [5, 1, " - Baillonette\n"],
    [6, 1, " - Viseur X2\n"],
    [6, 1, " - Viseur X4\n"],
    [6, 1, " - Viseur X6\n"],
    [14, " - 1 augmentation de dé\n"],
    [5, " - -1 Difficulté de visée\n"],
    [5, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [5, " - +1 Dégâts\n"],
    [MulOp(20, can_element), 1, sel_element],
],
capa_arme,
]

# GRENADES

arme_spe["COMMUN"]["GRENADE"] = Weight(1) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [1, 1, capa_grenade],
    [MulOp(2, can_element), sel_element],
]

arme_spe["INCOMMUN"]["GRENADE"] = Weight(2) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [2, 1,capa_grenade],
    [MulOp(3, can_element), 1, sel_element],
]

arme_spe["RARE"]["GRENADE"] = Weight(3) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [2, 1, capa_grenade],
    [MulOp(3, can_element), 1, sel_element],
]

arme_spe["EPIQUE"]["GRENADE"] = Weight(4) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [3, 1, capa_grenade],
    [MulOp(4, can_element), 1, sel_element],
]

arme_spe["ETECH"]["GRENADE"] = Weight(5) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [3, 1, capa_grenade],
    [MulOp(4, can_element), 1, sel_element],
]

arme_spe["LEGENDAIRE"]["GRENADE"] = Sequence() << [
Weight(5) << [
    [3, " - +2 Dégâts\n"],
    [3, " - -1 Difficulté de visée\n"],
    [1, " - +1D20 Bonus\n"],
    [MulOp(4, can_element), 1, sel_element],
],
capa_grenade
]

# BOUCLIERS

arme_spe["COMMUN"]["BOUCLIER"] = Weight(1) << [
    [2, " - << [[1d3+3]] Capacité\n"],
    [2, " - << [[1d3+1]] Cadence/tour\n"],
    [1, " - 1 Amélioration compétence spéciale\n"],
]

arme_spe["INCOMMUN"]["BOUCLIER"] = Weight(2) << [
    [2, " - << [[1d3+3]] Capacité\n"],
    [2, " - << [[1d3+1]] Cadence/tour\n"],
    [1, " - 1 Amélioration compétence spéciale\n"],
]

arme_spe["RARE"]["BOUCLIER"] = Weight(3) << [
    [4, " - << [[1d3+3]] Capacité\n"],
    [4, " - << [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [1, 1, capa_bouclier],
]

arme_spe["EPIQUE"]["BOUCLIER"] = Weight(4) << [
    [4, " - << [[1d3+3]] Capacité\n"],
    [4, " - << [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [2, 1, capa_bouclier],
]

arme_spe["ETECH"]["BOUCLIER"] = Weight(5) << [
    [3, " - << [[1d3+3]] Capacité\n"],
    [3, " - << [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
    [2, 1, capa_bouclier],
]

arme_spe["LEGENDAIRE"]["BOUCLIER"] = Sequence() << [
Weight(5) << [
    [3, " - + [[1d3+3]] Capacité\n"],
    [3, " - + [[1d3+1]] Cadence/tour\n"],
    [2, " - 1 Amélioration compétence spéciale\n"],
],
capa_bouclier
]