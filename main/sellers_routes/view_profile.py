from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/view_profile')
@seller_login_required
def view_profile():
    ''' to display the users information '''
    users = Sellers.query.filter_by(username=session['seller_name'])

    return render_template('seller/view_profile.html', users=users)