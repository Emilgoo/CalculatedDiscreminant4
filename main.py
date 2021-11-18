from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton

from kivy.lang import Builder

from kivymd.app import MDApp

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix import backdrop
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.textinput import TextInput
import kivy
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
KV = '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Gradient kivy_gradient.Gradient    
BoxLayout
    orientation: 'vertical'
    id: box
    canvas:
        Rectangle:
            size: self.size
            pos: self.pos
            texture: 
                Gradient.horizontal(
                get_color_from_hex("ed9153"), 
                get_color_from_hex("fca9f1")
                )
    MDToolbar:
        title: "Калькулятор дискрименанта"

    MDLabel:
        id : label
        text: "тут будет дискрименант"
        halign: "center"
    MDLabel:
        id : x1
        text: "x1"
        halign: "center"
    MDLabel:
        id : x2
        text: "x2"
        halign: "center"
    MDTextField:
        id : a
        hint_text: "введите а"
        helper_text: "здесь должено быть чило перед x² например 2x² вписываете число 2"
        helper_text_mode: "on_focus"
        line_color_focus: 0, 1, 1, .8
        pos_hint: {"center_z": .4}
        mode: "fill"
    MDTextField:
        id : b
        hint_text: "введите b"
        helper_text: "здесь должено быть чило перед x например 2x вписываете число 2"
        helper_text_mode: "on_focus"
        line_color_focus: 0, 1, 1, .8
        pos_hint: {"center_y": .6}
        mode: "fill"
    MDTextField:
        id : c
        hint_text: "введите c"
        helper_text: "здесь должено быть самое последнее число  например 2x² + 2x + 2 вписываете число 2"
        helper_text_mode: "on_focus"
        line_color_focus: 0, 1, 1, .8
        pos_hint: {"center_y": .6}
        mode: "fill"
    MDFillRoundFlatButton:
        id : data
        text: "Решить"
        pos_hint: {"center_x": .5, "center_y": .1}
        on_press : app.get_data()
'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CalculatedDiscreminant(MDApp):
    
    def build(self):

        screen = Screen()
        screen = Builder.load_string(KV)

        return screen
    
    def get_data(self):
        a = float(self.root.ids.a.text)
        b = float(self.root.ids.b.text)
        c = float(self.root.ids.c.text)
        d = float(b)**2 - float(4)*float(a)*float(c)
        print(d)
        self.label = self.root.ids.label
        self.label.text = str(d)
        self.x1 = self.root.ids.x1
        self.x2 = self.root.ids.x2
        if d == 0:
            x11 = float(-b)/float(2) * float(a)
            x7 = float(2) * float(a)
            self.x1.text = str(x11)
            self.x2.text = 'нет корня'
        if d < 0:
            self.x1.text = 'нет корня'
            self.x2.text = 'нет корня'
        if d > 0:
            x3 = float(-b) + d**float(0.5)
            x8 = float(d)**float(0.5)
            x4 = float(2) * float(a)
            x = float(x3)/float(x4)
            x5 = float(-b) - float(d)**float(0.5)
            x6 = float(2) * float(a)
            x9 = float(x5)/float(x6)
            self.x1.text = str(x)
            self.x2.text = str(x9)
if __name__ == "__main__":
    CalculatedDiscreminant().run()