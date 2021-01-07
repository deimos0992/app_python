from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.title = "Hello Kivy"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.prymary_palette = "Red"


MainApp().run()