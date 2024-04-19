from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Market)

@seller.route('/drop_item', methods=['GET','POST'])
@seller_login_required
def drop_item():
    if request.method == 'POST':
        '''check if item ID still exist'''
        dropid = int(request.form['dropid'])
        if dropid != "":
            '''FORM IS NOT EMPTY'''
            market_object = Market.query.filter_by(menu_id=dropid).first()
            if not market_object:
                flash(f'there is no request with the id {dropid}', 'caution')
                return redirect(url_for('seller.market'))
            else:
                db.session.delete(market_object)
                db.session.commit()

                flash(f'request has been removed from the market.', 'success')
                return redirect(url_for('seller.market'))
        else:
            '''FORM IS EMPTY'''

            flash(f'empty id "{dropid}" provided', 'caution')
            return redirect(url_for('seller.market'))
    else:

        flash(f'welcome to the seller Market', 'success')
        return redirect(url_for('seller.market'))
