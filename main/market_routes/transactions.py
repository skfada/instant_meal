from market_routes import *

@market.route('/txn')
@login_required
def txn():
    ''' function that records transactions '''
    return render_template('market/txn.html')
