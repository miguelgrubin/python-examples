import threading
import time

import redis


class Listener():
    def __init__(self, channels):
        self.redis = redis.StrictRedis()
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)
        self.main()

    def connected(self, item):
        print('Equipo conectado canal: ', item['channel'].decode('utf-8'))

    def disconnected(self, item):
        print('Equipo desconectado canal: ', item['channel'].decode('utf-8'))

    def msg_recived(self, item):
        print('------------------------------------------------')
        print('type: ', item['type'])
        print('channel: ', item['channel'].decode('utf-8'))
        print('pattern: ', item['pattern'])
        print('data: ', item['data'].decode('utf-8'))
        print('------------------------------------------------')
        if item['data'].decode('utf-8') == "kill":
            self.pubsub.unsubscribe()

    def main(self):
        for item in self.pubsub.listen():
            if item['type'] == "subscribe":
                self.connected(item)
            if item['type'] == "unsubscribe":
                self.disconnected(item)
            if item['type'] == "message":
                self.msg_recived(item)


if __name__ == "__main__":
    while True:
        client = threading.Thread(
            target=Listener, name="redisListener", args=(['test'])
        )
        client.setDaemon(True)
        client.start()
        client.join()
        time.sleep(30)
