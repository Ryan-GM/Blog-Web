from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object()

    return app