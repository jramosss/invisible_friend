from typing import List


class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.email == __o.email


Persons = List[Person]
