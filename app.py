from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


def init_db():
    from resources.groups.models import Group, Person
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
