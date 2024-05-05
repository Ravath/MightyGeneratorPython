# -*- coding: utf-8 -*-

# ================= MAGICK TRICK =================
# When using an external console, we need to manually
# add the project path or it won't find any relative
# dependencies.
import sys, os, pathlib
from functools import partial
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

# ================= GUI IMPORTS ==================
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.treeview import TreeViewLabel

kivy.require('2.1.0')

# ============== GENERATION IMPORTS ==============
from wordgenerator.Print import PrintNode
from importlib import import_module
PrintNode.print_to_buffer()

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
        button_text_color = (175/256, 130/256, 96 /256)
        button_text_color2 = (128/256, 61 /256, 59 /256)

        # Get the tree defined in the catalog.kv file
        tl = self.ids.tree_list
        tl._root.text = "Generators"
        tl._root.color = button_text_color2
        # print(tl._root.__dict__)
        
        # Get the generators module list
        WDIR="generators/"
        extension=".py"
        genprefix="gen_"
        desktop = pathlib.Path(WDIR)
        files = list(p for p in desktop.rglob("*.py")
                    if p.name.startswith("gen_"))
        names = list(str(f.name)
                    .replace("generators\\", "")
                    .replace(genprefix, "")
                    .replace(extension, "")
                    .replace("_", " ")
                    .capitalize() for f in files)
        df = dict()
        df["."] = tl._root;
        df["generators"] = tl._root;

        # Node creation function
        def create_node(path : pathlib.WindowsPath) :
            """For each folder in the generators module,
               Create a TreeNode"""
            if not str(path) in df:
                folder_node=TreeViewLabel(text=path.name.capitalize())
                folder_node.color = button_text_color2
                # save the node in order to not craete the same thing twice
                df[str(path)] = folder_node
                if path.parent.name == '':
                    parent = tl._root
                else:
                    parent = df[str(path.parent)]
                tl.add_node(folder_node, parent)

        # Create the tree
        for n, f in zip(names, files):
            # Create the folder structure
            if f.parents is not None:
                for p in f.parents.__reversed__():
                    create_node(p)

            # Create the leaf : generator selection
            leaf=TreeViewLabel(text=n)
            leaf.color = button_text_color
            leaf.on_touch_down = partial(self.select_generator, f)
            tl.add_node(leaf, df[str(f.parent)])


    def select_generator(self, gen, touch) :
        # When a generator is selected,
        # load the module an get the generation instance
        new_mod = import_module(str(gen)
                      .replace("\\", ".")
                      .replace(".py", ""))
        if "generation" in new_mod.__dict__ :
            self.generation = new_mod.__dict__["generation"]
        else :
            self.generation = None

    def generate_text(self):
        # On generation button pressed event,
        # Do a generation using the current generator
        if self.generation is None:
            self.generated_text = "No loaded generator."
        else :
            self.generation.execute()
            print("\\------------------------------------------------------------")
            print(self.generation.text)
            self.generated_text = str(self.generation.text)

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

