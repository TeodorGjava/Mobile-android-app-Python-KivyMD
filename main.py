import math

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.uix.picker import MDDatePicker
from math import *
from kivymd.uix.picker import MDDatePicker
from kivy.config import Config
from kivy.core.window import Window

# Config.set('kivy','log_dir','full path to save log report ')
Window.softinput_mode = "below_target"
rootkv = ("""
<MDTextField>
    spacing: "10dp"
    padding: "20dp"
    font_size: 28
    write_tab:False
<MDLabel>
    font_size: 28
    halign: "center"
BoxLayout:
    orientation: "vertical"
    spacing: "6dp"

    padding: "8dp"
    dobavka1:dobavka1
    kub1:kub1
    kub2:kub2
    m1:m1
    m2:m2
    m3:m3
    m4:m4
    m5:m5
    m6:m6
    m7:m7
    m8:m8
    voda1:voda1
    voda:voda
    vlojeno:vlojeno
    napravna:napravna
    h2o:h2o
    l:l
    vlajnosti:vlajnosti
    l1:l1
    l2:l2
    l3:l3
    l4:l4
    l5:l5
    l6:l6
    l7:l7
    l8:l8
    dobavka:dobavka
    wc:wc
    date:date
    den7:den7
    den2:den2
    den28:den28
    razlika:razlika
    teglo:teglo
    MDBottomNavigation:


        vlaga1:vlaga1
        vlaga2:vlaga2
        vlaga3:vlaga3
        MDBottomNavigationItem:
            name: "screen1"
            text: "Данни"
            icon: "amplifier"

            MDRaisedButton:
                size_hint : 0.225,.085
                pos_hint : {'x' : 0.01,'top': 1}
                text: "Дата: "
                on_release: app.showdate()
                font_size: "28dp"
            MDTextField:
                size_hint : 0.300,.115
                pos_hint : {'x' : 0.3,'top': 1}
                hint_text: "Бетонов възел: "
                font_size: "28dp"
            MDTextField:
                size_hint : 0.300,.115
                pos_hint : {'x' : 0.7,'top': 1}
                hint_text: "Клас: "
                font_size: "28dp"
            MDTextField:
                id:date
                size_hint : 0.225,.115
                pos_hint : {'x' : 0.01,'top': .9}
                hint_text: "Дата: "
                font_size: "30dp"
            MDTextField:
                id:den2
                size_hint : 0.225,.115
                pos_hint : {'x' : 0.25,'top': .9}
                hint_text: "2ден: "
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDTextField:
                id:den7
                size_hint : 0.225,.115
                pos_hint : {'x' : 0.50,'top': .9}
                hint_text: "7ден: "
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDTextField:
                id:den28
                size_hint : 0.225,.115
                pos_hint : {'x' : 0.75,'top': .9}
                hint_text: "28ден: "
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDTextField:
                size_hint : 0.900,.115
                pos_hint : {'x' : 0.01,'top': .8}
                hint_text: "Пепел: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.900,.115
                pos_hint : {'x' : 0.01,'top': .7}
                hint_text: "Цимент: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .6}
                hint_text: "Пясък 1: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .5}
                hint_text: "Пясък 2: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .4}
                hint_text: "Пясък 3: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .3}
                hint_text: "Камък 1: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .2}
                hint_text: "Камък 2: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint : 0.500,.115
                pos_hint : {'x' : 0.01,'top': .1}
                hint_text: "Камък 3: "
                multiline: False
                font_size: "28dp"
            MDTextField:
                size_hint: 0.300,.115
                pos_hint : {'x' : 0.6,'top': .6}
                mode: "rectangle"
                hint_text: "Добавка:"
                font_size: "28dp"
            MDTextField:
                size_hint: 0.300,.115
                pos_hint : {'x' : 0.6,'top': .490}
                mode: "rectangle"
                hint_text: "Слягане:"
                font_size: "28dp"
            MDTextField:
                size_hint: 0.300,.115
                pos_hint : {'x' : 0.6,'top': .380}
                mode: "rectangle"
                hint_text: "Клас по възд.:"
                font_size: "28dp"
            MDLabel:
                size_hint: 0.29,.1
                pos_hint : {'x' : .650,'top': .250}
                text:"Dark mode"
                font_size: "28dp"
            MDSwitch:
                id:switch
                pos_hint : {'x' : .75,'top': .150}
                on_active: app.check(*args)
                thumb_color: 73/255,72/255,73/255,1    
        MDBottomNavigationItem:

            spacing: "6dp"
            padding:"6dp"
            name: "screen2"
            text: "Сметки"
            icon: "blender"
            MDTextField:
                id:kub1
                size_hint_y: None
                size_hint : 0.225,.115
                pos_hint : {'x' : 0.01,'top': 1}
                hint_text: "15х15: "
                text: ""
                multiline: False
                input_type: "number"
                font_size:"28dp"
            MDTextField:
                id:kub2
                size_hint : 0.225,.115
                hint_text: "10х10: "
                pos_hint : {'x' : 0.265,'top': 1}
                text: ""
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDFloatingActionButton:
                icon: "equal"
                opposite_colors: True
                elevation_normal: 8               
                pos_hint : {'x' : .525,'top': .985}
                on_release: app.press2()
            MDTextField:
                id:l
                mode: "rectangle"
                size_hint : 0.20,.115
                hint_text: "Литри: "
                pos_hint : {'x' : 0.750,'top': 1}
                text: "0"
                multiline: False
                font_size:"28dp"
                input_type: "number"
            MDTextField:
                id:m1
                size_hint_y: None
                size_hint : 0.333,.115
                pos_hint : {'x' : 0.01,'top': .9}
                hint_text: "Пепел "
                text: ""
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l1
                size_hint_y: None
                size_hint : 0.27,.115
                pos_hint : {'x' : .350,'top': .925}
                text:""
                font_size: "28dp"
            MDTextField:
                id:m2
                size_hint_y: None
                size_hint : 0.333,.115
                pos_hint : {'x' : 0.01,'top': .8}
                hint_text: "Цимент  "
                text: ""
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l2
                size_hint_y: None
                size_hint : 0.27,.115
                pos_hint:{"x": .350,"top": .825}
                text:""
                font_size: "28dp"
            MDTextField:
                id:m3
                size_hint_y: None
                size_hint : 0.233,.115
                pos_hint : {'x' : 0.01,'top': .7}
                hint_text: "Пясък 1 "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDTextField:
                id:vlaga1
                size_hint_y: None
                size_hint : 0.11,.115
                pos_hint : {'x' : .235,'top': .7}
                hint_text: "Влажност % "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l3
                size_hint_y: None
                size_hint : 0.25,.115
                font_size: "28dp"
                pos_hint : {'x' : .350,'top': .725}
                text:""
                halign: "center"
            MDTextField:
                id:m4
                size_hint_y: None
                size_hint : 0.233,.115
                pos_hint : {'x' : .01,'top': .6}
                hint_text: "Пясък 2 "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDTextField:
                id:vlaga2
                size_hint_y: None
                size_hint : 0.11,.115
                pos_hint : {'x' : .235,'top': .6}
                hint_text: "Влажност % "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l4
                size_hint_y: None
                size_hint : 0.25,.115
                pos_hint : {'x' : .350,'top': .625}
                font_size: "28dp"
                halign: "center"
                text:""
            MDTextField:
                id:m5
                size_hint_y: None
                size_hint : 0.233,.115
                pos_hint : {'x' : .01,'top': .5}
                hint_text: "Пясък 3 "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDTextField:
                id:vlaga3
                size_hint_y: None
                size_hint : 0.11,.115
                pos_hint : {'x' : .235,'top': .5}
                hint_text: "Влажност % "
                text: "0"
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l5
                size_hint_y: None
                size_hint : 0.25,.115
                pos_hint : {'x' : .350,'top': .523}
                font_size: "28dp"
                halign: "center"
                text:""
            MDTextField:
                id:m6
                size_hint_y: None
                size_hint : 0.333,.115
                pos_hint : {'x' : .01,'top': .4}
                hint_text: "Камък 1 "
                text: ""
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l6
                size_hint_y: None
                size_hint : 0.25,.115
                pos_hint : {'x' : .350,'top': .415}
                text:""
                font_size: "28dp"
            MDTextField:
                id:m7
                size_hint_y: None
                size_hint : 0.333,.115
                pos_hint : {'x' : .01,'top': .3}
                hint_text: "Камък 2 "
                text: ""
                multiline: False
                font_size: "28dp"
                input_type: "number"
            MDLabel:
                id:l7
                size_hint_y: None
                size_hint : 0.25,.115
                pos_hint : {'x' : .350,'top': .315}
                text:""
                font_size: "28dp"
            MDTextField:
                id:m8
                size_hint_y: None
                size_hint : 0.333,.115
                pos_hint : {'x' : .01,'top': .2}
                hint_text: "Камък 3 "
                text: ""
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDLabel:
                id:l8
                text:"1"
                size_hint_y: None
                size_hint : 0.25,.115
                pos_hint : {'x' : .350,'top': .215}
                text:""
                font_size: "28dp"
            MDTextField:
                id:dobavka
                mode: "rectangle"
                size_hint_y: None
                size_hint : 0.3,None
                pos_hint : {'x' : .650,'top': .855}
                hint_text: "Добавка % "
                text: ""
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDLabel:
                id:dobavka1
                text:""
                size_hint: 0.2,None
                pos_hint: {"x": .750, "top": .875}
                font_size: "28dp"
            MDLabel:
                id: vlajnosti
                size_hint: 0.165,None
                pos_hint: {'x': .825,'top': .700}
                text:""
                font_size: "28dp"
            MDLabel:
                size_hint: 0.20,None
                font_size: "28dp"
                text: "Влага H2o: "
                pos_hint: {'x': .625,'top': .725}
            MDLabel:
                size_hint_y: None
                size_hint : 0.2,None
                pos_hint : {'x' : .625,'top': .600}
                text: "~Вл: "
                font_size: "28dp"
            MDLabel:
                id:vlojeno
                size_hint : 0.2,None
                pos_hint : {'x' : .825,'top': .6}
                halign: "left"
                text: ""
                font_size: "28dp" 
            MDTextField:
                id:voda
                size_hint_y: None
                size_hint : 0.15,None
                pos_hint : {'x' : .01,'top': .1}
                hint_text: "Предпол. вода "
                text: ""
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDLabel:
                id:voda1
                size_hint : 0.4,None
                pos_hint : {'x' : .25,'top': .125}
                text: ""
                font_size: "28dp"
                halign: "left"
            MDFloatingActionButton:
                icon: "cube-send"
                user_font_size: "40sp"
                pos_hint : {'x' : .875,'top': .11}
                on_release: app.press()

        MDBottomNavigationItem:
            spacing: "6dp"
            padding:"6dp"
            name: "screen3"
            text: "Резултати"
            icon: "cube-send"            
            MDTextField:
                id:napravna
                size_hint_y: None
                size_hint : 0.3,None
                pos_hint : {'x' : .1,'top': .975}
                hint_text: "Направна вода"
                text: ""
                mode: "rectangle"
                multiline: False
                input_type: "number"
                font_size: "28dp"            
            MDTextField:
                id:teglo
                size_hint_y: None
                size_hint : 0.3,None
                pos_hint : {'x' : .6,'top': .975}
                hint_text: "Тегло 5л:"
                text: ""
                mode: "rectangle"
                multiline: False
                input_type: "number"
                font_size: "28dp"
            MDLabel: 
                size_hint : 0.65,None
                pos_hint : {'x' : .01,'top': .675}  
                text: "Разлика тегло:" 
                halign: "left"
                font_size: "28dp" 
            MDLabel:
                id:razlika
                size_hint : 0.2,None
                pos_hint : {'x' : .7,'top': .675}
                text: ""
                font_size: "28dp" 

            MDLabel:
                text:"Вода+влаги"
                size_hint : 0.65,None
                pos_hint : {'x' : .01,'top': .875} 
                halign: "left"
                font_size: "28dp" 
            MDLabel:
                id:h2o
                size_hint : 0.2,None
                pos_hint : {'x' : .7,'top': .875}
                text: ""
                font_size: "28dp" 

            MDLabel:
                size_hint : 0.4,None
                pos_hint : {'x' : .01,'top': .475}               
                text: "В/Ц:"
                font_size: "28dp"
                halign: "left"
            MDLabel:
                id: wc
                size_hint : 0.3,None
                pos_hint : {'x' : .41,'top': .475}
                text: ''
                font_size: "28dp"             
            MDFloatingActionButtonSpeedDial:
                data: app.data
                root_button_anim : True
                input_type: "number"
                font_size:"26dp"
                hint_animation : False

                callback: app.callback


""")


