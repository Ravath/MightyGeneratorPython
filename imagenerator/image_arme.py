# -*- coding: utf-8 -*-
import re
from PIL import Image, ImageDraw, ImageFont, ImageShow
from generators.borderlands.gen_david_weapon import generation

###################
# Text Generation #
###################

res = generation.execute()
#res.display_vars()

find_weapon = re.findall(r"Pistolet|Fusil à pompe|Fusil d'assaut|Mitraillette|Sniper|Grenade|Bouclier", res.get_var("W_TYPE"))
find_rarity = re.findall(r"Commun|Uncommun|Rare|Epique|E-Tech|Légendaire", res.get_var("W_TYPE"))
find_brand = re.findall(r"Jakobs|Maliwan|Hyperion|Dahl|Vladof|Bandit|Tediore|Torgue|Classic|Contact|Proximity|MIRV|Singularity|Tesla|Transfusion|Betty|Absorb|Adaptive|Amplify|Booster|Lifeline|Nova|Raid|Shield|Spike|Turtle", res.get_var("ITEM_MANUFACTURER"))
find_X2_visor = re.findall(r"- Viseur X2", res.get_var("PROPERTIES"))
find_X4_visor = re.findall(r"- Viseur X4", res.get_var("PROPERTIES"))
find_X6_visor = re.findall(r"- Viseur X6", res.get_var("PROPERTIES"))

####################
# Image Generation #
####################

# Image background creation with dimensions
width = 250
height = 600

# Colors, used for later
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
# Background generation
image = Image.new('RGBA', (width, height), WHITE)

# Font used for Borderloot: compacta 
#font_used = ImageFont.load_default(15)
font_used = ImageFont.truetype('compacta.ttf', 18)
font_used2 = ImageFont.truetype('Compacta_Light.ttf', 18)
font_used_big = ImageFont.truetype('compacta.ttf', 32)
# get a drawing context
d = ImageDraw.Draw(image)

# Weapon name

d.text((10, 10), res.get_var("W_NAME"), font=font_used, fill=BLACK)

# Weapon type
if find_weapon:
    d.text((10, 30), find_weapon[0], font=font_used, fill=BLACK)
else:
    d.text((10, 30), "Rareté Inconnue", font=font_used, fill=BLACK)
    
# Rarity    

if ((find_rarity[0] == "Commun") or (find_rarity[0] == "Uncommun")) and ((find_weapon[0] == "Grenade") or (find_weapon[0] == "Mitraillette")) :
    d.text((100, 30), find_rarity[0] + "e", font=font_used, fill=BLACK)
elif find_rarity:
    d.text((100, 30), find_rarity[0], font=font_used, fill=BLACK)
else :
    d.text((100, 30), "Rareté Inconnue", font=font_used, fill=BLACK)

# Brand

if find_brand:
    d.text((190, 30), find_brand[0], font=font_used, fill=BLACK)
else:
    d.text((190, 30), "Marque Inconnue", font=font_used, fill=BLACK)

# Define if Weapon type is a Gun, a Shield or a Grenade
if   find_weapon[0] == "Pistolet":
    weapon_type = "gun"
elif find_weapon[0] == "Fusil à pompe":
    weapon_type = "gun"
elif find_weapon[0] == "Fusil d'assaut":
    weapon_type = "gun"
elif find_weapon[0] == "Mitraillette":
    weapon_type = "gun"
elif find_weapon[0] == "Sniper":
    weapon_type = "gun"
elif find_weapon[0] == "Grenade" :
    weapon_type = "grenade"
elif find_weapon[0] == "Bouclier" :
    weapon_type = "bouclier"
else :
    weapon_type = None

