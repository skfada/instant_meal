from main import *
from main.database.dbModels import Sellers

@seller.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        ''' checking for empty form submision '''
        if request.method == 'POST' or request.method == 'PUT':
            for key in request.form:
                if request.form[key] == "":
                    flash(f'please provide entry for "{key}"', 'caution')
                    return redirect(url_for('seller.update'))

        ''' comparing input data and existing data '''
        attempted_sellername = request.form["username"]
        attempte_password = request.form["pwd"]

        seller_object = Sellers.query.filter_by(username=attempted_sellername).first()

        if  seller_object:
            """ checking the loging attempt"""
            if seller_object.login_attempt == 3:
                flash(f"you have been blocked due to too many attempts,\
                        kindly reset your password with the form below","caution")
                return redirect(url_for('seller.password_reset'))

            verified_pwd = check_password_hash(seller_object.pwd_hashed,\
                                                attempte_password)

            if verified_pwd:
                """ reseting wrong attempt count to zero"""
                seller_object.login_attempt = 0
                db.session.commit()

                flash(f"Logged in as: {seller_object.username}","success")
                session["seller_name"] = seller_object.username
                session['seller_fmt_budget'] = fmtNumber(seller_object.wallet)

                '''checking if the seller has updated their personal details'''
                if seller_object.company_address == None:
                    return redirect(url_for('seller.update'))
                else:
                    return redirect(url_for('seller.dashboard'))
            else:
                """ counting the wrong attempt made"""
                seller_object.login_attempt += 1
                """ adding the changes to database"""
                db.session.commit()

                flash(f"Please check credentials carefully and\
                        try again","caution")
                return render_template('seller/login.html')
        else:
            flash(f"the Username <<{attempted_sellername}>> does not exist.\
                    Register if you dont have an account","caution")
            return redirect(url_for('seller.login'))

    else:
        return render_template('seller/login.html')
