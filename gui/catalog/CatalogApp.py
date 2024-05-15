# -*- coding: utf-8 -*-

# ================= MAGICK TRICK =================
# When using an external console, we need to manually
# add the project path or it won't find any relative
# dependencies.
import sys, os, pathlib
from functools import partial
from kivy.utils import platform
from jnius import autoclass

"""The folder containing the scripts."""
DATA_FOLDER="generators/"
if platform == 'android' :
    context = autoclass('android.content.Context')
    path_file = context.getExternalFilesDir(None)
    path = path_file.getAbsolutePath()
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.READ_EXTERNAL_STORAGE,
        Permission.WRITE_EXTERNAL_STORAGE,
        # Permission.MANAGE_EXTERNAL_STORAGE
    ])
    from android import loadingscreen
    loadingscreen.hide_loading_screen()

    # sdcard/
    DATA_FOLDER = os.getenv('EXTERNAL_STORAGE') or os.path.expanduser("~")
    DATA_FOLDER = os.path.join(DATA_FOLDER, "generators")
    if not os.path.exists(DATA_FOLDER) :
        os.makedirs(DATA_FOLDER)

else:
    DATA_FOLDER="generators/"
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


def error_log(message) :
    print(message)
    # f = open(os.getenv('EXTERNAL_STORAGE')+"/log.txt", "w")
    # f.write(message)
    # f.close()
    # f = open(os.getenv('EXTERNAL_STORAGE')+"/log.txt", "a")
    # f.write(message)
    # f.close()

#create your own sub folders and files...


# ================= GUI IMPORTS ==================
import kivy
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.treeview import TreeViewLabel

kivy.require('2.1.0')

# ============== GENERATION IMPORTS ==============
from importlib import import_module

# ============== WIDGET DEFINITIONS ==============

class CatalogWidget(Widget):
    """
    Main Kivy Widget of the application.
    """
    
    """Will display the result of the generated item"""
    generated_text = StringProperty()

    """Launch generation button"""
    generator_button = ObjectProperty()


    def __init__(self, **kwargs):
        super(CatalogWidget, self).__init__(**kwargs)
        self.generation=None
        self.generated_text = "No generator selected yet"
        self.debugtrace=""

        try :
            if os.path.isdir(DATA_FOLDER) :
                self.create_tree()
                self.app_log(self.debugtrace) 
            else :
                self.app_log("Catalog folder doesn't exist") 
        except Exception as e:
            # import traceback
            msg = "An error occured during tree generation: {0} - {1}\n{2}".format(
                type(e).__name__, e, "NO stack")
            self.app_log(msg)
    
    def create_tree(self) :
        button_text_color = (175/256, 130/256, 96 /256)
        button_text_color2 = (128/256, 61 /256, 59 /256)

        # Get the tree defined in the catalog.kv file
        tl = self.ids.tree_list
        tl._root.text = "Generators"
        tl._root.color = button_text_color2

        # nodes dictionnary
        df = dict()
        df["."] = tl._root;
        df["generators"] = tl._root;
        df[DATA_FOLDER] = tl._root;
        
        # Get the generators module list
        extension=".py"
        genprefix="gen_"
        toscan = [DATA_FOLDER]

        for d in toscan :
            for f in (p for p in os.listdir(d)) :
                fullpath = os.path.join(d,f)
                # If Folder
                if os.path.isdir(fullpath) and not f == "__pycache__":
                    toscan.append(fullpath)
                    # Create a TreeNode
                    if not str(fullpath) in df:
                        folder_node = TreeViewLabel(text=f.capitalize())
                        folder_node.color = button_text_color2
                        # save the node in order to not craete the same thing twice
                        df[fullpath] = folder_node
                        parent=os.path.dirname(fullpath)
                        if parent == '':
                            parent = tl._root
                        else:
                            parent = df[parent]
                        tl.add_node(folder_node, parent)
                # If generator file
                elif f.startswith(genprefix) and f.endswith(extension) :
                    parent=os.path.dirname(fullpath)
                    # Create the leaf : generator selection
                    leaf=TreeViewLabel(text=f
                        .replace("generators\\", "")
                        .replace(genprefix, "")
                        .replace(extension, "")
                        .replace("_", " ")
                        .capitalize())
                    leaf.color = button_text_color
                    leaf.on_touch_down = partial(self.select_generator, fullpath)
                    tl.add_node(leaf, df[parent])

    def select_generator(self, gen, touch) :
        # When a generator is selected,
        # load the module an get the generation instance

        # convert path to module name
        clean = gen.replace("\\", ".").replace("/", ".").replace(".py", "")
        # load the module
        new_mod = import_module(clean)
        # get the generator from the module
        if "generation" in new_mod.__dict__ :
            self.generation = new_mod.__dict__["generation"]
        else :
            self.generation = None

    def generate_text(self):
        # On generation button pressed event,
        # Do a generation using the current generator
        try :
            if self.generation is None:
                self.generated_text = "No loaded generator."
            else :
                self.generation.execute()
                print("\\------------------------------------------------------------")
                print(self.generation.text)
                self.generated_text = str(self.generation.text)
        except Exception as e:
            msg = "An error occured during generation: {0} - {1}\n{2}".format(
                type(e).__name__, e, e.__traceback__)
            self.app_log(msg)
    
    def app_log(self, message) :
        error_log(message)
        self.generated_text = message

# ================= APP DEFINITION ================

class CatalogApp(App):
    """
    The GUI interface for using any generator.

    For more information about widget organisation,
    see catalog.kv
    """

    def build(self):
        return CatalogWidget()

# ==================== APP RUN ====================

CatalogApp().run()

