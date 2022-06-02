from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Person {self.name}, {self.email}"


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __repr__(self):
        return f"Group('{self.name}')"


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship("Person", backref="profiles")
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("Group", backref="members")

    __table_args__ = (db.UniqueConstraint('person_id', 'group_id'), )

    def __repr__(self):
        return f"Profile {self.person.name} - {self.group.name}"
