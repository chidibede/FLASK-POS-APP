''' Application views script'''

# Libraries and imports needed
from pointofsale import app, db, bcrypt
from flask import Flask, render_template, url_for, flash, redirect
from pointofsale.forms import RegistrationForm, LoginForm
from pointofsale.models import User


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
        if form.username.data == 'chidibede' and form.password.data == '111':
            flash('Logged in Successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username or Password incorrect, Try again!', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


