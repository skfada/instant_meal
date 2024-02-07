from main import *
from main.database.dbModels import (Users,
                                    GeneralJournal, Sellers, Market,
                                    Orders)


@user.route('/update', methods=['PUT', 'POST', 'GET'])
@login_required
def update():
    if request.method == 'POST' or request.method == 'PUT':
        for key in request.form:
            if request.form[key] == "":
                flash(f'please provide entry for "{key}"', 'caution')
                return redirect(url_for('user.update'))

        first_name = request.form['firstname']
        last_name = request.form['lastname']
        date_of_birth = request.form['dob']
        occupation = request.form['occupation']
        phone_no = request.form['phone']
        country = request.form['country']
        state = request.form['state']
        lga = request.form['lga']
        house = request.form['house']

        '''checking if current user and existing user match'''
        current_user = session['user_name']
        user_object = Users.query.filter_by(username=current_user).first()

        if  user_object:
            '''updating the existin record'''
            user_object.first_name = first_name
            user_object.last_name = last_name
            user_object.date_of_birth = date_of_birth
            user_object.occupation = occupation
            user_object.phone_no = phone_no
            user_object.country_of_residence = country
            user_object.State_of_residence = state
            user_object.lga_residence = lga
            user_object.house_address = house
            '''commit the changes to reflect in database'''
            db.session.commit()

            flash('update completed', 'success')
            return redirect(url_for('user.dashboard'))

        else:
            flash('the user does not exist, please confirm details', 'caution')
            return redirect(url_for('user.update'))

    else:
        return render_template('user/user_update.html')


@user.route('/password_reset', methods=['PUT', 'POST', 'GET'])
def password_reset():
    if request.method == "POST" or request.method == "PUT":
        ''' checking for empty form submision '''
        if request.form["username"] == "":
            flash(f"Please Enter your User Name", "caution")
            return redirect(url_for('user.password_reset'))
        if request.form["email"] == "":
            flash(f"Please Enter your Email Address", "caution")
            return redirect(url_for('user.password_reset'))
        if request.form["pwd1"] == "":
            flash(f"Please Enter your Password", "caution")
            return redirect(url_for('user.password_reset'))
        if request.form["pwd2"] == "":
            flash(f"Please Enter Confrim Password", "caution")
            return redirect(url_for('user.password_reset'))

        ''' checking if password and confirmation password are same '''
        pwd1 = request.form["pwd1"]
        pwd2 = request.form["pwd2"]

        if pwd1 != pwd2:
            flash("inconsistent password", "caution")
            return redirect(url_for('user.password_reset'))

        ''' checking if user already exist in the database '''
        user_object = Users.query.filter_by(email=request.form["email"]).first()

        if user_object and user_object.email == request.form["email"]:
            hash_pwd = generate_password_hash(request.form["pwd2"]).decode("utf-8")

            """ seeting new password """
            user_object.pwd_hashed = hash_pwd
            """ setting the user attemt to zero to re-enable access """
            user_object.login_attempt = 0
            """ storing user data to the database """
            db.session.commit()
            flash("password reset Completed", "success")
            return redirect(url_for('user.login'))

        else:
            flash("User Does not Exist, please register to proceed")
            return redirect(url_for('user.register'))
    else:
        return render_template('user/password_reset.html')


@user.route('/fund_wallet', methods=['GET', 'PUT', 'POST'])
@login_required
def fund_wallet():
    '''this will enable users fund their wallet'''
    if request.method == "POST" or request.method == "PUT":
        for item in request.form:
            if request.form[item] == "":
                flash(f"Please provide information for {item}", "caution")
                return redirect(url_for('user.fund_wallet'))


        ''' comparing loged in user information with database '''
        user_object = Users.query.filter_by(username=request.form["user_name"]).first()
        admin_obj =  Users.query.filter_by(username='admin').first()
        if user_object:
            amount = int(request.form['amount'])

            ''' DEBIT ADMIN AND CREDIT USER'''
            admin_obj.wallet = admin_obj.wallet - amount
            user_object.wallet = user_object.wallet + amount
            db.session.commit()

            ''' RECORD TRANSACTION IN JOURNAL'''
            new_record = GeneralJournal(
                sender_username = admin_obj.username,
                receiver_username = user_object.username,
                description = f'from: {admin_obj.username} to: {user_object.username}',
                dr_amnt = amount,
                cr_amnt = amount,
                sender_wallet = admin_obj.wallet,
                receiver_wallet = user_object.wallet
            )
            db.session.add(new_record)
            db.session.commit()

            session['user_fmt_budget'] = fmtNumber(user_object.wallet)
            flash(f"Transaction was completed", "info")
            return redirect(url_for('user.market'))

        else:
            flash(f"user does not match for {request.form['user_id']}", "caution")
            return redirect(url_for('user.fund_wallet'))
    else:
        return render_template('user/user_fundwallet.html')


@user.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    '''
    - to take users to the dashboard where they will have
    - access to links for other personalized purposes
    '''
    user_object = Users.query.filter_by(username=session["user_name"]).first()
    session['user_fmt_budget'] = fmtNumber(user_object.wallet)


    order_obj = Orders.query.filter_by(buyer_name=session['user_name']).all()
    ''' i used .all() so it will enable me find the length of the object'''
    if not order_obj:
        flash('you are yet to purchase an item','info')
        return redirect(url_for('user.market'))
    elif len(order_obj) == 1:
        order_obj = Orders.query.filter_by(buyer_name=session['user_name']).first()
        ''' i used .first() so it will enable me to return the single object'''
        return render_template('user/single_order.html', orders=order_obj, formatNumber=fmtNumber)
    else:
        return render_template('user/user_dashboard.html', orders=order_obj, formatNumber=fmtNumber)


@user.route('/info', methods=['GET'])
@login_required
def view_profile():
    ''' to display the users information '''
    users = Users.query.filter_by(username=session['user_name'])

    return render_template('user/user_viewinfo.html', users=users)