# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:03:13 2020

@author: Ehlion
| Implementation of the character generation
| from http://cyberpunk2021.free.fr/creation2.php?lng=fr
"""

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import Title, Label
from wordgenerator.Generator import Generator

#################################################
#                   EVENEMENT                  #
#################################################

#Table 2A
chance = Interval("1d100") << [
    [ 1,  5, "Rentrée financière ([[1d5]] x 100 Euro)"],
    [ 6, 10, "Grosse affaire ! ([[1d10]] x 100 Euro)"],
    [11, 15, "Gagnez [[1d10]] x 100 Euro en matériel ou cyberware"],
    [16, 20, "Vous rencontrez un sensei (+2/+1 dans un art martial)"],
    [21, 25, "Vous rencontrez un instructeur (+2/+1 dans une compétence de REF autre qu'un art martial)"],
    [26, 30, "Vous rencontrez un professeur (+2/+1 dans une compétence d'INT)"],
    [31, 35, "Vous rencontrez un entraîneur (+2/+1 dans une compétence de CON ou à Athlétisme)"],
    [36, 40, "Vous rencontrez un professeur de technique (+2/+1 dans une compétence de TECH)"],
    [41, 45, "École de charme (+2/+1 dans une compétence d'EMP)"],
    [46, 50, "Vous découvrez la mode (+2/+1 dans une compétence de BT)"],
    [51, 55, "Vous apprenez une langue étrangère (+2/+1 dans une compétence de langue)"],
    [56, 60, "Vous apprenez les bases du Netrun (+2/+1 dans la compétence Interface)"],
    [61, 65, "Vous vivez dans la Rue (+2/+1 dans une compétence de SF)"],
    [66, 70, "Un gang du coin vous trouve sympa (avantage 'Rang' à 2 PCs, peut être augmenté)"],
    [71, 75, "Vous vous faites des amis nomades (avantage 'Famille' à 2 PCs, peut être augmenté)"],
    [76, 80, "Vous gagnez un contact ('Contact' à 2 PCs, peut être augmenté; à créer sur la table AEC)"],
    [81, 85, "Quelqu'un vous doit une faveur (à créer sur la table AEC)"],
    [86, 90, "Vous vous faites un nouvel ami (à créer sur la table AEC)"],
    [91, 95, "Un ennemi disparaît/meurs (choisissez en un, si vous n'avez pas d'ennemis relancez)"],
    [96, 100, "Vous avez fait quelque chose de vraiment impressionnant (+2 Réputation positive)"],
]

#Table 3B
malchance_blessure = Sequence() << [
    Interval("1d100") << [
        [ 1,  5, "Brûlures mineures *3*"],
        [ 6, 10, "Brûlures sérieuses *1* *3*"],
        [11, 15, "Perforation(s) *3*"],
        [16, 20, "Blessure par balle : a traversé proprement *3*"],
        [21, 25, "Blessure par balle : projectile resté dans la plaie, retiré *3*"],
        [26, 30, "Blessure par balle : projectile resté dans la plaie, jamais retiré *2* *3*"],
        [31, 35, "Blessure par balle : fragmentée, grosse blessure de sortie *1* *3*"],
        [36, 40, "Fracture mal rétablie *1* *2*"],
        [41, 45, "Lésions internes *1* *2*"],
        [46, 50, "Fracture du crâne : dégâts neurologiques mineurs"],
        [51, 55, "Fracture du crâne : dégâts neurologiques sévères"],
        [56, 60, "Éclats non retirés *2*"],
        [61, 65, "Dents en moins *3*"],
        [66, 70, "Doigts ou orteils en moins *1*"],
        [71, 75, "Perte d'un oeil *1*"],
        [76, 80, "Perte d'une oreille *2* *3*"],
        [81, 85, "Perte du nez *3*"],
        [86, 90, "Main/pied/membre tranché *1*"],
        [91, 95, "Blessure au dos *2*"],
        [96, 100, "Cicatrice impressionnante *3*"],
    ],
    # Légende
    "*1* - La blessure peut être guérie avec un remplacement cybernétique ou développé en cuve.",
    "*2* - La chirurgie peut remédier au problème en extrayant quelque chose ou en soignant directement.",
    "*3* - Une reconstruction faciale et/ou de la chirurgie esthétique peuvent corriger certains effets de cette blessure. Voir les règles de CP2020 sur l'amélioration de la BT.",
]

#Table 3A
malchance = Interval("1d100") << [
    [ 1,  5, "Perte financière ([[1d5]] x 100 Euro)"],
    [ 6, 10, "Dette ([[1d10]] x 100 Euro - payez maintenant, ou vous le payerez plus tard !)"],
    [11, 15, "Vous contractez une maladie; une caractéristique au hasard est réduite de 1"],
    [16, 20, "Dépendance. INT, REF, BODY ou EMP réduit de 1"],
    [21, 25, Title("Blessure (Ou désavantage 'Vieille Blessure') : ", malchance_blessure)],
    [26, 30, "Un ami, un amant ou une maîtresse meurt ou disparaît (tirez en un au hasard)"],
    [31, 35, "Un contact meurt ou disparaît (tirez en un au sort)"],
    [36, 40, "Vous vous faites un ennemi (à créer sur la table AEC)"],
    [41, 45, "Quelqu'un veut votre peau (le MJ créé un ennemi secret)"],
    [46, 50, "Trahi par un ami (un ami devient un ennemi)"],
    [51, 55, "Arrêté mais pas condamné ([[1d5]] semaines de prison)"],
    [56, 60, "Arrêté et condamné pour un délit mineur ([[1d10]] x 10 Euro d'amende)"],
    [61, 65, "Arrêté et condamné pour un crime ([[1d12]] mois en prison)"],
    [66, 70, "Vous êtes sous le coup d'un mandat d'arrêt quelque part (choisissez)"],
    [71, 75, "Un de vos implants tombe en panne, 1/2 prix d'achat pour le réparer"],
    [76, 80, "Vous avez fâché un gang, une bande de nomades ou un groupe du genre (au choix du MJ)"],
    [81, 85, "Vous êtes traqué par une corporation (tirez ou choisissez)"],
    [86, 90, "Vous devez une faveur à quelqu'un (à créer sur la table AEC)"],
    [91, 95, "Blâmé pour quelque chose que vous avez fait... ou pas (+1 Réputation négative)"],
    [96, 100, "Grossesse imprévue ! Il va falloir gérer, Choomba."],
]

#Table 4A
ami = Interval("1d100") << [
    [ 1,  4, "Un partenaire"],
    [ 5,  8, "Un collègue"],
    [ 9, 12, "Un contact"],
    [13, 16, "Un ex-amant ou une ex-maîtresse"],
    [17, 20, "Un ancien ennemi"],
    [21, 24, "Un ancien ami d'enfance"],
    [25, 28, "Un membre de votre famille, un proche"],
    [29, 32, "Vous vous rencontrez grâce à un intérêt commun"],
    [33, 36, "Vous lui avez sauvé la vie"],
    [37, 40, "Il vous a sauvé la vie"],
    [41, 44, "A une fête"],
    [45, 48, "Une personne pour qui vous avez travaillé"],
    [49, 52, "Une personne qui a travaillé pour vous"],
    [53, 56, "Vous vous rencontrez grâce à un ami commun"],
    [57, 60, "Vous vous rencontrez grâce à un 'Blind Date'"],
    [61, 64, "Vous étiez à l'école ensemble"],
    [65, 68, "Vous vous rencontrez grâce à un ennemi commun"],
    [69, 72, "A un concert"],
    [73, 76, "Dans un bar"],
    [77, 80, "Dans un centre commercial"],
    [81, 84, "Vous vous rencontrez grâce à un amant ou une maîtresse commun"],
    [85, 88, "Il vous a vendu quelque chose"],
    [89, 92, "Vous lui avez vendu quelque chose"],
    [93, 96, "Il vous a fait une faveur"],
    [97, 100, "Vous lui avez fait une faveur"],
]

#Table 5A
ennemi = Sequence() << [
    Title("LE CONNAISSIEZ-VOUS ?", Interval("1d100") << [
        [ 1, 10, "Ex-ami"],
        [11, 20, "Ex-amant ou ex-maîtresse"],
        [21, 30, "Un membre de la famille"],
        [31, 40, "Une personne pour qui vous travaillez"],
        [41, 50, "Une personne travaillant pour vous"],
        [51, 60, "Un partenaire ou un collègue"],
        [61, 100, "Un étranger complet"],
    ]),
    Title("QUI A COMMIS LA FAUTE ?", Interval("1d100") << [
        [ 1, 50, "C'est vous."],
        [51, 100, "C'est lui ou elle."],
    ]),
    Title("QUE S'EST-IL PASSÉ ?", Interval("1d100") << [
        [ 1,  4, "A tenté de tuer l'autre"],
        [ 5,  8, "A essayé de faire chanter l'autre"],
        [ 9, 12, "A révélé un secret"],
        [13, 16, "A monté une accusation contre l'autre"],
        [17, 20, "A déserté ou trahi"],
        [21, 24, "A fait des menaces physiques"],
        [25, 28, "A fait des menaces de mort"],
        [29, 32, "A endommagé/détruit des biens"],
        [33, 36, "A causé à l'autre une blessure (directement ou indirectement)"],
        [37, 40, "A causé une blessure à un parent, un ami, un amant ou une maîtresse"],
        [41, 44, "A causé la mort d'un parent, d'un ami, d'un amant ou d'une maîtresse"],
        [45, 48, "A fait perdre la face ou son statut à l'autre"],
        [49, 52, "A provoqué la fin d'une amitié"],
        [53, 56, "A fait perdre un emploi ou un contrat à l'autre"],
        [57, 60, "A repoussé les avances de l'autre"],
        [61, 64, "A volé des biens (valeur [[1D10]] x 10 Euro)"],
        [65, 68, "A volé de l'argent ([[1D10]] x 10 Euro)"],
        [69, 72, "Personnalités incompatibles"],
        [73, 76, "Désaccord mineur (quelque chose de bête)"],
        [77, 80, "Désaccord profond"],
        [81, 84, "A insulté un parent, un ami, un amant ou une maîtresse"],
        [85, 88, "A insulté ou accusé l'autre"],
        [89, 92, "A tenté de séduire l'amant ou la maîtresse de l'autre"],
        [93, 96, "A couché avec l'amant ou la maîtresse de l'autre"],
        [97, 100, "A fait échouer le plan de l'autre"],
    ]),
    Title("QUI EST L'OFFENSÉ ?", Interval("1d100") << [
        [ 1, 25, "Vous le ou la haïssez"],
        [26, 50, "Il ou elle vous hait"],
        [51, 100, "Le sentiment est mutuel"],
    ]),
    Title("QU'ALLEZ VOUS FAIRE (Si offensé uniquement) ?", Weight() << [
        ["Dire du mal de lui ou d'elle dans son dos."],
        ["Le crucifier verbalement à la moindre opportunité."],
        ["Le tabasser jusqu'à le laisser à moitié mort."],
        ["Tuer l'enfoiré à la première occasion."],
        ["L'éviter comme la peste."],
        ["Saboter ses projets indirectement."],
        ["Lui rendre la vie infernale (monter un coup contre lui, détourner ses amis, séduire sa maîtresse(s)...)."],
        ["Le blesser de la même manière qu'il vous a blessé, oeil pour oeil."],
        ["Sympathiser avec lui en attendant le meilleur moment pour le trahir."],
        ["Il n'est pas digne de votre attention. Ignorez le et faites comme s'il n'existait pas."],
    ]),
]

amour = Sequence() << [
    #Table 6A
    Title("COMMENT VOUS ÊTES VOUS RENCONTRÉS ?", Interval("1d100") << [
        [ 1,  5, "Un(e) partenaire"],
        [ 6, 10, "Un(e) collègue"],
        [11, 15, "Un contact"],
        [16, 20, "Un(e) ex-amant (maîtresse)"],
        [21, 25, "Un(e) ancien(ne) ennemi(e)"],
        [26, 30, "Un(e) ancien(ne) ami(e) d'enfance"],
        [31, 35, "Vous vous rencontrez grâce à un intérêt commun"],
        [36, 40, "Vous lui avez sauvé la vie"],
        [41, 45, "Il (elle) vous a sauvé la vie"],
        [46, 50, "A une fête"],
        [51, 55, "Une personne pour qui vous avez travaillé"],
        [56, 60, "Une personne qui a travaillé pour vous"],
        [61, 65, "Vous vous rencontrez grâce à un ami commun"],
        [66, 70, "Vous vous rencontrez grâce à un 'Blind Date'"],
        [71, 75, "Vous étiez à l'école ensemble"],
        [76, 80, "Vous vous rencontrez grâce à un ennemi commun"],
        [81, 85, "A un concert"],
        [86, 90, "Dans un bar"],
        [91, 95, "Dans un centre commercial"],
        [96, 100, "Vous vous rencontrez grâce à un amant ou une maîtresse commun"],
    ]),
    Title("DÉROULEMENT ?",
        Weight() << [
            [3, "Histoire rapide et rendez-vous brûlants."],
            [4, "Histoire d'amour heureuse."],
            #Table 6B
            [1, Title("Histoire d'amour tragique.", Interval("1d100") << [
                [ 1, 16, "Cela n'a pas collé entre vous"],
                [17, 22, "La personne aimée vous a laissé une lettre et a filé"],
                [23, 28, "La personne aimée est morte d'une maladie incurable"],
                [29, 34, "La personne aimée a été tué dans un accident"],
                [35, 40, "La personne aimée a disparu ou a été kidnappé"],
                [41, 46, "Un but personnel vous a séparés"],
                [47, 52, "La personne aimée a perdu la raison"],
                [53, 58, "La personne aimée s'est suicidée"],
                [59, 64, "La personne aimée a été tuée dans un combat"],
                [65, 70, "La personne aimée a été incarcérée (1D10 ans)"],
                [71, 76, "La personne aimée a été assassinée par un ennemi (choisissez lequel)"],
                [77, 82, "La personne aimée vous a quitté pour un ami (choisissez lequel)"],
                [83, 88, "La personne aimée vous a quitté pour un ennemi (choisissez lequel)"],
                [89, 94, "La personne aimée vous manipulait"],
                [95, 100, "La personne aimée vous a volé [[1d10]] x 100 Euro et s'est sauvée"],
            ])],
            #Table 6C
            [2, Title("Histoire d'amour problématique.", Interval("1d100") << [
                [ 1,  7, "La famille de la personne aimée vous hait"],
                [ 8, 14, "Les amis de la personne aimée vous haïssent"],
                [15, 21, "Votre famille hait la personne que vous aimez"],
                [22, 28, "Vos amis haïssent la personne que vous aimez"],
                [29, 35, "La personne aimée veut fréquenter un autre milieu"],
                [36, 42, "Vous voulez fréquenter un autre milieu"],
                [43, 49, "Vous êtes séparés d'une façon ou d'une autre"],
                [50, 56, "Vous n'arrêtez pas de vous battre"],
                [57, 62, "L'un de vous est d'une jalousie maladive"],
                [63, 68, "La personne aimée commence à chercher ailleurs"],
                [69, 74, "Vous commencez à chercher ailleurs"],
                [75, 80, "L'ex de la personne aimée veut votre peau"],
                [81, 87, "La personne aimée est dépendante à une drogue"],
                [88, 93, "La personne aimée est dans le coma"],
                [94, 100, "La personne aimée est mariée"],
            ])],
    ]),
    #Table 6D
    Title("SENTIMENTS MUTUELS ?(si Applicable)", Weight() << [
        ["La personne aimée vous aime toujours"],
        ["Vous l'aimez toujours"],
        ["Vous vous aimez toujours"],
        ["Vous la haïssez"],
        ["Elle vous hait"],
        ["Vous vous haïssez mutuellement"],
        ["Vous êtes restés amis"],
        ["Plus de sentiment des deux côtés, c'est fini"],
        ["Vous l'aimez mais il ou elle vous déteste"],
        ["Il ou elle vous aime mais vous le ou la haïssez"],
    ]),
]

#Table 1A
evenement = Weight() << [
    [3, Title("Vous avez de la chance", chance)],
    [3, Title("Un désastre frappe!", malchance)],
    [3, Title("Vous vous faites un ami", ami)],
    [3, Title("Vous vous faites un ennemi", ennemi)],
    [4, Title("Vie romantique", amour)],
    [4, "Rien ne vous est arrivé"]
]

#################################################
#                     AEC 1.0                   #
#################################################

sexe = Weight() << [
    "Masculin",
    "Feminin"
]


# Sous-Table 1.1
division_police = Interval("1d100") << [
    [ 1,  3, "Divisions des Affaire Internes (DIA)"],
    [ 4,  8, "Administration"],
    [ 9, 13, "Section Sécurité du Réseau (NetSec)"],
    [14, 18, "Homicide"],
    [19, 23, "Vice"],
    [24, 28, "Cambriolage"],
    [29, 33, "Enquêtes Spéciales (EnS)"],
    [34, 37, "Special Weapons And Tactics (SWAT)"],
    [38, 41, "Cyborg Suppression Unit (CSU, MaxTac, C-SWAT)"],
    [42, 46, "Section anti-émeutes"],
    [47, 50, "Patrouille aérienne"],
    [51, 67, "Patrouille motorisée"],
    [68, 82, "Circulation"],
    [83, 98, "Patrouille à pieds"],
    [99, 100, "Autoroute"],
]

occupation = Interval("1d100") << [
    [ 1, 20, Label("Emploi légal", Interval("1d100") << [
        [ 1,  6, "Comptable"],
        [ 7, 13, "Employé (vente ou autre)"],
        [14, 19, "Ouvrier du bâtiment"],
        [20, 25, "Coursier"],
        [26, 31, "Médecin/Infirmière"],
        [32, 37, "Ingénieur/Technicien"],
        [38, 44, "Concierge"],
        [45, 50, "Pilote"],
        [51, 56, "Secrétaire"],
        [57, 61, "Scientifique"],
        [62, 68, "Travailleur social"],
        [69, 75, "Lycéen"],
        [76, 80, "Étudiant"],
        [81, 87, "Professeur, lycée"],
        [88, 93, "Professeur, université"],
        [94, 100, "Chauffeur de bus/camion"],
    ])],
    [21, 35, Label("Street Trash", Interval("1d100") << [
        [ 1,  2, "Assassin"],
        [ 3,  7, "Barman"],
        [ 8, 11, "Garde du corps"],
        [12, 15, "Videur"],
        [16, 20, "Chauffeur de taxi"],
        [21, 23, "Escroc"],
        [24, 26, "Détenu"],
        [27, 28, "Faussaire"],
        [29, 30, "Producteur de drogue"],
        [31, 36, "Dealer"],
        [37, 40, "Ex-détenu"],
        [41, 44, "Fixer/Receleur"],
        [45, 49, "Membre de gang"],
        [50, 53, "Prostitué(e) (sans licence)"],
        [54, 58, "Junkie"],
        [59, 62, "Mercenaire"],
        [63, 65, "Netrunner"],
        [66, 69, "Nomade"],
        [70, 72, "Prostitué(e) (avec licence)"],
        [73, 74, "Charcudoc"],
        [75, 78, "Ronin"],
        [79, 82, "Contrebandier"],
        [83, 88, "Vendeur ambulant"],
        [89, 90, "Techie"],
        [91, 94, "Voleur/Cambrioleur"],
        [95, 100, "Vagabond"],
    ])],
    [36, 50, Label("Loi/Secours", Interval("1d100") << [
        [ 1,  5, "Chasseur de primes"],
        [ 6, 20, Label("Flic", division_police)],
        [21, 36, "Pompier"],
        [37, 40, "Avocat"],
        [41, 55, "Ambulancier"],
        [56, 61, "Gardien de prison"],
        [62, 75, "Détective privé"],
        [76, 90, "Vigile"],
        [91, 95, Label("Flic à la retraite", division_police)],
        [96, 100, "Milicien"],
    ])],
    [51, 65, Sequence() << [
        Label("Crime Organisé", Weight() << [
            [1, "Assassin"],
            [2, "Garde du corps"],
            [1, "Bookmaker"],
            [1, "Faussaire"],
            [3, "Homme de main"],
            [1, "Petit caïd"],
            [1, "Netrunner"],
        ]),
        # Sous-Table 1.2
        Label("Organisation  ", Weight() << [
            [4, "Les Yakuza (japonais)"],
            [3, "La Mafia (surtout italiens)"],
            [2, "Les Triades (chinois)"],
            [1, "Les Colombiens (et autres sud-américains)"],
        ]),
    ]],
    [66, 79, Sequence() << [
        Label("Corporatiste", Weight() << [
            [1, "Assassin/Ninja"],
            [1, "Police corpo/sécurité"],
            [1, "Médecin/MedTech"],
            [2, "Employé (de bureau, secrétaire, etc)"],
            [1, "Cadre intermédiaire"],
            [1, "Cadre supérieur"],
            [1, "Netrunner"],
            [1, "Samuraï"],
            [1, "Technicien"],
        ]),
        # Sous-Table 1.3
        Label("Corporation ", Interval("1d100") << [
            [ 1,  3, "Arasaka (CP, CR1)"],
            [ 4,  5, "BioMass Laboratories Group, GMbH (ERI)"],
            [ 6,  8, "Biotechnicia (CP)"],
            [ 9, 10, "Consolodated Agriculture (IF1.4)"],
            [11, 13, "Diverse Media Systems (RB)"],
            [14, 16, "Dornier AeroSpace (NO)"],
            [17, 19, "Euro-Business Machines Corporation (CP)"],
            [20, 21, "Fujiwara (PRS)"],
            [22, 23, "Hilliard Corporation (RGUK)"],
            [24, 25, "Imperial Metropolitan Agriculture, PLC (RGUK)"],
            [26, 28, "InfoComp (CP, ERI)"],
            [29, 31, "International Electric Corporation (CR1, DS)"],
            [32, 33, "Kendachi (PRS)"],
            [34, 35, "Lazarus Military Group (CR2)"],
            [36, 37, "Matsushima-Kiroshi (PRS)"],
            [38, 40, "Merrill, Asukaga,  Finch (CP)"],
            [41, 43, "MicroTech (CP)"],
            [44, 46, "MiliTech (CP, CR2)"],
            [47, 49, "Mitsubishi/Koridansu (DS)"],
            [50, 52, "Network News 54 (CP, RB)"],
            [53, 54, "No-Ahme Caldwell Genetic Engineering  Biochemicals (NO)"],
            [55, 56, "Ocean Technology  Energy Corporation (IF1.1)"],
            [57, 59, "Orbital Air (CP)"],
            [60, 61, "Peak  Derrera (ERI)"],
            [62, 64, "PetroChem (CP, CR3)"],
            [65, 67, "Raven MicroCybernetics (ERI)"],
            [68, 69, "RepliTech (DS)"],
            [70, 71, "Revolution Genetics, Inc. (IF1.3)"],
            [72, 73, "SegAtari (PRS)"],
            [74, 75, "Soviet World Oil Industries (CR3)"],
            [76, 77, "Storm Technologies Inc. (NT)"],
            [78, 79, "Sungan Industries (PRS)"],
            [80, 81, "Tanson Group (PRS)"],
            [82, 83, "Terra Nova (DS)"],
            [84, 85, "Tiger Medicines Corporation (PRS)"],
            [86, 88, "Trauma Team International (CP)"],
            [89, 90, "Tsunami Design Bureau (ERI)"],
            [91, 92, "Utopian Corporation (DS)"],
            [93, 95, "World News Service (CP)"],
            [96, 98, "WorldSat Communications Network (CP)"],
            [99, 100, "ZetaTech (CP)"],
        ]),
    ]],
    [80, 89, Label("Divertissement", Weight() << [
        [1, "Acteur"],
        [2, "Artiste"],
        [1, "Athlète"],
        [1, "Disk Jockey"],
        [1, Label("Média", Weight() << [
            # Sous-Table 1.4
            [1, "Reporter journal TV"],
            [2, "Journaliste"],
            [2, "Photographe"],
            [1, "Présentateur"],
            [1, "Cameraman/-woman"],
            [1, "Technicien du son"],
            [1, "Commentateur sportif"],
            [1, "Correspondant de guerre"],
        ])],
        [2, "Rocker"],
        [1, "Danseur"],
        [1, "Écrivain"],
    ])],
    [90, 100, Label("Gouvernement", Weight() << [
        [1, Label("Agent du LEDiv", Weight() << [
            # Sous-Table 1.5
            [1, "Administration"],
            [1, "Enquêtes Corporatistes"],
            [1, "Enquêtes Criminelles"],
            [1, "Anti-Drogue"],
            [1, "Renseignement"],
            [1, "Crime Organisé"],
            [1, "Archives"],
            [1, "Science/Tech"],
            [1, "Service Secret"],
            [1, "Opérations Spéciales"],
        ])],
        [1, "Assassin"],
        [4, Label("Militaire", Interval("1d100") << [
            # Sous-Table 1.6
            [ 1, 17, "Air Force, engagé"],
            [18, 20, "Air Force, officer"],
            [21, 37, "Army, engagé"],
            [38, 40, "Army, officer"],
            [41, 57, "Marines, engagé"],
            [58, 60, "Marines, officer"],
            [61, 77, "Navy, engagé"],
            [78, 80, "Navy, officer"],
            [81, 97, "Forces de l'État, engagé"],
            [98, 100, "Forces de l'État, officer"],
        ])],
        [1, "Netrunner"],
        [1, "Officiel/Politicien"],
        [2, "Techie"],
    ])],
]

# Table AEC 1.0
aec = Sequence() << [
    Label("- Sexe", sexe),
    Title("- Occupation", occupation),
]

#################################################
#                   GENERATION                  #
#################################################

root = Sequence() << [
    Title("Evènement de la vie") << evenement,
    "\r",
    Title("PNJ") << aec,
]

################ Generation

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute()
    generation.print_to_console()