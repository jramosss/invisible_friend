from typing import List, Tuple
from resources.groups.models import Person
from src.mail import send_email


def get_mail_body(recipient: Person, friend: Person):
    return f"""
    <h1>Hi {recipient.name}</h1>
    <p>Your invisible friend is {friend.name}.</p>
    """


def send_group_mails(bijections: List[Tuple[Person, Person]]):
    for recipient, friend in bijections:
        print(f"Sending mail to {recipient.name} {friend.name}")
        body = get_mail_body(recipient, friend)
        send_email([recipient.email], body)
