from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from config import config
import os

db = SQLAlchemy()

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

def create_app(config_name):
    app = Flask(__name__, static_folder=static_file_dir)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)
    return app