class MobileApp(MDApp):
    Clock.max_iteration = 20

    def __init__(self, **kwargs):
        super(MobileApp, self).__init__(**kwargs)

    data = {

        "Вода": "water-check",
        "Разлика": "triangle-outline",
        "В/Ц": "debian",

        #     "Добавка": "eyedropper",

    }

    def press2(self):

        try:
            for n in self.root.kub1.text:
                self.root.ids.l.text = str(
                    math.ceil(float(self.root.ids.kub1.text) * 3.375 + float(self.root.ids.kub2.text) + 2))
        except ValueError:
            pass

    def press(self):
        try:
            for n in self.root.m1.text:
                answer1 = float(self.root.ids.m1.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.l1.text = str(round(answer1, 2))
        except ValueError:
            pass
        try:
            for n in self.root.m2.text:
                answer2 = float(self.root.ids.m2.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.l2.text = str(round(answer2, 2))
        except ValueError:
            pass
        try:
            for n in self.root.ids.m3.text:
                answer3 = float(self.root.ids.m3.text) * float(self.root.ids.l.text) \
                          / 1000 + (
                              (float(self.root.ids.m3.text) / 100 * (float(self.root.ids.vlaga1.text)))) * float(
                    self.root.ids.l.text) / 1000
                self.root.ids.l3.text = str(round(answer3, 2))
        except ValueError:
            pass
        try:
            for n in self.root.ids.m4.text:
                answer4 = float(self.root.ids.m4.text) * float(self.root.ids.l.text) \
                          / 1000 + ((
                        float(self.root.ids.m4.text) / 100 * (float(self.root.ids.vlaga2.text)))) * float(
                    self.root.ids.l.text) / 1000
                self.root.ids.l4.text = str(round(answer4, 2))
        except ValueError:
            pass
        try:
            for n in self.root.ids.m5.text:
                answer5 = float(self.root.ids.m5.text) * float(self.root.ids.l.text) \
                          / 1000 + ((
                        float(self.root.ids.m5.text) / 100 * (float(self.root.ids.vlaga3.text)))) * float(
                    self.root.ids.l.text) / 1000
                self.root.ids.l5.text = str(round(answer5, 2))
        except ValueError:
            pass
        try:
            for n in self.root.m6.text:
                answer6 = float(self.root.ids.m6.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.l6.text = str(round(answer6, 2))
        except ValueError:
            pass
        try:
            for n in self.root.m7.text:
                answer7 = float(self.root.ids.m7.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.l7.text = str(round(answer7, 2))
        except ValueError:
            pass
        try:
            for n in self.root.m8.text:
                answer8 = float(self.root.ids.m8.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.l8.text = str(round(answer8, 2))
        except ValueError:
            pass
        try:
            for n in self.root.m1.text, self.root.m2.text:
                dobavka = (((float(self.root.ids.m1.text)
                             * float(self.root.ids.l.text) / 1000))
                           + (float(self.root.ids.m2.text)) *
                           float(self.root.ids.l.text) / 1000) * (float(self.root.ids.dobavka.text) * 10)
                self.root.ids.dobavka1.text = str(round(dobavka, 2))
        except ValueError:
            pass
        except TypeError:
            pass
        try:
            for n in self.root.m1.text, self.root.m2.text, self.root.m3.text \
                    , self.root.m4.text, self.root.m5.text \
                    , self.root.m6.text, self.root.m7.text, self.root.m8.text:
                vlojeno = float(self.root.ids.m1.text) + float(self.root.ids.m2.text) + float(self.root.ids.m3.text) \
                          + float(self.root.ids.m4.text) + float(self.root.ids.m5.text) \
                          + float(self.root.ids.m6.text) + float(self.root.ids.m7.text) + float(
                    self.root.ids.m8.text)
                self.root.ids.vlojeno.text = str(round(vlojeno))

        #        except TypeError and ValueError:
        #            vlojeno = float(self.root.ids.m2.text) + float(self.root.ids.m3.text) \
        #                      + float(self.root.ids.m4.text) + float(self.root.ids.m5.text) \
        #                      + float(self.root.ids.m6.text) + float(self.root.ids.m7.text) + float(self.root.ids.m8.text)
        #            self.root.ids.vlojeno.text = str(round(vlojeno, 1))
        except TypeError and ValueError:
            pass
        try:
            for n in self.root.voda.text:
                voda = float(self.root.ids.voda.text) * float(self.root.ids.l.text) / 1000
                self.root.ids.voda1.text = str(round(voda, 2))
        except ValueError and TypeError:
            pass

        try:
            for n in self.root.m3.text:
                h2o_vlajnosti = float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text) \
                                + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text) \
                                + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text)
                self.root.vlajnosti.text = str(round(h2o_vlajnosti, 2))
        except ValueError:
            pass

    def callback(self, instance):
        if instance.icon == 'water-check':
            try:
                napravna = float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                        float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text)
                        + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text)
                        + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))
                self.root.ids.h2o.text = str(round(napravna, 2))
            except ValueError and TypeError:
                napravna = float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                        + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text)
                        + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))
                self.root.ids.h2o.text = str(round(napravna, 2))
            except ValueError and TypeError:
                napravna = float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                        + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))
                self.root.ids.h2o.text = str(round(napravna, 2))
            except ValueError and TypeError:
                napravna = float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                        float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text)
                        + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))
                self.root.ids.h2o.text = str(round(napravna, 2))
            except ValueError:
                pass

        if instance.icon == "debian":
            try:
                for number in self.root.napravna.text:
                    wc = (float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                            float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text) \
                            + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text) \
                            + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))) / (
                                 float(self.root.ids.m1.text) + float(self.root.ids.m2.text))
                    self.root.ids.wc.text = str(round(wc, 3))
            except ValueError:
                wc = (float(self.root.ids.napravna.text) / float(self.root.ids.l.text) + (
                        float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text) \
                        + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text) \
                        + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text))) / (
                         float(self.root.ids.m2.text))
                self.root.ids.wc.text = str(round(wc, 3))
            except ValueError:
                pass

        if instance.icon == "triangle-outline":
            try:
                for number in self.root.teglo.text:
                    razlika = float(self.root.ids.teglo.text) - (
                                float(self.root.ids.m1.text) + float(self.root.ids.m2.text)
                                + float(self.root.ids.m3.text)
                                + float(self.root.ids.m4.text) + float(self.root.ids.m5.text)
                                + float(self.root.ids.m6.text) + float(self.root.ids.m7.text)
                                + float(self.root.ids.m8.text) + float(self.root.ids.h2o.text)
                                + (float(self.root.ids.vlaga1.text) / 100 * float(self.root.ids.m3.text)
                                   + float(self.root.ids.vlaga2.text) / 100 * float(self.root.ids.m4.text)
                                   + float(self.root.ids.vlaga3.text) / 100 * float(self.root.ids.m5.text)))
                self.root.ids.razlika.text = str(round(razlika))
            except UnboundLocalError:
                pass
            except ValueError:
                pass
            except TypeError:
                pass

    def build(self):

        self.root = Builder.load_string(rootkv)
        self.theme_cls.primary_palette = "Teal"

    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def on_save(self, instance, value, date_range):
        self.root.ids.date.text = str(value)

    def on_cancel(self, instance, value):
        pass

    def showdate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


def Mobile():
    MobileApp().run()


if __name__ == "__main__":
    Mobile()