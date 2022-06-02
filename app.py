from datetime import datetime
from os import getenv
from pprint import pprint

from flask import Flask, current_app

from resources.groups.models import Group, Person, Profile


def init_db(db):
    db.create_all()
    db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite3',
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
        'MAIL_SERVER': 'smtp.gmail.com',
        'MAIL_PORT': 587,
        'MAIL_USERNAME': getenv("MAIL_USERNAME"),
        'MAIL_PASSWORD': getenv("MAIL_PASSWORD"),
        'MAIL_USE_TLS': True,
        'MAIL_USE_SSL': False,
    })
    from resources.groups.models import db

    print("Creating database...")
    db.init_app(app)
    print("DB initialized")
    # init_db(db)
    with app.app_context():
        @app.shell_context_processor
        def shell_context():
            return {
                'db': db,
                'Group': Group,
                'Person': Person,
                'Profile': Profile,
                'pprint': pprint,
                'datetime': datetime
            }
        def register_blueprints():
            from resources.groups.views import groups
            current_app.register_blueprint(groups, template_folder="templates/")

    return app
