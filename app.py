from flask import Flask, render_template
from routers.groups import groups

app = Flask(__name__)
app.register_blueprint(groups)


@app.route('/')
def greet():
    return render_template('greet.html')
