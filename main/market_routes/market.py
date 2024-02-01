from flask import Blueprint
from flask import render_template, request, url_for, redirect
from main.database.dbModels import Users
from main import db
from flask import session
from main.myfunction import fmtNumber

market = Blueprint('market', __name__, url_prefix='/api')

@market.route('/market', methods=['POST','GET'])
def market_page():
    return render_template('market/market.html')
