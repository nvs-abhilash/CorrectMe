from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from correctme import suggestForMe as sm


class CorrectMeView(GridLayout):
    input_text = ObjectProperty(None)
    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)
    button4 = ObjectProperty(None)

    def __init__(self, dataset, **kwargs):
        super().__init__(**kwargs)
        self.tree, self.meta_dict = sm.initialize_app(dataset)
        self.buttons = [self.button1, self.button2, self.button3, self.button4]

    def on_release(self, text):
        words = self.input_text.text.strip().split()
        if len(words) > 0:
            words[-1] = text
        else:
            words.append(text)
        
        self.input_text.text = ' '.join(words).strip()
        self.input_text.focus = True

    def on_text(self, text):
        words = text.strip().split(' ')
        last_word = words[-1]
    
        bktree_words, metaphone_words, intersect_words = sm.get_suggestion(last_word, self.tree, self.meta_dict)

        # Need to form a list of four top words.
        # TODO: Need to change this algo in future for n-grams.
        i = 0
        for word in intersect_words:
            if i >= 4:
                break
            self.buttons[i].text = word 
            i += 1
        
        for word in bktree_words:
            if i >= 4:
                break
            self.buttons[i].text = word
            i += 1

        for word in metaphone_words:
            if i >= 4:
                break
            self.buttons[i].text = word
        
        print("BK tree suggestions")
        print(bktree_words)
        print('\n')

        print("Double Metaphone suggestions")
        print(metaphone_words)
        print('\n')

        print("Intersection of both")
        print(intersect_words)
        print('\n')

        print('-' * 50)


class CorrectMeApp(App):
    def __init__(self, dataset, **kwargs):
        super().__init__(**kwargs)
        self._dataset = dataset
    
    def build(self):
        return CorrectMeView(self._dataset)