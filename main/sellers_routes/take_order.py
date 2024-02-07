from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/take_order', methods=['GET', 'POST'])
@seller_login_required
def take_order():
    '''
    - for sellers to take order, and update the status of the order
    '''

    if request.method == 'POST':
        take_menuid = request.form['take_menuid']
        if take_menuid is not "":
            '''updating the status on database'''
            order_obj = Orders.query.filter_by(order_id=take_menuid).first()
            if order_obj:
                '''FOR ORDER THAT EXIST'''
                '''updating the status on database'''
                if order_obj.order_status == 'Pending':
                    order_obj.order_status = 'Processing'
                    db.session.commit()
                    flash(f'you have taken order for "Order_id = {take_menuid}"\
                            ', 'success')
                    return redirect(url_for('seller.dashboard'))
                else:
                    flash('Only pending orders can be Taken', 'caution')
                    return redirect(url_for('seller.dashboard'))

            else:
                '''FOR ORDER THAT DOES NOT EXIST'''
                flash(f'no order for "Order_id = {take_menuid}"', 'success')
                return redirect(url_for('seller.dashboard'))
        else:
            return redirect(url_for('seller.market'))
    else:
        return redirect(url_for('seller.market'))