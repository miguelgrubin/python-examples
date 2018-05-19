import threading
import time

import redis


class Listener():
    def __init__(self, patterns):
        self.redis = redis.StrictRedis()
        self.pubsub = self.redis.pubsub()
        self.pubsub.psubscribe(patterns)
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
            self.pubsub.punsubscribe(item['pattern'])

    def main(self):
        for item in self.pubsub.listen():
            if item['type'] == "psubscribe":
                self.connected(item)
            if item['type'] == "punsubscribe":
                self.disconnected(item)
            if item['type'] == "pmessage":
                self.msg_recived(item)


if __name__ == "__main__":
    while True:
        client = threading.Thread(
            target=Listener, name="redisListener", args=(['test-*-*reen'])
        )
        client.setDaemon(True)
        client.start()
        client.join()
        time.sleep(30)
