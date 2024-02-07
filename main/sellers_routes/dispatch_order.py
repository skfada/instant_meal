from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/dispatch_order', methods=['GET', 'POST'])
@seller_login_required
def dispatch_order():
    '''
    - for sellers to dispatch order, and update the status of the order
    '''
    if request.method == 'POST':
        dispatch_menuid = request.form['dispatch_menuid']
        if dispatch_menuid is not "":
            '''updating the status on database'''
            order_obj = Orders.query.filter_by(order_id=dispatch_menuid).first()
            if order_obj:
                '''FOR ORDER THAT EXIST'''
                '''updating the status on database'''
                if order_obj.order_status == 'Processing':
                    order_obj.order_status = 'Dispatching'
                    db.session.commit()
                    flash(f'you are dispatching order for "Order_id = {dispatch_menuid}"', 'success')
                    return redirect(url_for('seller.dashboard'))
                else:
                    flash('only processing order can be dispatch','caution')
                    return redirect(url_for('seller.dashboard'))
            else:
                '''FOR ORDER THAT DOES NOT EXIST'''
                flash(f'no order for "Order_id = {dispatch_menuid}"', 'success')
                return redirect(url_for('seller.dashboard'))
        else:
            return redirect(url_for('seller.market'))
    else:
        return redirect(url_for('seller.market'))