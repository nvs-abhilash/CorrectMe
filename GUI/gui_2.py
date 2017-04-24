from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

from kivy.lang import Builder
Builder.load_file("SimpleKivy.kv")


class TextScreen(GridLayout):
    def __init__(self, **kwargs):
        super(TextScreen, self).__init__(**kwargs)
        self.rows = 3
        self.cols = 2
        self.sentence = ""


        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        # self.add_widget(Label(text="Suggestions!!"))
        # self.add_widget(FloatLayout())
        self.health_label = Label(text="CorrectMe is here!!!")
        self.add_widget(self.health_label)
        # self.add_widget(Button(text="Auth User and Password", on_press=self.auth))
        self.but_1 = Button(id="but_1", text="but_1")
        self.but_1.bind(on_press=lambda a: self.auth(self.but_1.text))
        self.add_widget(self.but_1)

        self.but_2 = Button(id="but_2", text="but_2")
        self.but_2.bind(on_press=lambda a: self.auth(self.but_2.text))
        self.add_widget(self.but_2)

        self.but_3 = Button(id="but_3", text="but_3")
        self.but_3.bind(on_press=lambda a: self.auth(self.but_3.text))
        self.add_widget(self.but_3)

        self.but_4 = Button(id="but_4", text="but_4")
        self.but_4.bind(on_press=lambda a: self.auth(self.but_4.text))
        self.add_widget(self.but_4)



    def auth(self, bText):
        print "auth called---"
        print self.username.text
        words = self.username.text.split(" ")
        words = words[0:-1]
        str1 = ''.join(words)
        self.username.text = str1 + " " + bText



class SimpleKivy(App):
    def build(self):
        return TextScreen()

if __name__ == "__main__":
    SimpleKivy().run()
