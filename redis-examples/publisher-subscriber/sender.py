import redis


def main():
    r = redis.Redis()
    r.publish('test', 'envio canal')
    r.publish('test-one', 'envio #1')
    r.publish('test-one', 'envio #2')
    r.publish('test-two', 'envio #1')
    r.publish('test-two', 'envio #2')
    r.publish('test-one-screen', 'envio #1')


if __name__ == '__main__':
    main()
