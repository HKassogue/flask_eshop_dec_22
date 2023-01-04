import os

DEBUG = True

# ceci uniquement en mode développement
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/flask_eshop_dec_22'
SQLALCHEMY_TRACK_MODIFICATIONS = False
