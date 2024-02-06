from main import *
from main.database.dbModels import Sellers

@seller.route('/update', methods=['POST','GET'])
@seller_login_required
def update():
    if request.method == 'POST' or request.method == 'PUT':
        for key in request.form:
            if request.form[key] == "":
                flash(f'please provide entry for "{key}"', 'caution')
                return redirect(url_for('seller.update'))

        
        company_name = request.form['company_name']
        company_reg_no = request.form['company_reg_no']
        date_of_establishment = request.form['date_of_establishment']
        occupation = request.form['type_of_service']
        company_phone_no = request.form['company_phone_no']
        country_of_operation = request.form['country_of_operation']
        State_of_opration = request.form['State_of_opration']
        lga_operation = request.form['lga_operation']
        company_address = request.form['company_address']
        
        '''checking if current user and existing user match'''
        current_user = session['seller_name']
        seller_obj = Sellers.query.filter_by(username=current_user).first()

        if  seller_obj:
            '''updating the existin record'''
            seller_obj.company_name = company_name
            seller_obj.company_reg_no = company_reg_no
            seller_obj.date_of_establishment = date_of_establishment
            seller_obj.occupation = occupation
            seller_obj.company_phone_no = company_phone_no
            seller_obj.country_of_operation = country_of_operation
            seller_obj.State_of_opration = State_of_opration
            seller_obj.lga_operation = lga_operation
            seller_obj.company_address = company_address
            '''commit the changes to reflect in database'''
            db.session.commit()

            flash('update completed', 'success')
            return redirect(url_for('seller.home'))

        else:
            flash('the user does not exist, please confirm details', 'caution')
            return redirect(url_for('seller.update'))

    else:
        return render_template('seller/update.html')
