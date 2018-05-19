import redis


def main():
    r = redis.Redis()
    r.publish('test', 'kill')
    r.publish('test-one', 'kill')
    r.publish('test-two', 'kill')


if __name__ == '__main__':
    main()
