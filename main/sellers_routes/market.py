from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/market', methods=['POST','GET'])
@seller_login_required
def market():
    item_obj = Market.query.filter_by(seller_name=session['seller_name']).all()

    if not item_obj:
        flash('you are yet to upload an item. \
                add item to the market for customers to purchase.', 'info')
        return redirect(url_for('seller.upload_meal'))
    elif len(item_obj) < 2:
        item_obj = Market.query.filter_by(seller_name=session['seller_name']).first()
        return render_template('seller/single_market.html', items=item_obj, formatNumber=fmtNumber)
    else:
        '''user_obj = Sellers.query.filter_by(username=session['username']).first()'''
        '''session['seller_fmt_budget'] = fmtNumber(seller_object.wallet)'''
        return render_template('seller/market.html', items=item_obj, formatNumber=fmtNumber)
