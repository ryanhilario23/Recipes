from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User import User
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#This is where the user can be routed and do CRUD
#The Links page

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/regi_user', methods=['POST'])
def register_user():

    if request.form['password'] =='':
        flash('Please fill out form','register')
        return redirect('/')
    
    if not User.validate_regi_user(request.form):
        return redirect('/')
    
    pw_has = bcrypt.generate_password_hash(request.form['password'])
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email':request.form['email'],
        'password_c': request.form['password_c'],
        'password': pw_has
    }
    id = User.save_user(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login_user', methods=['POST'])
def login_user():
    if User.validate_login(request.form):
        return redirect('/')

    login_info={
        'email': request.form['email'],
        'password':request.form['password']
        }
    account = User.login_email(login_info)
    if not account:
        User.invalid_account(account)
        return redirect('/')
    pass_check = bcrypt.check_password_hash(account['password'],request.form['password'])

    if not pass_check:
        User.invalid_account(pass_check)
        return redirect('/')

    session['user_id'] = account['user_id']
    print(session)
    return redirect('/dashboard')

@app.route('/dashboard')
def logged_in_user():
    data= {'user_id':session['user_id']}
    one_user = User.logged_in_user(data)
    print(one_user)
    return render_template('dashboard.html', user = one_user)

@app.route('/logout')
def logout():
    session.clear()
    print('session gone')
    return redirect('/')