# Gun damage, magazine, difficulty threshold, brand information and properties#
if weapon_type == "gun":
    find_shoot_simple = re.findall(r"Tir Simple", res.get_var("W_SHOOT"))
    find_shoot_burst = re.findall(r"Tir Rafale", res.get_var("W_SHOOT"))
    find_shoot_auto = re.findall(r"Tir Automatique", res.get_var("W_SHOOT"))
    difficulty = int(res.get_var("W_AIM")) 
    bonus_2x = 0
    bonus_4x = 0
    bonus_6x = 0
    range_0x = 6
    
    if find_X2_visor :
        bonus_2x = -2
    if find_X4_visor :
        bonus_4x = -4
    if find_X6_visor :
        bonus_6x = -6

    range_2x = 8 + bonus_2x
    range_4x = 10 + bonus_4x
    range_6x = 12 + bonus_6x

    # Table for Difficulty threshold #
    nb_lines_table = [0, 1, 2, 3, 4]
    for l in nb_lines_table :
        d.line((5,(300 + l * 25 ),245,(300 + l * 25)), fill=BLACK)
        
    nb_columns_table = [0, 1, 2, 3, 4, 5]
    for c in nb_columns_table :
        d.line(((5 + c * 48),300,(5 + c * 48),400), fill=BLACK)
        
    d.text((7, (300+8 )), "Distance"   , font=font_used, fill=BLACK)
    d.text((7, (300+32)), "Simple"      , font=font_used, fill=BLACK)
    d.text((7, (300+58)), "Rafale"      , font=font_used, fill=BLACK)
    d.text((7, (300+82)), "Auto"        , font=font_used, fill=BLACK)    
    
    d.text(((5+52 ), (300+8)), "0-5"     , font=font_used, fill=BLACK)
    d.text(((5+100), (300+8)), "6-10"    , font=font_used, fill=BLACK)
    d.text(((5+148), (300+8)), "11-15"  , font=font_used, fill=BLACK)
    d.text(((5+196), (300+8)), "16-20"  , font=font_used, fill=BLACK)
    
    if find_shoot_simple:
        d.text(((5+70 ), (300+32)), str(difficulty+range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (300+32)), str(difficulty+range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (300+32)), str(difficulty+range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (300+32)), str(difficulty+range_6x), font=font_used, fill=BLACK)
    if find_shoot_burst:
        d.text(((5+70 ), (300+58)), str(difficulty +2 +range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (300+58)), str(difficulty +2 +range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (300+58)), str(difficulty +2 +range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (300+58)), str(difficulty +2 +range_6x), font=font_used, fill=BLACK)
    if find_shoot_auto:
        d.text(((5+70 ), (300+82)), str(difficulty +4 +range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (300+82)), str(difficulty +4 +range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (300+82)), str(difficulty +4 +range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (300+82)), str(difficulty +4 +range_6x), font=font_used, fill=BLACK)

    # Frames for weapon damage and weapon magazine
    frame_square = Image.open('BL_Frame_Square116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (5, 100))
    back_im.paste(frame_square, (126, 100))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((10, 110), "Degats", font=font_used, fill=BLACK)
    BL_image_arme.text((10, 158), res.get_var("W_DGTS"), font=font_used_big, fill=BLACK)   
    # Magazine
    BL_image_arme.text((131, 110), "Magasin", font=font_used, fill=BLACK)
    BL_image_arme.text((131, 158), res.get_var("W_MAG"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 410), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()

elif weapon_type == "grenade":
    # Frame for grenade damage
    frame_square = Image.open('BL_Frame_Rectangle_232x116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (10, 100))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((15, 110), "Dégâts", font=font_used, fill=BLACK)
    BL_image_arme.text((15, 158), res.get_var("W_DGTS"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 250), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()


elif weapon_type == "bouclier":
    # Frame for shield capacity
    frame_square = Image.open('BL_Frame_Rectangle_232x116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (10, 100))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((15, 110), "Capacité", font=font_used, fill=BLACK)
    BL_image_arme.text((15, 158), res.get_var("W_CAPA"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 250), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()

else:
    print("Arme inconnue")
    print(find_weapon[0])