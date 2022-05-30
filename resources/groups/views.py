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


@groups.route('/create', methods=["GET", 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups.index'))
    return render_template("group_create.html")


@groups.route('/edit/<int:group_id>', methods=["GET", 'POST'])
def edit(group_id: int):
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        new_user_name = request.form['user_name']
        new_user_email = request.form['user_email']
        if new_user_email in [user.email for user in group.people]:
            abort(400, "Email already in group")
        new_user = Person(name=new_user_name, email=new_user_email, group=group)
        db.session.add(new_user)
        db.session.commit()
        group = Group.query.get_or_404(group_id)
    return render_template("group.html", group=group)


@groups.route('/register', methods=["GET", "POST"])
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
