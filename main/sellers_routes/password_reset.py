from main import *
from main.database.dbModels import Sellers

@seller.route('/password_reset', methods=['POST','GET'])
def password_reset():
    if request.method == "POST" or request.method == "PUT":
        ''' checking for empty form submision '''
        if request.method == 'POST' or request.method == 'PUT':
            for key in request.form:
                if request.form[key] == "":
                    flash(f'please provide entry for "{key}"', 'caution')
                    return redirect(url_for('seller.password_reset'))

        ''' checking if password and confirmation password are same '''
        pwd1 = request.form["pwd1"]
        pwd2 = request.form["pwd2"]

        if pwd1 != pwd2:
            flash("inconsistent password", "caution")
            return redirect(url_for('seller.password_reset'))

        ''' checking if user already exist in the database '''
        seller_object = Sellers.query.filter_by(company_email=request.form["email"]).first()

        if seller_object and seller_object.company_email == request.form["email"]:
            hash_pwd = generate_password_hash(request.form["pwd2"]).decode("utf-8")

            """ seeting new password """
            seller_object.pwd_hashed = hash_pwd
            """ setting the user attemt to zero to re-enable access """
            seller_object.login_attempt = 0
            """ storing user data to the database """
            db.session.commit()
            flash("password reset Completed", "success")
            return redirect(url_for('seller.login'))

        else:
            flash("User Does not Exist, please register to proceed")
            return redirect(url_for('seller.register'))
    else:
        return render_template('seller/password_reset.html')
