# app/__init__.py
from flask import Flask, render_template
from flask_migrate import Migrate
from .config.config import Config
from .config.db import db
from .models.users import Users
from .models.pacients import Pacients
from .models.exams import Exams
from .models.exam_types import ExamTypes 
from .routes.users import users_blueprint
from .routes.pacients import pacients_blueprint

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    # Inicializar o banco de dados
    db.init_app(app)

    # Configurar Flask-Migrate
    Migrate(app, db)
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    # Registrar blueprints
    app.register_blueprint(users_blueprint)
    app.register_blueprint(pacients_blueprint)

    return app
