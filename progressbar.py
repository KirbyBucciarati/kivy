from kivy.app import App 
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput

class MinhaApp (App):
    def build (self):
        return ProgressBar(value=50)
        return TextInput(text='Digite aqui')
    
if __name__ == "__main__":
 MinhaApp().run()