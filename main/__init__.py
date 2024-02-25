""" importing modules from python """
from flask import Flask, session, flash, redirect, url_for
from flasgger import Swagger
from main.database.config import DB_URI, CKRIT
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import Blueprint, request, render_template
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from main.myfunction import fmtNumber
from datetime import datetime
app = Flask(__name__, template_folder='templates', static_folder='static')
""" configuring the app """
app.config['SECRET_KEY'] = CKRIT
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

swagger = Swagger(app)
db = SQLAlchemy(app)

''' creating blueprints  '''
home = Blueprint("home", __name__, url_prefix="/")
market = Blueprint('market', __name__, url_prefix='/market')
seller = Blueprint('seller', __name__, url_prefix='/seller')
user = Blueprint('user', __name__, url_prefix='/user')

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_name" in session:
            return func(*args, **kwargs)
        else:
            flash('Kindly loging to access the route', 'caution')
            return redirect(url_for('user.login'))

    return wrapper


def seller_login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "seller_name" in session:
            return func(*args, **kwargs)
        else:
            flash('Kindly loging to access the route', 'caution')
            return redirect(url_for('seller.login'))

    return wrapper
