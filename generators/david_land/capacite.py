# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence
from ponderation import pond_type, pond_fabriquant, pond_element, can_element
from ponderation import nbr_of_constructor_properties
from macro.calc import SubOp, MulOp

#################################################
#                WEAPON BONUSES                 #
#################################################

capa_arme = Weight().extend([
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
])

capa_grenade = Weight().extend([
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
])

capa_bouclier = Weight().extend([
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
])

arme_spe = dict()
grenade_spe = dict()
bouclier_spe = dict()

#TODO When weight.nbrTirage as ValueIf implemented : nbr_tirage = x-pretirage
# use nbr_of_constructor_properties

# TODO : the unique capacities must be drawn after every other capacity
#   Because : if a elementary prop is drawn along the way, will inbalance chances of elem unic capas
#   How : raise a flag and resolve at end of generation

# TODO : elementary properties

arme_spe["COMMUN"] = Weight(1, False).extend([
    [10, " - Baillonette\n"],
    [10, " - Viseur X2\n"],
    [6, " - Viseur X4\n"],
    [3, " - Viseur X6\n"],
    [11, " - 1 augmentation de dé\n"],
    [15, " - -1 Difficulté de visée\n"],
    [15, " - +2 Magasin\n"],
    [10, " - Dégâts critiques +25%\n"],
    [10, " - +1 Dégâts\n"],
    [MulOp(10, can_element), "PROP_ELEMENTAIRE\n"],
])

arme_spe["INCOMMUN"] = Weight(2, False).extend([
    [8, " - Baillonette\n"],
    [9, " - Viseur X2\n"],
    [6, " - Viseur X4\n"],
    [4, " - Viseur X6\n"],
    [11, 0, " - 1 augmentation de dé\n"],
    [15, 0, " - -1 Difficulté de visée\n"],
    [15, 0, " - +2 Magasin\n"],
    [10, 0, " - Dégâts critiques +25%\n"],
    [10, 0, " - +1 Dégâts\n"],
    [MulOp(12, can_element), "PROP_ELEMENTAIRE\n"],
])

arme_spe["RARE"] = Weight(3, False).extend([
    [7, " - Baillonette\n"],
    [8, " - Viseur X2\n"],
    [6, " - Viseur X4\n"],
    [4, " - Viseur X6\n"],
    [11, 0, " - 1 augmentation de dé\n"],
    [10, 0, " - -1 Difficulté de visée\n"],
    [10, 0, " - +2 Magasin\n"],
    [10, 0, " - Dégâts critiques +25%\n"],
    [10, 0, " - +1 Dégâts\n"],
    [MulOp(14, can_element), "PROP_ELEMENTAIRE\n"],
    [10, capa_arme],
])

arme_spe["EPIQUE"] = Weight(4, False).extend([
    [7, " - Baillonette\n"],
    [7, " - Viseur X2\n"],
    [7, " - Viseur X4\n"],
    [5, " - Viseur X6\n"],
    [12, 0, " - 1 augmentation de dé\n"],
    [7, 0, " - -1 Difficulté de visée\n"],
    [7, 0, " - +2 Magasin\n"],
    [10, 0, " - Dégâts critiques +25%\n"],
    [7, 0, " - +1 Dégâts\n"],
    [MulOp(16, can_element), "PROP_ELEMENTAIRE\n"],
    [15, capa_arme],
])

arme_spe["ETECH"] = Weight(5, False).extend([
    [5, " - Baillonette\n"],
    [6, " - Viseur X2\n"],
    [6, " - Viseur X4\n"],
    [6, " - Viseur X6\n"],
    [13, 0, " - 1 augmentation de dé\n"],
    [5, 0, " - -1 Difficulté de visée\n"],
    [5, 0, " - +2 Magasin\n"],
    [10, 0, " - Dégâts critiques +25%\n"],
    [6, 0, " - +1 Dégâts\n"],
    [MulOp(18, can_element), "PROP_ELEMENTAIRE\n"],
    [20, capa_arme],
])

arme_spe["LEGENDAIRE"] = Sequence().extend([
    Weight(5, False).extend([
        [5, " - Baillonette\n"],
        [6, " - Viseur X2\n"],
        [6, " - Viseur X4\n"],
        [6, " - Viseur X6\n"],
        [14, 0, " - 1 augmentation de dé\n"],
        [5, 0, " - -1 Difficulté de visée\n"],
        [5, 0, " - +2 Magasin\n"],
        [10, 0, " - Dégâts critiques +25%\n"],
        [5, 0, " - +1 Dégâts\n"],
        [MulOp(20, can_element), "PROP_ELEMENTAIRE\n"],
    ]),
    capa_arme
])

