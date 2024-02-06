from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/dashboard')
@seller_login_required
def dashboard():
    '''
    - to take users to the dashboard where they will have
    - access to links for other personalized purposes
    '''
    order_obj = Orders.query.filter_by(seller_name=session['seller_name']).all()
    ''' i used .all() so it will enable me find the length of the object'''
    if not order_obj:
        flash('customers are yet to purchase your item. \
                add item to the market for customers to purchase. \
                    or advertise your product for customers to see.','info')
        return redirect(url_for('seller.market'))
    elif len(order_obj) == 1:
        order_obj = Orders.query.filter_by(seller_name=session['seller_name']).first()
        ''' i used .first() so it will enable me to return the single object'''
        return render_template('seller/single_order.html', orders=order_obj, formatNumber=fmtNumber)
    else:
        return render_template('seller/dashboard.html', orders=order_obj, formatNumber=fmtNumber)
