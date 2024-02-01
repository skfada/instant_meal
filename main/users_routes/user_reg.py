from flask import Blueprint, flash
from flask import render_template, request, url_for, redirect
from main.database.dbModels import Users
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from main import db, session


user_reg = Blueprint('user', __name__, url_prefix='/user')

@user_reg.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        ''' checking for empty form submision '''
        if request.form["username"] == "":
            flash(f"Please Enter your User Name", "caution")
            return render_template('user/register.html')
        if request.form["email"] == "":
            flash(f"Please Enter your Email Address", "caution")
            return render_template('user/register.html')
        if request.form["pwd1"] == "":
            flash(f"Please Enter your Password", "caution")
            return render_template('user/register.html')
        if request.form["pwd2"] == "":
            flash(f"Please Enter Confrim Password", "caution")
            return render_template('user/register.html')

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
        return redirect(url_for('user_login.login'))
    else:
        return render_template('user/register.html')
