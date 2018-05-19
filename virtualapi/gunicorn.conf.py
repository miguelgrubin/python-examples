host = '127.0.0.1'
port = '8000'

loglevel = 'info'
accesslog = 'logs/gunicorn-access.log'
errorlog = 'logs/gunicorn.err'

reload = True
workers = 2