# GRENADES

grenade_spe["COMMUN"] = Weight(1, False).extend([
    [3, 0, " - +2 Dégâts\n"],
    [3, 0, " - -1 Difficulté de visée\n"],
    [1, 0, " - +1D20 Bonus\n"],
    [1, capa_grenade],
    [MulOp(2, can_element), "PROP_ELEMENTAIRE\n"],
])

grenade_spe["INCOMMUN"] = Weight(2, False).extend([
    [3, 0, " - +2 Dégâts\n"],
    [3, 0, " - -1 Difficulté de visée\n"],
    [1, 0, " - +1D20 Bonus\n"],
    [2, capa_grenade],
    [MulOp(3, can_element), "PROP_ELEMENTAIRE\n"],
])

grenade_spe["RARE"] = Weight(3, False).extend([
    [3, 0, " - +2 Dégâts\n"],
    [3, 0, " - -1 Difficulté de visée\n"],
    [1, 0, " - +1D20 Bonus\n"],
    [2, capa_grenade],
    [MulOp(3, can_element), "PROP_ELEMENTAIRE\n"],
])

grenade_spe["EPIQUE"] = Weight(4, False).extend([
    [3, 0, " - +2 Dégâts\n"],
    [3, 0, " - -1 Difficulté de visée\n"],
    [1, 0, " - +1D20 Bonus\n"],
    [3, capa_grenade],
    [MulOp(4, can_element), "PROP_ELEMENTAIRE\n"],
])

grenade_spe["ETECH"] = Weight(5, False).extend([
    [3, 0, " - +2 Dégâts\n"],
    [3, 0, " - -1 Difficulté de visée\n"],
    [1, 0, " - +1D20 Bonus\n"],
    [3, capa_grenade],
    [MulOp(4, can_element), "PROP_ELEMENTAIRE\n"],
])

grenade_spe["LEGENDAIRE"] = Sequence().extend([
    Weight(5, False).extend([
        [3, 0, " - +2 Dégâts\n"],
        [3, 0, " - -1 Difficulté de visée\n"],
        [1, 0, " - +1D20 Bonus\n"],
        [MulOp(4, can_element), "PROP_ELEMENTAIRE\n"],
    ]),
    capa_grenade
])

# BOUCLIERS

bouclier_spe["COMMUN"] = Weight(1, False).extend([
    [2, " - + [[1d3+3]] Capacité\n"],
    [2, " - + [[1d3+1]] Cadence/tour\n"],
    [1, " - 1 Amélioration compétence spéciale\n"],
])

bouclier_spe["INCOMMUN"] = Weight(2, False).extend([
    [2, 0, " - + [[1d3+3]] Capacité\n"],
    [2, 0, " - + [[1d3+1]] Cadence/tour\n"],
    [1, 0, " - 1 Amélioration compétence spéciale\n"],
])

bouclier_spe["RARE"] = Weight(3, False).extend([
    [4, 0, " - + [[1d3+3]] Capacité\n"],
    [4, 0, " - + [[1d3+1]] Cadence/tour\n"],
    [2, 0, " - 1 Amélioration compétence spéciale\n"],
    [1, capa_bouclier],
])

bouclier_spe["EPIQUE"] = Weight(4, False).extend([
    [4, 0, " - + [[1d3+3]] Capacité\n"],
    [4, 0, " - + [[1d3+1]] Cadence/tour\n"],
    [2, 0, " - 1 Amélioration compétence spéciale\n"],
    [2, capa_bouclier],
])

bouclier_spe["ETECH"] = Weight(5, False).extend([
    [3, 0, " - + [[1d3+3]] Capacité\n"],
    [3, 0, " - + [[1d3+1]] Cadence/tour\n"],
    [2, 0, " - 1 Amélioration compétence spéciale\n"],
    [2, capa_bouclier],
])

bouclier_spe["LEGENDAIRE"] = Sequence().extend([
    Weight(5, False).extend([
        [3, 0, " - + [[1d3+3]] Capacité\n"],
        [3, 0, " - + [[1d3+1]] Cadence/tour\n"],
        [2, 0, " - 1 Amélioration compétence spéciale\n"],
    ]),
    capa_bouclier
])