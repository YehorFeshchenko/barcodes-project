import os.path
from flask import current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


def init_app(app):
    """
    App db initialization
    """
    global db
    global ma
    db = SQLAlchemy(app)
    ma = Marshmallow(app)
