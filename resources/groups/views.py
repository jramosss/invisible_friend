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
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        group_id = request.form['group_id']
        if not Group.query.filter_by(group_id).exists():
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
