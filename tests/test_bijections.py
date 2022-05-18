from src.person import Person
from src.tuples import make_bijections


padrino = Person('Padrino', 'padro@primavera.com')
berka = Person('Berka', 'berka@primavera.com')
franlu = Person('Franlu', 'franlu@primavera.com')
negro = Person('Negro', 'negro@primavera.com')
santiju = Person('Santiju', 'santiju@primavera.com')
gibran = Person('Gibran', 'gibran@primavera.com')
cortez = Person('cortez', 'joacoco@primavera.com')
joacoto = Person('pototo', 'pototo@primavera.com')
julian = Person('julan', 'julian@primavera.com')

persons_list = [padrino, berka, franlu, negro, santiju, gibran,
                cortez, joacoto, julian]


def update_checked_people_dict(d: dict, name: str, column: str):
    if name in d:
        d[name][column] = True
    else:
        d[name] = {"left_column": False, "right_column": False}


bijection = make_bijections(persons_list)


def test_none_left_behind():
    checked_people = {}
    for p1, p2 in bijection:
        update_checked_people_dict(checked_people, p1.name, "left_column")
        update_checked_people_dict(checked_people, p2.name, "right_column")

    assert len(checked_people.keys()) == len(persons_list)
    assert any(checked_people.values())


def test_bijections():
    equals = False
    for p1, p2 in bijection:
        if p1 == p2:
            equals = True
            break

    assert not equals
    print(bijection)
