from flask import Flask
from app.models import db
from app.routers.loja import loja_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
    app.config['SECRET_KEY'] = 'troque-isso-depois'

    db.init_app(app)
    app.register_blueprint(loja_bp)

    with app.app_context():
        db.create_all()

    return app
