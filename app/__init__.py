from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail


bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)
mail = Mail()
# Initializing application
def create_app(config_name):
    app = Flask(__name__ )


    #Initializing extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap = Bootstrap(app)
    mail.init_app(app)


    #setting up configuration
    app.config.from_object(config_options[config_name])
    configure_uploads(app, photos)



    #registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')


    #will return the app
    return app
