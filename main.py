from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MortgageCalculator"
        left_action_items: [["menu", lambda x: app.callback(x)]]
        

    MDLabel:
        text: "Content"
        halign: "center"
    Widget:
        MDTextField:
            hint_text:"No helper text"
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        menu_items = [
            {
                "text": f"Ввод",
                "on_release": lambda x=f"Ввод": self.menu_callback(x),
            },
            {
                "text": f"Расчет",
                "on_release": lambda x=f"Расчет": self.menu_callback(x),
            },
            {
                "text": f"График",
                "on_release": lambda x=f"График": self.menu_callback(x),
            },
            {
                "text": f"Диаграмма",
                "on_release": lambda x=f"Диаграмма": self.menu_callback(x),
            },
            {
                "text": f"Итого",
                "on_release": lambda x=f"Итого": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(items=menu_items)
        return Builder.load_string(KV)

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()


Test().run()