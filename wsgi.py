import os

from __init__ import create_app

from flask import Flask

app = create_app(self)

# Load default config and override config from an environment variable

app.config.update(dict(

    DATABASE=os.path.join(app.root_path, 'flaskr.sqlite'),

    DEBUG=True,

    SECRET_KEY='development key',

    USERNAME='admin',

    PASSWORD='default'

))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)