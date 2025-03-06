from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializuojame SQLAlchemy objektą
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Flask konfigūracija
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workplaces.db'  # SQLite duomenų bazės adresas
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Pašaliname nereikalingus perspėjimus

    # Susiejame aplikaciją su SQLAlchemy
    db.init_app(app)

    # Registruojame routes.py blueprint'ą
    from app.routes import main
    app.register_blueprint(main)

    return app
