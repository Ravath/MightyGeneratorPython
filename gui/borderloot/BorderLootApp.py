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
from generators.borderlands.items import generation, force_chest_type, force_item_type, force_item_rarity
from wordgenerator.Print import PrintNode
PrintNode.print_to_buffer()

# ============== WIDGET DEFINITIONS ==============
class ChestDropDown(DropDown):
    def attribute_chest_type(self, che:str):
        global FORCED_CHEST
        FORCED_CHEST = che
pass

class ItemDropDown(DropDown):
    def attribute_item_type(self, i_typ:str):
        """" Put an item type on pressing the corresponding button, then stores
        it for generation with force_item_type function"""
        global FORCED_ITEM_TYPE
        FORCED_ITEM_TYPE = i_typ
pass

class RarityDropDown(DropDown):
    def attribute_rarity(self, rar:str):
        """" Put a rarity on pressing the corresponding button, then stores
        it for generation with force_item_rarity function"""
        global FORCED_RARITY
        FORCED_RARITY = rar
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
    item_button = ObjectProperty()
    rarity_button = ObjectProperty()

    def __init__(self, **kwargs):
        super(BorderlootWidget, self).__init__(**kwargs)

        # dropdown lists
        self.c_dropdown = ChestDropDown()
        self.i_dropdown = ItemDropDown()
        self.r_dropdown = RarityDropDown()
        self.c_dropdown.bind(on_select=lambda instance, x: setattr(self.chest_button, 'text', x))
        self.i_dropdown.bind(on_select=lambda instance, x: setattr(self.item_button, 'text', x))
        self.r_dropdown.bind(on_select=lambda instance, x: setattr(self.rarity_button, 'text', x))

    def display_text(self):
        # If a button has been pressed for item change, apply its forced specs
        if ('FORCED_CHEST' in globals()):
            global FORCED_CHEST
            force_chest_type(FORCED_CHEST)
        else :
            pass
        if ('FORCED_ITEM_TYPE' in globals()):
            force_item_type(FORCED_ITEM_TYPE)
        else :
            pass
        if ('FORCED_RARITY' in globals()):
            force_item_rarity(FORCED_RARITY)
        else :
            pass
        generation.execute()
        print("\\------------------------------------------------------------")
        print(generation.text)
        self.item_text = str(generation.text)

# ================= APP DEFINITION ================

class BorderlootApp(App):
    """
    The GUI interface for generating borderland loot.

    For more information about Borderloot organisation widget,
    see borderloot.kv
    """

    def build(self):
        return BorderlootWidget()

# ==================== APP RUN ====================

BorderlootApp().run()

