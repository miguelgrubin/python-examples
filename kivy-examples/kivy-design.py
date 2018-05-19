
from kivy.app import App, Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation


class MyFirstWidget(BoxLayout):

    txt_inpt = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))

    def btn_click(self, instance, pos):
        print(pos)
        print(instance)
        Animation(valign='top', d=.3, t='out_quart').start(
            self.ids.txt_label
        )


class TestApp(App):

    def build(self):
        return MyFirstWidget()

    def on_pause(self):
        return True


TestApp().run()
