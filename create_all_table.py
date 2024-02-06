#!/usr/bin/python3
''' this script will create all the tables listed below '''
from main import generate_password_hash
from datetime import datetime
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)
from main import app, db

'''
creating a default admin user
this will be used for debiting to credit user
when they fund their account
'''
admin_user = Users(
    username='admin',
    email='admin@gmail.com',
    pwd_hashed=generate_password_hash("admin"),
    first_name='admin',
    last_name='admin',
    date_of_birth=datetime.utcnow(),
    occupation='admin',
    phone_no='08036106904',
    country_of_residence='admin',
    State_of_residence='admin',
    lga_residence='admin',
    house_address='admin'
)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add(admin_user)
        db.session.commit()