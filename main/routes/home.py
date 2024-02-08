from main import *

@home.route("/", strict_slashes=False)
@home.route("/home", strict_slashes=False)
def home_page():
    """
    this function render a home page html
    """
    return render_template("home.html")
