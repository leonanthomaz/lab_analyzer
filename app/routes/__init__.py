# app/routes/__init__.py
from flask import Flask
from .users import users_blueprint
from .pacients import pacients_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(pacients_blueprint)