import kivy
kivy.require('2.3.0')
#Esto es opcional

from kivy.app import App 
from kivy.uix.label import Label

class MyApp(App): #MyApp es hija de App por lo que hereda las propiedades de App.  
    
    def build(self):
        return Label(text='Hola mundo')
    
if __name__ == '__main__':
    MyApp().run() #.run() es una propiedad de App 