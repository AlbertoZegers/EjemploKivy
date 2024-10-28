from kivy.clock import Clock

def mi_llamada(dt):
    print('Llamada realizada', dt)
    
def mi_llamada_multiple(dt):
    print('Llamada doble realizada')
    Clock.schedule_once(mi_llamada_multiple, 1)