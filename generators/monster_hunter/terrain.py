# -*- coding: utf-8 -*-

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Sequence import S
from wordgenerator.Print import Title, Label
from wordgenerator.Generator import Generator

################ GEOGRAPHIE

elevation = Weight() << [
    ["Plaine"],
    ["Vallées"],
    ["Collines"],
    ["Plateaux"],
    ["Montagnes"],
    ["Crevasses"],
    ["Grottes"],
    ["Pilliers"],
    ["Falaises"],
]

climat = Weight() << [
    ["Froid"],
    ["Tempéré"],
    ["Chaud"],
]

hydrometrie = Weight() << [
    ["Sec"],
    ["Humide"],
    ["Fleuve"],
    ["Rivières"],
    ["Cascades"],
    ["Rapides"],
    ["Lacs"],
    ["Marais"],
    ["Lagunes"],
    ["Mangroves"],
    ["Tourbes"],
    ["Etangs"],
    ["Iles"],
    ["Littoral"],
    ["Mer"],
    ["Glacier"],
    ["Neige"],
]

################ METEO

meteo = Weight() << [
    ["Sans"],
    ["Brise"],
    ["Vent Fort"],
    ["Bourasques"],
    ["Tempête"],
    ["Ouragan"],
    ["Cyclone"],
]

précipitations = Weight() << [
    ["Sans"],
    ["Sècheresse"],
    ["Inondation"],
    ["Pluie"],
    ["Brouillard"],
    ["Tempête"],
]

autres = Weight() << [
    ["Non"],
    ["Orage"],
    ["Coulées de Boue"],
    ["Tremblement de Terre"],
]

element = Weight() << [
    ["Magie"],
    ["Onirique"],
    ["Entité Surnaturelle"],
    ["Manifestation divine"],
    ["Acide"],
    ["Gaz"],
    ["Glace"],
    ["Eau"],
    ["Vapeur"],
    ["Boue"],
    ["Feu"],
    ["Lave"],
    ["Foudre"],
    ["Ténèbres"],
    ["Lumière"],
    ["Ombres"],
    ["Aurores Boréales"],
    ["Nécromancie"],
    ["Cadavres"],
    ["Nécroses"],
    ["Sang"],
    ["Spectres"],
    ["Radioactivité"],
    ["Alignement (Bon, maléfique, Loi, Chaos, ...)"],
    ["Eruptions"],
    ["Gravité (Légère, lourde, apesanteur)"],
    ["Folie"],
    ["Temps (fixe, rapide, lent, Rétrograde, Sporadique, Turbulent, Visions d'un autre age)"],
    ["Phénomène Céleste (Météorite, Comète, Aurore, Pluie d'étoiles, Aube, Coucher de Soleil, ..."],
    ["Sons (Agréables, Cacophoniques, surnaturels, musique, cris, ...)"],
    ["Pollen"],
    ["Couleurs"],
    ["Croissances (Accélérées, Rétrogrades, Arrêt / Age, Taille, Pousse, ...)"],
    ["Sommeil"],
    ["Hypnose"],
    ["Hallucinations"],
    ["Reflets"],
    ["Enchantements"],
    ["Féérique"],
    ["Température Anormale"],
]

################ FLORE

flore = Weight() << [
    ["Stérile/Désolé"],
    ["Sable"],
    ["Boue"],
    ["Rocailleux"],
    ["Foret"],
    ["Jungle"],
    ["Toundra"],
    ["Savane"],
    ["Buissons"],
    ["Champs/prairies"],
    ["Brousailles"],
]

flore_type = Weight() << [
    ["Herbe"],
    ["Buisson"],
    ["Liane"],
    ["Arbre Moyen"],
    ["Arbre Grand"],
    ["Fougères"],
    ["Mousse"],
    ["Algues"],
    ["Champignons"],
]

feuillage = Weight() << [
    ["Inexistant"],
    ["Epars"],
    ["Dru"],
    ["Sec et Mort"],
]

feuille = Weight() << [
    ["Simples"],
    ["Composées"],
    ["Aiguille"],
    ["Ecaille"],
]

fruit = Weight() << [
    ["Pollen"],
    ["Fruits"],
    ["Grappes"],
    ["Graines"],
]

flore_autre = Weight() << [
    ["Epineux"],
    ["Carnivore"],
    ["Mobile"],
    ["Organes inhabituels"],
    ["Sentient"],
    ["Lumineux"],
    ["Odeur forte (Agréable ou pas)"],
    ["Sêve étrange (sang, lumière, ...)"],
    ["Parasite/Symbiote Animal/Végétal/Minéral"],
    ["Sort"],
    ["Gaz"],
]

################ Faune

faune = Weight() << [
    ["Déserte/Rare"],
    ["Normale"],
    ["Abondante"],
]

faune_taille = Weight() << [
    ["Petit"],
    ["Moyen"],
    ["Grand"],
]

faune_type = Weight() << [
    ["Animal"],
    ["Insecte"],
    ["Créature Magique"],
    ["Monstre/Aberration"],
    ["Saurien/Dragon"],
]

