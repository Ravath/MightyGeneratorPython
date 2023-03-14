# -*- coding: utf-8 -*-

# ================= MAGICK TRICK =================
# When using an external console, we need to manually
# add the project path or it won't find any relative
# dependencies.
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# ================= GUI IMPORTS ==================
import kivy
from kivy.app import App
from kivy.uix.button import Button

kivy.require('1.0.9')

# ============== GENERATION IMPORTS ==============
# exec(open("generators/borderlands/items.py", encoding='utf-8').read())
from generators.borderlands.items import generation
from wordgenerator.Print import PrintNode
PrintNode.print_to_buffer()

# ============== BUTTON DEFINITIONS ==============

def loot_generation_callback(instance):
    """
    Generates an item and prints it.
    """
    generation.execute()
    print("\\---------------------------------------------------------------")
    print(generation.text)

generation_button = Button(text='GENERATE')
generation_button.bind(on_press=loot_generation_callback)

# ================= APP DEFINITION ================

class BorderLootApp(App):
    """
    The GUI interface for generating borderland loot.
    """
    
    def build(self):
        return generation_button

# ==================== APP RUN ====================

BorderLootApp().run()

