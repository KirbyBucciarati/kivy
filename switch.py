from kivy.app import App 
from kivy.uix.switch import Switch

class MinhaApp(App):
    def build(self):
        return Switch(activate=False)
    
if __name__ == "__main__":
 MinhaApp().run()