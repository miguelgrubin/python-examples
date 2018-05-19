import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


class FtpHandler(FileSystemEventHandler):
    """docstring for FtpHandler"""

    def __init__(self):
        super(FtpHandler, self).__init__()

    def on_created(self, event):
        print('created')
        print(str(event))
        return True

    def on_deleted(self, event):
        print('deleted')
        print(str(event))
        return True

    def on_modified(self, event):
        print('modified')
        print(str(event))
        return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = '.'
    event_handler = LoggingEventHandler()
    event_handler = FtpHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
