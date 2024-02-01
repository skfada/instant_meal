from flask import Blueprint, flash, session
from flask import render_template, request, url_for, redirect
from main.database.dbModels import Users
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from main import db, login_required
from main.myfunction import fmtNumber

user_login = Blueprint('user_login', __name__, url_prefix='/user')

@user_login.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        ''' checking for empty form submision '''
        if request.form["username"] == "":
            flash(f"Please Enter your User Name","caution")
            return render_template('user/login.html')
        if request.form["pwd"] == "":
            flash(f"Please Enter Password","caution")
            return render_template('user/login.html')

        ''' comparing input data and existing data '''
        attempted_username = request.form["username"]
        attempte_password = request.form["pwd"]

        user_object = Users.query.filter_by(username=attempted_username).first()

        if  user_object:
            """ checking the loging attempt"""
            if user_object.login_attempt == 3:
                flash(f"you have been blocked due to too many attempts,\
                        kindly reset your password with the form below","caution")
                return redirect(url_for('user_update.password_reset'))

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
                    return redirect(url_for('user_update.update'))
                else:
                    return redirect(url_for('market.market_page'))
            else:
                """ counting the wrong attempt made"""
                user_object.login_attempt += 1
                """ adding the changes to database"""
                db.session.commit()

                flash(f"Please check credentials carefully and\
                        try again","caution")
                return render_template('user/login.html')
        else:
            flash(f"Please check credentials carefully and try again\
                    or Register if you dont have an account","caution")
            return render_template('user/login.html')

    else:
        return render_template('user/login.html')

@user_login.route('/logout')
@login_required
def logout():
    session.pop('user_name')
    flash("Logged out Successfull!!!", "success")
    return render_template('home.html')