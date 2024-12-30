from kivy.app import App

#hay diferentes tipos de propiedades para describir el tipo de dato a manejar
#algunas de estas son:
#StringProperty, NumericProperty, BoundedNumericProperty, ObjectProperty, DictProperty, ListProperty,
#OptionProperty, AliasProperty, BooleanProperty, ReferenceListProperty

#herramientas que usaremos en kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class WidgetRaiz(BoxLayout):
    
    def __init__(self, **kwargs):
        super(WidgetRaiz, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_presionado)
        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))

    def btn_presionado(self, instance, pos):
        print('pos: imprimido de WidgetRaiz: {pos}'.format(pos=pos))

class CustomBtn(Widget):

    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch): # def on_touch_down(self, touch): es un metodo que Widget necesita
        if self.collide_point(*touch.pos): # self.collide_point(*touch.pos) es un atributo heredado del objeto Widget
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos): # def on_pressed(self, instance, pos): es un metodo que Widget necesita
        print('presionado en {pos}'.format(pos=pos))

class TestApp(App):

    def build(self):
        return WidgetRaiz()

TestApp().run()