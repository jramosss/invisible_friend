from app import db
from flask import Flask
from flask_testing import TestCase
from resources.groups.models import Group, Person, Profile
from src.tuples import make_bijections


class TestMailSending(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testing_db.sqlite3"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app()
        db.create_all()

        padrino = Person(name='Padrino', email='padro@primavera.com')
        berka = Person(name='Berka', email='berka@primavera.com')
        franlu = Person(name='Franlu', email='franlu@primavera.com')
        negro = Person(name='Negro', email='negro@primavera.com')
        santiju = Person(name='Santiju', email='santiju@primavera.com')
        gibran = Person(name='Gibran', email='gibran@primavera.com')
        cortez = Person(name='cortez', email='joacoco@primavera.com')
        joacoto = Person(name='pototo', email='pototo@primavera.com')
        julian = Person(name='julian', email='julian@primavera.com')

        self.people = [padrino, berka, franlu, negro, santiju, gibran, cortez, joacoto, julian]

        self.primavera = Group(name="Primavera")

        self.profiles = [Profile(person=p, group=self.primavera) for p in self.people]

        db.session.add_all(self.people)
        db.session.add(self.primavera)
        db.session.add_all(self.profiles)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        with self.app.app_context() as ctx:
            db.drop_all(app=self.app)
            try:
                ctx.pop()
            except:
                pass


    def test_health(self):
        print(Group.query.all())
