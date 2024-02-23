#!/usr/bin/python3
""" importing from the main/__init__.py"""
from main import app

from main.routes.home import home
from main.market_routes import market
from main.sellers_routes import seller
from main.users_routes import user

""" registering blueprint routes """
app.register_blueprint(home)
app.register_blueprint(market)
app.register_blueprint(seller)
app.register_blueprint(user)

host = "0.0.0.0"
port = 8000
debug = True

if __name__ == "__main__":
    with app.app_context():
        app.run(host=host)