from flask import Blueprint, render_template, url_for

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/", strict_slashes=False)
@home.route("/home", strict_slashes=False)
def home_page():
    """
    this function render a home page html
    """
    return render_template("home.html")