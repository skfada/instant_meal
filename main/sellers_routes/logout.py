from main import *
from main.database.dbModels import Sellers

@seller.route('/logout')
@seller_login_required
def logout():
    session.pop('seller_name')
    flash("Logged out Successfull!!!", "success")
    return render_template('seller/home.html')