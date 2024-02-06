from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@user.route('/buy_item', methods=['GET','POST'])
@login_required
def buy_item():
    if request.method == 'POST':

        '''check if item ID still exist'''
        item_obj = Market.query.filter_by(menu_id=request.form['menu_id']).first()
        if item_obj:
            ''' ensuring seller is not buying his own item '''
            item_sellername = item_obj.seller_name
            if item_sellername == session['user_name']:
                flash('you cannot buy your own Item','caution')
                return redirect(url_for('user.market'))

            '''' debit buyer and credit seller '''
            sellert_obj = Sellers.query.filter_by(id=item_obj.seller_id).first()
            buyer_obj = Users.query.filter_by(username=session['user_name']).first()

            item_price = item_obj.menu_price
            buyer_account = buyer_obj.wallet
            seller_account = sellert_obj.wallet

            '''  checking if buyer has enough funds. '''
            if buyer_account < item_price :
                flash('Your balance is not enough to purchase item\
                        please fund your account','caution')
                return redirect(url_for('user.fund_wallet'))


            buyer_account = buyer_account - item_price
            seller_account = seller_account + item_price

            ''' updating the respective wallet to the database'''
            buyer_obj.wallet=buyer_account
            sellert_obj.wallet=seller_account
            db.session.commit()

            ''' RECORD TRANSACTION IN JOURNAL'''
            new_record = GeneralJournal(
                sender_username = buyer_obj.username,
                receiver_username = sellert_obj.username,
                description = f'Purchase of: {item_obj.menu_name} From: {sellert_obj.username}',
                dr_amnt = item_price,
                cr_amnt = item_price,
                sender_wallet = buyer_account,
                receiver_wallet = seller_account
            )
            db.session.add(new_record)
            db.session.commit()

            '''RECORDING THE ORDER INTO THE ORDER TABLE'''
            new_order = Orders(
                seller_id=sellert_obj.id,
                buyer_id=buyer_obj.id,
                seller_name=sellert_obj.username,
                buyer_name=buyer_obj.username,
                menu_name=item_obj.menu_name,
                menu_price=item_obj.menu_price,
                order_status='Pending'

            )

            db.session.add(new_order)
            db.session.commit()
            session['user_fmt_budget'] = fmtNumber(buyer_obj.wallet)
            session['seller_fmt_budget'] = fmtNumber(sellert_obj.wallet)
            flash('transaction completed','success')
            return redirect(url_for('user.dashboard'))

        else:
            flash('Item Has been purchased by another User','caution')
            return redirect(url_for('user.market'))

    else:
        return render_template('user/market.html')
