import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from auto_shark.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
app_root = os.path.dirname(os.path.abspath(__file__))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from auto_shark.views.main.routes_main import main
    from auto_shark.views.users.routes_users import users
    from auto_shark.views.admins.routes_admins import admins
    from auto_shark.views.programs.routes_programs import programs
    from auto_shark.views.projects.routes_projects import projects
    from auto_shark.views.modules.routes_modules import modules
    from auto_shark.views.finals.routes_finals import finals

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(admins)
    app.register_blueprint(programs)
    app.register_blueprint(projects)
    app.register_blueprint(modules)
    app.register_blueprint(finals)

    return app
