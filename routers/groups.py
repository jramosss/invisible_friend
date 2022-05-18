from flask import redirect, render_template, request, url_for, Blueprint
from flaskr.db import get_db

groups = Blueprint('groups', __name__,
                   template_folder='templates', url_prefix='/groups')


@groups.route('/')
def index():
    return "Welcome to groups view"
    db = get_db()
    groups = db.execute(
        'SELECT g.id, g.name, g.email, COUNT(*) AS members' +
        ' FROM group g JOIN user_group ug ON g.id = ug.group_id GROUP BY g.id'
    ).fetchall()
    print(groups)
    return render_template('groups/index.html', groups=groups)


@groups.route('/register/', methods=['POST', 'GET'])
def register_someone():
    if request.method == 'GET':
        return render_template("404.html")
    else:
        name = request.form['name']
        email = request.form['email']
        db = get_db()
        if not name:
            return '<p>Please enter a name</p>'
        if not email:
            return '<p>Please enter an email</p>'
        try:
            db.execute(
                "INSERT INTO person (name, email, group_id) VALUES (?, ?, ?)",
                (name, email, 1),
            )
            db.commit()
        except db.IntegrityError:
            return f"User {name} is already registered."
        else:
            return redirect(url_for("groups.register"))
