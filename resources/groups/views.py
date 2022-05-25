from flask import redirect, render_template, request, url_for, Blueprint, abort
from app import db
from .models import Group, Person

groups = Blueprint('groups', __name__,
                   template_folder='templates', url_prefix='/groups')


@groups.route('/')
def index():
    groups = Group.query.all()
    users = Person.query.all()
    return render_template('index.html', groups=groups, users=users)


@groups.route('/create', methods=["GET", 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups.index'))
    return render_template("group_create.html")


@groups.route('/register', methods=["GET", "POST"])
def add_to_group():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        group_id = request.form['group_id']
        if not Group.query.filter_by(id=group_id).exists():
            abort(500)
        if not name:
            return '<p>Please enter a name</p>'
        if not email:
            return '<p>Please enter an email</p>'
        new_person = Person(name=name, email=email, group_id=group_id)
        db.session.add(new_person)
        db.session.commit()
    else:
        return render_template("group_register.html")
