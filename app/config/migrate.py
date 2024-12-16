# migrate.py
from app import create_app
from .db import db
from flask_migrate import Migrate, upgrade

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
