import modulo as md

from kivy.app import App



event = Clock.schedule_interval(md.mi_llamada, 1 / 30)
Clock.unschedule(event)
#event.cancel()

event = Clock.schedule_once(md.mi_llamada_limitada, 1)
Clock.unschedule(event)

event = Clock.schedule_once(md.mi_llamada_doble, 1)
Clock.unschedule(event)

trigger = Clock.create_trigger(md.mi_llamada)
#se activa con:
trigger()