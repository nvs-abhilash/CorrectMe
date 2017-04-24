from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# callback function when the text changes
def on_text(instance, value):
    print('The widget', instance, 'have:', value)

class LoginScreen(GridLayout):

        def __init__(self, **kwargs):
            super(LoginScreen, self).__init__(**kwargs)
            self.cols = 1
            self.username = TextInput(multiline=False)
            self.username.bind(text=on_text)        # specify the callback function when the text changes for the textinput
            self.add_widget(self.username)
            
        
class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

