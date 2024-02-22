from urllib.parse import quote_plus
from os import urandom
''' creating URI demo credential for the database connection '''
user = 'instant_meal'
pwd = quote_plus('instantmeal@2024')
host = 'localhost'
database = 'instant_meal'

CKRIT = urandom(20)
DB_URI_MYSQL = f'mysql+mysqldb://{user}:{pwd}@{host}/{database}'
DB_URI = f'sqlite:///instantmeal.db'
