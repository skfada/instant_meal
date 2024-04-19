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
    seller_object = Sellers.query.filter_by(username=session['seller_name']).first()
    session['seller_fmt_budget'] = fmtNumber(seller_object.wallet)
    order_obj = Orders.query.filter_by(seller_name=session['seller_name']).all()
    if seller_object.company_address == None:
        '''directing user to update their information'''
        flash('Kindly Update Details to continue', 'info')
        return redirect(url_for('seller.update'))

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
