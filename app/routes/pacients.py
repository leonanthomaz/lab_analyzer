# app/routes/pacients.py
from flask import Blueprint

pacients_blueprint = Blueprint('pacients', __name__)

@pacients_blueprint.route('/pacients')
def pacients_dashboard():
    return 'Bem-vindo ao painel pacients'