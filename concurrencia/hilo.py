import threading
import time


class Hilo(threading.Thread):
    """
    El hilo dura tanto como dure el main().
    El stdout y stderr (print y errores) es es mismo que el main()
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.contador_segundos = 0

    def run(self):
        while True:
            self.contador_segundos += 1
            time.sleep(1)
            print(self.contador_segundos)


def main():
    h = Hilo()
    h.start()
    time.sleep(10)


if __name__ == '__main__':
    main()
