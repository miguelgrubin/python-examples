from kombu import Connection, Exchange, Queue, Consumer
from kombu.async import Hub
import time
import uuid
import threading

config = {
    'rabbit': {
        'user': '',
        'pass': '',
        'ip': '',
        'port': '5672'
    }
}


class rabbitConsumer():

    def __init__(self):
            self.tryReconect = 0
            self.id = "id." + str(uuid.uuid4())
            print("conecto..." + self.id)
            self.hub = Hub()
            self.exchange = Exchange(
                name="nombre-exchange", type='fanout',
                durable=False, expire=300
            )
            self.queue = Queue(
                name='prefijo-queue-' + str(uuid.uuid4()),
                exchange=self.exchange
            )
            url = [
                'amqp://',
                config['rabbit']['user'], ':',
                config['rabbit']['pass'], '@',
                config['rabbit']['ip'], ':',
                config['rabbit']['port'], '//'
            ].join('')
            self.conn = Connection(url)
            self.conn.ensure_connection(
                errback=self.reconecto(),
                max_retries=10, interval_start=5
            )
            self.conn.register_with_event_loop(self.hub)
            self.start()

    def reconecto(self):
        try:
            self.tryReconect = self.tryReconect + 1
            print("reconecto: " + str(self.tryReconect))
        except Exception as ex:
            print("error reconecto: " + str(ex))
            return

    def start(self):
        try:
            print("run: " + self.id)
            with Consumer(self.conn, [self.queue], on_message=self.on_message):
                self.hub.run_forever()

        except Connection.connection_errors as exc:
            print('Connection lost' + str(exc))
            return
        except Exception as ex:
            print("error start: " + str(ex))
            return

    def on_message(self, message):
        print('received: {0!r}'.format(message.body))
        print("id: " + self.id)
        message.ack()


if __name__ == '__main__':
    while True:
        rabbit = threading.Thread(
            target=rabbitConsumer, name="metodo-hilo", args=[]
        )
        rabbit.setDaemon(True)
        rabbit.start()
        rabbit.join()
        print("FIN DE CONEXION")
        time.sleep(5)
