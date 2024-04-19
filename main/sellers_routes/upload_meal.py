from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)

@seller.route('/upload_meal', methods=['GET','POST'])
@seller_login_required
def upload_meal():
    if request.method == 'POST' or request.method == 'PUT':
        for key in request.form:
            if request.form[key] == "":
                flash(f'please provide entry for "{key}"', 'caution')
                return redirect(url_for('seller.upload_meal'))
        '''assign user id to the owneid to the item'''
        seller_obj = Sellers.query.filter_by(username=session['seller_name']).first()
        if seller_obj:
            new_item = Market(
                seller_id=seller_obj.id,
                seller_name=seller_obj.username,
                menu_category=request.form['menu_category'],
                menu_name=request.form['menu_name'],
                menu_price=request.form['menu_price'],
                menu_description=request.form['menu_description']
            )
            ''' store item in the data database '''
            db.session.add(new_item)
            db.session.commit()
            flash('upload successfull','success')
            return redirect(url_for('seller.market'))
        else:
            flash('Login or create an account to upload item','caution')
            return render_template('seller/login.html')
    else:
        return render_template('seller/upload_meal.html')
