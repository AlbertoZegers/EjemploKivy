import modulo as md

from kivy.app import App

#herramientas que usaremos en kivy
from kivy.event import EventDispatcher

class DespachadorDeEvento(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('evento_prueba')
        super().__init__(**kwargs)
        
    def accion(self, value):
        self.dispatch('evento_prueba', value)
        
    def evento_prueba(self, *args):
        print("Despachado...->", args)
  
class MiApp(App):
    def build(self):
        ev = DespachadorDeEvento()
        ev.bind(evento_prueba=md.mi_llamada)
        ev.accion('test')
        
    
MiApp().run()      
