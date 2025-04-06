# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageShow

# Image background creation with dimensions
width = 250
height = 600

# Colors, used for later
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
# Background generation
image = Image.new('RGBA', (width, height), WHITE)

# Font used for Borderloot: compacta TO FIND
font_used = ImageFont.load_default(15)

# get a drawing context
d = ImageDraw.Draw(image)

# Name
d.text((10, 10), "Nom d'Arme", font=font_used, fill=(0, 0, 0, 255))

d.text((10, 25), "Type Arme", font=font_used, fill=(0, 0, 0, 255))
# Weapon type (underlined)
# Weapon rarity (bold)
# Weapon brand (italic)
# Weapon line of sight (scheme)
# Damage (case)
# Magazine (case)
# Difficulty threshold (chart)
# Brand information (main words italic)
# Properties (main word underlined)


# Table for Difficulty threshold #
nb_lines_table = [0, 1, 2, 3, 4]
for l in nb_lines_table :
    d.line((5,(300 + l * 25 ),245,(300 + l * 25)), fill=BLACK)
    
nb_columns_table = [0, 1, 2, 3, 4, 5]
for c in nb_columns_table :
    d.line(((5 + c * 48),300,(5 + c * 48),400), fill=BLACK)

frame_square = "BL_Frame_Square.ppm"
image.open(frame_square)

out = Image.alpha_composite(image, image)

out.show()