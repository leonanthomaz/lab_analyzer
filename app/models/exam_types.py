# app/models/exam_types.py
from app.config.db import db

class ExamTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    reference_min = db.Column(db.Float, nullable=False)
    reference_max = db.Column(db.Float, nullable=False)
