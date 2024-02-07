from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/reject_item', methods=['GET','POST'])
@seller_login_required
def reject_item():
    if request.method == 'POST':
        '''check if item ID still exist'''
        rejectid = request.form['rejectid']
        if reject_item is not "":
            '''FORM IS NOT EMPTY'''
            order_object = Orders.query.filter_by(order_id=rejectid).first()
            if order_object.order_id == None:
                flash(f'there is no request with the id {rejectid}', 'caution')
                return redirect(url_for('seller.dashboard'))
            elif order_object.order_status == 'Pending':
                order_object.order_status = 'Declined'

                '''reversing the funds transafer'''
                seller = session['seller_name']
                buyer = order_object.buyer_name

                seller_obj = Sellers.query.filter_by(username=seller).first()
                buyer_obj = Users.query.filter_by(username=buyer).first()
                '''debit seller'''
                seller_obj.wallet = seller_obj.wallet - order_object.menu_price
                '''credit buyer'''
                buyer_obj.wallet = buyer_obj.wallet + order_object.menu_price

                db.session.commit()

                gl_obj = GeneralJournal.query.filter_by(txn_id=order_object.order_id).first()
                '''record reverserval in journal'''
                debit_record = GeneralJournal(
                    sender_username = seller_obj.username,
                    receiver_username = buyer_obj.username,
                    description = 'Refund: '+gl_obj.description,
                    dr_amnt = order_object.menu_price,
                    cr_amnt = order_object.menu_price,
                    sender_wallet = seller_obj.wallet,
                    receiver_wallet = buyer_obj.wallet
                )

                db.session.add(debit_record)
                db.session.commit()

                session['user_fmt_budget'] = fmtNumber(buyer_obj.wallet)
                session['seller_fmt_budget'] = fmtNumber(seller_obj.wallet)

                flash(f'request has be decline.', 'success')
                return redirect(url_for('seller.dashboard'))

            else:
                flash(f'request cannot be decline. It is beyond pending stage', 'caution')
                return redirect(url_for('seller.dashboard'))
        else:
            '''FORM IS EMPTY'''

            flash(f'empty id "{rejectid}" provided', 'caution')
            return redirect(url_for('seller.dashboard'))
    else:

        flash(f'welcome to the seller dashboard', 'success')
        return redirect(url_for('seller.dashboard'))
