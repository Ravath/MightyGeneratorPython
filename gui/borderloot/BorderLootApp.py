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
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.dropdown import DropDown

kivy.require('2.1.0')

# ============== GENERATION IMPORTS ==============
# exec(open("generators/borderlands/items.py", encoding='utf-8').read())
from generators.borderlands.items import generation, force_item_rarity
from wordgenerator.Print import PrintNode
PrintNode.print_to_buffer()

# ============== WIDGET DEFINITIONS ==============
class TreasureDropDown(DropDown):
    pass

class WeaponDropDown(DropDown):
    pass

class RarityDropDown(DropDown):
    pass

class BorderlootWidget(Widget):
    """
    Constructing Kivy Widget.
    
    item_text : (String) Will display the result of the generated item
    display_text : Executes generation from borderlands/items and stores
    generated text into item_text
    """

    item_text = StringProperty()
    
    """Dropdown buttons"""
    treasure_button = ObjectProperty()
    weapon_button = ObjectProperty()
    rarity_button = ObjectProperty()

    def __init__(self, **kwargs):
        super(BorderlootWidget, self).__init__(**kwargs)

        # dropdown lists
        self.t_dropdown = TreasureDropDown()
        self.w_dropdown = WeaponDropDown()
        self.r_dropdown = RarityDropDown()
        self.t_dropdown.bind(on_select=lambda instance, x: setattr(self.treasure_button, 'text', x))
        self.w_dropdown.bind(on_select=lambda instance, x: setattr(self.weapon_button, 'text', x))
        self.r_dropdown.bind(on_select=lambda instance, x: setattr(self.rarity_button, 'text', x))

    def display_text(self):
        force_item_rarity("LEGENDARY")
        generation.execute()
        print("\\------------------------------------------------------------")
        print(generation.text)
        self.item_text = str(generation.text)
        
# ================= APP DEFINITION ================

class BorderlootApp(App):
    """
    The GUI interface for generating borderland loot.
    
    For more information
    about Borderloot organisation widget, see borderloot.kv
    """
    
    def build(self):
        return BorderlootWidget()

# ==================== APP RUN ====================

BorderlootApp().run()

