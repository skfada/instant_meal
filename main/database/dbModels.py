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
    date_of_birth =  db.Column(db.DateTime())
    occupation = db.Column(db.String(20))
    phone_no = db.Column(db.String(20))
    """ address information """
    country_of_residence =  db.Column(db.String(30))
    State_of_residence =  db.Column(db.String(20))
    lga_residence =  db.Column(db.String(20))
    house_address = db.Column(db.String(150))
    reg_date = db.Column(db.DateTime(), default=datetime.utcnow)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow)
    login_attempt = db.Column(db.Integer(), default=0)
    profile_pic = db.Column(db.String(100))
    gltxn_id = db.Relationship('GeneralJournal', backref='txnid', lazy=True)


class GeneralJournal(db.Model):
    txn_id = db.Column(db.Integer(), primary_key=True)
    txn_date = db.Column(db.DateTime(), default=datetime.utcnow)
    sender_username = db.Column(db.ForeignKey(Users.username))
    receiver_username = db.Column(db.String(15))
    description = db.Column(db.String(150))    
    dr_amnt = db.Column(db.Integer(), default=0)
    cr_amnt = db.Column(db.Integer(), default=0)
    sender_wallet = db.Column(db.Integer(), default=0)
    receiver_wallet = db.Column(db.Integer(), default=0)
    
