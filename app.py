from datetime import datetime
from os import getenv
from pprint import pprint

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)


def init_db():
    from resources.groups.models import Group, Person, Profile
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
    db.create_all()
    db.session.commit()


def register_blueprints():
    from resources.groups.views import groups
    app.register_blueprint(groups, template_folder="templates/")


@app.route('/')
def greet():
    return render_template('greet.html')


init_db()
register_blueprints()
