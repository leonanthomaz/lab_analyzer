# app/routes/users.py
from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users')
def users_dashboard():
    return jsonify({"message": "Bem-vindo ao painel de usuários!"})
