def mi_llamada(dt):
    print('Llamada realizada', dt)
    
def mi_llamada_limitada(dt, contador):
    contador = contador + 1
    if contador == 10:
        print('Última llamada, adiós')
        return False
    print('Llamada realizada')
    
def mi_llamada_doble(dt):
    print('Llamada realizada')
    Clock.schedule_once(mi_llamada_doble, 1)