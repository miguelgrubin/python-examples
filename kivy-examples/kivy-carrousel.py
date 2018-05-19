from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock


class CarouselApp(App):

    def next_img(self, inst):
        self.carousel.load_next()

    def build(self):
        self.carousel = Carousel(direction='right')
        for i in range(10):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            image = AsyncImage(source=src, allow_stretch=True)
            self.carousel.add_widget(image)
        self.carousel.loop = True
        Clock.schedule_interval(self.next_img, 5)
        return self.carousel


CarouselApp().run()
