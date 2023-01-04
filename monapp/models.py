from flask_sqlalchemy import SQLAlchemy
from .views import app
import logging as lg

# Config options − Make sure you created a ’ config .py’ file .
app.config.from_object('config')

# création d’un objet de connexion à la base de données
db = SQLAlchemy(app)

# création du modèle
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=db.func.now())

# db.create_all()


def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database init...')