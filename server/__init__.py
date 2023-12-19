"""
Flask Quick-Start Template
Application bootstrap
"""

import json
import os.path

from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()


def create_app():
    """
    Create application
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['FLASK_DEBUG'] = True

    # pylint: disable=import-outside-toplevel,wrong-import-position,unused-import

    # setup database
    from . import db

    db.init_app(app)

    # register blueprints
    from . import contacts

    app.register_blueprint(contacts.blueprint)

    # register index route
    @app.route("/")
    def index():
        """Sample app index"""
        return 'Components index'

    return app
