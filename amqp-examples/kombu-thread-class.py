import time
import json
import uuid
import threading
import socket

from kombu import Connection, Exchange, Queue, Consumer
from kombu.async import Hub
import requests


config = {
    'rabbit': {
        'user': '',
        'pass': '',
        'ip': '',
        'port': '5672'
    },
    'apitest': 'http://testmq.es/'
}


class RabbitConsumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.setName('metodo-hilo')
        self.setDaemon(True)
        self.tryReconect = 0
        self.id = "id." + str(uuid.uuid4())
        print("conecto..." + self.id)
        self.hub = Hub()
        self.exchange = Exchange(
            name="msp-control", type='fanout',
            durable=False, expire=300
        )
        self.queue = Queue(
            name='msp-control' + str(uuid.uuid4()),
            exchange=self.exchange,
            durable=False
        )
        conn_url = "".join([
            'amqp://', config['rabbit']['user'], ':', config['rabbit']['pass'],
            '@', config['rabbit']['ip'], ':', config['rabbit']['port'], '/'
        ])
        self.conn = Connection(conn_url)
        self.conn.ensure_connection(
            errback=self.reconecto(),
            max_retries=10, interval_start=5
        )
        self.conn.register_with_event_loop(self.hub)

    def reconecto(self):
        try:
            self.tryReconect = self.tryReconect + 1
            print("reconecto: " + str(self.tryReconect))
        except Exception as ex:
            print("error en reconecto: " + str(ex))
            return

    def run(self):
        try:
            print("run: " + self.id)
            with Consumer(self.conn, [self.queue], on_message=self.on_message):
                self.hub.run_forever()
        except Connection.connection_errors as exc:
            print('Connection lost' + str(exc))
            return
        except Exception as ex:
            print("error en run: " + str(ex))
            return

    def on_message(self, message):
        print('received: {0!r}'.format(message.body))
        print("id: " + self.id)
        msg = json.loads(message.body)
        msg['consumer_id'] = self.id
        msg['consumer_hostname'] = socket.gethostname()
        res = requests.post(config['apitest'] + 'api/stats', json=msg)
        msg = res.json()
        msg['http_latency'] = res.elapsed.total_seconds()
        requests.post(config['apitest'] + 'api/receive', json=msg)
        message.ack()


if __name__ == '__main__':
    while True:
        rabbit = RabbitConsumer()
        rabbit.start()
        rabbit.join()
        print("FIN DE CONEXION")
        time.sleep(5)
