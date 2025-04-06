# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageShow, PSDraw

# Define the PostScript file
ps_file = open("bl_weapon.ps", "wb")

# Create a PSDraw object
ps_object = PSDraw.PSDraw(ps_file)

# Start the document
ps_object.begin_document()

# Image background creation with dimensions
width = 250
height = 600

# Colors, used for later
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
# Background generation
image = Image.new('RGBA', (width, height), WHITE)

# Define the PostScript font
font_name = "Helvetica-Narrow-Bold"
font_size = 15
ps_object.setfont(font_name, font_size)

text = "Nom d'Arme"
# Assuming average character width as 0.6 of the font size
text_width = len(text) * font_size * 0.6
text_height = font_size
# Set the position (top-center)
page_width, page_height = 595, 842  # A4 size in points
text_x = (page_width - text_width) // 2
text_y = page_height - text_height - 50  # Distance from the top of the page



# Name
ps_object.text((0, 0), "Nom d'Arme")

ps_object.text((10, 25), "Type Arme")
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
    ps_object.line([5,(300 + l * 25 )],[245,(300 + l * 25)])
    
nb_columns_table = [0, 1, 2, 3, 4, 5]
for c in nb_columns_table :
    ps_object.line([(5 + c * 48),300],[(5 + c * 48),400])

image_path = "BL_Frame_Square.ppm"
with Image.open(image_path) as im:
    # Resize the image if it's too large
    im.thumbnail((page_width - 100, page_height // 2))
    ps_object.image([0, 0 + im.width, 0, 0 + im.height], im, 75)

# End the document
ps_object.end_document()
ps_file.close()