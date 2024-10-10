from kivy.app import App # para inicializar Kivy con .run()

#herramientas que usaremos en kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class PantallaLogin(GridLayout):
    def __init__(self, **kwargs):
        super(PantallaLogin, self).__init__(**kwargs) #super().__init__(**kwargs) -> es lo mismo ya que python es capaz de interpretar
        #Lo anterior es nesesario en herencia de multiples padres (Esta es una propiedad de python heredada de c++)
        
        self.cols =2
        
        self.add_widget(Label(text='Usuario'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        self.add_widget(Label(text='contraseña'))
        self.passkey = TextInput(password=True, multiline=False)
        self.add_widget(self.passkey)
        
class MiApp(App):
    def build(self):
        return PantallaLogin()
    
MiApp().run()