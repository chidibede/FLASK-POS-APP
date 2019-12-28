''' Application views script'''

# Libraries and imports needed
from pointofsale import app, db, bcrypt
from flask import Flask, render_template, url_for, flash, redirect
from pointofsale.forms import RegistrationForm, LoginForm
from pointofsale.models import User
from flask_login import login_user, logout_user, current_user, login_required


# function that renders home page
@app.route('/')
@app.route('/home')
def home():
    '''
     Function that renders the homepage
     of the app
    '''
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
     Function that renders the registration page
     of the app and creates the user that registered
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        role = form.role.data
        user = User(fullname=fullname, username=username, email=email, role=role, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created Succesfully for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
     Function that renders the Login
     page of the app
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            return redirect('dashboard')
        else:
            flash('Username or Password incorrect, Try again!', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    '''
     Function that logs out user
    '''
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/inventory')
@login_required
def inventory():
    return render_template('inventory.html')

@app.route('/employee')
def employee():
    return render_template('employee.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')
