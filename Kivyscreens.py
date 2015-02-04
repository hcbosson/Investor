#!/usr/bin/env python

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Label:
            text: '[anchor=(300,300)]Networth'+' is'+' unknown.'
            
        Button:
            text: 'Buy'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
            on_press: root.manager.current='buy'
        Button:
            text: 'Sell'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
            on_press: root.manager.current='sell'
        Button:
            text: 'Debt'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
            on_press: root.manager.current='debt'
        Button:
            text: 'Derivatives'
            size_hint: (.2,.5)
            pos_hint: {'x':0.6,'y':0}
            on_press: root.manager.current='der'
        Button:
            text: 'Information'
            size_hint: (.2,.5)
            pos_hint: {'x':0.8,'y':0}
            on_press: root.manager.current='info'
<BuyScreen>:
    FloatLayout:
        Button:
            text: 'Deposits'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
        Button:
            text: 'Bonds'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
        Button:
            text: 'CDOs'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
        Button:
            text: 'Stocks'
            size_hint: (.2,.5)
            pos_hint: {'x':0.6,'y':0}
        Button:
            text: 'Return'
            size_hint: (.2,.5)
            pos_hint: {'x':0.8,'y':0}
            on_press: root.manager.current='menu'
<SellScreen>:
    FloatLayout:
        Button:
            text: 'Deposits'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
        Button:
            text: 'Bonds'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
        Button:
            text: 'CDOs'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
        Button:
            text: 'Stocks'
            size_hint: (.2,.5)
            pos_hint: {'x':0.6,'y':0}
        Button:
            text: 'Return'
            size_hint: (.2,.5)
            pos_hint: {'x':0.8,'y':0}
            on_press: root.manager.current='menu'
<DebtScreen>:
    FloatLayout:
        Button:
            text: 'Borrow'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
        Button:
            text: 'Repay'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
        Button:
            text: 'Return'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
            on_press: root.manager.current='menu'
<DerScreen>:
    FloatLayout:
        ToggleButton:
            text: 'Buy'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
            group: 'buysell'
        ToggleButton:
            text: 'Sell'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
            group: 'buysell'
        Button:
            text: 'Options'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
        Button:
            text: 'Return'
            size_hint: (.2,.5)
            pos_hint: {'x':0.6,'y':0}
            on_press: root.manager.current='menu'
<InfoScreen>:
    FloatLayout:
        Button:
            text: 'My Wealth'
            size_hint: (.2,.5)
            pos_hint: {'x':0,'y':0}
        Button:
            text: 'Economy'
            size_hint: (.2,.5)
            pos_hint: {'x':0.2,'y':0}
        Button:
            text: 'Stock Market'
            size_hint: (.2,.5)
            pos_hint: {'x':0.4,'y':0}
        Button:
            text: 'Bonds'
            size_hint: (.2,.5)
            pos_hint: {'x':0.6,'y':0}
        Button:
            text: 'Return'
            size_hint: (.2,.5)
            pos_hint: {'x':0.8,'y':0}
            on_press: root.manager.current='menu'

""")



class MenuScreen(Screen):
    pass

class BuyScreen(Screen):
    pass

class SellScreen(Screen):
    pass

class DebtScreen(Screen):
    pass

class DerScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(BuyScreen(name='buy'))
sm.add_widget(SellScreen(name='sell'))
sm.add_widget(DebtScreen(name='debt'))
sm.add_widget(DerScreen(name='der'))
sm.add_widget(InfoScreen(name='info'))
class TestApp(App):

    def build(self):
        return sm

if __name__=='__main__':
    TestApp().run()