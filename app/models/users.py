# Exemplo: app/models/users.py
from app.config.db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    crm = db.Column(db.String(10))
