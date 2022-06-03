import pytest
from app import create_app
from resources.groups.models import Group, Person, Profile


@pytest.fixture
def persons():
    padrino = Person(name='Padrino', email='padro@primavera.com')
    berka = Person(name='Berka', email='berka@primavera.com')
    franlu = Person(name='Franlu', email='franlu@primavera.com')
    negro = Person(name='Negro', email='negro@primavera.com')
    santiju = Person(name='Santiju', email='santiju@primavera.com')
    gibran = Person(name='Gibran', email='gibran@primavera.com')
    cortez = Person(name='cortez', email='joacoco@primavera.com')
    joacoto = Person(name='pototo', email='pototo@primavera.com')
    julian = Person(name='julian', email='julian@primavera.com')

    yield [padrino, berka, franlu, negro, santiju, gibran, cortez, joacoto, julian]


@pytest.fixture
def group():
    yield Group(name="Primavera")


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': "sqlite:///testing_db.sqlite3",
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'PRESERVE_CONTEXT_ON_EXCEPTION': False
    })
    yield app


@pytest.fixture
def profiles(group, persons):
    yield [Profile(person=p, group=group) for p in persons]
