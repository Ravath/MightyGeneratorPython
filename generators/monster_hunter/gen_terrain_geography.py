# -*- coding: utf-8 -*-

if __name__ == "__main__" :
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

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
    )
)

################ Generation

generation = Generator(root)
if __name__ == "__main__" :
    generation.execute()
    generation.print_to_console()