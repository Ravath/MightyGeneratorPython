# -*- coding: utf-8 -*-
import re
from PIL import Image, ImageDraw, ImageFont, ImageShow
from generators.borderlands.gen_david_weapon import generation

###################
# Text Generation #
###################

res = generation.execute()
#res.display_vars()

#find_weapon = re.findall(r"Pistolet|Fusil à pompe|Fusil d'assaut|Mitraillette|Sniper|Grenade|Bouclier", res.get_var("W_TYPE"))
find_rarity = re.findall(r"Commun|Uncommun|Rare|Epique|E-Tech|Légendaire", res.get_var("W_TYPE"))
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
if res.get_var("ITEM_TYPE"):
    d.text((10, 30), res.get_var("ITEM_TYPE"), font=font_used, fill=BLACK)
    write_item=res.get_var("ITEM_TYPE")
else:
    d.text((10, 30), "Arme Inconnue", font=font_used, fill=BLACK)
    write_item="Arme Inconnue"
#Save item word length for rarity word emplacement
item_length = d.textlength(write_item, font_used)+6

# Rarity

if ((res.get_var("ITEM_RARITY") == "COMMON") or (res.get_var("ITEM_RARITY") == "UNCOMMON")) and ((res.get_var("ITEM_TYPE") == "GRENADE") or (res.get_var("ITEM_TYPE") == "MACHINEGUN")) :
    d.text((10+item_length, 30), res.get_var("ITEM_RARITY") + "E", font=font_used, fill=BLACK)
    write_rar=res.get_var("ITEM_RARITY") + "E"
elif res.get_var("ITEM_RARITY"):
    d.text((10+item_length, 30), res.get_var("ITEM_RARITY"), font=font_used, fill=BLACK)
    write_rar=res.get_var("ITEM_RARITY")
else :
    d.text((10+item_length, 30), "Rareté Inconnue", font=font_used, fill=BLACK)
    write_rar="Rareté Inconnue"
#Save rarity word length for brand word emplacement
rar_length = d.textlength(write_rar, font_used)+6

# Brand

if res.get_var("ITEM_MANUFACTURER"):
    d.text((10+item_length+rar_length, 30), res.get_var("ITEM_MANUFACTURER"), font=font_used, fill=BLACK)
else:
    d.text((10+item_length+rar_length, 30), "Marque Inconnue", font=font_used, fill=BLACK)

# Gun damage, magazine, difficulty threshold, brand information and properties#
if (res.get_var("ITEM_TYPE") == "HANDGUN") or (res.get_var("ITEM_TYPE") == "SHOTGUN") or (res.get_var("ITEM_TYPE") == "RIFLE") or (res.get_var("ITEM_TYPE") == "MACHINEGUN") or (res.get_var("ITEM_TYPE") == "SNIPER"):       
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
        d.line((5,(188 + l * 25 ),245,(188 + l * 25)), fill=BLACK)
        
    nb_columns_table = [0, 1, 2, 3, 4, 5]
    for c in nb_columns_table :
        d.line(((5 + c * 48),188,(5 + c * 48),288), fill=BLACK)
        
    d.text((7, (188+8 )), "Distance"   , font=font_used, fill=BLACK)
    d.text((7, (188+32)), "Simple"      , font=font_used, fill=BLACK)
    d.text((7, (188+58)), "Rafale"      , font=font_used, fill=BLACK)
    d.text((7, (188+82)), "Auto"        , font=font_used, fill=BLACK)    
    
    d.text(((5+52 ), (188+8)), "0-5"     , font=font_used, fill=BLACK)
    d.text(((5+100), (188+8)), "6-10"    , font=font_used, fill=BLACK)
    d.text(((5+148), (188+8)), "11-15"  , font=font_used, fill=BLACK)
    d.text(((5+196), (188+8)), "16-20"  , font=font_used, fill=BLACK)
    
    if find_shoot_simple:
        d.text(((5+70 ), (188+32)), str(difficulty+range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (188+32)), str(difficulty+range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (188+32)), str(difficulty+range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (188+32)), str(difficulty+range_6x), font=font_used, fill=BLACK)
    if find_shoot_burst:
        d.text(((5+70 ), (188+58)), str(difficulty +2 +range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (188+58)), str(difficulty +2 +range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (188+58)), str(difficulty +2 +range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (188+58)), str(difficulty +2 +range_6x), font=font_used, fill=BLACK)
    if find_shoot_auto:
        d.text(((5+70 ), (188+82)), str(difficulty +4 +range_0x), font=font_used, fill=BLACK)
        d.text(((5+118), (188+82)), str(difficulty +4 +range_2x), font=font_used, fill=BLACK)
        d.text(((5+166), (188+82)), str(difficulty +4 +range_4x), font=font_used, fill=BLACK)
        d.text(((5+214), (188+82)), str(difficulty +4 +range_6x), font=font_used, fill=BLACK)

    # Frames for weapon damage and weapon magazine
    frame_square = Image.open('BL_Frame_Square116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (5, 50))
    back_im.paste(frame_square, (126, 50))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((10, 60), "Degats", font=font_used, fill=BLACK)
    BL_image_arme.text((10, 108), res.get_var("W_DGTS"), font=font_used_big, fill=BLACK)   
    # Magazine
    BL_image_arme.text((131, 60), "Magasin", font=font_used, fill=BLACK)
    BL_image_arme.text((131, 108), res.get_var("W_MAG"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 308), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()
    
# Grenade damage and properties, including brand information#
elif res.get_var("ITEM_TYPE") == "GRENADE":
    # Frame for grenade damage
    frame_square = Image.open('BL_Frame_Rectangle_232x116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (10, 50))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((15, 60), "Dégâts", font=font_used, fill=BLACK)
    BL_image_arme.text((15, 108), res.get_var("W_DGTS"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 200), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()

# Shield Capacity and properties, including brand information#
elif res.get_var("ITEM_TYPE") == "SHIELD":
    # Frame for shield capacity
    frame_square = Image.open('BL_Frame_Rectangle_232x116.png')
    back_im = image.copy()
    back_im.paste(frame_square, (10, 50))
    BL_image_arme = ImageDraw.Draw(back_im)
    # Damage
    BL_image_arme.text((15, 60), "Capacité", font=font_used, fill=BLACK)
    BL_image_arme.text((15, 108), res.get_var("W_CAPA"), font=font_used_big, fill=BLACK)
    # Properties
    BL_image_arme.text((15, 200), res.get_var("PROPERTIES"), font=font_used, fill=BLACK) 
    out = Image.alpha_composite(back_im, back_im)
    
    out.show()

else:
    print("Arme inconnue: ")
    print(res.get_var("ITEM_TYPE"))