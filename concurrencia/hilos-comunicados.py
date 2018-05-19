import threading
import random
import time


class Hilo(threading.Thread):
    """
    El hilo dura tanto como dure el main().
    El stdout y stderr (print y errores) es es mismo que el main()
    """

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName('Thread-' + name.upper())
        self.axis = name
        self.coord = 0

    def run(self):
        print('Started:', self.getName())
        self.coord = random.randint(-10, 10)
        while True:
            print('Sigo Vivo =>', self.getName())
            time.sleep(1)

    def get_axis(self):
        res = {}
        res[self.axis] = self.coord
        return res


all_coords = {}


def get_coords():
    for thr in threading.enumerate():
        if type(thr) is Hilo:
            all_coords.update(thr.get_axis())
    print('Coords:', all_coords)


def main():
    x = Hilo('x')
    x.start()
    y = Hilo('y')
    y.start()
    z = Hilo('z')
    z.start()
    time.sleep(2)
    get_coords()
    time.sleep(5)


if __name__ == '__main__':
    main()
