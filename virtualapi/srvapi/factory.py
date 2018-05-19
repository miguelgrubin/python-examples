import logging

from flask import Flask

from srvapi import views

logging.basicConfig(filename='logs/srvapi.log', level=logging.DEBUG)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(views.base_web)
    return app
