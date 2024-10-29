import modulo as md

from kivy.app import App

#herramientas que usaremos en kivy
from kivy.event import EventDispatcher

#DespachadorDeEvento es un objeto encargado de gentionar como eventos las llamadas que una haga a las fuciones
class DespachadorDeEvento(EventDispatcher): 
    def __init__(self, **kwargs):
        self.register_event_type('on_test')
        super().__init__(**kwargs)
        
    def accion(self, value): #ejecuta el metodo on_test
        self.dispatch('on_test', value)
        
    def on_test(self, *args): # def on_test(self, *args): es un metodo que EventDispatcher necesita 
        print("Despachado...->", args)
  
class MiApp(App):
    def build(self):
        ev = DespachadorDeEvento()
        ev.bind(on_test=md.mi_llamada)
        ev.accion('test')
         
MiApp().run()