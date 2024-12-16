# app/models/exams.py
from app.config.db import db

class Exams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('pacients.id'), nullable=False)
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_types.id'), nullable=False)
    value = db.Column(db.Float, nullable=False)

    # Relacionamentos
    patient = db.relationship('Pacients', back_populates='exams')
    exam_type = db.relationship('ExamTypes')
