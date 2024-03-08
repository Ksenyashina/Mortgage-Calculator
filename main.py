from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.icon_definitions import md_icons

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MortgageCalculator"
    MDTabs:
        id: tabs

    MDLabel:
        text: "Content"
        halign: "center"
    Widget:
        MDTextField:
            hint_text:"No helper text"

'''

class Tab(MDFloatLayout, MDTabsBase):
    pass
class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    def on_start(self):
        icons_item = {
                "Ввод": "Ввод",
                "Расчет": "Расчет",
                "График": "График",
                "Диаграмма": "Диаграмма",
                "Итого": "Итого"
            }
        # for name_tab in list(md_icons.keys())[15:30]:
        #     self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))
        for icon_name, name_tab in icons_item.items():
            self.root.ids.tabs.add_widget(Tab(title=name_tab))


Test().run()