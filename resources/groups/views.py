from flask import Blueprint, abort, redirect, render_template, request, url_for
from resources.groups.utils import send_group_mails
from src.person import Person
from src.tuples import make_bijections

from .models import Group, Profile, db

groups = Blueprint(
    'groups', __name__,
    template_folder='templates',
    url_prefix='/groups'
)


@groups.route('/create', methods=["GET", 'POST'])
def create():
    if request.method == "POST":
        name = request.form['name']
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('groups.update', group_id=group.id))
    return render_template("group_create.html")


@groups.route('/<int:group_id>', methods=["GET", 'POST'])
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


@groups.route('/')
def view():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)


@groups.route('/delete/<int:group_id>', methods=['POST'])
def delete_group(group_id: int):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for('groups.view'))


@groups.route('/remove_participant/<int:profile_id>', methods=['POST'])
def remove_participant(profile_id: int):
    profile = Profile.query.get_or_404(profile_id)
    group_id = profile.group.id
    db.session.delete(profile)
    db.session.commit()
    return redirect(url_for('groups.update', group_id=group_id))


@groups.route('/edit_participant/<int:profile_id>', methods=['POST'])
def edit_participant(profile_id: int):
    profile = Profile.query.get_or_404(profile_id)
    group_id = profile.group.id
    new_user_name = request.form.get('new_user_name', None)
    new_user_email = request.form.get('new_user_email', None)
    if new_user_name:
        profile.person.name = new_user_name
    if new_user_email:
        profile.person.email = new_user_email
    db.session.commit()
    return redirect(url_for('groups.update', group_id=group_id))

@groups.route('/send_mails/<int:group_id>', methods=['POST'])
def send_mails(group_id: int):
    group = Group.query.get_or_404(group_id)
    people = [m.person for m in group.members]
    bijection = make_bijections(people)
    send_group_mails(bijection)
    return redirect(url_for('groups.view'))
