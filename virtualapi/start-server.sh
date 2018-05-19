#!/bin/bash

./venv/bin/gunicorn -c gunicorn.conf.py srvapi:app
