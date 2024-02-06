from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@market.route('/market', methods=['POST','GET'])
def market():
    item_obj = Market.query.all()
    return render_template('market/market.html', items=item_obj)
