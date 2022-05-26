# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:03:13 2020

@author: Ehlion
"""

from wordgenerator.Weight import WeightNode as Weight
from wordgenerator.Interval import IntervalNode as Interval
from wordgenerator.Sequence import SequenceNode as Sequence
from wordgenerator.Print import Title, Label
from macro.dice import Pool, PoolSum

d100 = PoolSum(Pool(1,100))
_3d6 = PoolSum(Pool(3,6))

################ HUMAIN

humain_historique = Weight().extend([
    ["Vous êtes mort et vous êtes revenu à la vie. Vous commencez le jeu avec 1d6 points de Folie."],
    ["Vous avez été brièvement possédé par un démon. Vous commencez le jeu avec 1 en Corruption."],
    ["Vous avez passé 1d6 années emprisonné dans un donjon."],
    ["Vous avez assassiné quelqu’un de sang-froid. Vous commencez le jeu avec 1 en Corruption."],
    ["Vous avez attrapé une terrible maladie mais vous vous en êtes remis."],
    ["Vous apparteniez à un culte étrange et vous avez vu des choses bizarres. Vous commencez le jeu avec 1 en Folie."],
    ["Les fées vous ont gardé captif pendant 1d20 années."],
    ["Vous avez perdu un être cher et sa perte vous hante."],
    ["Vous avez perdu un doigt, quelques dents ou une oreille ou vous avez une cicatrice."],
    ["Vous avez gagné votre vie en exerçant votre profession."],
    ["Vous êtes tombé amoureux et cette relation s’est bien terminée ou perdure."],
    ["Vous avez un mari ou une femme et 1d6–2 enfants (minimum 0)."],
    ["Vous avez beaucoup voyagé. Vous parlez une langue supplémentaire."],
    ["Vous avez reçu une bonne éducation. Vous savez lire la langue commune."],
    ["Vous avez sauvé votre ville de monstres terrifiants."],
    ["Vous avez déjoué un complot visant à tuer quelqu’un d’important ou vous avez traîné un assassin devant la justice."],
    ["Vous avez accompli un grand exploit et vous êtes un héros pour les gens de votre ville natale."],
    ["Vous avez trouvé une vieille carte au trésor."],
    ["Quelqu’un d’important et de puissant vous doit une faveur."],
    ["Vous avez gagné de l’argent et vous commencez le jeu avec 2d6 sc."],
])

humain_personalite = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes cruel, mauvais et égoïste. Vous aimez faire souffrir les autres."],
    [ 4,  4, "Vous êtes instable et imprévisible. Vous avez beaucoup de mal à tenir parole et vous avez tendance à être capricieux."],
    [ 5,  6, "La force fait loi. Obéir à l’autorité est le plus grand des idéaux."],
    [ 7,  8, "Vous vous préoccupez avant tout de vous. Trahir vos amis ne vous fait pas peur."],
    [ 9, 12, "Vous vous préoccupez avant tout de vos intérêts et de ceux de vos amis."],
    [13, 14, "Vous aidez les autres car c’est la bonne chose à faire."],
    [15, 16, "Vous essayez de faire ce que vous croyez juste même si cela enfreint des lois et des conventions sociales."],
    [17, 17, "Votre honneur et votre devoir guident vos moindres actes."],
    [18, 18, "Vous vous consacrez entièrement au bien et aux nobles causes et vous restez fidèle à vos croyances même si cela peut vous coûter la vie."],
])

humain_religion = Interval(_3d6).extend([
    [ 3,  3, "Vous appartenez à un culte voué à une sombre puissance."],
    [ 4,  4, "Vous faites partie d’une secte hérétique."],
    [ 5,  6, "Vous avez été élevé selon les enseignements de la sorcellerie."],
    [ 7, 10, "Vous suivez les préceptes de la Vieille Foi."],
    [11, 15, "Vous appartenez au Culte du Nouveau dieu."],
    [16, 18, "Vous n’avez aucune religion."],
])

humain_age = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un enfant de 11 ans ou plus jeune."],
    [ 4,  7, "Vous êtes un adolescent âgé de 12 à 17 ans."],
    [ 8, 12, "Vous êtes un jeune adulte âgé de 18 à 35 ans."],
    [13, 15, "Vous êtes un adulte d’âge moyen de 36 à 55 ans."],
    [16, 17, "Vous êtes un adulte âgé, entre 56 et 75 ans."],
    [18, 18, "Vous êtes un adulte d’âge vénérable d’au moins 76 ans."],
])

humain_stature = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes petit et mince."],
    [ 4,  4, "Vous êtes petit et corpulent."],
    [ 5,  6, "Vous êtes petit."],
    [ 7,  8, "Vous êtes mince."],
    [ 9, 12, "Vous avez une taille et un poids moyens."],
    [13, 14, "Vous êtes un peu en surpoids."],
    [15, 16, "Vous êtes grand."],
    [17, 17, "Vous êtes grand et mince."],
    [18, 18, "Vous êtes très grand et corpulent."],
])

humain_apparence = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes hideux. Vous ressemblez à un monstre. Vous faites pleurer les enfants que vous croisez, les personnes sensibles s’évanouissent en vous voyant et un individu a même vomi après vous avoir dévisagé."],
    [ 4,  4, "Vous êtes laid et les gens trouvent votre visage déplaisant à cause d’une cicatrice, un kyste, un front proéminent, des furoncles, d’un oeil larmoyant ou baladeur ou autre chose de ce type."],
    [ 5,  6, "La plupart des gens vous considèrent comme un individu qui n’est pas très beau mais pas non plus laid."],
    [ 7,  8, "Vous êtes quelconque et votre apparence n’a rien d’intéressant. Les gens vous remarquent mais vous ne marquez pas les esprits."],
    [ 9, 12, "Vous avez une apparence parfaitement commune. Vous pourriez être n’importe qui."],
    [13, 14, "Vous avez un trait physique qui vous rend attrayant. Il peut s’agir de vos beaux yeux, de vos lèvres, de vos cheveux, de votre aspect général ou d’autre chose."],
    [15, 16, "Vous avez plusieurs traits physiques qui vous rendent très attrayant."],
    [17, 17, "Vous êtes un des individus les plus beaux de la région, avec une silhouette et une apparence presque incomparables. Les gens vous remarquent."],
    [18, 18, "Les gens qui sont beaux ont honte quand ils se comparent à vous. Vous êtes tellement magnifique que les têtes se tournent sur votre passage et qu’on vous suit du regard. Les gens s’amourachent facilement de vous, bredouillent en vous parlant et se sentent troublés quand vous leur témoignez une certaine attention. La frontière est assez étroite entre l’amour et la haine. Si vous rejetez les gens que vous avez séduits, leur affection peut se transformer en ressentiment et même en haine."],
])

################ AUTOMATE

automate_age = Interval(_3d6).extend([
    [ 3,  8, "Vous êtes récent, âgé de 5 ans ou moins."],
    [ 9, 12, "Vous êtes expérimenté, âgé de 6 à 10 ans."],
    [13, 15, "Vous êtes âgé, entre 11 et 50 ans."],
    [16, 17, "Vous êtes très âgé, entre 51 et 150 ans."],
    [18, 18, "Vous êtes ancien, plus de 150 ans."],
])

automate_fonction = Weight().extend([
    ["Vous avez été conçu pour la guerre. Augmentez votre Force ou votre Agilité de 2."],
    ["Vous avez été conçu pour travailler. Augmentez votre Force de 2."],
    ["Vous avez été conçu pour utiliser la magie. Augmentez votre Intellect de 2."],
    ["Vous avez été conçu pour espionner ou assassiner des cibles. Augmentez votre Agilité ou votre Intellect de 2."],
    ["Vous avez été conçu dans un but inconnu ou incompréhensible. Augmentez l’un de vos attributs de 2."],
])

automate_forme = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un petit automate ailé. Réduisez votre Santé de 5 points et votre Gabarit à 1/2. Vous pouvez voler mais vous devez atterrir à la fin de votre déplacement ou tomber. Vous mesurez 1 m et vous pesez 25 kilos."],
    [ 4,  5, "Vous êtes un petit automate arachnéen avec des mains fonctionnelles. Réduisez votre Gabarit à 1/2. Vous ignorez les effets d’un terrain difficile quand vous escaladez. Vous mesurez 1 m et vous pesez 25 kilos."],
    [ 6,  9, "Vous êtes un petit automate humanoïde. Réduisez votre Gabarit à 1/2. Vous mesurez 1,2 m et vous pesez 35 kilos."],
    [10, 15, "Vous êtes un automate humanoïde. Vous mesurez 1,8 m et vous pesez 135 kilos."],
    [16, 17, "Vous êtes un grand automate humanoïde. Augmentez votre Gabarit à 2 mais réduisez votre Vitesse et votre Défense de 2. Vous mesurez 3 m et vous pesez 340 kilos."],
    [18, 18, "Vous êtes un grand automate et la partie inférieure de votre corps est celle d’un cheval. Augmentez votre Gabarit à 2 et votre Vitesse de 2. Réduisez votre Défense de 3. Vous avez une taille et une longueur de 3 m et vous pesez 340 kilos."],
])

automate_apparence = Interval(_3d6).extend([
    [ 3,  3, "Vous avez une apparence étrange et perturbante."],
    [ 4,  4, "Votre apparence est grossière et vous êtes mal formé."],
    [ 5,  6, "Vous semblez cabossé, cassé et en mauvais état."],
    [ 7,  8, "Votre visage est lisse sans trait ni marque distinctive."],
    [ 9, 12, "Les traits de votre visage sont à peine esquissés."],
    [13, 14, "Vous semblez bien conçu et en bon état."],
    [15, 16, "Vous avez un corps finement ouvragé."],
    [17, 17, "Vous avez un corps finement ouvragé orné de gravures et de joyaux décoratifs."],
    [18, 18, "Vous avez un corps superbe orné de fines gravures, de joyaux décoratifs et de métaux précieux. Si vous êtes démonté, les morceaux de votre corps valent 1d6 co."],
])

automate_historique = Weight().extend([
    ["Votre âme provient de l’Enfer. Vous commencez le jeu avec 1d3 en Corruption."],
    ["Votre âme a été arrachée au Royaume des morts avant d’avoir oublié son ancienne vie. Vous commencez le jeu avec 1d6 en Folie et vous ajoutez une profession supplémentaire."],
    ["Vous avez passé 1d20 ans dans un état dormant."],
    ["Votre créateur vous maltraitait. Vous avez fui et vous craignez qu’il ne vous retrouve."],
    ["Le feu, les épidémies ou des monstres ont détruit votre foyer et vous êtes le seul survivant."],
    ["Vous avez été volé dans l’atelier qui vous a vu naître et vous avez été esclave pendant 1d6 ans."],
    ["Les gobelins vous ont capturé et vous ont presque entièrement démonté. Vous avez remplacé les pièces manquantes avec des morceaux de bois, de vieilles armes et d’autres camelotes."],
    ["Vous avez dû découvrir la vie par vous-même quand votre créateur est mort."],
    ["Vous êtes tombé d’un bateau et vous avez mis 2 ans à rejoindre la côte."],
    ["Pendant 1d6 ans, vous avez accompli ce pour quoi vous avez été créé."],
    ["Choisissez un membre du groupe. Ce personnage vous a trouvé et a tourné votre clef. Vous avez une dette envers lui."],
    ["Vous avez été créé en même temps que cinq autres automates. Vous espérez les retrouver un jour."],
    ["Vous avez été conçu pour être traducteur. Vous parlez une langue supplémentaire."],
    ["Vous avez été conçu pour être copiste. Vous savez lire et écrire la langue commune."],
    ["Votre créateur vous a libéré pour que vous trouviez votre destinée."],
    ["Vous ne vous souvenez pas de votre passé. Vous ignorez d’où vous venez ou comment vous êtes arrivé là où vous êtes."],
    ["Vous avez construit un monument dans votre communauté."],
    ["Vous avez découvert un message énigmatique dans votre corps. Vous ne l’avez pas encore déchiffré."],
    ["Une épée a été greffée sur l’un de vos bras."],
    ["Vous avez gagné de l’argent et vous commencez le jeu avec 2d6 sc."],
])

automate_personalite = Interval(_3d6).extend([
    [ 3,  3, "Vous haïssez les êtres vivants et vous prenez plaisir à les démembrer."],
    [ 4,  4, "Vous êtes terrifié à l’idée de vous retrouver dans un état dormant."],
    [ 5,  7, "Votre corps vous octroie force et puissance. Vous les utilisez pour imposer votre volonté aux autres."],
    [ 8,  8, "Vous n’avez pas demandé cette existence mais vous en tirez le meilleur profit."],
    [ 9, 13, "Vous cherchez une raison d’être dans ce monde où vous n’avez pas votre place."],
    [14, 14, "Vous avez été créé pour servir. Vous consacrez votre existence à aider les autres."],
    [15, 15, "Vous ne savez pas comment vous intégrer à ce monde mais vous passerez votre vie à essayer."],
    [16, 17, "Vous obéissez aux instructions de toute personne que vous estimez incarner l’autorité."],
    [18, 18, "Votre créateur vous a donné trois commandements et vous devez y obéir."],
])

################ CHANGELIN

changelin_age = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un enfant de 8 ans ou plus jeune."],
    [ 4,  7, "Vous êtes un adolescent âgé de 9 à 14 ans."],
    [ 8, 12, "Vous êtes un jeune adulte âgé de 15 à 25 ans."],
    [13, 15, "Vous êtes un adulte d’âge moyen de 26 à 40 ans."],
    [16, 17, "Vous êtes un adulte âgé, entre 41 et 60 ans."],
    [18, 18, "Vous êtes un adulte d’âge vénérable d’au moins 61 ans."],
])

changelin_sexe = Weight().extend([
    ["Vous avez une apparence masculine."],
    ["Vous avez une apparence féminine."],
])

changelin_ascendance = Interval(_3d6).extend([
    [ 3,  4, "Vous avez l’apparence d’un gobelin. Reportez-vous à la section Gobelin pour déterminer votre âge, votre stature et votre apparence."],
    [ 5,  7, "Vous avez l’apparence d’un nain. Reportez-vous à la section Nain pour déterminer votre âge, votre stature et votre apparence."],
    [ 8, 15, "Vous avez l’apparence d’un humain. Reportez-vous à la section Humain pour déterminer votre âge, votre stature et votre apparence."],
    [16, 17, "Vous avez l’apparence d’un orc. Reportez-vous à la section Orc pour déterminer votre âge, votre stature et votre apparence."],
    [18, 18, "Le MJ détermine votre ascendance, votre âge, votre stature et votre apparence."],
])

changelin_historique = Weight().extend([
    ["Vous venez récemment de découvrir votre véritable nature et vous avez du mal à accepter cette réalité. Vous commencez le jeu avec 1 en Folie."],
    ["Vous ne savez pas que vous êtes un changelin. Vous pensez être un membre de l’espèce dont vous avez pris la forme. Ajoutez une profession supplémentaire déterminée aléatoirement. Jusqu’à ce que vous soyez neutralisé ou que vous touchiez du fer pour la première fois, vous ne pouvez pas utiliser Usurpation d’identité."],
    ["Vous avez été asservi par une mégère qui vous a contraint à accomplir des actes abominables. Vous commencez le jeu avec 1 en Corruption."],
    ["Vous avez assassiné la personne dont vous avez usurpé l’identité pour pouvoir lui voler sa vie. Vous commencez le jeu avec 1 en Corruption."],
    ["Quand vos « parents » ont découvert ce que vous étiez, ils vous ont chassé et vous avez dû vous débrouiller seul."],
    ["Vous avez fui de votre foyer quand vous avez découvert ce que vous étiez et vous avez vécu parmi les fées pendant de nombreuses années."],
    ["Vous vous êtes attiré l’inimitié d’un chasseur de sorciers. Cet adversaire vous traque et tentera de vous tuer si vos chemins se croisent."],
    ["Des citoyens effrayés vous ont chassé de votre ville natale. Vous les détestez et vous envisagez de vous venger."],
    ["La première fois que vous avez usurpé l’identité de quelqu’un, vous lui avez aussi volé une partie de sa mémoire."],
    ["Vous avez gagné votre vie en exerçant votre profession."],
    ["Vous êtes tombé amoureux mais la personne que vous aimez ignore tout de votre véritable identité."],
    ["Après avoir été exilé de votre ville natale, un druide ou un sorcier vous a recueilli et s’est occupé de vous. Vous êtes toujours chez vous chez ce personnage."],
    ["Vous avez travaillé en tant qu’informateur pour l’Inquisition."],
    ["Vous avez reçu une bonne éducation. Vous savez lire et écrire la langue commune."],
    ["Vous avez découvert un terrible secret en vous faisant passer pour quelqu’un d’autre. Définissez la nature de ce secret avec votre MJ."],
    ["Vos parents vous ont élevé même en sachant ce que vous étiez. Leur amour et leur soutien vous ont permis de bénéficier de la stabilité dont vous aviez besoin pour devenir une personne mature."],
    ["L’elfe qui vous a créé vous a récemment retrouvé et s’est lié d’amitié avec vous. Vous pouvez lui demander une faveur en parlant dans un coquillage qu’il ou elle vous a donné. C’est au MJ de déterminer l’étendue de cette faveur."],
    ["Vous avez pris la forme d’une personne célèbre, puissante et importante."],
    ["Vous avez des liens avec une organisation criminelle dans laquelle vous avez été recruté pour vos dons magiques."],
    ["Vous avez découvert de l’argent et vous commencez le jeu avec 2d6 sc."],
])

changelin_particularite = Weight().extend([
    ["Vous parlez toujours à la troisième personne."],
    ["Vos yeux brillent d’une couleur verte dans le noir."],
    ["Vous rendez les animaux nerveux."],
    ["Vous ne pouvez prendre que des formes féminines ou que des formes masculines."],
    ["Vous êtes féroce et impulsif."],
    ["Vous reprenez toujours la première forme que vous avez prise."],
    ["L’odeur du fer vous donne la nausée."],
    ["Vous faites de terribles cauchemars."],
    ["Parfois, il vous arrive d’entendre des voix."],
    ["Vous avez tendance à perdre des petites choses sans importance."],
    ["Une nuit par an, vous perdez votre talent d’Usurpation d’identité."],
    ["Vous ne pouvez prendre l’apparence que des personnes décédées."],
    ["Vous parlez en murmurant."],
    ["Vous dégagez une étrange odeur de terre."],
    ["Vous ne pouvez jamais garder vos vêtements propres."],
    ["Vous ne pouvez pas être ivre."],
    ["Vous devez toujours dire la vérité telle que vous la connaissez."],
    ["Vous trouvez la viande répugnante."],
    ["Vous riez aux moments les plus inappropriés."],
    ["Les formes que vous prenez n’ont ni cheveux, ni poils, ni ongles."],
])

changelin_personalite = Interval(_3d6).extend([
    [ 3,  3, "Vous volez l’apparence des autres pour pouvoir faire ce que vous voulez sans en assumer les conséquences. Vous ne vous souciez pas de la manière dont ça peut les affecter."],
    [ 4,  5, "Vous aimez prendre des formes qui vous permettent de commettre des méfaits."],
    [ 6,  6, "Vous prenez des formes qui vous donnent du pouvoir sur les autres. Le pouvoir renforce votre sécurité."],
    [ 7, 10, "Vous prenez d’autres formes pour votre profit personnel généralement pour pénétrer dans des lieux auxquels vous n’avez pas accès."],
    [11, 13, "Vous faites attention aux formes que vous prenez. Vous essayez d’éviter les ennuis et de protéger vos secrets."],
    [14, 14, "Vous voulez faire ce qui est bien et vous utilisez vos déguisements pour aider les autres ainsi que pour vous protéger de vos ennemis."],
    [15, 16, "Votre nature est un don et vous l’utilisez pour faire ce que vous pensez être le bien même si cela en contrarie certains."],
    [17, 17, "Vous tentez de conserver la même forme le plus longtemps possible ; vous avez besoin de stabilité et vous feriez tout pour être « normal »."],
    [18, 18, "Vous utilisez vos talents pour aider les autres, pour rendre le monde meilleur et pour redresser les torts."],
])

################ GOBELIN

gobelin_age = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un enfant de 6 ans ou plus jeune."],
    [ 4,  7, "Vous êtes un adolescent âgé de 7 à 10 ans."],
    [ 8, 12, "Vous êtes un jeune adulte âgé de 11 à 25 ans."],
    [13, 15, "Vous êtes un adulte d’âge moyen de 26 à 50 ans."],
    [16, 17, "Vous êtes un adulte âgé, entre 51 et 75 ans."],
    [18, 18, "Vous êtes un adulte d’âge vénérable d’au moins 76 ans."],
])

gobelin_stature = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes petit et frêle."],
    [ 4,  4, "Vous êtes petit et rondelet."],
    [ 5,  6, "Vous êtes petit."],
    [ 7,  8, "Vous êtes filiforme."],
    [ 9, 12, "Vous avez une taille et un poids moyens pour un gobelin."],
    [13, 14, "Vous êtes grassouillet."],
    [15, 16, "Vous êtes grand."],
    [17, 17, "Vous êtes très grand et dégingandé."],
    [18, 18, "Vous êtes très grand et corpulent."],
])

gobelin_apparence = Weight().extend([
    ["Vous avez un long nez pointu."],
    ["Vous avez une peau vert clair ou orange."],
    ["Vous avez la tête d’un chien."],
    ["Vous avez une apparence reptilienne avec de petites cornes sur le sommet de la tête."],
    ["Vous avez un large sourire concupiscent."],
    ["Vous avez un groin à la place du nez."],
    ["Vous avez de longs doigts fins."],
    ["Vous avez une dent qui pousse sur votre front."],
    ["Vous avez une queue."],
    ["Vos bras et vos jambes sont couverts d’une épaisse fourrure."],
    ["Vous êtes totalement imberbe."],
    ["Vous êtes couvert de verrues."],
    ["Un gros kyste pousse dans votre dos."],
    ["Vous avez un menton anormalement long et pointu."],
    ["Une unique corne pousse sur un côté de votre tête."],
    ["Vous avez un seul oeil."],
    ["Vous avez 1d6 doigts supplémentaires répartis où vous voulez sur votre corps."],
    ["Vous avez des oreilles énormes."],
    ["Vous avez des petites jambes trapues."],
    ["Imaginez quelque chose !"],
])

gobelin_habitude = Weight().extend([
    ["Vous récupérez toutes vos sécrétions dans de petites bouteilles que vous offrez aux gens que vous appréciez."],
    ["Vous ne prenez jamais de bain."],
    ["Vous ponctuez vos phrases en crachant."],
    ["Vous avez de terribles flatulences mais vous semblez ne pas les remarquer."],
    ["Vous ne mangez que des sucreries."],
    ["Vous récupérez les parties génitales des créatures que vous tuez et vous les portez comme des bijoux."],
    ["Vous léchez les choses pour signifier qu’elles vous appartiennent."],
    ["Vous vous habillez avec des tenues fantaisistes."],
    ["Vous refusez de porter des chaussures."],
    ["Vous avez des cafards comme animaux de compagnie."],
    ["Vous inspectez toujours vos excréments avant de les étaler avec vos doigts."],
    ["Vous conservez toujours sur vous un morceau de fer."],
    ["Vous parlez avec une voix chantante."],
    ["Vous dévorez un peu de la chair de chaque créature que vous tuez."],
    ["Vous pleurez beaucoup."],
    ["Vous racontez des blagues dégoûtantes aux moments les plus inappropriés."],
    ["Vous portez des habits d’enfant et vous refusez de les enlever."],
    ["Vous avez une grande collection de cuillères."],
    ["Vous aimez vous cacher."],
    ["Imaginez quelque chose !"],
])

gobelin_historique = Weight().extend([
    ["Vous avez été saoul pendant 1d6 années. Vous n’en êtes pas fier."],
    ["Le Roi Gobelin vous a transformé en crapaud. Vous avez échappé à ce triste sort après avoir convaincu une jeune vierge elfe de vous embrasser. Quand elle l’a fait et qu’elle s’est mise à hurler, vous l’avez tuée. Vous commencez le jeu avec 1 en Corruption."],
    ["Accidentellement, vous avez provoqué la mort de tous les membres de votre tribu."],
    ["Orphelin, vous avez été élevé par des rats géants."],
    ["Vous avez accidentellement libéré un démon sur le monde."],
    ["Vous avez passé deux jours à croire que vous étiez un chien féroce. Vous commencez le jeu avec 1 en Folie."],
    ["Une mégère a fait de vous son esclave sexuel pendant 1d6 années."],
    ["Les nains ont presque exterminé votre tribu. Vous êtes l’un des 1d6 survivants."],
    ["Vous vous êtes presque noyé quand les égouts ont été inondés."],
    ["Vous avez gagné votre vie en exerçant votre profession."],
    ["Choisissez un personnage. Il ou elle vous a sauvé la vie et vous avez une dette envers lui/elle."],
    ["Vous êtes un criminel impénitent. Ajoutez une profession criminelle déterminée aléatoirement à votre liste de professions."],
    ["Vous avez beaucoup voyagé. Vous parlez une langue supplémentaire."],
    ["Vous avez volé un couteau à un fringuant chevalier."],
    ["Vous vous êtes faufilé dans Alfheim et vous avez volé une boucle de cheveux de la Reine des Fées."],
    ["Vous avez tué et mangé 100 rats malades."],
    ["Vous étiez le serviteur d’un puissant mage."],
    ["Vous avez trouvé un anneau sigillaire dans les égouts."],
    ["Vous êtes le dix-septième fils ou la dix-septième fille du Roi Gobelin."],
    ["Vous avez gagné de l’argent et vous commencez le jeu avec 2d6 sc."],
])

gobelin_personalite = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes une brute qui aime tyranniser et tourmenter tout ce qui est plus faible que vous."],
    [ 4,  4, "Vous aimez la violence surtout quand elle est gratuite et insensée."],
    [ 5,  6, "Vous essayez d’échapper à la crasse et aux conditions de vie sordides de votre peuple pour faire le bien dans le monde."],
    [ 7,  8, "Vous aimez jouer des tours aux autres et vous trouvez leur souffrance hilarante."],
    [ 9, 12, "Vous ne vous préoccupez que de vous. Au diable les autres !"],
    [13, 14, "Vous essayez juste de rester en vie !"],
    [15, 16, "Votre peuple n’a pas mérité d’être exilé, mais c’est pourtant le cas. Vous êtes convaincu que vous vous ferez une place au sein de la société et que vous prouverez à ces elfes puants qu’ils ont eu tort."],
    [17, 17, "Vous ne vivez que pour servir les forts et les puissants."],
    [18, 18, "Vous espérez racheter votre peuple aux yeux de la Reine des Fées."],
])

################ NAIN

nain_age = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un enfant de 20 ans ou plus jeune."],
    [ 4,  7, "Vous êtes un adolescent âgé de 20 à 30 ans."],
    [ 8, 12, "Vous êtes un jeune adulte âgé de 31 à 50 ans."],
    [13, 15, "Vous êtes un adulte d’âge moyen de 51 à 100 ans."],
    [16, 17, "Vous êtes un adulte âgé, entre 101 et 150 ans."],
    [18, 18, "Vous êtes un adulte d’âge vénérable d’au moins 151 ans."],
])

nain_stature = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes petit et maigrichon."],
    [ 4,  6, "Vous êtes petit et enveloppé."],
    [ 7,  8, "Vous êtes un peu plus petit que les autres nains."],
    [ 9, 12, "Vous avez une taille et un poids moyens."],
    [13, 15, "Vous avez une magnifique bedaine."],
    [16, 17, "Vous êtes grand."],
    [18, 18, "Vous êtes très grand et massif."],
])

nain_apparence = Interval(_3d6).extend([
    [ 3,  4, "Vous avez une apparence monstrueuse certainement due à vos rudes conditions de vie et à des incidents auxquels vous avez partiellement échappé. Votre visage est couvert de cicatrices et il vous manque probablement une oreille, un oeil ou pire. Vous avez aussi une habitude inhabituelle comme enfoncer des clous dans votre crâne ou huiler votre corps avec de la graisse de troll."],
    [ 5,  6, "Vous avez certaines caractéristiques intéressantes qui se combinent pour vous donner l’aspect d’une brute particulièrement laide. De la crasse incrustée à force de creuser la terre, des mites dans vos cheveux, une peau couverte de cicatrices et une odeur de vomi... tous ces éléments contribuent à votre style particulier."],
    [ 7,  8, "Vous êtes chevelu, corpulent et crasseux."],
    [ 9, 11, "Vous êtes un nain moyen, chevelu et crasseux, mais soigné."],
    [12, 15, "Vous êtes fier de votre apparence. Vous restez propre, vous huilez votre barbe et votre moustache et vous les tressez pour les décorer d’anneaux métalliques."],
    [16, 18, "Vous êtes plutôt ravissant pour un nain. Vous avez des traits fins et agréables, un bon maintien et une voix profonde. Vous êtes fier de votre apparence."],
])

nain_haine = Weight().extend([
    ["Ogres"],
    ["Troglodytes"],
    ["Hommes-bêtes"],
    ["Orcs"],
    ["Gobelins"],
    ["Elfes"],
    ["Trolls"],
    ["Géants"],
    ["Dragons"],
    ["Démons"],
])

nain_historique = Weight().extend([
    ["Vous avez vendu votre âme à un diable pour faire fortune. Le diable vous a trahi et vous a laissé sans le sou. Vous commencez le jeu avec 1 en Corruption."],
    ["Vos ancêtres vous sont apparus dans une vision et vous ont envoyé récupérer une relique légendaire."],
    ["Vous avez accidentellement tué un proche."],
    ["Vous avez volé de l’or à un clan rival et vous avez honte."],
    ["Vous avez combattu des créatures que vous haïssez et vous avez perdu."],
    ["Vous avez déshonoré votre nom et votre clan. Vous vivez en exil en quête de Rédemption même si pour cela il vous faut mourir glorieusement."],
    ["Vous avez été prisonnier des créatures que vous haïssez. Vous avez vécu comme un esclave pendant 2d6 années."],
    ["Les créatures que vous haïssez ont envahi votre foyer et ont exterminé votre clan."],
    ["Vous avez survécu à un éboulement et vous êtes un peu nerveux quand vous êtes sous terre."],
    ["Vous avez gagné votre vie en exerçant votre profession."],
    ["Vous avez juré de servir le Roi Nain."],
    ["Vous êtes un artisan talentueux. Ajoutez artisan (n’importe lequel) à votre liste de professions."],
    ["Vous avez beaucoup voyagé. Vous parlez une langue supplémentaire."],
    ["Vous avez hérité de la hache de bataille ou du marteau de guerre d’un ancêtre."],
    ["Vous avez découvert une veine d’or sous la montagne qui est votre foyer."],
    ["Vous avez traqué et participé à l’exécution d’une créature que vous haïssez."],
    ["Vous avez accompli un grand exploit et vous êtes un héros pour votre clan."],
    ["Vous avez la clef d’une ancienne salle des trésors perdue depuis longtemps."],
    ["Vous êtes l’héritier légitime d’une forteresse envahie par les ennemis de votre peuple."],
    ["Vous avez gagné de l’argent et vous commencez le jeu avec 2d6 sc."],
])

nain_personalite = Interval(_3d6).extend([
    [ 3,  3, "Votre haine est presque vivante. Elle vous motive, vous donne la force et vous aide à triompher de vos ennemis."],
    [ 4,  4, "Vous cherchez une mort glorieuse en tuant vos ennemis."],
    [ 5,  6, "Vous aimez l’or plus que toute autre chose. Vous aimez sa texture, son tintement et même son goût."],
    [ 7,  8, "Vous pensez que tout le monde convoite votre fortune. C’est votre devoir de protéger ce qui vous appartient, quel qu’en soit le prix."],
    [ 9, 12, "Votre honneur est votre vie. Vous ne feriez rien qui puisse déshonorer votre peuple."],
    [13, 14, "Vous vous soumettez à la volonté de vos ancêtres, aux coutumes de votre peuple et à l’intérêt général."],
    [15, 16, "Vous pensez que votre peuple doit surmonter sa tendance cupide et méfiante. En cette sombre époque, vous devez vous unir pour surmonter le funeste destin qui vous menace tous."],
    [17, 17, "Vous aimez et ne faites confiance qu’aux nains, mais les autres peuvent être utiles."],
    [18, 18, "Vous vous fichez des coutumes de votre peuple. Il est temps de renoncer aux cavernes poussiéreuses et d’aller chercher fortune ailleurs."],
])

################ Orc

orc_age = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes un enfant de 8 ans ou plus jeune."],
    [ 4,  7, "Vous êtes un adolescent âgé de 8 à 12 ans."],
    [ 8, 12, "Vous êtes un jeune adulte âgé de 13 à 18 ans."],
    [13, 15, "Vous êtes un adulte d’âge moyen de 19 à 26 ans."],
    [16, 17, "Vous êtes un adulte âgé, entre 27 et 32 ans."],
    [18, 18, "Vous êtes un adulte d’âge vénérable d’au moins 33 ans."],
])

orc_stature = Interval(_3d6).extend([
    [ 3,  3, "Vous êtes petit et maigre."],
    [ 4,  4, "Vous êtes petit et musclé."],
    [ 5,  6, "Vous êtes petit."],
    [ 7,  8, "Vous êtes mince."],
    [ 9, 12, "Vous avez une taille et un poids moyens."],
    [13, 14, "Vous êtes corpulent."],
    [15, 16, "Vous êtes grand."],
    [17, 17, "Vous êtes très grand et émacié."],
    [18, 18, "Vous êtes un géant parmi les orcs."],
])

orc_apparence = Interval(_3d6).extend([
    [ 3,  5, "Vous êtes grotesque. Votre visage est constellé de cicatrices. Votre corps est couvert de plaies refermées par des sutures rudimentaires en lanière de cuir. De certaines de ces plaies s’écoulent du pu et vous puez les excréments, le sang et la pourriture."],
    [ 6,  8, "Vous êtes monstrueux avec des traits grossiers et brutaux, d’étranges excroissances sur votre peau et de vilaines cicatrices irrégulières sur votre peau épaisse."],
    [ 9, 12, "Vous êtes laid. Vous avez des défenses épaisses qui dépassent de vos larges mâchoires, un front fuyant et deux tout petits yeux enfoncés profondément dans votre crâne."],
    [13, 15, "Vous avez l’aspect classique d’un orc crasseux et négligé."],
    [16, 17, "Vos traits sont un peu plus fins et moins brutaux même si votre peau peut avoir une couleur inhabituelle, être couverte d’encore plus de poils ou avoir d’autres caractéristiques particulières."],
    [18, 18, "Vous vous démarquez nettement de ceux de votre espèce. Contrairement aux autres orcs, votre corps n’est pas couvert de plaies et de cicatrices et vous êtes en bonne santé."],
])

orc_historique = Weight().extend([
    ["Vous avez massacré des innocents. Gagnez 2 points de Corruption."],
    ["Vous avez été brièvement possédé par un démon. Gagnez 1 point de Corruption."],
    ["Vous avez passé 1d6 ans dans les fosses de combat à vous mesurer aux autres orcs pour amuser la foule."],
    ["Vous êtes resté loyal à l’Empire et vous avez combattu les autres orcs. Vous êtes considéré comme un traître et vous avez été banni."],
    ["Vous avez attrapé la lèpre et vous avez perdu votre nez et vos oreilles."],
    ["Vous avez été enchaîné aux bancs de nage d’un bateau esclavagiste pendant 1d6 ans."],
    ["Vous êtes un eunuque et vous montiez la garde pour protéger les concubines de l’empereur."],
    ["Du tissu cicatriciel recouvre la moitié de votre corps qui a été prise dans le souffle d’un sort."],
    ["Vous avez fui l’esclavage et, depuis, vous vivez en pleine nature."],
    ["Vous avez gagné votre vie en exerçant votre profession."],
    ["Vous êtes tombé amoureux d’une humaine mais vous avez été rejeté."],
    ["Vous avez engendré ou enfanté 3d6 enfants. Lancez de nouveau 3d6 et soustrayez le résultat au nombre de vos enfants pour déterminer combien ont survécu (minimum 0)."],
    ["Vous avez beaucoup voyagé. Vous parlez une langue supplémentaire."],
    ["Vous avez reçu une bonne éducation. Vous savez lire et écrire la langue commune."],
    ["Vous avez combattu bravement pour l’Empereur et on vous a décerné une médaille pour votre courage."],
    ["Vous avez sauvé un noble important d’une tentative d’assassinat."],
    ["Un humain a brisé vos chaînes et vous a libéré afin que vous soyez le seul maître de votre destin."],
    ["Vous avez pris l’épée d’un guerrier que vous avez tué."],
    ["Les Divinités du Sang et du Fer viennent vous voir dans vos rêves. Vous commencez le jeu avec 1 en Folie."],
    ["Vous avez gagné de l’argent et vous commencez le jeu avec 2d6 sc."],
])

orc_personalite = Interval(_3d6).extend([
    [ 3,  3, "Vous combattez pour libérer votre peuple de l’esclavage."],
    [ 4,  4, "Les orcs sont bien plus que les tueurs créés par l’empereur. Ils forment un peuple ; ils ont une âme et un coeur ; ils ont des rêves et des ambitions. Il vous faut surmonter votre nature sauvage et trouver votre place dans ce monde."],
    [ 5,  6, "L’Enfer s’abat sur le monde. Qu’il en soit ainsi."],
    [ 7,  8, "Vous vous préoccupez de vous, vous prenez ce que vous voulez et vous faites ce que bon vous semble."],
    [ 9, 12, "Tuer !"],
    [13, 14, "Vous ne discutez jamais les ordres. Vous faites toujours ce qu’on vous dit."],
    [15, 16, "Vous voulez vous venger et vous tuerez tous ceux qui essaieront de vous en empêcher."],
    [17, 17, "Vous pensez avoir été créé pour une raison. Sans vos chaînes, vous n’avez plus de but."],
    [18, 18, "Vous pensez que votre peuple a commis un grand mal au nom de l’Empire. Vous essayez de réparer ces torts."],
])

################ PROFESSION

pro_academique = Weight().extend([
    ["Architecture "],
    ["Astrologie "],
    ["Ingénierie "],
    ["Etiquette et coutumes "],
    ["Folklore "],
    ["Géographie "],
    ["Héraldique "],
    ["Histoire "],
    ["Loi "],
    ["Littérature "],
    ["Magie "],
    ["Médecine "],
    ["Navigation "],
    ["Occulte "],
    ["Philosophie "],
    ["Politique "],
    ["Nature "],
    ["Religion "],
    ["Science "],
    ["Guerre "],
])

pro_commune = Weight().extend([
    ["Dompteur/Dresseur "],
    ["Apothicaire ou Guérisseur "],
    ["Artisan, Choisissez un domaine artisanal. Exemples : boulanger, frogeron, relieur, brasseur, chapentier, accastilleur, cordonnier, teinturier, souffleur de verre, joaillier, tanneur, maçon, potier, imprimeur et tailleur. "],
    ["Artiste. Choisissez un art. Exemples : peintre, poëte, sculpteur et écrivain. Si vous choisissez poëte ou écrivain, vous pouvez lire et écrire une des langues que vous parlez. "],
    ["Batelier ou Passeur "],
    ["Boucher "],
    ["Cuisinier "],
    ["Berger ou Eleveur "],
    ["Saltimbanque. Choisissez un mode d'expression. Exemples : acteur, athlète, comédien, courtisane, danseur, orateur, marionnettiste, chanteur et conteur. "],
    ["Fermier "],
    ["Pêcheur ou Baleinier "],
    ["Palefrenier "],
    ["Travailleur. Choisissez un travail. Exemples : ramoneur, fossoyeur, porteur, débardeur et balayeur. "],
    ["Marchand. Choisissez une marchandise. Exemples : armes, céréales, bétail, esclaves, épices et textiles. "],
    ["Mineur "],
    ["Musicien. Choisissez un instrument. Exemples : percussions, instruments à cordes et instruments à vent. "],
    ["Marin "],
    ["Serviteur ou Valet "],
    ["Commerçant "],
    ["Charretier "],
])

pro_criminelle = Weight().extend([
    ["Agitateur "],
    ["Mendiant "],
    ["Cambrioleur "],
    ["Fêtard ou Débauché "],
    ["Charlatan ou Manipulateur "],
    ["Cultiste "],
    ["Receleur "],
    ["Faussaire "],
    ["Flambeur "],
    ["Pilleur de tombes "],
    ["Informateur "],
    ["Meurrtrier "],
    ["Pcikpocket "],
    ["Pirate "],
    ["Prostitué "],
    ["Rebelle ou Terroriste "],
    ["Saboteur "],
    ["Espion "],
    ["Malfrat "],
    ["Gamin des rues "],
])

pro_martiale = Weight().extend([
    [1, "Agent "],
    [1, "Détective "],
    [2, "Garde "],
    [1, "Geôlier "],
    [1, "Officier "],
    [1, "Marin "],
    [1, "Mercenaire "],
    [2, "Milicien "],
    [2, "Patrouilleur "],
    [3, "Conscrit paysan "],
    [1, "Esclave "],
    [2, "Soldat "],
    [1, "Ecuyer "],
    [1, "Tortionnaire "],
])

pro_religieuse = Weight().extend([
    [2, "Adepte. Vous êtes un fervent fidèle des préceptes de votre religion. Vous pouvez lire et écrire une des langues que vous parlez. "],
    [2, "Evangéliste. Vous voyagez pour prêcher la bonne parole à qui veut l'entendre et vous dépendez de la charité des croyants. Vous pouvez lire et écrire une des langues que vous parlez. "],
    [1, "Fanatique. Par le dénuement vous pensez pouvoir vous rapporcher de vos dieux. Vous pouvez vous flageller, vous priver de nourriture et de boisson ou trouver un autre moyen de vous faire souffir. "],
    [1, "Hérétique. Vos croyances religieuses sont considérées comme dangeureuses et hérétiques par les responsables de votre foi. "],
    [2, "Initié de la Vieille Foi. Vous avez été initié à la Vieille Foi. "],
    [2, "Ministre du culte. Vous êtes le chef religieux de votre communauté. Vous pouvez lire et écrire une des langues que vous parlez. "],
    [2, "Acolyte du Nouveau Dieu. Vous étudiez pour devenir un prêtre du Culte du Nouveau Dieu. Vous pouvez lire et écrire une des langues que vous parlez. "],
    [1, "Serviteur d'un inquisiteur. Vous êtes au service d'un inquisiteur ou d'un chasseur de sorciers. "],
    [3, "Pélerin. Vous voyagez pour vous rendre sur les lites sacrés de votre religion. "],
    [2, "Prédicateur de rue. Vous prêchez dans les rues, en implorant les passants de se repentir car la fin est proche. "],
    [2, "Pupille du temple. Vous avez été élevé dans un temple. Vous étiez probablement un orphelin qui a été confié au clergé. "],
])

pro_marginale = Weight().extend([
    [1, "Bandit, Brigand, Bandit de grand chemin "],
    [1, "Barbare "],
    [1, "Exilé "],
    [1, "Cueilleur "],
    [2, "Guide "],
    [1, "Ermite "],
    [2, "Chasseur "],
    [1, "Nomade ou Vagabond "],
    [1, "Pionnier "],
    [1, "Braconnier ou Voleur de bétail "],
    [1, "Prospecteur "],
    [1, "Hors-la-loi "],
    [2, "Réfugié "],
    [1, "Spéléologue "],
    [1, "Pisteur "],
    [1, "Trappeur "],
    [1, "Bûcheron "],
])

################ EQUIPEMENT

equipement = Interval(_3d6).extend([
    [ 3,  4, "Misérable" ],
    [ 5,  8, "Pauvre" ],
    [ 9, 13, "Modeste" ],
    [14, 16, "Confortable" ],
    [17, 17, "Aisé" ],
    [18, 18, "Riche" ],
])

################ ELEMENT INTERESSANT

element = Weight().extend([
# Table 1
    ["Une petite boîte métallique sans ouverture d’où provient un tic-tac à peine perceptible."],
    ["Un crâne en cristal transparent."],
    ["Une sphère en verre remplie d’eau dans laquelle vit un minuscule poisson rouge."],
    ["Une odeur curieuse, une odeur âcre ou un problème de peau qui ne disparaît jamais."],
    ["Une bouteille de larme de vierges."],
    ["Une fleur qui ne fane jamais."],
    ["Un petit aimant ou un miroir en argent."],
    ["Une invitation à une fête ou un masque de bal masqué."],
    ["Un mouchoir brodé avec des initiales qui ne se salit jamais."],
    ["Un couteau pliant dont la lame est toujours aiguisée."],
    ["Une paire de chaussons de danse."],
    ["Une minuscule araignée mécanique inerte."],
    ["Une tête réduite."],
    ["Un oeil de verre ou un bézoard."],
    ["Un livre rédigé en une langue inconnue ou qui contient des choses que vous auriez aimé ne jamais connaître."],
    ["Un paquet de cartes pour dire la bonne aventure."],
    ["Une paire de dés pipés."],
    ["Six petits gâteaux. Une personne qui en mange un est rassasiée jusqu’au lendemain à l’aube."],
    ["Un phylactère qui contient un morceau de papier sur lequel est inscrit un seul mot."],
    ["La réputation d’être un dur à cuire."],
# Table 2
    ["Une flûte ou une flûte de pan ou un autre instrument de musique."],
    ["Un reliquaire contenant un petit os."],
    ["Une minuscule idole de démon taillée dans une pierre verte."],
    ["Un gage d’amour d’un admirateur ou d’un amant."],
    ["Un lapin, un écureuil ou une souris de compagnie."],
    ["Un monocle ou une lourde paire de lunettes."],
    ["Un collier en argent avec un médaillon."],
    ["Une tabatière remplie de tabac à priser."],
    ["Une écaille de dragon étincelante."],
    ["Un oeuf de la taille d’un poing couvert de points bleus."],
    ["Un amour non partagé."],
    ["Un chaudron noir en fer rempli d’ossements."],
    ["Une boîte avec 1d20 clous en fer."],
    ["Une fiole d’un parfum à la senteur sucrée ou une bouteille de tord-boyaux."],
    ["Une plume en bronze."],
    ["Une pièce de monnaie en fer rayée d’un côté ou une pièce de monnaie en acier avec une tête de dragon des deux côtés."],
    ["Une boîte contenant 1d6+1 pinceaux."],
    ["Une poupée tachée de sang."],
    ["Une bague de fiançailles en argent valant 1 ca."],
    ["Une brosse, un peigne ou une ombrelle."],
# Table 3
    ["Une savonnette ou une serviette."],
    ["Trente mètres de ficelle enroulée en pelote."],
    ["Un médaillon avec un portrait, une boucle de cheveux ou un autre présent offert par une personne qui vous aime."],
    ["Un petit tonnelet de bière."],
    ["Deux lapins ou un sac rempli de casseroles et de poêles."],
    ["Une flèche ou un carreau avec une pointe en argent."],
    ["La moitié d’une carte au trésor, la carte d’une région étrangère ou une grande carte bleue couverte de cercles avec d’étranges inscriptions entre chacun d’eux."],
    ["Une arme au choix du MJ."],
    ["Un bouclier léger ou lourd avec une devise inhabituelle."],
    ["Une élégante tenue d’une étrange teinte."],
    ["Un serviteur."],
    ["Un symbole sacré en argent ou une belle icône religieuse."],
    ["Un sac avec 2d6 pierres, des glands, des têtes coupées ou des champignons savoureux."],
    ["Une boîte à musique qui joue un air très, très triste quand on l’ouvre."],
    ["Un sac avec 100 billes."],
    ["Un flacon en verre rempli de salive, un sac rempli de morceaux pourris de poulets ou une cicatrice indécente."],
    ["Un petit sac contenant 3d6 dents, un collier avec 1d6 oreilles ou 1d6 têtes coupées attachées ensemble par leurs cheveux."],
    ["Un nouveau-né qui peut être le vôtre ou pas."],
    ["Une boîte contenant six magnifiques bougies blanches."],
    ["Un petit chien ayant tendance à être féroce."],
# Table 4
    ["Un flacon en verre contenant un coléoptère couvert de points lumineux (éclaire comme une bougie)."],
    ["Une paire de bottes qui accorde 1 avantage aux jets de déplacement discret ou une cape grise qui accorde 1 avantage aux jets pour se cacher."],
    ["Un flacon en verre contenant un étrange organe dans de l’alcool."],
    ["Une minuscule cage en verre."],
    ["Une boîte contenant 1d6 bouteilles d’encre, chacune d’une couleur différente."],
    ["Un minuscule hibou mécanique inerte."],
    ["2 m d’une corde qui ne peut être coupée."],
    ["L’insigne d’une compagnie de mercenaires."],
    ["Une boîte à cigares ou une poche et une blague à tabac."],
    ["Un médaillon avec le visage d’une femme hideuse."],
    ["Un collier garni de pointes, des pinces pour la peau et un fouet."],
    ["Un sac de farine de 5 kg."],
    ["Une plaque en bronze avec un nom gravé dessus."],
    ["Une bouteille en cristal contenant un fluide qui émet de la lumière sur 60 cm de rayon quand on retire le bouchon."],
    ["Une petite boîte avec six morceaux de craie."],
    ["Une lettre d’introduction signée par une personne puissante et influente."],
    ["Un éclat de miroir sur la surface duquel se reflète un lieu étrange."],
    ["Une petite cage dorée contenant une fée vivante qui ne peut pas parler."],
    ["Une bouteille avec inscrit sur son étiquette : « OEil de Triton »."],
    ["Un sac de haricots."],
# Table 5
    ["Un pot de graisse ou un pot de colle."],
    ["Un globe en verre rempli d’une brume tourbillonnante."],
    ["Une cape avec 2d20 poches cachées dans sa doublure."],
    ["Une paire de lunettes qui vous permet parfois de voir à travers 30 cm de pierre."],
    ["Une petite boîte bleue qui est plus grande à l’intérieur (deux fois son volume normal)."],
    ["Une petite sphère en acier."],
    ["Une main pétrifiée qui se contracte à la lueur de la pleine lune."],
    ["Le véritable nom d’un diable très mineur."],
    ["Un squelette de souris animé."],
    ["Une arme au choix du MJ qui émet constamment de la lumière sur 1 m de rayon."],
    ["Une poche qui contient 1d6+1 pincées d’une poussière qui, quand elle est saupoudrée, transforme 1 m cube de pierre en argile molle."],
    ["Un pot de peinture qui se remplit entièrement tous les jours à l’aube."],
    ["Une minuscule bille en métal qui flotte à 2,5 cm au-dessus de n’importe quelle surface solide."],
    ["Une poche contenant 1d6+1 pincées de poudre de diamant."],
    ["Un cerveau dans un bocal."],
    ["Un sac rempli de tiges étrangement charnues."],
    ["Une masse en métal violet avec un nom gravé sur le manche."],
    ["Un énorme morceau de charbon qui semble très menaçant"],
    ["Un morceau d’ambre contenant une mouche à visage humain."],
    ["Des regrets pour toute une vie."],
# Table 6
    ["La réputation d’être un amant remarquable."],
    ["Un halfelin momifié."],
    ["Une tenue qui peut changer d’aspect tous les matins à l’aube."],
    ["Une conserve de betteraves."],
    ["Un rôdeur qui vous suit mais fuit quand vous approchez."],
    ["Un passé honteux."],
    ["Un rêve récurrent et perturbant."],
    ["Une malle remplie de morceaux de corps."],
    ["Une charrette ou une carriole tirée par un âne triste."],
    ["Trois petites souris blanches qui vous murmurent des choses étranges quand vous dormez."],
    ["Un tic nerveux ou facial ou un rire énervant."],
    ["Un thermomètre."],
    ["Une perche télescopique de 3 m de long."],
    ["L’ombre que vous projetez ne correspond jamais complètement à vos mouvements."],
    ["De la peur et du dégoût."],
    ["Un penchant pour l’alcool."],
    ["Une fine chemise de mailles qui compte comme une armure légère et peut être portée sous des vêtements normaux (fonctionne comme une cotte de mailles et n’est pas cumulative avec une autre armure)."],
    ["Un fétiche bizarre."],
    ["Une épouse exigeante."],
    ["Un terrible secret que vous n’osez pas révéler."],
])

################ TRAITS

trait_positif = Weight().extend([
    ["Bienveillant"],
    ["Joyeux"],
    ["Courageux"],
    ["Fiable"],
    ["Déterminé"],
    ["Consciencieux"],
    ["Compréhensif"],
    ["Honnête"],
    ["Clément"],
    ["Courtois"],
    ["Généreux"],
    ["Serviable"],
    ["Sincère"],
    ["Honorable"],
    ["Humble"],
    ["Idéaliste"],
    ["Ingénieux"],
    ["Gentil"],
    ["Noble"],
    ["Méthodique"],
])

trait_negatif = Weight().extend([
    ["Distant"],
    ["Arrogant"],
    ["Prétentieux"],
    ["Lâche"],
    ["Fourbe"],
    ["Impulsif"],
    ["Fainéant"],
    ["Malveillant"],
    ["Antipathique"],
    ["Querelleur"],
    ["Grossier"],
    ["Sarcastique"],
    ["Égoïste"],
    ["Négligé"],
    ["Radin"],
    ["Renfrogné"],
    ["Grincheux"],
    ["Irréfléchi"],
    ["Inamical"],
    ["Vulgaire"],
])

################ ROOT

def S(*args) :
    return Sequence().extend([*args])

sel_main = S(
    Weight().extend([
        Title("Humain", S(
            Label("Historique  ", humain_historique),
            Label("Personalité ", humain_personalite),
            Label("Religion    ", humain_religion),
            Label("Age         ", humain_age),
            Label("Stature     ", humain_stature),
            Label("Apparence   ", humain_apparence),
        )),
        Title("Automate", S(
            Label("Age         ", automate_age),
            Label("Fonction    ", automate_fonction),
            Label("Forme       ", automate_forme),
            Label("Apparence   ", automate_apparence),
            Label("Historique  ", automate_historique),
            Label("Personalité ", automate_personalite),
        )),
        Title("Changelin", S(
            Label("Age Véritable", changelin_age),
            Label("Sexe Apparent", changelin_sexe),
            Label("Ascendance Apparente", changelin_ascendance),
            Label("Historique  ", changelin_historique),
            Label("Particularité", changelin_particularite),
            Label("Personalité ", changelin_personalite),
        )),
        Title("Gobelin", S(
            Label("Age         ", gobelin_age),
            Label("Stature     ", gobelin_stature),
            Label("Apparence Distinctive", gobelin_apparence),
            Label("Habitude Etrange", gobelin_habitude),
            Label("Historique  ", gobelin_historique),
            Label("Personalité ", gobelin_personalite),
        )),
        Title("Nain", S(
            Label("Age         ", nain_age),
            Label("Stature     ", nain_stature),
            Label("Apparence   ", nain_apparence),
            Label("Haine       ", nain_haine),
            Label("Historique  ", nain_historique),
            Label("Personalité ", nain_personalite),
        )),
        Title("Orc", S(
            Label("Age         ", orc_age),
            Label("Stature     ", orc_stature),
            Label("Apparence   ", orc_apparence),
            Label("Historique  ", orc_historique),
            Label("Personalité ", orc_personalite),
        )),
    ]),
    '\r',
    Label("Profession", Weight().extend([
        pro_academique,
        pro_commune,
        pro_criminelle,
        pro_martiale,
        pro_religieuse,
        pro_marginale,
    ])),
    Label("Equipement", S(equipement)),
    Label("Element particulier", S(element)),
    Label("Trait Positif", S(trait_positif)),
    Label("Trait Negatif", S(trait_negatif)),
)

sel_main.execute()
