#!/usr/bin/python3
''' this script will create all the tables listed below '''
from main.database.dbModels import Users, GeneralJournal
from main import app, db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()