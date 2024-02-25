from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)


@user.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        ''' checking for empty form submision '''
        for item in request.form:
            if request.form[item] == "":
                flash(f"Please provide information for {item}", "caution")

        ''' comparing input data and existing data '''
        attempted_username = request.form["username"]
        attempte_password = request.form["pwd"]

        user_object = Users.query.filter_by(username=attempted_username).first()
        if  user_object:
            """ checking the loging attempt"""
            if user_object.login_attempt == 3:
                flash(f"kindly reset your password", "caution")
                return redirect(url_for('user.password_reset'))
            verified_pwd = check_password_hash(user_object.pwd_hashed,\
                                                attempte_password)
            if verified_pwd:
                """ reseting wrong attempt count to zero"""
                user_object.login_attempt = 0

                db.session.commit()
                flash(f"Logged in as: {user_object.username}","success")
                session["user_name"] = user_object.username
                user_name = user_object.username
                session["user_id"] = user_object.id
                user_id = user_object.id
                session['user_fmt_budget'] = fmtNumber(user_object.wallet)
                '''checking if the user has updated their personal details'''
                if user_object.house_address == None:
                    return redirect(url_for('user.update'))
                else:
                    return redirect(url_for('user.dashboard'))
            else:
                """ counting the wrong attempt made"""
                user_object.login_attempt += 1
                """ adding the changes to database"""
                db.session.commit()
                flash(f"Please check credentials carefully and\
                        try again","caution")
                return redirect(url_for('user.login'))
        else:
            flash(f"the Username <<{attempted_username}>> does not exist.\
                    Register if you dont have an account","caution")
            return redirect(url_for('user.login'))
    else:
        return render_template('user/login.html')

@user.route('/logout')
@login_required
def logout():
    session.pop('user_name')
    flash("Logged out Successfull!!!", "success")
    return render_template('home.html')