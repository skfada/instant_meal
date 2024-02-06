from main import *
from main.database.dbModels import Market


@market.route('/txn')
def txn():
    ''' function that records transactions '''
    return render_template('market/txn.html')
