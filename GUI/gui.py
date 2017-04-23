from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
Builder.load_file("SimpleKivy.kv")


class TextScreen(GridLayout):
    def __init__(self, **kwargs):
        super(TextScreen, self).__init__(**kwargs)
        self.rows = 2

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        # self.add_widget(Label(text="Suggestions!!"))
        self.add_widget(FloatLayout())
    
	

class SimpleKivy(App):
    def build(self):
        return TextScreen()
		

if __name__ == "__main__":
    SimpleKivy().run()