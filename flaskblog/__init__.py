from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#protect cross browser attacks
#  import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = '667c3b63ea9f67b79ce202777d22a1f7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes