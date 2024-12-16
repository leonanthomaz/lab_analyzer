# app/models/pacients.py
from app.config.db import db

class Pacients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Relacionamento
    exams = db.relationship('Exams', back_populates='patient')
