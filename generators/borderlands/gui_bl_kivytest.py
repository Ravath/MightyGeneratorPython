# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label as LabKivy
from kivy.uix.button import Button
from itemskivy import text_to_return

#exec(open("itemskivy.py").read())



def callback(instance):
    print(text_to_return)

generate_button= Button(text='GENERATE')
generate_button.bind(on_press=callback)

class GuiTest(App):
    
    # def build(self):
    #     return generate_button
    pass
    
GuiTest().run()
