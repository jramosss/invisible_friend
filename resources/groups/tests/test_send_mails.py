from resources.groups.tests.conftest import app, group, profiles, persons
from src.tuples import make_bijections
import pytest


def test_health(group):
    print(group)