faune_regime = Weight() << [
    ["Herbivore"],
    ["Prédateur"],
    ["Charognard"],
    ["Granivore"],
    ["Mange-Magie"],
    ["Fouille-Terre"],
    ["Insectivore"],
]

faune_reproduction = Weight() << [
    ["Mammifère"],
    ["Ovipare"],
    ["Clonage"],
    ["Parasitisme"],
]

faune_locomotion = Weight() << [
    ["Bipère"],
    ["Quadripède"],
    ["Beaucoup de pattes"],
    ["Reptation"],
    ["Ailes"],
]

faune_autre = Weight() << [
    ["C'est tout"],
    ["Ailes"],
    ["Amphibien"],
    ["Creusement"],
]

################ Faune - Suite

faune_milieu_naturel = Weight() << [
    ["Surface"],
    ["Aquatique"],
    ["Amphibie"],
    ["Arboricole"],
    ["Souterrain"],
]

faune_organisation_sociale = Weight() << [
    ["Solitaire"],
    ["Couple"],
    ["Groupe (4-6)"],
    ["Meute (10-20)"],
    ["Troupeau (10-100)"],
    ["Horde (100-500+)"],
]

faune_comportement = Weight() << [
    ["Territorial"],
    ["Nomade"],
    ["Colonie"],
    ["Parasite"],
]

faune_attitude = Weight() << [
    ["Peureux"],
    ["Curieux"],
    ["Aggressif"],
    ["Placide"],
]

faune_aspect = Weight() << [
    ["Carapace"],
    ["Venin"],
    ["Souffle"],
    ["Magie"],
    ["Tentacules"],
    ["Cornes"],
    ["Pince/Dard"],
]

################ Population

population_type = Weight() << [
    ["Aucune"],
    ["Campement"],
    ["Tribale"],
    ["Clanique"],
    ["Village"],
    ["Cité"],
    ["Bastide"],
    ["Forteresse"],
    ["Urbaine"],
]

population_race = Weight() << [
    ["Humanoide"],
    ["Humanoide Monstrueuse"],
    ["Monstrueuse"],
    ["Magique"],
]

population_organisatoin_sociale = Weight() << [
    ["Libérale"],
    ["Méritocratie/Aristocratie"],
    ["Monarchie"],
    ["Théocratie"],
    ["Magocratie"],
    ["Oligarchie"],
    ["Gérontocratie"],
    ["Démocratie"],
    ["Caste"],
    ["Dictature"],
]

################ Minéraux

minéraux = Weight() << [
    ["Sable"],
    ["Terre"],
    ["Boue"],
    ["Pierre"],
    ["Métaux"],
    ["Gemmes"],
]

################ Magie

magie = Weight() << [
    ["Morte"],
    ["Faible"],
    ["Normale"],
    ["Intense"],
    ["Erratique"],
    ["Chaotique"],
    ["Tempête"],
    ["Altérée (Element, ...)"],
]

################ Point d'interet

point_interet = Weight() << [
    ["Volcan"],
    ["Geysers"],
    ["Volcan"],
    ["Crépuscule éternel"],
    ["Cimetière"],
    ["Champ de Bataille"],
    ["Ruines"],
    ["Zone de Reproduction"],
    ["Zone de Chasse"],
    ["Zone de Migration"],
    ["Zone de Cimetière"],
    ["Zone"],
]

################ ROOT

root = S(
    # Geographie
    Title("Terrain") << S(
        Label("Elevation  ", elevation),
        Label("Climat     ", climat),
        Label("Hydrometrie", hydrometrie)
    ),
    # Meteo
    Title("Climat") << S(
        Label("Meteo         ", meteo),
        Label("Précipitations", précipitations),
        Label("Autres        ", autres),
        Label("Element       ", element),
    ),
    # Flore
    Title("Flore") << S(
        flore,
        Title("Specimen") << S(
            Label("Type      ", flore_type),
            Label("Feuillage ", feuillage),
            Label("Feuilles  ", feuille),
            Label("Fruit     ", fruit),
            Label("Autre     ", flore_autre),
        ),
    ),
    # Faune
    Title("Faune") << S(
        faune,
        Title("Specimen") << S(
            Label("Taille    ", faune_taille),
            Label("Type      ", faune_type),
            Label("Regime    ", faune_regime),
            Label("Reproduction", faune_reproduction),
            Label("Locomotion", faune_locomotion),
            Label("Autre     ", faune_autre),
            Label("Milieu naturel", faune_milieu_naturel),
            Label("Organisaton Sociale", faune_organisation_sociale),
            Label("Comportement", faune_comportement),
            Label("Attitude    ", faune_attitude),
            Label("Aspect     ", faune_aspect),
        ),
    ),
    # Population
    Title("Population") << S(
        Label("Type      ", population_type),
        Label("Race      ", population_race),
        Label("Organisation Sociale", population_organisatoin_sociale),
    ),
    # Minéraux
    Title("Minéraux") << S(
        Label("Minéraux      ", minéraux),
    ),
    # Magie
    Title("Magie") << S(
        Label("Magie ", magie),
    ),
    # Point d'interet
    Title("Point d'interet") << S(
        point_interet,
    ),
)

################ Generation

generator = Generator(root)
generator.execute()
generator.print_to_console()