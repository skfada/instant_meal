from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)


@user.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        ''' checking for empty form submision '''
        if request.method == 'POST' or request.method == 'PUT':
            for key in request.form:
                if request.form[key] == "":
                    flash(f'please provide entry for "{key}"', 'caution')
                    return redirect(url_for('user.register'))

        ''' checking if password and confirmation password are same '''
        pwd1 = request.form["pwd1"]
        pwd2 = request.form["pwd2"]

        if pwd1 != pwd2:
            flash("inconsistent password", "caution")
            return render_template('user/register.html')

        ''' checking if user already exist in the database '''
        user_object = Users.query.filter_by(email=request.form["email"]).first()
        if user_object:
            flash("User already Exist", "caution")
            return render_template('user/register.html')

        hash_pwd = generate_password_hash(request.form["pwd2"]).decode("utf-8")
        ''' storing user data to the database '''
        user = Users(username=request.form["username"],\
                        email=request.form["email"], pwd_hashed=hash_pwd)

        db.session.add(user)
        db.session.commit()

        flash("Registration Completed", "success")
        ''' redirecting by using the blueflash name and the route '''
        return redirect(url_for('user.login'))
    else:
        return render_template('user/register.html')
