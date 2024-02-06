from main import *



@seller.route("/", strict_slashes=False)
@seller.route("/home", strict_slashes=False)
def home():
    """
    this function render a home page html
    """
    return render_template("/seller/dashboard.html")