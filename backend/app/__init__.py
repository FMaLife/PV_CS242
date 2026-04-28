from flask import Flask
from flask_cors import CORS
from app.routes import register_blueprints
from app.models import db
from app import models

def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    # config
    app.config.from_object('app.config.Config')
    app.config['JSON_SORT_KEYS'] = False

    # init database
    db.init_app(app)

    # init routes
    register_blueprints(app)

    return app