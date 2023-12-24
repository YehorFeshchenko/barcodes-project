"""
Flask Quick-Start Template
Application bootstrap
"""

import json
import os.path

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS

from server.controllers.componentController import components_blueprint

load_dotenv()


def create_app():
    """
    Create application
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    CORS(app)

    app.register_blueprint(components_blueprint)

    # register index route
    @app.route("/")
    def index():
        """Sample app index"""
        return 'Components index'

    return app
