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

app = Flask(__name__, template_folder='templates', static_folder='static')
""" configuring the app """
app.config['SECRET_KEY'] = CKRIT
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

swagger = Swagger(app)
db = SQLAlchemy(app)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_name" in session:
            return func(*args, **kwargs)
        else:
            flash('Kindly loging to access the route', 'caution')
            return redirect(url_for('user_login.login'))
    return wrapper
