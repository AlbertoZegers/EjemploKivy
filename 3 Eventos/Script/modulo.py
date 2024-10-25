from kivy.clock import Clock

def mi_llamada(dt):
    print('Llamada realizada', dt)
    
def mi_llamada_limitada(dt, contador=0):
    contador = contador + 1
    print(f'Llamada {contador} realizada')
    if contador == 10:
        print('Última llamada, adiós')
        return False
    
def mi_llamada_doble(dt):
    print('Llamada doble realizada')
    Clock.schedule_once(mi_llamada_doble, 1)