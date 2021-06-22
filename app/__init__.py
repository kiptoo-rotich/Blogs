from app.config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#Create app instance
def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config_options[config_name])
  from .auth import auth as authentication_blueprint
  from .main import main as main_blueprint

  #Registering bluenprints
  app.register_blueprint(authentication_blueprint)
  app.register_blueprint(main_blueprint)

  #Initializing flask extensions
  login_manager.init_app(app)
  db.init_app(app)
  bootstrap.init_app(app)
  mail.init_app(app)

  return app
