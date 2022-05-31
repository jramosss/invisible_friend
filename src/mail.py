from typing import List

from app import app
from flask_mail import Mail, Message


mail = Mail(app)


def send_email(recipients: List[str], text_body: str):
    msg = Message(
        subject="Your invisible friend isss...",
        sender=app.config["MAIL_USERNAME"],
        recipients=recipients
    )
    msg.body = text_body
    msg.html = "<b>{}</b>".format(text_body)
    mail.send(msg)
