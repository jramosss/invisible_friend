from app import db
from flask import Blueprint, abort, redirect, render_template, request, url_for

from .models import Group, Person, Profile

groups = Blueprint('groups', __name__,
                   template_folder='templates', url_prefix='/groups')


@groups.route('/')
def index():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)


@groups.route('/create', methods=["GET", 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups.update', group_id=group.id))
    return render_template("group_create.html")


@groups.route('/edit/<int:group_id>', methods=["GET", 'POST'])
def update(group_id: int):
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        new_user_name = request.form['user_name']
        new_user_email = request.form['user_email']
        if new_user_email in [profile.person.email for profile in group.members]:
            abort(400, "Email already in group")
        # TODO get or create
        new_user = Person(name=new_user_name, email=new_user_email)
        new_profile = Profile(person=new_user, group=group)
        db.session.add_all([new_user, new_profile])
        db.session.commit()
        group = Group.query.get_or_404(group_id)
    return render_template("group.html", group=group)
