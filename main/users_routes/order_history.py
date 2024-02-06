from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@user.route('/order_history', methods=['POST','GET'])
@login_required
def order_history():
    order_obj = Orders.query.filter_by(buyer_name=session['user_name']).all()
    
    if order_obj is None:

        return redirect(url_for('user.market'))
    else:
        return render_template('user/user_dashboard.html', orders=order_obj, formatNumber=fmtNumber)
