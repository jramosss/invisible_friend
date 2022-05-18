from app import app
from flask import redirect, request, url_for
from flaskr.db import get_db
from flaskr.groups import bp


@app.route('/')
def greet():
    return '<p>Hello World!</p>'


@bp.route('/register', methods=['POST', 'GET'])
def register_someone():
    if request.method == 'GET':
        print("Hi")
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
