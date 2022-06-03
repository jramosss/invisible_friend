from resources.groups.tests.conftest import app, group, profiles, persons
from src.tuples import make_bijections
import pytest


def test_health(group, persons, profiles):
    print(group)
    print(persons)
    print(profiles)


@pytest.fixture
def client(app):
    return app.test_client()


def test_send_mails_endpoint(client, group):
    response = client.post(f'/groups/')
    # response = client.post(f'/groups/send_mails/{group.id}')
    print(response)
