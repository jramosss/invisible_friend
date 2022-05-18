from random import shuffle
from src.person import Persons

def is_repeated(l1: Persons, l2: Persons):
    for p1, p2 in list(zip(l1,l2)):
        if p1 == p2:
            return True
    return False

def make_bijections(s1: Persons):
    s2 = s1.copy()
    shuffle(s2)
    while is_repeated(s1, s2):
        shuffle(s2)

    return zip(s1, s2)
