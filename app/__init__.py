from flask import Flask
from flask_login import login_manager
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .auth import auth as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    return app