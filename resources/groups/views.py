from flask import redirect, render_template, request, url_for, Blueprint, abort
from app import db
from resources.groups.utils import get_groups
from .models import Group, Person, Profile

groups = Blueprint('groups', __name__,
                   template_folder='templates', url_prefix='/groups')


@groups.route('/')
def index():
    groups = get_groups()
    print(groups)
    return render_template('index.html', groups=groups)


@groups.route('/register/', methods=['POST'])
def add_to_group():
    name = request.form['name']
    email = request.form['email']
    group_id = request.form['group_id']
    if not Group.query.filter_by(id=group_id).exists():
        abort(500)
    if not name:
        return '<p>Please enter a name</p>'
    if not email:
        return '<p>Please enter an email</p>'
    person = Person.query.filter_by(email=email).first()
    group = Group.query.filter_by(group_id=group_id).first()
    new_profile = Profile(person=person, group=group)
    db.session.add(new_profile)
    db.session.commit()
    return redirect(url_for("groups.register"))
