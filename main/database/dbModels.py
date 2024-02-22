''' importing items from main magic file '''
from main import db
from datetime import datetime

''' creating class for user table '''
class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pwd_hashed = db.Column(db.String(150), nullable=False)
    wallet = db.Column(db.Integer(), default=0)
    """ bio information update """
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    date_of_birth =  db.Column(db.Date)
    occupation = db.Column(db.String(20))
    phone_no = db.Column(db.String(20))
    """ address information """
    country_of_residence =  db.Column(db.String(30))
    State_of_residence =  db.Column(db.String(20))
    lga_residence =  db.Column(db.String(20))
    house_address = db.Column(db.String(150))
    reg_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    login_attempt = db.Column(db.Integer(), default=0)
    profile_pic = db.Column(db.String(100))
    orders = db.relationship('Orders', backref='user', lazy=True)


''' creating class for sellers table '''
class Sellers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    company_email = db.Column(db.String(100), unique=True, nullable=False)
    pwd_hashed = db.Column(db.String(150), nullable=False)
    wallet = db.Column(db.Integer(), default=0)
    """ company information update """
    company_name = db.Column(db.String(100))
    company_reg_no = db.Column(db.String(15))
    year_of_establishment =  db.Column(db.Date)
    occupation = db.Column(db.String(20))
    company_phone_no = db.Column(db.String(20))
    """ address of the company information """
    country_of_operation =  db.Column(db.String(30))
    State_of_opration =  db.Column(db.String(20))
    lga_operation =  db.Column(db.String(20))
    company_address = db.Column(db.String(150))
    reg_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    login_attempt = db.Column(db.Integer(), default=0)
    profile_pic = db.Column(db.String(100))
    menu = db.relationship('Market', backref='seller', lazy=True)



class GeneralJournal(db.Model):
    txn_id = db.Column(db.Integer(), primary_key=True)
    txn_date = db.Column(db.DateTime, default=datetime.utcnow)
    sender_username = db.Column(db.String(20))
    receiver_username = db.Column(db.String(20))
    description = db.Column(db.String(150))
    dr_amnt = db.Column(db.Integer(), default=0)
    cr_amnt = db.Column(db.Integer(), default=0)
    sender_wallet = db.Column(db.Integer(), default=0)
    receiver_wallet = db.Column(db.Integer(), default=0)


class Market(db.Model):
    menu_id = db.Column(db.Integer(), primary_key=True)
    seller_id = db.Column(db.ForeignKey(Sellers.id))
    seller_name = db.Column(db.String(20))
    menu_category =  db.Column(db.String(20), nullable=False)
    menu_name = db.Column(db.String(20), nullable=False)
    menu_price =  db.Column(db.Integer(), nullable=False ,default=0)
    menu_description =  db.Column(db.String(150))
    menu_picture =  db.Column(db.String(100))


class Orders(db.Model):
    order_id = db.Column(db.Integer(), primary_key=True)
    seller_id = db.Column(db.ForeignKey(Sellers.id))
    buyer_id = db.Column(db.ForeignKey(Users.id))
    seller_name = db.Column(db.String(20))
    buyer_name = db.Column(db.String(20))
    order_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    menu_name = db.Column(db.String(20), nullable=False)
    menu_price = db.Column(db.Integer(), nullable=False ,default=0)
    order_status = db.Column(db.String(15), default='pending')
    delivery_datetime = db.Column(db.DateTime)