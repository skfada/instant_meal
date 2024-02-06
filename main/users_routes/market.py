from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@user.route('/market', methods=['POST','GET'])
@login_required
def market():
    item_obj = Market.query.all()

    '''user_obj = Sellers.query.filter_by(username=session['username']).first()'''
    '''session['seller_fmt_budget'] = fmtNumber(seller_object.wallet)'''
    return render_template('user/market.html', items=item_obj, formatNumber=fmtNumber)
