from typing import List
from app import app
from flask_mail import Mail, Message
from os import getenv


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
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
