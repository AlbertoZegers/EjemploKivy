import modulo as md

from kivy.app import App

#herramientas que usaremos en kivy
from kivy.clock import Clock

class MiApp(App):
    def build(self):
        # event = Clock.schedule_interval(md.mi_llamada, 1 / 30) #evento iterativo periodico
        # Clock.unschedule(event) #event.cancel() hace lo mismo
        
        # event = Clock.schedule_once(md.mi_llamada, 1) #evento unico
        # Clock.unschedule(event)
        
        # contador = 0
        # while True:
        #     contador = contador + 1
        #     event = Clock.schedule_once(md.mi_llamada, 1)
        #     if contador == 11:
        #         Clock.unschedule(event)
        #         break

        # event = Clock.schedule_once(md.mi_llamada_multiple, 1) #evento anidado(reverbera)
        # Clock.unschedule(event)

        # trigger = Clock.create_trigger(md.mi_llamada)
        # trigger() #activa el trigger
        
MiApp().run()