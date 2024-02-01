#!/usr/bin/python3
""" importing from the main/__init__.py"""
from main import app

""" importing from the main/routes """
from main.routes.home import home
from main.users_routes.user_reg import user_reg
from main.users_routes.user_login import user_login
from main.users_routes.user_profile import user_update
from main.users_routes.user_profile import user_info
from main.market_routes.market import market

""" registering blueprint routes """
app.register_blueprint(home)
app.register_blueprint(user_reg)
app.register_blueprint(user_login)
app.register_blueprint(user_update)
app.register_blueprint(user_info)
app.register_blueprint(market)

host = "0.0.0.0"
port = 5000
debug = True

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=debug, host=host, port=port)