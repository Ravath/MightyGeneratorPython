# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import SequenceNode as Sequence

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
        [" de mamans"],
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