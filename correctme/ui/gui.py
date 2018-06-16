from os.path import join, dirname

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file(join(dirname(__file__), r'SimpleKivy.kv'))

from correctme import suggestForMe as sm


class TextScreen(GridLayout):
    prev1 = []
    prev2 = []
    prev3 = []

    def __init__(self, dataset, **kwargs):
        super(TextScreen, self).__init__(**kwargs)
        self.rows = 6
        self.cols = 1
        self.sentence = ""

        self.health_label = Label(text="CorrectMe is here!!!")
        self.add_widget(self.health_label)
        self.username = TextInput(multiline=False)
        self.username.bind(text=self.on_text)  # specify the callback function when the text changes for the textinput
        self.username.keyboard_suggestions = True
        self.add_widget(self.username)
        self.tree, self.meta_dict = sm.initializeApp(dataset)

        self.intersection = GridLayout(cols=2)
        self.union = GridLayout(cols=1)
        self.user_dic = GridLayout(cols=1)

        self.but_1 = Button(id="but_1", text="")
        self.but_1.bind(on_press=lambda a: self.auth(self.but_1.text))
        self.add_widget(self.but_1)

        self.but_2 = Button(id="but_2", text="")
        self.but_2.bind(on_press=lambda a: self.auth(self.but_2.text))
        self.add_widget(self.but_2)

        self.but_3 = Button(id="but_3", text="")
        self.but_3.bind(on_press=lambda a: self.auth(self.but_3.text))
        self.add_widget(self.but_3)

        self.but_4 = Button(id="but_4", text="")
        self.but_4.bind(on_press=lambda a: self.auth(self.but_4.text))

        self.add_widget(self.but_4)

    def auth(self, bText):
        print "auth called---"
        print self.username.text
        words = self.username.text.split(" ")
        words = words[0:-1]
        str1 = ''.join(words)
        self.username.text = str1 + " " + bText

    def on_text(self, instance, value):
        lastWord = value.split(' ')[-1]
        if lastWord:
            self.prev1, self.prev2, self.prev3 = sm.getSuggestion(lastWord, self.tree, self.meta_dict)

            if len(self.prev3) >= 4:
                self.but_1.text = self.prev3[0]
                self.but_2.text = self.prev3[1]
                self.but_3.text = self.prev3[2]
                self.but_4.text = self.prev3[3]
            if len(self.prev1) == 0:
                self.but_1.text = self.prev2[0]
                self.but_2.text = self.prev2[1]
                self.but_3.text = self.prev2[2]
                self.but_4.text = self.prev2[3]

            if len(self.prev2) == 0:
                self.but_1.text = self.prev1[0]
                self.but_2.text = self.prev1[1]
                self.but_3.text = self.prev1[2]
                self.but_4.text = self.prev1[3]

            else:
                if len(self.prev3) == 3:
                    self.but_1.text = self.prev3[0]
                    self.but_2.text = self.prev3[1]
                    self.but_3.text = self.prev3[2]
                    self.but_4.text = self.prev2[0]

                if len(self.prev3) == 2:
                    self.but_1.text = self.prev3[0]
                    self.but_2.text = self.prev3[1]
                    self.but_3.text = self.prev1[0]
                    self.but_4.text = self.prev2[0]

                if len(self.prev3) == 1:
                    self.but_1.text = self.prev3[0]
                    self.but_2.text = self.prev1[0]
                    self.but_3.text = self.prev2[0]

                    if len(self.prev2) >= 2:
                        self.but_4.text = self.prev2[1]
                    elif len(self.prev1) >= 2:
                        self.but_4.text = self.prev2[1]

                else:
                    self.but_1.text = self.prev2[0]
                    self.but_2.text = self.prev2[1]
                    self.but_3.text = self.prev2[2]
                    self.but_4.text = self.prev1[0]

            print "BK tree suggestions\n"
            print self.prev1
            print "\n"

            print "Double Metaphone suggestions\n"
            print self.prev2
            print "\n"

            print "Intersection of both\n"
            print self.prev3
            print "---------------------------------------------------------------------------------------------------------------------------------------\n"

        else:
            print "BK tree suggestions\n"
            print self.prev1
            print "\n"

            print "Double Metaphone suggestions\n"
            print self.prev2
            print "\n"

            print "Intersection of both\n"
            print self.prev3
            print "---------------------------------------------------------------------------------------------------------------------------------------\n"


class SimpleKivy(App):
    def __init__(self, dataset):
        super(SimpleKivy, self).__init__()
        self.__dataset = dataset

    def build(self):
        return TextScreen(self.__dataset)
