from main import *
from main.database.dbModels import Sellers

@seller.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        ''' checking for empty form submision '''
        if request.method == 'POST' or request.method == 'PUT':
            for key in request.form:
                if request.form[key] == "":
                    flash(f'please provide entry for "{key}"', 'caution')
                    return redirect(url_for('seller.register'))

        ''' checking if password and confirmation password are same '''
        pwd1 = request.form["pwd1"]
        pwd2 = request.form["pwd2"]

        if pwd1 != pwd2:
            flash("inconsistent password", "caution")
            return render_template('seller/register.html')

        ''' checking if seller already exist in the database '''
        seller_object = Sellers.query.filter_by(company_email=request.form["email"]).first()
        if seller_object:
            flash("User already Exist", "caution")
            return render_template('seller/register.html')

        hash_pwd = generate_password_hash(request.form["pwd2"]).decode("utf-8")
        ''' storing seller data to the database '''
        seller = Sellers(username=request.form["username"],\
                        company_email=request.form["email"], pwd_hashed=hash_pwd)

        db.session.add(seller)
        db.session.commit()

        flash("Registration Completed", "success")
        ''' redirecting by using the blueflash name and the route '''
        return redirect(url_for('seller.login'))
    else:
        return render_template('seller/register.html')
