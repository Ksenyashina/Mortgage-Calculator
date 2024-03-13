from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.icon_definitions import md_icons
from kivymd.font_definitions import fonts

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons

MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MortgageCalculator"
    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
        height: "48dp"
        tab_indicator_anim: False
        Tab:
            id: tab1
            name: 'tab1'
            icon: "calculator-variant"
            title: "Ввод"
            
            BoxLayout:
                orientation: 'vertical'
                padding: "10dp"
    
                BoxLayout:
                    orientation: 'horizontal'
                    icon:"calendar-month"
                    title:"Start date"
    
                    MDIconButton:
                        icon: "calendar-month"
    
                    MDTextField:
                        hint_text:"Start date"
    
                BoxLayout:
                    orientation: 'horizontal'
    
                    MDIconButton:
                        icon: "cash"
    
                    MDTextField:
                        hint_text: "Loan"
                
                BoxLayout:
                    orientation: 'horizontal'
    
                    MDIconButton:
                        icon: "clock-time-five-outline"
    
                    MDTextField:
                        hint_text: "Months"
    
    
                BoxLayout:
                    orientation: 'horizontal'
    
                    MDIconButton:
                        icon: "bank"
    
                    MDTextField:
                        hint_text: "Interest, %"
    
                    MDTextField:
                        hint_text: "Payment type"
        Tab:
            id: tab2
            name: 'tab2'
            icon: "table-large"
            title: "Расчет"
        Tab:
            id: tab3
            name: 'tab3'
            icon: "chart-areaspline"
            title: "График"
        Tab:
            id: tab4
            name: 'tab4'
            icon: "chart-pie"
            title: "Диаграмма"
        Tab:
            id: tab5
            name: 'tab5'
            icon: "book-open-variant"
            title: "Итого"
            
'''

class Tab(MDFloatLayout, MDTabsBase):
    pass
class MortgageCalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        print("Tab clicked!"+tab_text)


MortgageCalculatorApp().run()