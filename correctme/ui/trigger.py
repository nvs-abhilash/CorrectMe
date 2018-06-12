from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import fuzzy
import sys
sys.path.insert(0, '../')

import suggestForMe as sm


class LoginScreen(GridLayout):
        prev = []

        def __init__(self, **kwargs):
            super(LoginScreen, self).__init__(**kwargs)
            self.cols = 1
            self.username = TextInput(multiline=False)
            self.username.bind(text=self.on_text)        # specify the callback function when the text changes for the textinput
            self.username.keyboard_suggestions = True
            self.add_widget(self.username)
            self.tree, self.meta_dict = sm.initializeApp ()
            
        # callback function when the text changes
        def on_text(self,instance, value):
            # self.username.text = "fuck yes"
            lastWord = value.split(' ')[-1]
            if lastWord:
                self.prev =  sm.getSuggestion(lastWord, self.tree, self.meta_dict)
                print self.prev
            else:
                print self.prev




class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

